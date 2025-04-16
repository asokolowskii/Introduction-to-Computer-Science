"""Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym."""

def palindrom(a):
    temp = a
    rev = 0
    while a>0:
        digit=a%10
        rev = rev*10+digit
        a=a//10
    return rev==temp

def palindrom_string(n):
    return n==n[::-1]

def dec_to_bin(a):
    result=""
    while a>0:
        digit=a%2
        a=a//2
        result = str(digit)+result
    return result

def palindrom_dec_bin(a):
    decimal_palindrom=palindrom(a)
    binary_palindrom=palindrom_string(dec_to_bin(a))
    if decimal_palindrom and binary_palindrom:
        return "Jest palindromem zarówno w systemie dziesiętnym, jak i dwójkowym"
    elif decimal_palindrom:
        return "Jest palindromem w systemie dziesiętnym"
    elif binary_palindrom:
        return "Jest palindromem w systemie dwójkowym"
    else:
        return "Nie jest palindromem ani w systemie dziesiętnym, ani dwójkowym"

a=int(input())
print(palindrom_dec_bin(a))