"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr.
"""

def only_odd(num):
    while num!=0:
        next_digit=num%10
        num=num//10
        if next_digit%2==0:
            return False
    return True

def check_row(row):
    for el in row:
        if only_odd(el):
            return True
    return False

def check_tab(T):
    for row in T:
        if not check_row(row):
            return False
    return True

T = [ [6,2,15], [15,4,15], [44,6,92] ]
print(check_tab(T))