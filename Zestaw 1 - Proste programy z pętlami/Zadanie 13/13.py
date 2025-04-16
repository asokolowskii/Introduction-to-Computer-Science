"""Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać program wyszukujący liczby doskonałe
mniejsze od miliona.
"""

from math import sqrt
def suma_dzielnikow(n):
    suma = 1 #1 jest podzielnikiem każdej liczby
    for k in range(2, int(n**0.5)+1):
        if n%k==0:
            suma+=k
            if k!=n//k:
                suma+=n//k
    return suma

def doskonala(n):
    if n==1:
        return False
    return suma_dzielnikow(n) == n

for i in range(1, 1000000):
    if doskonala(i):
        print(i, end=" ")






