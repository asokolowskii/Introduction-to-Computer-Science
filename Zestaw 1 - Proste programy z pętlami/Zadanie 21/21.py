"""
Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
wyrazów ciągu Fibonacciego. Wyznaczyć ten ilorazy dla różnych wartości dwóch początkowych wyrazów
ciągu.
"""
def ciag_fibonacciego(eps):
    a, b = 1, 1
    while abs((b/a)-((a+b)/b)) > eps:
        a,b = b, a+b

    return b/a

print(ciag_fibonacciego(1e-6))
