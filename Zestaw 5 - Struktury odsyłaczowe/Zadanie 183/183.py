"""
Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
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

def zad184(p):
    rem=0
    head=Node()
    guard=head
    if p:
        p.val+=1
    while p:
        sume=p.val+rem
        if sume>=10:
            rem=sume//10
            sume = sume%10
        head.next=Node(sume)
        head=head.next
        p=p.next

    if rem:
        head.next=Node(rem)
    return guard.next

