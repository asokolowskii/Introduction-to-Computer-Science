"""Dana jest lista, która być może zakończona jest cyklem.
Napisać funkcję, która sprawdza ten fakt."""

class Node:
    def __init__(self,val=None, next=None):
        self.val=val
        self.next=next

def zad196(p):
    slow=p
    fast=p
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False











