"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
się znaleźć taki ciąg oraz długość tego ciągu.
"""

def zad99(T):
    n=len(T)
    maxi=0
    for i in range(n):
        for j in range(n):
            k=0
            length=2
            while i+k<n-2 and j+k<n-2:
                q=T[i+k+1][j+k+1]/T[i+k][j+k]
                if T[i+k+2][j+k+2]/T[i+k+1][j+k+1] == q:
                    length+=1
                    k+=1
                else:
                    break
            if length>=3:
                maxi=max(maxi, length)

    return maxi




