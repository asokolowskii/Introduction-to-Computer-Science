"""Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
wartości prawdopodobieństwa dla N z zakresu 20-40."""

from random import randint

def birthday_chance(n):
    if n<2:
        return 0
    if n>=366:
        return 1

    szansa=1
    for i in range(n):
        szansa*=(365-i)/365.0
    return 1-szansa

def probability_birth(n):
    dni_roku = [0 for i in range(366)]
    cnt=0

    for _ in range(100):
        for i in range(n):
            birthday = randint(0,365)
            dni_roku[birthday]+=1

        for el in dni_roku:
            if el>=2:
                cnt+=1
                break

        dni_roku = [0 for i in range(366)]

    return cnt/100

n=int(input())
print(birthday_chance(n))
print(probability_birth(n))