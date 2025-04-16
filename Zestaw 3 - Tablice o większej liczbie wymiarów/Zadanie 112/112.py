"""
Dana jest plansza o wymiarach NxN zawierająca wartości 0 i 1. Pola o wartości 1 zawierają
pułapki. Skoczek musi dotrzeć z górnego wiersza planszy do dolnego. Każdy ruch skoczka musi go przybliżać
do dolnego wiersza. Proszę napisać program, który zwraca długość najkrótszej bezpiecznej drogi skoczka z
wiersza górnego do wiersza dolnego.
"""

def pulapka_na_skoczka(T):
    n = len(T)
    # Możliwe ruchy skoczka przybliżające do dolnego wiersza
    moves = [(2, 1), (2, -1), (1, 2), (1, -2)]

    # Inicjalizacja tablicy minimalnych odległości
    min_odl = [[float('inf')] * n for _ in range(n)]

    # Ustawienie wartości początkowych dla pierwszego wiersza
    for col in range(n):
        if T[0][col] == 0:
            min_odl[0][col] = 0

    # Przeglądanie wierszy tablicy
    for row in range(n - 1):  # Od górnego wiersza do przedostatniego
        for col in range(n):
            if min_odl[row][col] == float('inf'):
                continue  # Pole nieosiągalne, pomijamy

            for move in moves:
                new_row, new_col = row + move[0], col + move[1]

                # Sprawdzenie, czy ruch mieści się w tablicy
                if 0 <= new_row < n and 0 <= new_col < n:
                    # Sprawdzenie, czy pole docelowe nie zawiera pułapki
                    if T[new_row][new_col] == 0:
                        min_odl[new_row][new_col] = min(
                            min_odl[new_row][new_col], min_odl[row][col] + 1
                        )

    # Znalezienie minimalnej odległości w dolnym wierszu
    result = min(min_odl[n - 1])

    # Jeśli nie znaleziono drogi, zwracamy -1
    return result if result < float('inf') else -1

# Przykład użycia
T = [[1, 0, 1],
     [1, 1, 0],
     [0, 0, 1]]

print(pulapka_na_skoczka(T))  # Wynik: 3





