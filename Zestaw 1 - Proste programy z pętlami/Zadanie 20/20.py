"""Dla ciągu z poprzedniego zadania proszę znaleźć najmniejszy wyraz początkowy N, dla
którego ciąg osiąga wartość 1 dokładnie po N krokach."""

N = int(input())
def liczba_krokow(A):
    cnt=0
    while A!=1:
        cnt+=1
        A = (A%2) * (3*A + 1) + (1- A%2) * (A/2)

    return cnt == N

def ciag_w_n_krokach():
    for i in range(2, 10001):
        if liczba_krokow(i):
            return i

    return None


print(ciag_w_n_krokach())


