"""Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0
oraz wartość False w przeciwnym przypadku.
"""
def zadanie101(T):
    n=len(T) #rozmiar tablicy
    column_has_zero=[False for _ in range(n)] #sprawdzam, czy każda kolumna ma zero

    for y in range(n):
        row_has_zero=False #Czy wiersz ma zero?
        for x in range(n):
            if T[y][x]==0:
                row_has_zero=True
                column_has_zero[x]=1
        # Jeśli po przejściu wiersza nie znaleziono zera, zwracamy False

    for el in column_has_zero:
        if not el:
            return False
    return True

T=[[0,2,8,4],[1,3,5,0],[2,7,0,6],[6,0,1,8]]
print(zadanie101(T))


