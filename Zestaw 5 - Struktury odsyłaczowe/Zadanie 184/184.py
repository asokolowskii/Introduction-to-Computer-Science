"""
Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.
"""

class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def reverse(p):
    prev,curr=None,p
    while curr:
        next_node=curr.next
        curr.next=prev
        prev,curr=curr,next_node
    return prev

def zad184(p,q):
    rem=0
    head=Node()
    guard=head
    while p and q:
        sume=p.val+q.val+rem
        if sume>=10:
            rem=sume//10
            sume = sume%10
        head.next=Node(sume)
        head=head.next
        p=p.next
        q=q.next

    while p:
        sume=p.val+rem
        if sume>=10:
            rem=sume//10
            sume=sume%10
        head.next=Node(sume)
        head=head.next
        p=p.next

    while q:
        sume=q.val+rem
        if sume>=10:
            rem=sume//10
            sume=sume%10
        head.next=Node(sume)
        head=head.next
        q=q.next

    if rem:
        head.next=Node(rem)

    return guard.next

