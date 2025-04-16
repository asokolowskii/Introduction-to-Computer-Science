class Node:
    def __init__(self,val=None, next=None):
        self.val=val
        self.next=next

def print_list(head):
    print('GUARDIAN ->', end='')
    while head.next!=None:
        print(str(head.next.val)+'->',end='')
        head=head.next
    print('KONIEC')

def list_to_linked_list(list):
    g=Node()
    for elem in list[::-1]:
        new_node=Node(elem,g.next)
        g.next=new_node
    return g