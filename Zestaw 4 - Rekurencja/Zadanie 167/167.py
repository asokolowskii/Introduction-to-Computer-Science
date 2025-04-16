"""Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na co najmniej
 dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
 zwraca liczbę sposobów pocięcia słowa na kawałki."""

def czy_samogloska(l):
    samogloski=['a','e','y','i','o','u']
    return 1 if l in samogloski else 0

def cut_word(s):
    def rek(s,i,cnt):

        if i ==len(s):
            return 1 if cnt==1 else 0 #Jeśli w ostatnim fragmencie jest jedna samogłoska zwracam 1, inaczej 0
        if cnt>1: #Jeśli liczba znalezionych samogłosek >1 zwracam 0
            return 0

        cont = rek(s,i+1, cnt+czy_samogloska(s[i])) #kontynuujemy bieżący fragment dopóki cnt<2

        new=0
        if cnt==1:
            new = rek(s,i+1, czy_samogloska(s[i])) #rozpoczynamy nowy fragment,
            #gdzie sprawdzamy czy pierwsza litera jest samogłoską


        return cont + new

    return rek(s,0,0)

print(cut_word("anakonda"))
