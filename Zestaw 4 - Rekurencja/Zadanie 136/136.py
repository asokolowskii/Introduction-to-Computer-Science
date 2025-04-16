"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia
pola szachownicy o wymiarach NxN ruchem skoczka szachowego.
"""
def knights_walk(T, w=0,k=0,cnt=1):
    #Tablica (szachownica z zerami), w - wiersz, k - kolumna, cnt - licznik liczby ruchów
    n = len(T)
    if cnt == n**2: #na każdym polu możemy być dokładnie 1 raz
        return True

    jumps = [(-2,1),(-2,-1),(2,1),(2,-1), (1,2), (1,-2),(-1,-2),(-1,2)]
    for jump in jumps:
        next_w= w + jump[0]
        next_k= k + jump[1]

        if contains(T,next_w,next_k) and T[next_w][next_k]==0:
            #czy nie wychodzimy poza szachownicę    #czy nie byliśmy już na tym polu wcześniej
            if knights_walk(T,next_w,next_k,cnt+1):
                return True

    T[w][k]=0 #jeśli dana ścieżka jest "niedobra" zerujemy szachownicę, startujemy raz jeszcze
    return False #zwracamy False

def contains(T,w,k):
    n=len(T)
    if 0<=w<n and 0<=k<n:
        return True
    return False

T2 = [[0 for _ in range(6)] for _ in range(6)]

print(knights_walk(T2))
for row in T2:
    print(row)


