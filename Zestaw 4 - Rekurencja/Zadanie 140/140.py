"""Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce"""

def zad140(T, M):
    # M - określona masa do odważenia
    def rek(T,i,r):
        # T - tablica odważników, i - indeks, r - remaining, pozostała masa do odważenia
        n=len(T)
        if r==0:
            return True
        if r<0 or i>(n-1):
            return False

        return rek(T, i+1, r) or rek(T, i+1, r-T[i])
                #nie biorę             #biorę

    return rek(T, 0, M)

T=[6,2,4,1]
print(zad140(T,9))





