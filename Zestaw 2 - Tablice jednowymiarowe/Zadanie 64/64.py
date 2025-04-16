"""Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym
wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
"""

def sprawdz_ciag(N):
    biggest_n = [0]*N
    while True:
        x=int(input("Podaj liczbę: "))
        if x==0:
            break

        for i in range(N):
            if x>biggest_n[i]:
                x, biggest_n[i]=biggest_n[i], x

    return biggest_n[-1]

print(sprawdz_ciag(10))
