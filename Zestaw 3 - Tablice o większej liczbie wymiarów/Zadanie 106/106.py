"""Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
będącą liczbą pierwszą?"""

from math import sqrt

def is_prime(n):
    if n==2 or n==3:
        return True
    if n<=1 or n%2==0 or n%3==0:
        return False

    k=5
    while k<=sqrt(n):
        if n%k==0 or n%(k+2)==0:
            return False
        k+=6
    return True

def at_least_one_prime(num):
    while num>0:
        digit=num%10
        if is_prime(digit):
            return True
        num=num//10
    return False

def zad106(T):
    n=len(T)
    for row in range(n):
        flag=True
        for col in range(n):
            if not at_least_one_prime(T[row][col]):
                flag=False
                break

        if flag: return True

    return False




