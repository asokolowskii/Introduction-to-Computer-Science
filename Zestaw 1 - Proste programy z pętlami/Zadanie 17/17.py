# Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
from math import pi
from math import floor
def cos(x):
    eps = 1e-4 #dokładność
    c=0 #suma szeregu
    w=1 #pierwszy wyraz szeregu
    i=0 #indeks wyrazu

    while abs(w) >= eps:
        c+=w
        i+=1
        w*=((-1)*(x**2))/((2*i -1)*(2*i))

    return c

print(cos((3*pi)/4))