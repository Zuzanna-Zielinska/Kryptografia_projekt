import random

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
    # Initialize result
    res = 1;

    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):

        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;

        # y must be even now
        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;
def miller(n: int, k:int, show_details: bool, a0 = -1):

    txt = ""
    if type(n) != int:
        raise TypeError("n must be integer")

    if n <= 3:
        return True, txt

    if n % 2 == 0:
        return False, "Liczba jest parzysta."

    set_a0 = False
    if type(a0) == int and a0 > 1 and a0 < n - 1:
        set_a0 = True

    n1 = n - 1

    #n-1 = 2^s * m
    s = 0
    while n1 % 2 == 0:
        n1 //= 2
        s += 1

    d = n1
    txt = txt + f"n-1 = 2^{s} * {d}\n"
    # print(f"n-1 = 2^{s} * {d}")



    for i in range(k):
        txt = txt + f"\nk = {i}\n------------------\n"
        # print(f"\nk = {i}\n------------------")

        a = random.randint(2, n - 2)
        if i == 0 and set_a0:
            a = a0

        txt = txt + f"a = {a}\n"

        # print(f"a = {a}")

        x = power(a, d, n)

        if show_details:

            txt = txt + f"\nx = {a}^{d} % {n}\n"
            txt = txt + f"x = {x}\n\n"
            txt = txt + f"y = {x}^2 % {n}\n"
        # print(f"\nx = {a}^{d} % {n}")
        # print(f"x = {x}\n")
        # print(f"y = {x}^2 % {n}")


        for r in range(s):
            y = x**2 % n
            if r == 0:
                if show_details:
                    txt = txt + f"y = {y}\n\n"
                # print(f"y = {y}\n")
            if show_details:
                txt = txt + f"y = {y} oraz x = {x}\n"
            # print(f"y = {y} and x = {x}")

            if y == 1 and x != 1 and x != n - 1:
                txt = txt + f"Liczba jest złożona\n"
                return False, txt
            x = y
        if y != 1:
            txt = txt + f"Liczba jest złożona\n"
            return False, txt

        txt = txt + f"Liczba jest pierwsza\n"
    return True, txt


#19999

# n = 19997
# k = 4
#
# print(f"n = {n}")
# result = miller(n, k, False, 5)
#
# if result[0]:
#     print("prime")
# else:
#     print("composite")
#
# print(result[1])

