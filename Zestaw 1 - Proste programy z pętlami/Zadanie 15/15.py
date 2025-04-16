"""
Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb naturalnych.
"""

def NWD(a,b):
    while b>0:
        a,b = b, a%b
    return a

a = int(input())
b = int(input())
c = int(input())

print(NWD(NWD(a,b), c))