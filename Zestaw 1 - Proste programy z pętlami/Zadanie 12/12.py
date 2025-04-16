# Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze.
from math import sqrt
def rozklad_na_czynniki(n):
    if n<2:
        return "Podaj liczbę wiekszą równą 2"

    while n%2==0:
        print(2, end=" ")
        n=n//2
    #end while

    k=3
    while k <=sqrt(n):
        while n%k==0:
            print(k, end=" ")
            n=n//k
        k+=2
    #end while

    if n>2:
        print(n)

n=int(input())
print(rozklad_na_czynniki(n))

