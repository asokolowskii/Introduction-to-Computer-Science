"""
Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy
jako liczbę zapisaną w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000.
Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze,
dla których różnica zawartych w wierszach liczb jest największa. Do funkcji należy przekazać tablicę,
funkcja powinna zwrócić odległość pomiędzy znalezionymi wierszami. Można założyć,
że żadne dwa wiersze nie zawierają identycznego ciągu cyfr.
"""

def bin_to_dec(row):
    res=0
    exp=0
    for i in range(len(row)-1,-1,-1):
        res+=(2**exp) *row[i]
        exp+=1
    return res

def bigger(row1,row2):
    l = len(row1)
    for i in range(l):
        if row1[i]>row2[i]:
            return True
        elif row1[i]<row2[i]:
            return False
    return True

def distance(T):
    n=len(T)
    mini_ind,maxi_ind=None,None
    for row in range(n):
        if bigger(T[row],T[maxi_ind]):
            maxi_ind=row
        if bigger(T[mini_ind],T[row]):
            mini_ind=row

    return bin_to_dec(T[maxi_ind])-bin_to_dec(T[mini_ind])



