"""
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy
króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest
globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik
ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do
prawego dolnego narożnika.
"""

from math import log10

def num_length(num):
    return int(log10(num))+1

def zad151(T,w,k):
    if w==k==len(T)-1:
        return True
    else:
        flag=False

        for el in [(1,0),(1,1),(0,1)]:
            if w+el[0]<len(T) and k+el[1]<len(T):
                next_n=T[w+el[0]][k+el[1]]

                if T[w][k]%10 < next_n//10**(num_length(next_n)-1):
                    flag = flag or zad151(T,w+el[0],k+el[1])

        return flag

T=[[11,1],[4,21]]

print(zad151(T,0,0))