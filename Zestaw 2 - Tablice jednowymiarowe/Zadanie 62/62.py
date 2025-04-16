"""Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa."""

def is_prime(N):
    is_prime = [True]*(N+1)
    is_prime[0]=is_prime[1]=False #0 i 1 nie są liczbami pierwszymi
    for i in range(2, int(N**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,N+1, i):
                is_prime[j]=False

    primes = [i for i in range(2, N+1) if is_prime[i]]
    return primes

N=int(input())
print(is_prime(N))

