# Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
#analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

suma = 10000
wyrazy = (1,1)

for i in range(1, 2025):
    a = i
    b = 2024


    while a > 0 and b > a:
        a, b = b-a, a
        print(a,b)

    if a+b < suma:
        wyrazy = (a, b)
        suma = a+b

print(suma, wyrazy)




