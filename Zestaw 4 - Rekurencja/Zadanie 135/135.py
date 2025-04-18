"""
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę T oraz startową kolumnę k. Koszt
przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia.
"""
from random import randint

def krol(T,w,k):
    if w==7:            #Warunek końca
        return T[w][k]

    if k>0:             #Pozycja krola nie jest przy lewej krawędzi
        left=krol(T,w+1,k-1)
    else:
        left=float('inf')

    if k<7:             #Pozycja krola nie jesy przy prawej krawędzi
        right=krol(T,w+1,k+1)
    else:
        right=float('inf')

    middle = krol(T, w+1, k)

    return min(left,right,middle)+T[w][k]

T=[[randint(1,20) for _ in range(8)] for _ in range(8)]
for el in T:
    print(el)
print(krol(T,0,0))

