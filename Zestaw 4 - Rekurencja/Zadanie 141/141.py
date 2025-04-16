"""Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach"""

def zad141(T,M):
    # M - masa do odważenia
    def rek(T, i, r):
        # T -- tablica odważników, i - indeks, r - różnica między wagą na obu szalkach
        n=len(T)
        if r==0:
            return True
        if r<0 or i > (n-1):
            return False

        return rek(T,i+1,r) or rek(T,i+1, r-T[i]) or rek(T, i+1, r+T[i])
                #nie biorę       #biorę 1. szalka       #biorę 2. szalka

    return rek(T, 0, M)

T=[9,2,4,8,1,3]
print(zad141(T, 9))