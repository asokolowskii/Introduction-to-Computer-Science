"""
Proszę napisać funkcję usuwającą ostatni element listy.
Do funkcji należy przekazać wskazanie na pierwszy element listy.
"""

class Node:
    def __init__(self,val, next=None):
        self.val=val
        self.next=next

def remove_at_end(p):
    start=p
    while p.next.next:
        p=p.next

    p.next=None
    return start