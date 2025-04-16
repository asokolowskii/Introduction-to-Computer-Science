"""Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję,
która odpowiada na pytanie czy jest możliwe pocięcie ciągu na kawałki, z których każdy reprezentuje
liczbę pierwszą. Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011
jest to możliwe, a dla ciągu 110100 nie jest możliwe"""

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

def zad137(T):
    def rek(T,i,x,k):
        #tablica zer i jedynek, i - aktualny indeks w tablicy T
        #x - zmienna, która przechowuje aktualnie budowaną liczbę w formie binarnej, indeks ostatniego cięcia







