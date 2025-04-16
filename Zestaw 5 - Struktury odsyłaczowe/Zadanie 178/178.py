"""
Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
"""

class Node:
    def __init__(self,val,next):
        self.val=val
        self.next=next

def reverse_linked_list(head):
    prev,curr=None,head
    while curr:
        next_node=curr.next
        curr.next=prev
        prev,curr=curr,next_node
    return prev

c=Node(3,None)
b=Node(2,c)
a=Node(1,b)

print(reverse_linked_list(a))

while c:
    print(c.val)
    c=c.next

