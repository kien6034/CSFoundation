from ..linkedlist import *

"""Implement an algorithm to find the kth to last element of a singly linked list"""

def find_kth_to_last2(ll, k):
    #O(n) time, O1 space
    p1 = ll.head
    p2 = ll.head

    i = 0
    while p2 != None:
        p2 = p2.next 
        i += 1

        if i == k:
            break 
    
    if i != k:
        print("The length of linked list is smaller than k")
        return 
    
    while p2 != None:
        p2 = p2.next
        p1 = p1.next 
    print(p1.data)

def dive(node, k):
    if node == None:
        return 0     
    d = dive(node.next, k) + 1

    if d == k:
        print(f"kth to last is {node.data}")
    return d

def find_kth_to_last(ll, k):
    #find kth to the last using recursive
    #O(n) space, O(n) time
    tmp = ll.head
    return dive(tmp, k)

sll = SingleLinkedList()

data = [2, 3, 2, 4, 5, 6, 3, 1, 2, 7, 3]
for dt in data:
    sll.add_tail(dt)

sll.print_list()

k = int(input("Enter k: "))
ans = find_kth_to_last2(sll, k)
