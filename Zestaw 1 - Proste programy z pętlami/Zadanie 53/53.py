"""Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
niż 2, 3, 5. Jedynka też jest taką liczbą. Proszę napisać program, który wylicza ile takich
liczb znajduje się w przedziale od 1 do N włącznie."""

from math import sqrt
def rozklad_na_czynniki(n):
    if n==1:
        return True

    for factor in [2,3,5]:
        while n%factor==0:
            n=n//factor

    return n==1

def dwu_trzy_piatkowa(n):
    cnt=0
    for i in range(1, n+1):
        if rozklad_na_czynniki(i):
            cnt+=1

    return cnt

n=int(input())
print(dwu_trzy_piatkowa(n))

