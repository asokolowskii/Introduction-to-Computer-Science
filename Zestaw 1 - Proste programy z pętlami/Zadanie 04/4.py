# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.

def czy_istn_fib(n):
    a=b=x=y=1
    suma = 0
    while suma < n:
        suma+=a
        a,b=b,a+b

    while suma > n:
        suma-=x
        x,y = y, x+y

    return (suma == n)

n = int(input())
print(czy_istn_fib(n))


