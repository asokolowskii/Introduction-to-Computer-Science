# Proszę napisać program poszukujący trójkątów Pitagorejskich,
#w których długość przeciwprostokątnej jest mniejsza od liczby N wprowadzonej z klawiatury.
from math import sqrt
N  = int(input())
for a in range(1, N):
    for b in range(a, N):
        c = int(sqrt(a**2 + b**2))
        if c**2 == (a**2 + b**2) and c < N:
            print(a,b,c, end=", ")


