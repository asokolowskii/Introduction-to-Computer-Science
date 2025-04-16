"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa.
"""

from random import randint

def sum_of_neighbours(T):
    n=len(T)
    max_sum=0
    sides = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    max_row,max_col=None, None
    for row in range(n):
        for col in range(n):
            suma=0
            for k in sides:
                if 0<=row+k[0]<n and 0<=col+k[1]<n:
                    suma+=T[row+k[0]][col+k[1]]

            if suma>max_sum:
                max_sum=suma
                max_row,max_col=row,col

    return (max_row, max_col)

n=int(input())
T=[[randint(1,20) for _ in range(n)] for _ in range(n)]
print(sum_of_neighbours(T))


