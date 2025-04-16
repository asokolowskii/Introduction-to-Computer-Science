"""
Dane są ciągi: An+1 =√An ∗ Bn oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do wspólnej
granicy nazywanej średnią arytmetyczno-geometryczną. Proszę napisać program
wyznaczający średnią arytmetyczno-geometryczną dwóch liczb naturalnych.
"""
from math import sqrt
def srednia(A,B):
    eps = 1e-6
    while abs(A-B)>eps:
        A = sqrt(A*B)
        B = (A+B)/2.0

    return A

A = int(input())
B = int(input())
print(srednia(A,B))
