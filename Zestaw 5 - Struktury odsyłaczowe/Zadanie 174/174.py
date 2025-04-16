"""
Zliczanie elementów łańcucha
"""
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def get_length(self):
        itr = self.head
        cnt=0
        while itr:
            cnt+=1
            itr=itr.next
        return cnt

d=Node(4,None)
c=Node(3,d)
b=Node(2,c)
a=Node(1,b)

ll=LinkedList()
ll.head=a

print(ll.get_length())