from  ..linkedlist import *

"""
    Remove duplicates from an unsorted linked list 
    FOLLOW UP: how do you solve this if addtional buffer is not allowed?
"""

    
def remove_dups_1(ll):
    dups = set()
    
    tmp = ll.head
    while tmp != None:
        x = tmp.data

        if x in dups:
            p = tmp.pre
            n = tmp.next
            p.next = n
            if n != None:    
                n.pre= p 
            del tmp 
            tmp = n    
        else:
            dups.add(x)
            tmp = tmp.next
        
def remove_dups_2(ll):
    cur = ll.head 

    while cur != None:
        runner = cur
        while runner.next != None:
            if runner.next.data == cur.data:
                #remove node 
                runner.next = runner.next.next 
                if runner.next != None:
                    runner.next.pre = runner 
            else:
                runner = runner.next
        cur = cur.next
def main():
    dll = DoubleLinkedList()

    data = [2, 3, 2, 4, 5, 6, 3, 1, 2, 7, 3]
    for dt in data:
        dll.add_tail(dt)
    
    dll.print_list()
    remove_dups_2(dll)
    dll.print_list()

main()