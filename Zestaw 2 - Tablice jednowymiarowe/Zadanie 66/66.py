"""Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste."""

from random import randint

def all_odd(a):
    while a>0:
        if (a%10)%2==0:
            return False
        else:
            a=a//10

    #end while
    return True

def check_list(T,N):
    for el in T:
        if all_odd(el):
            return "Istnieje", T
    #end for
    return False

N = int(input())
T = [randint(1,1000) for _ in range(0,N)]
print(check_list(T,N))

