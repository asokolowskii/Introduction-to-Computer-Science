"""Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków."""

def liczba_krokow(A):
    cnt=0

    while A!=1:
        cnt+=1
        A = (A%2) * (3*A +1) + (1 - A%2) * (A/2)

    return cnt

def ciag_start():
    max_start = None
    max_steps = 0
    for i in range(1,10001):
        steps = liczba_krokow(i)
        if steps > max_steps:
            max_steps = steps
            max_start = i

    return max_steps, max_start

print(ciag_start())