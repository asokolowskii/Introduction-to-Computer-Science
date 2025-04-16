# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def is_fibonacci(x):
    if x<1:
        return False

    a,b = 1, 1
    while a*b < x:
        a,b = b, a+b

    return x==a*b
x = int(input("podaj liczbę: "))
print(is_fibonacci(x))


