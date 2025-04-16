"""Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu. (którykolwiek z narożników)"""

from math import log10

def num_length(num):
    return int(log10(num))+1

def check_if_closer(w,k,w_end,k_end,move):
    return (w+move[0]-w_end)**2+(k+move[1]-k_end)**2 < (w-w_end)**2+(k-k_end)**2

def zad152(T,w,k):
    moves = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1),(-1,1)]
    M=[[-1 for _ in range(len(T))] for _ in range(len(T))]
    corners=[(0,0),(0,len(T)-1),(len(T)-1,0),(len(T)-1, len(T)-1)]

    def rek(w,k,ec):
        w_end = ec[0]
        k_end = ec[1]

        if w==w_end and k==k_end:
            return True
        else:

            #Rozważamy wszystkie narożniki, a zatem ruchy w każdym kierunku
            for i in range(8):
                el = moves[i]
                #Dochodzi dolny warunek wyjścia poza tablicę (sprawdzamy możliwość wykonania ruchu)
                if -1<w+el[0]<len(T) and -1<k+el[1]<len(T) and check_if_closer(w,k,w_end,k_end,el):
                    next_move = T[w+el[0]][k+el[1]]

                    if T[w][k]%10 < next_move//10**(num_length(next_move)-1):
                        if rek(w+el[0],k+el[1],ec):
                            M[w][k]=i
                            return True

            return False

    for ec in corners:
        if rek(w,k,ec):
            for el in M:
                print(el)
            return True
    return False

T=[[14,1,2],[51,21,3],[4,5,6]]

print(zad152(T,1,1))
