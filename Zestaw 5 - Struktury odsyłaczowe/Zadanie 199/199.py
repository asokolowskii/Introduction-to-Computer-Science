"""
Dana jest lista, która zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
ostatniego elementu przed cyklem.
"""

class Node:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def zad199(p):
    slow=p
    fast=p
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break

    slow=p
    while slow.next!=fast.next:
        slow=slow.next
        fast=fast.next
    return slow.val

