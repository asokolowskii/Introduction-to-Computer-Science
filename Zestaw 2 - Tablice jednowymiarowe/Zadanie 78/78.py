"""Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
"""

T=[1,3,7,4,15,5,6,7,8,9,16]

def sum_index_element(T):
    n=len(T)
    maxi=0
    for i in range(n-1): #bo szukam podciągów stąd nie n a n-1
        sum_el=T[i]
        sum_index=i
        cnt=1
        if T[i]<T[i+1]:
            for j in range(i+1,n):
                if not T[j-1]<T[j]:
                    break
                else:
                    sum_el+=T[j]
                    sum_index+=j
                    cnt+=1
                    if sum_el==sum_index:
                        maxi=max(maxi,cnt)
    return maxi

print(sum_index_element(T))

