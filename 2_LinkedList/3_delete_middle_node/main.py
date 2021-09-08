"""
    Implement an algorithm to delete the node in the middle (any node except the first and the last node) of 
    a singly linked list, given only access to that node 
"""

import random, sys
from ..linkedlist import * 


def delete_node(ll, node):
    tmp = node.next 
    node.data = node.next.data
    node.next = node.next.next
    

def get_random_access(ll, k):
    tmp = ll.head.next 

    i = 0
    while tmp != None:
        tmp = tmp.next 
        i += 1
        if i == k:
            return tmp 
        
    return None

sll = SingleLinkedList()

data = [2, 3, 2, 4, 5, 6, 3, 1, 2, 7, 3]
for dt in data:
    sll.add_tail(dt)

#get random access to a node 
node = get_random_access(sll, 4)

if node == None:
    print("Choose anthoer value of k")
    sys.exit()
else: 
    if node.next == None:
        print("Not choosing the end node plz")
        sys.exit()

#delete node 
sll.print_list()
print(f"Random access of node is {node.data}")
delete_node(sll, node)
sll.print_list()