"""Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość
typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
wartości)."""

from random import randint
def generuj_tablice(n):
    return [randint(1,100) for _ in range(n)]

def czy_max_min(T):
    n=len(T)
    min_el=max_el=T[0]
    min_cnt=max_cnt=1

    for el in range(1,n):
        if T[el]<min_el:
            min_el = T[el]
            min_cnt=1
        elif T[el]==min_el:
            min_cnt+=1
        #end if

        if T[el]>max_el:
            max_el=T[el]
            max_cnt=1
        elif T[el]==max_el:
            max_cnt+=1
        #end if
    #end for
    return min_cnt==1 and max_cnt==1, T

n=int(input())
T=generuj_tablice(n)
print(czy_max_min(T))
