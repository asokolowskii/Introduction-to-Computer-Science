"""
Dana jest lista, która zakończona jest cyklem.
Napisać funkcję, która zwraca liczbę elementów przed cyklem
"""

class Node:
    def __init__(self,val=None, next=None):
        self.val=val
        self.next=next

def zad198(p):
    slow=p
    fast=p
    """W tym fragmencie używamy algorytmu "żółwia i zająca" do wykrycia cyklu w liście.
    Jeśli slow == fast, oznacza to, że oba wskaźniki znajdują się wewnątrz cyklu."""
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break

    """Po wykryciu cyklu przestawiamy wskaźnik slow na początek listy."""
    slow=p
    cnt=0
    """Teraz przesuwamy oba wskaźniki (slow i fast) o jeden krok na raz."""
    """Liczymy kroki (cnt), aż slow i fast spotkają się ponownie. 
    To miejsce spotkania to początek cyklu."""
    while slow!=fast:
        slow=slow.next
        fast=fast.next
        cnt+=1
    return cnt








