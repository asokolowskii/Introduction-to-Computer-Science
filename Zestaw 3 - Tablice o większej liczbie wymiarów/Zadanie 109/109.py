"""
Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
maksymalnego podciągu.
"""

def zad109(T):
    n=len(T)
    biggest_sum=-float('inf')

    for row in range(n):
        for col in range(n):
            #Suma podciągu w poziomie
            i=0
            curr_sum=0
            while col+i<n and i<10:
                curr_sum+=T[row][col+i]
                biggest_sum=max(biggest_sum,curr_sum)
                i+=1

            #Suma podciągu w pionie
            i=0
            curr_sum=0
            while row+i<n and i<10:
                curr_sum+=T[row+i][col]
                biggest_sum=max(biggest_sum,curr_sum)
                i+=1

    return biggest_sum


