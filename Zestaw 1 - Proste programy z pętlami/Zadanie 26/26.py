"""Proszę napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie
dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
"""

def ulamek(a,b,n):
    #część całkowita ułamka
    print(a//b, end=".")

    #pozostałość (reszta)
    a = (a%b)*10

    #obliczanie n cyfr po przecinku
    for _ in range(n):
        print(a//b, end="")
        a = (a%b)*10


a=int(input())
b=int(input())
n=int(input())
ulamek(a,b,n)