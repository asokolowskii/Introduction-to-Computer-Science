"""Napisać funkcję, która dla N-elementowej tablicy T wypełnionej
liczbami naturalnymi wyznacza długość najdłuższego, spójnego podciągu arytmetycznego."""

def ciag_arytm(T):
    n=len(T)
    cnt=2
    maxi=2
    r=T[1]-T[0]
    for i in range(2,n):
        if T[i]-T[i-1]==r:
            cnt+=1
        else:
            maxi=max(maxi,cnt)
            cnt=2
            r=T[i]-T[i-1]

    return max(maxi,cnt)

T = [1,4,7,10,11,12,13,14,15,5,2]
print(ciag_arytm(T))