# Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

from math import sqrt
def is_prime(n):
    if n==2 or n==3:
        return True
    if n<=1 or n%2==0 or n%3==0:
        return False

    k=5
    while k <= sqrt(n):
        if n%k==0 or n%(k+2)==0:
            return False
        k+=6
    return True

n = int(input("Podaj liczbę: "))
print(is_prime(n))


