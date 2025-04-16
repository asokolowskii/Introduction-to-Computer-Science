"""Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbę złożoną wyłącznie
z cyfr będących liczbami pierwszymi?"""

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

def all_primes(a):
    while a>0:
        digit=a%10
        if not is_prime(digit):
            return False
        a=a//10
    return True

def check_row(row):
    for el in row:
        if all_primes(el):
            return True
    return False

def zad107(T):
    n=len(T)
    for row in T:
        if not check_row(row):
            return False
    return True


