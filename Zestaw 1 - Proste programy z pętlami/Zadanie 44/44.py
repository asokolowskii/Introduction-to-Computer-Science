"""Liczbę pierwszą będącą palindromem nazywamy “palindromem pierwszym”. Liczbę nazywamy
“super palindromem pierwszym” jeżeli podczas odrzucania parami skrajnych cyfr do końca pozostaje
ona palindromem pierwszym. Na przykład, liczba 373929373 jest super palindromem pierwszym bo
373929373, 7392937, 39293, 929, 2 są palindromami pierwszy- mi.
Początkowymi super palindromami pierwszymi są: 2, 3, 5, 7, 11, 131, 151.
Proszę napisać program, który wylicza ile jest super
palindromów pierwszych mniejszych od zadanej liczby n."""

from math import sqrt, log10
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

def palindrom(n):
    temp = n
    rev = 0
    while n>0:
        digit=n%10
        rev = rev*10 + digit
        n=n//10

    return rev==temp

def super_palindrom(n):
    cnt=0
    for num in range(2,n):
        if is_prime(num) and palindrom(num):
            cut_num=num
            can_be_cut=True

            while cut_num>0 and can_be_cut:
                if not is_prime(cut_num) or not palindrom(cut_num):
                    can_be_cut=False
                else:
                    cut_num=str(cut_num)
                    if len(cut_num)<=2:
                        cut_num=0
                    else:
                        cut_num=int(cut_num[1:-1])

            if can_be_cut==True:
                cnt+=1

    return cnt

n=int(input())
print(super_palindrom(n))