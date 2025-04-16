"""
Wprowadzenie do Linked List
"""


"""Podstawowa struktura"""
class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

"""Wypisanie elementów listy"""
def print_list(head):
    while head!=None:
        print(str(head.val) + '->', end=" ")
        head=head.next
    print("Koniec")

"""Usunięcie elementu z listy"""
def remove_element(p, to_delete):
    prev=None
    start=p

    while p!=None:
        if p.val==to_delete:
            if prev==None:
                return p.next

            else:
                prev.next=prev.next.next
                return start

        prev=p
        p=p.next
    return start

"""Dodanie elementu do listy"""
def add_element(p, to_add):
    prev=None
    start=p

    while p!=None:
        prev=p
        p=p.next

    if prev==None:
        return Node(to_add)
    prev.next=Node(to_add)
    return start

c= Node(3)
b= Node(2,c)
a= Node(1,b)
print(print_list(a))



