""" Zamienia liczbę zapisaną w systemie o podstawie `base` (jako int) na system dziesiętny."""
def to_decimal(num, base):
    result = 0
    power = 0

    while num > 0:
        digit = num % 10  # Pobieramy ostatnią cyfrę
        result += digit * (base ** power)
        power += 1
        num //= 10  # Usuwamy ostatnią cyfrę

    return result

print(to_decimal(101, 2))



