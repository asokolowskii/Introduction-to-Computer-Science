"""Dana jest N-elementowa tablica T wypełniona liczbami naturalnymi. Proszę napisać
funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
podciągu lub wartość 0 jeżeli taki podciąg nie istnieje."""

T=[1,3,5,7,7,5,3,1]

def is_odd(a):
    return a%2==1

def palindrom(T,a,b):
    n=len(T)
    cnt=0
    i=0
    while a-i>=0 and b+i<n:
        if not T[a-i]==T[b+i]:
            return cnt

        if is_odd(T[a-i]) and is_odd(T[b+i]):
            cnt+=2
            i+=1
        else:
            return cnt
    #end while
    return cnt

def zlicz_palindrom(T):
    n=len(T)
    maxi=0
    for i in range(1,n-1):
        if is_odd(T[i]):
            if is_odd(T[i+1]) and T[i]==T[i+1]:
                maxi=max(maxi, palindrom(T, i, i+1))
            maxi=max(maxi, palindrom(T,i-1,i+1)+1)
    #end for
    return maxi

print(zlicz_palindrom(T))