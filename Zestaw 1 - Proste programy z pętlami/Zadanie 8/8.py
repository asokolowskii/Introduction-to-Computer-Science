# Proszę napisać program rozwiązujący równanie
# x**x = 2024 metodą bisekcji.

# Definicja funkcji f(x) = x^x - 2024
def f(x):
    return x**x - 2024

# Funkcja rozwiązująca równanie metodą bisekcji
def bisection_method(eps=1e-2):
    a, b = 0, 5
    if f(a)*f(b) > 0:
        return None #brak zmiany znaku funkcji na końcach przedziału

    while abs(a-b)>eps:
        x = (a+b)/2
        if f(x) == 0:
            return x
        elif f(a)*f(x)<0: #nowy przedział to [a, x]
            b = x
        else: #nowy przedział to [x,b]
            a = x

    return (a+b)/2

print(bisection_method(eps=1e-2))
