"""Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali.
"""


def generuj_tablice(n):
    return [[None for i in range(n)] for j in range(n)]

def task92(T):
    n=len(T)
    min_x=min_y=0
    max_x=max_y=n-1
    cnt=1
    while min_x<=max_x and min_y<=max_y:
        for i in range(min_x, max_x+1):
            T[min_y][i]=cnt
            cnt+=1
        min_y+=1

        for i in range(min_y, max_y+1):
            T[i][max_x]=cnt
            cnt+=1
        max_x-=1

        for i in range(max_x, min_x-1, -1):
            T[max_y][i]=cnt
            cnt+=1
        max_y-=1

        for i in range(max_y, min_y-1, -1):
            T[i][min_x]=cnt
            cnt+=1
        min_x+=1

    for element in T:
        print(element)

n=int(input())
T=generuj_tablice(n)
task92(T)






