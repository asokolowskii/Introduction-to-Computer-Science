"""Dla pewnej N-cyfrowej liczby naturalnej obliczono sumę N-tych potęg cyfr tej liczby otrzymując kolejną liczbę N-cyfrową. Na przykład dla liczb: 354, 543, 600, ... suma ta wynosi 216. Niestety pierwotna
liczba zaginęła ale wiadomo, że była to największa z możliwych takich liczb. Proszę napisać program, który
na podstawie zachowanej sumy wyznaczy pierwotną liczbę"""

from math import log10
def potega_cyfr_liczby(n):
    n_length=int(log10(n))+1
    suma=0
    while n>0:
        next_digit=n%10
        next_digit=next_digit**n_length
        suma+=next_digit
        n=n//10
    return suma

def maksymalna_liczba(n):
    n_length=int(log10(n))+1
    maxi=None

    for i in range(10**n_length-1, 10**(n_length-1)-1, -1):
        if potega_cyfr_liczby(i)==n:
            maxi=i
            break

    return maxi

n=int(input())
print(maksymalna_liczba(n))