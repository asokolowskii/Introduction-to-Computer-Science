"""Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
przyjaciółkami
"""

def friends(a,b):
    T=[0 for _ in range(10)]
    n=len(T)
    while a>0:
        digit=a%10
        T[digit]=1
        a=a//10

    while b>0:
        digit=b%10
        if T[digit]!=0:
            T[digit]=2
        else:
            return False
        b=b//10

    for i in range(n):
        if T[i]==1:
            return False
    return True

def side_friends(T,i,j):
    n=len(T)
    sides=[(-1,0),(-1,1),(-1,-1),(1,-1),(1,1),(1,0),(0,-1),(0,1)]
    for k in sides:
        if 0<=i+k[0]<n and 0<=j+k[1]<n:
            if not friends(T[i][j], T[i+k[0]][j+k[1]]):
                return False
    return True

def zad102(T):
    n=len(T)
    cnt=0
    for i in range(n):
        for j in range(n):
            if side_friends(T,i,j):
                cnt+=1

    return cnt

T=[[ 98,  22,  72,  10 , 95],
 [88,  17,  1,  78, 24],
 [15, 23, 37,  74,  49],
 [36,  65,  7,  54,  93],
 [7,  49,  90, 100,  37]]

print(zad102(T))



