"""Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16."""

# 1. sposób
def system_conversion(num, podst):
    t = [0 for i in range(16)]
    index = 0

    while num>0:
        t[index]=num%podst
        num = num//podst
        index+=1
    #end while

    for j in range(index-1,-1,-1):
        print("0123456789ABCDEF"[t[j]], end=" ")

liczba=int(input())
podst=int(input())
system_conversion(liczba,podst)


# 2. sposób
def przelicz_na_system(num,podst):
    result=' '
    while num!=0:
        next_digit=num%podst
        num=num//podst
        if next_digit>=10:
            next_digit-=10
            result = chr(ord('A')+next_digit)+result
        else:
            result=str(next_digit)+result

    return result


n=int(input())
system=int(input())
tab="0123456789ABCDEF"

# 3. trzeci sposób
def zamiana(n, system):
    result=""
    while n>0:
        result+=tab[n%system]
        n=n//system

    return result[::-1]

print(zamiana(n, system))











