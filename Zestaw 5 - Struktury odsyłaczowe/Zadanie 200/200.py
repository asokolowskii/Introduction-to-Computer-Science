"""
Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w drugiej. Do funkcji
należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną.
"""

class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

def print_list(p):
    while p is not None:
        print(str(p.val)+'->',end='')
        p=p.next

def contains(p,q):
    def function(p,q):
        first_p = p
        first_q = q

        while p is not None:

            if q is None:
                return True

            if p.val==q.val:
                q=q.next
                p=p.next

            else:
                p=p.next
                q=first_q

        if p==None and q==None:
            return True
        return False

    return function(q,p) or function(p,q)




