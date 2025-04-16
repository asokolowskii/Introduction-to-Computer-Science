"""Napisać funkcje sprawdzającą czy dwie liczby naturalne są zbudowane z takich samych
cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001."""
def same_digits(a,b):
    tab_a=[0]*10
    tab_b=[0]*10

    while a>0:
        tab_a[a%10]+=1
        a=a//10
    #end while
    while b>0:
        tab_b[b%10]+=1
        b=b//10
    #end while

    return tab_a==tab_b

a=int(input())
b=int(input())
print(same_digits(a,b))



