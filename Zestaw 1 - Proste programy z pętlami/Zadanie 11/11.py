# Proszę napisać program wypisujący podzielniki liczby

from math import sqrt
def podzielniki(n):
    if n == 0:
        return "Każda liczba jest podzielnikiem zera"

    if n < 0:
        return "Podaj liczbę nieujemną"


    k=1
    while k <= sqrt(n):
        if n%k==0:
            print(k,end=" ")
            if k!=n//k:
                print(n//k, end=" ")
        k+=1


n = int(input())
print(podzielniki(n))

