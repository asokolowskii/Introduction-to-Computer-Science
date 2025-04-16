"""
Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2.
Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
??bartek??leszek??marek??ola??zosia?? .Proszę napisać stosowne
definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem zasady poprzedzania. Do funkcji należy
przekazać wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą, czy
udało się wstawić napis do listy. Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo
wstawiony element.
"""

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zad209(p,string):
    first=string[0]
    last=string[-1]
    start=p
    while p.next!=start:
        word1=p.val
        word2=p.next.val
        if ord(word1[-1])<ord(first) and ord(word2[0])>ord(last):
            a=Node(string) #Tworzymy nowy węzeł z wartością string.
            a.next=p.next #nowy węzeł wskazuje na następny węzeł w liście.
            p.next=a #bieżący węzeł wskazuje na nowy węzeł.
            p=p.next
            return True
        p=p.next
    return False
