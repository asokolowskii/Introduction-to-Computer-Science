"""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe
o jeden ruch skoczka szachowego.
"""

def pary(T,iloczyn):
    n=len(T)
    cnt=0
    # Kierunki "naprzód", aby uniknąć liczenia w obu kierunkach
    moves = [(1, 2), (2, 1), (1, -2), (2, -1)]
    for row in range(n):
        for col in range(n):
            for k in moves:
                if 0<=row+k[0]<n and 0<=col+k[1]<n:
                    if T[row][col]*T[row+k[0]][col+k[1]]==iloczyn:
                        cnt+=1

    return cnt


