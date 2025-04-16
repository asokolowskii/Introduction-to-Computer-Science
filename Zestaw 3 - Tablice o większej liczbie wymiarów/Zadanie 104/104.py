"""Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest
tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy
nie posiadające liczby komplementarnej."""

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

def zad104(T):
    n=len(T)
    for y in range(n):
        for x in range(n):
            found=False
            for j in range(n):
                for i in range(n):
                    if y==j and x==i:
                        continue
                    if T[j][i]==0:
                        continue
                    if is_prime(T[y][x]+T[j][i]):
                        found=True
                        break

                if found:
                    break
            if not found:
                T[y][x]=0

    return T

T=[[2,3],[3,12]]
print(zad104(T))



