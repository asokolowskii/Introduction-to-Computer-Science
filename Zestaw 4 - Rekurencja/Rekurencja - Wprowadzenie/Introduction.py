"""Napisz program, który (używając rekurencji) zwróci sumę elementów w tablicy T"""
def rek(T,i):
    n=len(T) #zwracam długość tablicy
    if i>(n-1): #Warunek końca
        return 0
    return T[i] + rek(T, i+1)

T=[2,4,5,6]
print(rek(T,0))

"""
T[0]=2 + rek(T,1) 
T[1]=4 + rek(T,2)
T[2]=5 + rek(T,3)
T[3]=6 + rek(T,4)


rek(T, 4) zwraca 0. (Warunek końca i>n-1)
To jest wartość zwrócona z warunku końca. Komputer zapisuje tę wartość i przekazuje ją do funkcji rek(T, 3).

rek(T, 3) oblicza T[3] + rek(T, 4) (czyli 6 + 0 = 6) i zwraca tę wartość.

Wartość 6 jest przekazywana wyżej, do rek(T, 2).
rek(T, 2) oblicza T[2] + rek(T, 3) (czyli 5 + 6 = 11) i zwraca tę wartość.

Wartość 11 jest przekazywana wyżej, do rek(T, 1).
rek(T, 1) oblicza T[1] + rek(T, 2) (czyli 4 + 11 = 15) i zwraca tę wartość.

Wartość 15 jest przekazywana wyżej, do rek(T, 0).
rek(T, 0) oblicza T[0] + rek(T, 1) (czyli 2 + 15 = 17) i zwraca tę wartość.

Czyli funkcja tak naprawdę oblicza sumę tablicy w ten sposób (idąc od końca do początku):
0
6+0
5+6+0
4+5+6+0
2+4+5+6+0

"""

#######################################
"Napisz funkcję, która zwróci n-ty element ciągu Fibonacciego"
def fib_rek(n):
    if n==1 or n==2:
        return 1
    return fib_rek(n-1)+fib_rek(n-2)

n=6
print(fib_rek(n))

#####################################
"""Napisz funkcję, która sprawdza, czy w tablicy T (skł. się z wartości True, False)
występuje min. jedna wartość True"""
def rek(T,i):
    n=len(T)
    if i>(n-1):
        return False

    return T[i] or rek(T, i+1)

T=[False,False,False,True,False]
print(rek(T,0))

#####################################
"""Napisz funkcję, która sprawdza, czy w tablicy T
występują same wartości True"""
def rek(T,i):
    n=len(T)
    if i==(n-1):
        return T[i]
    if i>(n-1):
        return False

    return T[i] and rek(T, i+1)

T=[True,True,True,True]
print(rek(T,0))

"""Napisz funkcję, która sprawdza, czy w tablicy T (skł. się z wartości True, False)
występują gdziekolwiek dwie wartości True z rzędu"""
def rek(T,i):
    n=len(T)
    if i==(n-2):
        return T[i] and T[i+1]

    return (T[i] and T[i+1]) or rek(T, i+1)

T=[True,False,True,False,True,True,False]
print(rek(T,0))

