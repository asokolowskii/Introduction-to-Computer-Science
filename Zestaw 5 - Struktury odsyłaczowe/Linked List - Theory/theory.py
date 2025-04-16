"""
Struktury odsyłaczowe - wprowadzenie
"""
class Node: #Reprezentuje pojedynczy węzeł (element) w liście odsyłaczowej.
    def __init__(self, data=None, next=None):
        self.data=data #przechowuje wartość przechowywaną w węźle.
        self.next=next #to wskaźnik do następnego węzła w liście (lub None, jeśli jest to ostatni element).

class LinkedList: #Reprezentuje całą listę odsyłaczową.
    def __init__(self):
        self.head=None #to wskaźnik na pierwszy węzeł listy. Początkowo jest None, bo lista jest pusta.

    def insert_at_beginning(self, data): #Wstawia element na początku listy.
        node = Node(data, self.head) #Tworzy nowy węzeł Node z wartością data oraz aktualnym self.head jako wskaźnikiem next.
        self.head=node #Ustawia self.head na nowo utworzony węzeł, dzięki czemu nowy węzeł staje się początkiem listy.

    def print(self):
        if self.head is None: #Jeśli lista jest pusta (self.head jest None), wypisuje informację i kończy.
            print("Linked list is empty")
            return

        itr = self.head
        llstr= ''
        while itr: #W przeciwnym razie iteruje po każdym węźle, dodając jego wartość (data) do łańcucha llstr.
            llstr+=str(itr.data) + '-->'
            itr = itr.next
        print(llstr) #Wypisuje całą listę w formacie wartość1-->wartość2-->....

    def insert_at_end(self,data):
        if self.head is None: #Jeśli lista jest pusta (self.head jest None)
            self.head = Node(data,None) #Tworzy nowy węzeł Node i ustawia go jako self.head.
            return

        itr=self.head #Jeśli lista nie jest pusta
        while itr.next: #Iteruje przez listę do ostatniego węzła (itr.next jest None).
            itr = itr.next

        itr.next = Node(data,None) #Ustawia next ostatniego węzła na nowo utworzony węzeł Node.

    def insert_values(self,data_list): #Wstawia wiele elementów z listy data_list.
        self.head=None #Resetuje listę, ustawiając self.head na None.
        for data in data_list: #Iteruje przez podaną listę data_list i dla każdego elementu wywołuje insert_at_end.
            self.insert_at_end(data)

    def get_length(self): #Oblicza długość listy
        cnt=0 #Inicjalizuje licznik cnt na 0.
        itr = self.head
        while itr: #Iteruje przez każdy węzeł listy, zwiększając licznik o 1.
            cnt+=1
            itr=itr.next
        return cnt #Zwraca wartość licznika.


    def remove_at(self,index):
        #Sprawdza, czy indeks jest poprawny
        #(większy lub równy 0, mniejszy niż długość listy). Jeśli nie, wypisuje błąd.
        if index<0 or index>=self.get_length():
            print("Niepoprawny indeks!")
            return
        if index==0: #Jeśli indeks to 0 (pierwszy element)
            self.head=self.head.next #Ustawia self.head na self.head.next, co usuwa pierwszy węzeł.
            return

        #Dla innych indeksów:
        cnt=0
        itr=self.head
        while itr:
            if cnt == index-1: #Iteruje do węzła przed tym, który ma zostać usunięty.
                itr.next=itr.next.next #Ustawia next tego węzła na itr.next.next, pomijając usuwany węzeł.
                break
            itr=itr.next
            cnt+=1

    def insert_at(self,index,data): #Wstawia nowy element o wartości data na pozycji index.
        if index<0 or index>=self.get_length(): #Sprawdza, czy indeks jest poprawny.
            print("Niepoprawny indeks!")
            return

        if index==0: #Jeśli index == 0:
            self.insert_at_beginning(data) #Wywołuje insert_at_beginning, aby wstawić element na początku.
            return

        #Dla innych indeksów:
        count=0
        itr=self.head
        while itr: #Iteruje do węzła przed pozycją index.
            if count==index-1:
                node=Node(data,itr.next) #Tworzy nowy węzeł Node, ustawiając jego next na itr.next.
                itr.next=node #Wstawia nowy węzeł, ustawiając itr.next na nowo utworzony węzeł.
                break
            itr=itr.next
            count+=1


if __name__=='__main__':
    ll=LinkedList()
    # ll.insert_at_beginning(6)
    # ll.insert_at_beginning(77)
    # ll.insert_at_end(97)
    ll.insert_values(["banana","mango","avocado","grapes","orange"])
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_at(3,"apple")
    ll.insert_at(0,"kiwi")
    ll.print()
    print("length: ", ll.get_length())


