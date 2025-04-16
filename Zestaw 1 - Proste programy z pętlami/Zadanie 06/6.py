# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona (metodą Newtona-Raphsona)
n = int(input("Z jakiej liczby chcesz policzyć pierwiastek?  "))
a = n/2
b = n/a
eps = 1e-6
while abs(n-a*a)>eps:
    a=(a+b)/2
    b=n/a

print(a)

#Drugi sposób z wykorzystaniem wzoru: a_n+1 = (a1 + n/a1)*0.5
n = int(input())
eps = 1e-6

a1 = n/2
a2 = (a1 + n/a1)*0.5 #To jest to samo, co na górze, czyli (a1 + a2)/2 to jest drugi bok w drugiej iteracji

while abs(a2-a1)>eps:
    a1=a2
    a2=(a1+n/a1)*0.5

print(a2)
