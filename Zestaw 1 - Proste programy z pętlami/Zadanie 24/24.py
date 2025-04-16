"""
Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi pomimo pozbawiania
ich skrajnych cyfr. Na przykład: 71317 → 131 → 3. Proszę napisać program, który wypisuje wszystkie takie
liczby mniejsze od N.
"""
from math import sqrt
def is_prime(a):
    if a==2 or a==3:
        return True
    if a<=1 or a%2==0 or a%3==0:
        return False

    k=5
    while k<=sqrt(a):
        if a%k==0 or a%(k+2)==0:
            return False
        k+=6
    return True

def palindrom(a):
    temp = a
    rev = 0

    while a>0:
        dig = a%10
        rev = rev*10 + dig
        a = a//10

    return rev==temp

def is_prime_palindrom(N):
    for num in range(2, N):
        if is_prime(num) and palindrom(num):
            cut_num = num
            can_be_cut = True #flaga, która śledzi czy można uciąć skrajne cyfry liczby

            while cut_num>0 and can_be_cut:
                if not is_prime(cut_num):
                    can_be_cut = False
                else:
                    cut_num = str(cut_num)
                    if len (cut_num)<=2:
                        cut_num=0
                    else:
                        cut_num = int(cut_num[1:-1])

            if can_be_cut==True:
                print(num)

N = int(input())
is_prime_palindrom(N)







