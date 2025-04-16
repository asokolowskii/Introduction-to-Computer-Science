# Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
#Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2

n=int(input())
a1 = 1
suma = 1
cnt=1

while suma <= n:
    a1 = a1+2
    suma+=a1
    cnt += 1

print(cnt-1)




