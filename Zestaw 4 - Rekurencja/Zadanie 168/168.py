""" Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
 czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba
 kawałków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True,
 podział na 23 i 47, natomiast divide(2255)=False"""

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

def zad168(n):
    def rek(n, x, ilosc_cyfr, cnt):
        if n==0:
            print(x, cnt)
            return is_prime(x) and is_prime(cnt)
        else:
            x+=(n%10)*(10**(ilosc_cyfr))
            if is_prime(x):
                return rek(n//10,0,0,cnt+1) or rek(n//10,x,ilosc_cyfr+1,cnt)
            else:
                return rek(n//10,x, ilosc_cyfr+1,cnt)

    return rek(n,0,0,1)


  

