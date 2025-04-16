"""Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfr"""

from math import sqrt,log10
#Funkcja is_prime sprawdza, czy zadana liczba jest liczbą pierwszą,
#zwraca wartość True lub False
#wykorzystuje algorytm sita Eratostenesa
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

def delete_elements(num):
    n_length=int(log10(num))+1 #zwracam długośc naszej liczby num
    def rek(num,y,i):
        #num - liczba, z której usuwane są cyfry,
        #y - liczba zbudowana z zachowanych cyfr,
        #i - pozycja w liczbie y (długość nowej liczby y)
        if num==0:
            #Przypadek, kiedy nie ma już cyfr do usunięcia (i zarazem dodania do y)
            if i!=n_length and i>=2 and is_prime(y):
                print(y)

        else:
            rek(num//10, y, i) #usuwam ostatnią cyfrę z liczby num i nie dodaję jej do y
            rek(num//10, y+(num%10)*(10**i),i+1) #usuwam ostatnią cyfrę z liczby num

    rek(num,0,0)







