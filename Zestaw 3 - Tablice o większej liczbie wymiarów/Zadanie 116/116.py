"""
Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnym >1 odbywają się wyścigi wież.
Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża startuje z prawego
górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w
lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą
wykonać ruch z jednego pola na drugie tylko wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę
napisać funkcję, która dla danej tablicy zwraca numer wieży, która wygra wyścig lub zero jeżeli wyścig będzie
nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym polu
"""

from random import randint
def generuj_tablice(n):
    return [[randint(1,20) for _ in range(n)] for _ in range(n)]

def is_coprime(a,b):
    while b!=0:
        a,b=b,a%b

    return a==1

def rook_race(T):
    rook1_time=float('inf')
    rook2_time=float('inf')
    #Rekurencja dla wieży 1 (w lewym górnym rogu)
    def rook1_rec(row,col,cnt):
        n=len(T)
        nonlocal rook1_time
        if row==col==n-1:
            rook1_time=min(rook1_time,cnt)

        else:
            for i in range(row+1,n): #Pętla dla ruchów w dół (względem wierszy)
                if is_coprime(T[row][col],T[i][col]):
                    rook1_rec(i,col,cnt+1)

            for i in range(col+1,n): #Pętla dla ruchów w prawo (względem kolumn)
                if is_coprime(T[row][col],T[row][i]):
                    rook1_rec(row,i,cnt+1)

    #Rekurencja dla wieży 2 (w prawym górnym rogu)
    def rook2_rec(row,col,cnt):
        nonlocal rook2_time
        n=len(T)
        if row==n-1 and col==0:
            rook2_time=min(rook2_time,cnt)

        else:
            for i in range(row+1,n):
                if is_coprime(T[row][col],T[i][col]):
                    rook2_rec(i,col,cnt+1)

            for i in range(col-1,-1,-1):
                if is_coprime(T[row][col],T[row][i]):
                    rook2_rec(row,i,cnt+1)


    rook1_rec(0,0,0)
    rook2_rec(0,len(T)-1,0)
    if rook1_time==rook2_time:
        return 0
    elif rook1_time<rook2_time:
        return 1
    else:
        return 2

n=3
T=generuj_tablice(n)
for el in T:
    print(el)
print(rook_race(T))







