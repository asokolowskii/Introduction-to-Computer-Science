"""
Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′ →
117, 108, 97 oraz ′′exe′′ → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza
czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1.
Dodatkowo funkcja powinna wypisać znaleziony wyraz.
"""

def czy_samogloska(ch):
    samogloski = ['a','e','y','i','o','u']
    return 1 if ch in samogloski else 0

def wyraz(s1,s2):
    samogloski_s1=0
    suma_ascii_s1=0

    for i in range(len(s1)):
        samogloski_s1+=czy_samogloska(s1[i])
        suma_ascii_s1+=ord(s1[i])

    def rek(i,suma_ascii,cnt):
        if i==len(s2):
            return suma_ascii==suma_ascii_s1 and cnt==samogloski_s1

        return rek(i+1,suma_ascii,cnt) or rek(i+1,suma_ascii+ord(s2[i]),cnt+czy_samogloska(s2[i]))

    return rek(0,0,0)
