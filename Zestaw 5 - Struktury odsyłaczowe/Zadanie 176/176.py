"""
Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy
funkcje:
• inicjalizującą tablicę,
• zwracającą wartość elementu o indeksie n,
• podstawiającą wartość value pod indeks n.
"""

class Node:
    def __init__(self,ind,val,next=None):
        self.val=val ## Wartość elementu
        self.next=next ## Wskaźnik na następny węzeł
        self.ind=ind ## Indeks elementu

class SparseArray:
    def __init__(self):
        # Inicjalizacja tablicy jako pustej listy odsyłaczowej
        self.head=None

#zwraca wartość elementu o indeksie n
    def get_value(self,ind):
        itr=self.head
        while itr:
            if itr.ind==ind:
                return itr.val
            itr=itr.next
        return None

#podstawia wartość value pod indeks n
    def insert_at(self,ind,val):
        # Wstawianie na początek
        if self.head is None or self.head.ind>ind:
            self.head=Node(ind,val,self.head)
            return

        p=self.head
        # Sprawdzenie czy aktualny węzeł ma taki sam indeks
        if p.ind==ind:
            p.val=val
            return

        # Przechodzimy przez listę, szukając miejsca do wstawienia
        while p.next and p.next.ind<ind:
            p=p.next

        # Aktualizacja wartości w istniejącym węźle
        if p.next and p.next.ind==ind:
            p.next.val=val

        # Wstawianie nowego węzła
        else:
            q=Node(ind,val,p.next)
            p.next=q