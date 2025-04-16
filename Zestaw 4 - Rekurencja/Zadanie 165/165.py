"""Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory
o jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool."""

def zad165(T,k):
    def rek(T,k,i,a,b,suma):

        if suma==0 and a!=0 and b!=0:
            if a+b==k:
                return True

        if i==len(T):
            return False

        return rek(T,k,i+1,a+1,b,suma+T[i]) or rek(T,k,i+1,a,b+1,suma-T[i]) or rek(T,k,i+1,a,b,suma)

    return rek(T,k,0,0,0,0)
