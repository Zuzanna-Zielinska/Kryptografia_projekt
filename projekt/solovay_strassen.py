# Python3 program to implement Solovay-Strassen
# Primality Test
import random


def modulo(base, exponent, mod):
    # szybkie potęgowanie modulo - wykorzystuje zapis bitowy
    act_val = 1
    act_base = base
    while (exponent > 0):
        if (exponent % 2 == 1):
            act_val = (act_val * act_base) % mod

        act_base = (act_base * act_base) % mod
        exponent = exponent // 2

    return act_val % mod


# To calculate Jacobian symbol of a
# given number
def calculateJacobian(a, n):

    # liczy symbol jakobiego (a/n)
    # n - testowana, nieparzysta liczba, której względną pierwszość testujemy
    # a - liczba, dla której liczymy symbol Jacobiego

    # zwraca 1, jeżeli istnieje t, że t^2==a (mod n)
    # zwraca 0 jeżeli a==0 (mod n)
    # zwraca -1 jeżeli nie istnieje t, że t^2==a (mod n)


    if a == 0:
        return 0  # (0/n) = 0

    ans = 1

    if a < 0:
        # jeżeli a<0 to (a/n) = (-a/n)*(-1/n)
        a = -a
        if (n % 4 == 3):
            # (-1/n) = -1 jeżeli n = 3 (mod 4); 1 jeżeli n = 1 (mod 4)
            ans = -ans

    if a == 1:
        return ans  # (1/n) = 1

    while a != 0:
        if a < 0:
            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if (n % 4 == 3):
                # (-1/n) = -1 jeżeli n = 3 (mod 4); 1 jeżeli n = 1 (mod 4)
                ans = -ans

        # (2*a/n) = (a/n) * (2/n)
        while a % 2 == 0:
            a = a // 2
            if n % 8 == 3 or n % 8 == 5:
                #  (2/n) = -1 jeżeli n = 3 (mod 8); 1 jeżeli n = 5 (mod 8)
                ans = -ans

        # (a/b) = (b/a) * (-1)^((a-1)*(b-1)/4)
        # próbujemy skrócić mianownik, żeby nie liczyć dużych liczb
        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n

        # jeżeli a jest większe niż n/2 to zmieniamy znak nie liczyć dużych liczb
        if a > (n // 2):
            a = a - n

    # jeżeli n=1 to we wcześniejszym kroku a == 1, więc zwracamy ans
    if (n == 1):
        return ans
    # w przciwnym wypadku zwracamy 0, ponieważ liczby te nie są względnie pierwsze
    return 0



def solovay_strassen(p, iterations, show_details: bool, a0 = -1):
    # Test Solovaya-Strassena do sprawdzania pierwszości liczby p
    # p - testowana liczba nieparzysta
    # iterations - liczba iteracji algorytmu

    txt = ""

    if (p < 2):
        return False, txt
    if (p != 2 and p % 2 == 0):
        return False, "Liczba jest parzysta."

    set_a0 = False
    if type(a0) == int and a0 > 1 and a0 < p - 1:
        set_a0 = True, txt

    if show_details:
        txt = txt + f"J(a, n) - symbol Jakobiego\n\n"

    for i in range(iterations):

        txt = txt + f"k = {i}\n------------------\n"

        # Generate a random number a
        a = random.randrange(2, p - 2) + 1

        if i == 0 and set_a0:
            a = a0

        txt = txt + f"a = {a}\n"

        jacobian = calculateJacobian(a, p) % p
        mod = modulo(a, (p - 1) / 2, p)

        if show_details:
            # txt = txt + f"\nJ({a}, {p}) % {p} = {jacobian}\n"

            txt = txt + f"\nx = {a}^({p - 1} / {2}) % {p}\n"
            txt = txt + f"x = {mod}\n\n"

            txt = txt + f"y = J({a}, {p}) % {p}\n"
            txt = txt + f"y = {jacobian}\n\n"


        if (jacobian == 0 or mod != jacobian):
            # if i != 0:
                # print(f"Found composite number on iter {i}")
            if show_details:
                txt = txt + f"\n{jacobian} = 0 lub {jacobian} = {a}^({p - 1} / {2}) % {p}\n"
            txt = txt + f"Liczba jest złożona\n"
            return False, txt

        txt = txt + f"Liczba jest pierwsza\n\n"
    return True, txt

w = solovay_strassen(9, 1, True)
print(w[0])
print(w[1])

