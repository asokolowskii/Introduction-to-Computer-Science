"""Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę
jedynek, np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2<N1. Proszę napisać
funkcję, która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba
zgodnych elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne
tablice powinny pozostać nie zmieniane.
"""

def count_ones_in_binary(n):
    count = 0
    while n > 0:
        count += n % 2
        n //= 2
    return count

def are_grids_similar(T1, T2):
    N1 = len(T1)
    N2 = len(T2)
    total_elements = N2 * N2

    for i in range(N1 - N2 + 1):  # Slide T2 inside T1 vertically
        for j in range(N1 - N2 + 1):  # Slide T2 inside T1 horizontally
            matching = 0
            for x in range(N2):
                for y in range(N2):
                    if count_ones_in_binary(T1[i + x][j + y]) == count_ones_in_binary(T2[x][y]):
                        matching += 1
            if matching / total_elements > 0.33:
                return True

    return False




