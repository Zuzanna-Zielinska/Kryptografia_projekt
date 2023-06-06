import random
def jacobi_symbol(a, n):
    if a == 0:
        return 0
    if a == 1:
        return 1

    if a % 2 == 0:
        return jacobi_symbol(a // 2, n) * ((-1) ** ((n ** 2 - 1) // 8))
    else:
        return jacobi_symbol(n % a, a) * ((-1) ** ((a - 1) * (n - 1) // 4))
def solovay_strassen(n, k, show_details):

    if n == 2 or n == 3:
        return True, ""
    if n % 2 == 0:
        return False, "Liczba jest parzysta."

    txt = ""
    for i in range(k):
        txt = txt + f"\nk = {i}\n------------------\n"
        a = random.randint(2, n - 2)
        txt = txt + f"a = {a}\n"
        x = a ** ((n - 1) // 2) % n
        if show_details:
            txt = txt + f"\nx = {a}^({n}-1)/2 % {n}\n"
            txt = txt + f"x = {x}\n\n"
            txt = txt + f"y = {a}^{n-1} % {n}\n"
        # print(f"\nx = {a}^({n}-1)/2 % {n}")
        # print(f"x = {x}\n")
        # print(f"y = {a}^{n-1} % {n}")

        if x != 1 and x != n - 1:
            txt = txt + f"Liczba jest złożona\n"
            return False, txt

        if x % n == jacobi_symbol(a, n):
            txt = txt + f"Liczba jest prawdopodobnie pierwsza\n"
            # print(f"Liczba jest prawdopodobnie pierwsza\n")
        else:
            txt = txt + f"Liczba jest złożona\n"
            return False, txt

    txt = txt + f"Liczba jest prawdopodobnie pierwsza\n"
    return True, txt

