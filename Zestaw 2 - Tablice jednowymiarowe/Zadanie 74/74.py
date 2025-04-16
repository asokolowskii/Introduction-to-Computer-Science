"""Dana jest duża tablica T. Proszę napisać funkcję, która zwraca informację czy w tablicy
zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego
są liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”"""

from math import sqrt
from random import randint

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    k = 5
    while k <= sqrt(n):
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True

def is_fibonacci(n):
    elements = [False] * n
    a, b = 0, 1
    while a < n:
        elements[a] = True
        a, b = b, a + b
    return elements

def check_list(T):
    n = len(T)
    indeksy_fib = is_fibonacci(n)
    flag = False

    # Sprawdzenie, czy wszystkie liczby na indeksach Fibonacciego są liczbami złożonymi
    for i in range(n):
        if indeksy_fib[i] and is_prime(T[i]):
            return False, T  # Warunek niespełniony

    # Szukanie liczby pierwszej poza indeksami Fibonacciego
    for i in range(n):
        if not indeksy_fib[i] and is_prime(T[i]):
            flag = True
            break

    return flag, T

n = 10
tab = [4, 6, 8, 9, 10, 15, 24, 25, 7, 14]
print(check_list(tab))

