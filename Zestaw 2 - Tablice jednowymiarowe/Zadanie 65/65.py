"""Napisać program wypełniający N-elementową tablicę T liczbami naturalnymi 1-1000
i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
"""

from random import randint
def at_least_one_odd(a):
    while a>0:
        if (a%10)%2==1:
            return True
        else:
            a = a//10
    return False

def check_list(T, N):
    for el in T:
        if not at_least_one_odd(el):
            return False
    return "Zawiera", T

N=int(input())
T = [randint(1,1000) for _ in range(0,N)]
print(check_list(T,N))


