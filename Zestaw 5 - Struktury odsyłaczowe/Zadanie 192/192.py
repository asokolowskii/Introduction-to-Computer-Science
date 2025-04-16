"""Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji
należy przekazać wskazanie na pierwszy element listy."""

class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def uniq_elem(p):
    guard=Node(0,p)
    prev=guard
    current=p

    while current:
        has_duplicate=False

        while current.next and current.val==current.next.val:
            current=current.next
            has_duplicate=True

        if has_duplicate:
            prev.next=current.next
        else:
            prev=prev.next

        current=current.next

    return guard.next


