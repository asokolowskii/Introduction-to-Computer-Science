"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
element do sumy elementów wiersza w którym leży element jest największa.
"""

def sum_of_row(T,row):
    n=len(T)
    sum=0
    for i in range(n):
        sum+=T[row][i]
    return sum

def sum_of_col(T,col):
    n=len(T)
    sum=0
    for i in range(n):
        sum+=T[i][col]
    return sum

def iloraz(T):
    n=len(T)
    maxi=0
    max_col,max_row=0,0
    for row in range(n):
        for col in range(n):
            ilo = sum_of_col(T,col)/sum_of_row(T,row)
            if ilo>maxi:
                maxi=ilo
                max_col,max_row=col,row

    return max_col,max_row

T=[[2,4,5],[3,6,7],[15,4,3]]
print(iloraz(T))