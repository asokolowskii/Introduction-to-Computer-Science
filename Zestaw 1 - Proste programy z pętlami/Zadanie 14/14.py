"""Dwie różne liczby nazywamy zaprzyjaźnionymi gdy każda jest równa sumie podzielników
właściwych drugiej liczby, na przykład 220 i 284. Proszę napisać program wyszukujący liczby zaprzyjaźnione
mniejsze od miliona."""

def dzielniki(n):
    suma = 1
    for k in range(2, int(n**0.5)+1):
        if n%k==0:
            suma+=k
            if k!=n//k:
                suma+=n//k

    return suma

for i in range(2, 10**6):
    wspolne_sumy = dzielniki(i)

    if wspolne_sumy < 10**6 and wspolne_sumy > i and dzielniki(wspolne_sumy) == i:
        print(i, wspolne_sumy)

