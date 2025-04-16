"""
Dana jest lista, która zakończona jest cyklem.
Napisać funkcję, która zwraca liczbę elementów w cyklu.
"""

class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def zad197(p):
    """
    Ustawiamy dwa wskaźniki na początek listy:
    -slow przesuwa się o jeden krok na raz.
    -fast przesuwa się o dwa kroki na raz.
    """
    slow=p
    fast=p

    """Wykrywanie cyklu (algorytm "żółwia i zająca")"""
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next

        """Jeśli lista zawiera cykl, slow i fast na pewno się spotkają w cyklu."""
        if slow==fast:
            break

    cnt=1
    """
    Przesuwamy wskaźnik slow o jeden krok na raz, 
    zaczynając od elementu po punkcie spotkania.
    """
    slow=slow.next
    while slow!=fast:
        slow=slow.next
        cnt+=1

    """Po zakończeniu liczenia funkcja zwraca długość cyklu."""
    return cnt







