"""”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool"""

def waga(num):
    cnt=0 #ilość czynników pierwszych

    i=2 #dzielnik i
    while num!=1:
        if num%i==0:
            cnt+=1
        while num%i==0:
            num=num//i
        i+=1

    return cnt

def zad134(T):
    n=len(T)
    # i - nr elementu w jakim teraz jesteśmy; a,b,c - wagi zbiorów
    def rek(i,a,b,c):
        if i==n:
            return a==b and b==c

        return rek(i+1,a+waga(T[i]),b,c) or rek(i+1,a,b+waga(T[i]),c) or rek(i+1,a,b,c+waga(T[i]))

    return rek(0,0,0,0)

T=[1,3,5,2,3,7,32,55,64,36,90,46]
print(zad134(T))
