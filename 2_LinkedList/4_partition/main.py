"""
    Write code to partition a linked list aroudn a value x, such that all nodes less than x come before all nodes 
    greater or equal to x. If x is contained within a list, the values of x only need to be after the elements less than x 
    The partition element x can appear anywhere in the "right partition"; it does not need to be appear between the left and 
    the right partition

    Example: 
        Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
        Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from ..linkedlist import * 

def partition(ll, x):  
    p1 = None
    p2 = ll.head 

    while p2.data >= x:
        p2 = p2.next 

    p1 = p2 #first value that smaller than x 

    while p2.next != None:   
        if p2.next.data > x:
            p2 = p2.next 
        else:
            #remove tmp after p2 
            tmp = p2.next 
            p2.next =p2.next.next 
            #append tmp before p1
            tmp.next = p1
            p1 = tmp 
    ll.head = p1


sll = SingleLinkedList()
data = [3, 5, 8, 5, 10, 2, 1]
data2 = [6, 3, 5, 8, 5, 10, 2, 1, 8]
for dt in data2:
    sll.add_tail(dt)

sll.print_list()
partition(sll, 5)
sll.print_list()