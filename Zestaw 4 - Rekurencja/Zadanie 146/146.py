"""
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2
"""

def zad146(n):
    T = [0 for _ in range(n)] #Tworzę tablicę długości n (tyle jedynek ma nasza liczba) wypełnioną zerami
    def rek(n, i, T): #Tworzę funkcję rek, n-zadana liczba, i-aktualny indeks w tablicy T, T-tablica zer
        if n==0: #Warunki końca
            print(T)
        if i==0:
            mini=1
        else: mini = T[i-1]

        for j in range(mini, n+1):
            T[i]=j
            rek(n-j,i+1,T)
            T[i]=0

    rek(n,0,T)
print(zad146(4))
