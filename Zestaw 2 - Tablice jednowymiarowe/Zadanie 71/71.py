"""Proszę napisać program, który wypełnia N-elementową tablicę T pseudolosowymi liczbami
nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego
o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
indeksach."""

from random import randint

def ciag_arytm(T):
    n=len(T)
    rosn_len=mal_len=2
    best_rosn=best_mal=2
    r=abs(T[1]-T[0])

    #Ciąg rosnący
    for i in range(2,n):
        if T[i]-T[i-1]>0 and abs(T[i]-T[i-1])==r:
            rosn_len+=1
        else:
            best_rosn=max(best_rosn, rosn_len)
            rosn_len=2
            r=abs(T[i]-T[i-1])
        #end if
    #end for
        best_rosn=max(best_rosn, rosn_len)


    r=abs(T[1]-T[0])
    #Ciąg malejący
    for j in range(2,n):
        if T[j]-T[j-1]<0 and abs(T[j]-T[j-1])==r:
            mal_len+=1
        else:
            best_mal=max(best_mal, mal_len)
            mal_len=2
            r = abs(T[j] - T[j - 1])
        #end if
    #end for
        best_mal=max(best_mal, mal_len)

    return abs(best_rosn-best_mal)

n=int(input())
T=[randint(1,99) | 1 for _ in range(n)]
print(T)
print(ciag_arytm(T))