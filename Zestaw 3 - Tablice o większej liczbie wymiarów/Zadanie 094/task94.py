"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą.
"""

def at_least_one_even(num):
    while num!=0:
        next_digit=num%10
        num=num//10
        if next_digit%2==0:
            return True
    return False

def check_row(row):
    for el in row:
        if not at_least_one_even(el):
            return False
    return True

def check_tab(T):
    for row in T:
        if check_row(row):
            return True
    return False

T=[[32,55,67], [15,3,5], [17,45,77]]
print(check_tab(T))