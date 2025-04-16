"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi.
"""

def sum_of_row(T,r):
    sum=0
    for i in range(len(T)):
        sum+=[r][i]
    return sum

def sum_of_column(T,c):
    sum=0
    for i in range(len(T)):
        sum+=[i][c]
    return sum

def zad111(T):
    n=len(T)
    biggest_sum=-float('inf')
    for r in range(n):
        for c in range(n):
            for y in range(n):
                for x in range(n):
                    if r!=y and c!=x:
                        sum = sum_of_row(T,r)+sum_of_row(T,y)+sum_of_column(T,c)+sum_of_column(T,x)-2*T[r][c]-2*T[y][x]-T[r][x]-T[y][c]
                        biggest_sum=max(sum,biggest_sum)

    return biggest_sum

