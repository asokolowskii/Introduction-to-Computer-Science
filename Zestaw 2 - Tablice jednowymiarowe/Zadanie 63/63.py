"""Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! +
1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
"""

def euler(N):
    e=1
    fact=1
    next_digits = [0]*(N+1)
    for i in range(1, N+1):
        fact*=i
        next_digits[i]=(1/fact)
        e+=next_digits[i]
    #end for

    return e, next_digits

print(euler(1000))



