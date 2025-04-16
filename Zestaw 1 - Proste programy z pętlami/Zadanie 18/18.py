"""Nieskończony iloczyn... ma wartość 2/π. Proszę napisać program
korzystający z tej zależności i wyznaczający wartość π.
"""

from math import sqrt
def iloczyn(eps):
    a1 = sqrt(0.5)
    pi = a1
    a2 = sqrt(0.5+0.5*a1)

    while abs(a2-a1)>eps:
        a1=a2
        pi*=a1
        a2=sqrt(0.5+0.5*a1)

    return 2/pi

print(iloczyn(1e-6))