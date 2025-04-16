"""
Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej
liście liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby
występujące w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
łączną liczbę usuniętych elementów.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def zad202(p, q):
    dummy_p = Node(None, p)
    dummy_q = Node(None, q)
    cnt = 0

    prev_q = dummy_q
    curr_q = q

    while curr_q:
        val = curr_q.val

        # Try to find val in list p (sorted)
        prev_p = dummy_p
        curr_p = dummy_p.next
        while curr_p and curr_p.val < val:
            prev_p = curr_p
            curr_p = curr_p.next

        if curr_p and curr_p.val == val:
            # Delete from both lists
            prev_p.next = curr_p.next
            prev_q.next = curr_q.next
            cnt += 2  # removed from both

            curr_q = prev_q.next  # move forward in q after deletion
        else:
            prev_q = curr_q
            curr_q = curr_q.next

    return cnt, dummy_p.next, dummy_q.next  # zwracamy także nowe głowy list







        
