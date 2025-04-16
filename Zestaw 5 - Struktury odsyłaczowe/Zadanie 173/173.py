"""
wypisywanie elementów łańcucha
"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def wypisz(head):
    while head!=None:
        print(str(head.val)+'->', end="")
        head=head.next
    print("Koniec")

c=Node(3,None)
b=Node(2,c)
a=Node(1,b)
wypisz(a)
