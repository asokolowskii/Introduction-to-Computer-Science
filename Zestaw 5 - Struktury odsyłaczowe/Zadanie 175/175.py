"""
Zadanie 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
1. czy element należy do zbioru
2. wstawienie elementu do zbioru
3. usunięcie elementu ze zbioru
"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    #czy element należy do zbioru
    def search(self,target):
        current=self.head
        while current:
            if current.val==target:
                return True
            current=current.next
        return False

    def get_length(self):
        cnt=0
        itr=self.head
        while itr:
            cnt+=1
            itr=itr.next
        return cnt

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node


    #wstawienie elementu do zbioru
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            print("Niepoprawny indeks!")
            return

        if self.search(data):
            print("Ten element już jest w zbiorze!")
            return

        if index==0:
            self.insert_at_beginning(data)
            return

        cnt=0
        itr=self.head
        while itr:
            if cnt==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            cnt+=1

    #usunięcie elementu ze zbioru
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            print("Niepoprawny indeks!")
            return
        if index==0:
            self.head=self.head.next
            return

        cnt=0
        itr=self.head
        while itr:
            if cnt==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            cnt+=1


d=Node(4,None)
c=Node(3,d)
b=Node(2,c)
a=Node(1,b)

ll=LinkedList()
ll.head=a

print(ll.search(4))


