"""
Problem wież w Hanoi (treść oczywista)
"""

def move(from_start, to_end):
    print("Move", from_start, "to", to_end)

"""
Parameters:
    - n: Number of disks
    - A: The starting rod
    - B: The auxiliary rod
    - C: The target rod
"""

def tower_of_hanoi(n,A,B,C):
    if n==0:
        return
    if n==1:
        move(A,C)
        return
    else:
        tower_of_hanoi(n-1,A,C,B)
        move(A,C)
        tower_of_hanoi(n-1,B,A,C)
    #end def

n=int(input())
print(tower_of_hanoi(2,'A','B','C'))