"""
Proszę napisać funkcję wstawiającą na koniec listy nowy element.
Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość.
"""
class Node:
    def __init__(self,val, next=None):
        self.val=val
        self.next=next


def insert_at_end(p, value):
    head=p
    while p.next:
        p=p.next
    p.next=Node(value)
    return head