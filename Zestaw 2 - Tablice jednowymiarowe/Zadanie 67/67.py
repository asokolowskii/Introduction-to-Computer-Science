"""Dana jest N-elementowa tablica T zawierająca liczby naturalne. W tablicy możemy przeskoczyć z pola
o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby T[k]. Napisać
funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""

# 1. sposób
from math import sqrt
def czynniki_pierwsze(n):
    czynniki = [0]*int(n**0.5+1)
    index=0
    b=2
    while b<=sqrt(n):
        while n%b==0:
            czynniki[index]=b
            n=n//b
            index+=1
        b+=1
        #end while 1
    #end while 2
    if n>1:
        czynniki[index]=n

    return [i for i in czynniki if i!=0]


def sprawdz(T):
    n = len(T)
    T2 = [False for _ in range(n)]
    T2[0]=True #zaczynamy od pierwszego pola

    for i in range(n):
        if T2[i]:
            factors = czynniki_pierwsze(T[i])

            for k in factors:
                if i+k<n:
                    T2[i+k]=True

    return T2[-1]

t = [6, 1, 5, 2, 4, 3, 9, 6, 1, 2, 4]
print(sprawdz(t))  # Sprawdza, czy można przejść z pierwszego do ostatniego pola

# 2. sposób
def rozklad_na_czynniki(a):
    czynniki = [0]*(int(sqrt(a))+1)
    index=0

    if a<2:
        return []

    while a%2==0:
        czynniki[index]=2
        index+=1
        a=a//2
    #end while

    k=3
    while k<=sqrt(a):
        while a%k==0:
            czynniki[index]=k
            index+=1
            a=a//k
        k+=2
    #end while

    if a>2:
        czynniki[index]=a
        index+=1

    czynniki = [i for i in czynniki if i!=0]
    return czynniki

def jump_n_digits(T):
    N=len(T)
    T2=[False for _ in range(N)]
    T2[0]=True

    for k in range(N):
        if T2[k]:
            digits=rozklad_na_czynniki(T[k])
            for n in digits:
                if k+n<N:
                    T2[k+n]=True

    return T2[-1]
