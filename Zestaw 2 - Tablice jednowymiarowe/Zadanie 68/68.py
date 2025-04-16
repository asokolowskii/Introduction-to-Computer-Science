"""Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnymi
wyznacza długość najdłuższego, spójnego podciągu rosnącego."""

def ciag_rosnacy(T):
    n=len(T)
    cnt=1
    maxi=1

    for i in range(1,n):
        if T[i]>T[i-1]:
            cnt+=1
        else:
            maxi=max(maxi,cnt)
            cnt=1

    return max(maxi,cnt)

T=[1,2,3,4,5,6,7,8,9]
print(ciag_rosnacy(T))