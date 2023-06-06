# Python3 program Miller-Rabin primality test
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


# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);

    # Compute a^d % n
    x = power(a, d, n);
    print(f"b0 = {x}")

    if (x == 1 or x == n - 1):
        return True;

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        print(f"b = {x}")
        print(f"b^2 = {d}")

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    print(f"b == n - 1: {d == n - 1}")
    print("koniec")
    # Return composite
    return False;


# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime(n, k):

    steps = []
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    # Find r such that n =
    # 2^s * d + 1 for some r d= 1



    d = n - 1;
    s = 0
    while (d % 2 == 0):

        d //= 2;
        s += 1;

    print(f"s = {s}")
    print(f"d = {d}")
    print(f"n-1 = 2^s * d: {2**s * d == n-1}")

    # Iterate given number of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False, steps;

    return True, steps;


# Driver Code
# Number of iterations
k = 1;

# print("All primes smaller than 100: ");
# for n in range(1, 100):
#     if (isPrime(n, k)):
#         print(n, end=" ");


#




def get_15_numbers():
    numbers = []
    for i in range(1000):
        numbers.append(random.randint(1, 1000))

    result = random.randint(0, 1)

    return bool(result), numbers

n = 99
def miller(n: int, k:int, show_details: bool):

    txt = ""
    if type(n) != int:
        raise TypeError("n must be integer")

    if n <= 3:
        return True, txt

    if n % 2 == 0:
        return False, "Liczba jest parzysta."

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

        txt = txt + f"a = {a}\n"

        # print(f"a = {a}")

        x = a ** d % n

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
# result = miller(n, k, False)
#
# if result[0]:
#     print("prime")
# else:
#     print("composite")

# print(result[1])

