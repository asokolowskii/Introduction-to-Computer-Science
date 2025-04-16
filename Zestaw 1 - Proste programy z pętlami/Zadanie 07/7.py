# Proszę zmodyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek
#stopnia 3.

n = int(input())
a1 = 1
a2 = (2*a1 + n/(a1*a1))/3.0
eps = 1e-6

while abs(a2-a1)>eps:
    a1 = a2
    a2 = (2*a1 + n/(a1*a1))/3.0

print(a1)