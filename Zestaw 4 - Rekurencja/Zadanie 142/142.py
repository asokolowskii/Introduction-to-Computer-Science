"""
Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
"""

def zad142(T,M):
    # M - masa do odważenia
    stop = False
    def rek(T,i,r, w1, w2):
        # T - tablica odważników, i - indeks, r - różnica między wagą na obu szalkach
        # w1 - odważnik 1., w2 - odważnik 2.
        nonlocal stop
        if stop:
            return False
        n=len(T)
        if r==0:
            stop = True
            print("Odważniki na lewej szalce:", w1)
            print("Odważniki na prawej szalce:", w2)
            return True
        if r<0 or i>(n-1):
            return False

        return rek(T,i+1,r,w1,w2) or rek(T,i+1,r-T[i], w1+[T[i]],w2) or rek(T,i+1, r+T[i], w1, w2+[T[i]])

    return rek(T,0,M,[],[])

T=[1,3,6,5,4,8,99,13]
print(zad142(T,105))



