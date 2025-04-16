"""Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w
obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum."""

from random import randint
from math import sqrt

def generuj_tablice(n):
    return [randint(1,100) for _ in range(n)]

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

def create_mask(t1,t2,mask):
    sum=0
    n=len(t1)
    for i in range(n):
        if mask%3==0: sum+=t1[i]+t2[i]
        elif mask%3==1: sum+=t1[i]
        elif mask%3==2: sum+=t2[i]
        mask=mask//3
    return sum

def print_sums(t1,t2):
    n=len(t1)
    cnt=0
    masks=3**n
    for mask in range(masks):
        if is_prime(create_mask(t1,t2,mask)):
            cnt+=1

    return cnt, t1,t2

n = int(input())
t1=generuj_tablice(n)
t2=generuj_tablice(n)
print(print_sums(t1,t2))


