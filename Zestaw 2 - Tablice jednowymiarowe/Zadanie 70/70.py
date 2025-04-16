"""Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym
wyznacza długość najdłuższego, spójnego podciągu geometrycznego."""

def ciag_geometr(T):
    n=len(T)
    cnt=2
    maxi=2
    q=round(T[1]/T[0])
    for i in range(2,n):
        if round(T[i]/T[i-1])==q:
            cnt+=1
        else:
            maxi=max(maxi,cnt)
            cnt=2
            q=round(T[i]/T[i-1])

    return max(maxi,cnt)

T=[1,2,4,8,16,10,5,2.5,1.25,0.625, 0.3125, 1,2,3]
print(ciag_geometr(T))
