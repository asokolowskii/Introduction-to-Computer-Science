"""Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! +
1/1! + 1/2! + 1/3! + ..."""

def euler(eps):
    e = 2
    fact = 1
    i = 2

    next_elem = 1/fact
    while next_elem > eps:
        fact*=i
        i +=1
        next_elem = 1/fact
        e+=next_elem

    return e

print(euler(1e-6))