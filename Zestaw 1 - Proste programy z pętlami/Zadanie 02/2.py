# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

a, b = 1, 1
while a < 1000000:
    print(a, end=" ")
    a, b = b, a+b

