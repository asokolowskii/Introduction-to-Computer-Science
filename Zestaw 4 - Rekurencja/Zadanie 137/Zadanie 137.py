"""Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki, z których każdy reprezentuje liczbę pierwszą.
Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla
ciągu 110100 nie jest możliwe"""

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

#Funkcja decimal(T) zamienia liczbę w postaci binarnej na jej wartość dziesiętną.
def decimal(T):
    res=0
    for el in T:
        res = res*2 + el
    return res

def zad137(T):
    n=len(T)
    def rek(i,j):
        #i - początek kawałka, j - koniec kawałka
        if j>n-1: #nie chcemy wyjść poza tablicę(warunek końca)
            return False
        if j==(n-1):
            if T[j]==0 and j-i+1!=2: #Jeśli liczba kończy się 0 w syst. bin.
                return False        #i jej dł. jest różna od 2, to na pewno jest złożona
            return is_prime(decimal(T[i:j+1]))

        if is_prime(decimal(T[i:j+1])):
            return rek(j+1,j+2) #tworzymy nowe pocięcie
        return rek(i,j+1)       #kontunuujemy obecny fragment

    return rek(0,1) if n>1 else False

T=[1,1,0,1,0,0]
print(zad137(T))





