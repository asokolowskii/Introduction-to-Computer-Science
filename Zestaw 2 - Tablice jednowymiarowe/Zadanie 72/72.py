"""Proszę napisać program, który wypełnia N-elementową tablicę T trzycyfrowymi liczbami
pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu.
Na przykład dla tablicy: t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4."""

from random import randint

def generuj_tablice(N):
    return [randint(100, 999) for _ in range(N)]

def znajdz_najdluzszy_rewers(T):
    n = len(T)
    best_dlugosc = 0

    for i in range(n):
        for j in range(i, n):  # podciąg od i do j włącznie
            podciag = T[i:j+1]
            rewers = podciag[::-1]

            # Sprawdzamy, czy rewers istnieje gdzieś indziej w tablicy
            for k in range(n - len(rewers) + 1):
                if k == i:
                    continue  # pomijamy to samo miejsce
                if T[k:k+len(rewers)] == rewers:
                    best_dlugosc = max(best_dlugosc, len(podciag))
                    break  # nie trzeba sprawdzać dalej dla tej długości

    return best_dlugosc

t = generuj_tablice(30)
print("Tablica:", t)
print(znajdz_najdluzszy_rewers(t))


