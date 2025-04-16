"""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
"""

from random import randint
def czy_nieparzysta(num):
    return num>1 and num%2==1

def right_square(T,k):
    n=len(T) #rozmiar tablicy (NxN)

    for y in range(n):
        for x in range(n):
            bok = 3 #minimalny bok kwadratu o niep. liczbie pól to 3
            while y+bok < n and x+bok < n:
                if czy_nieparzysta(bok**2):
                    iloczyn = T[y][x]*T[y+bok][x]*T[y][x+bok]*T[y+bok][x+bok]

                    if iloczyn==k:
                        return (y+bok//2), (x+bok//2)

                bok+=2

    return False

n=int(input())
T=[[randint(1,10) for _ in range(n)] for _ in range(n)]
for el in T:
    print(el)
print(right_square(T,6))



