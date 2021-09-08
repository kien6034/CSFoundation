#intersection 

"""
    Given two singly linked list, determine if two lists intersect. Return the intersecting node 
    Note that the intersection is defined based on reference, not value     
    That is, if the kth node of the first linked list is exact same node (by reference)  as the jth node 
    of the second linked list, they are intersecting
"""
from ..linkedlist import *

def get_tail_and_size(ll):
    tmp = ll.head   

    size = 1
    while tmp.next != None:
        tmp = tmp.next 
        size +=1 
    
    return size, tmp
    
def strim_head_ll(ll, diff):
    tmp = ll.head
    for i in range(0, diff):
        ll.head = tmp.next
        del tmp  

def dive(node1, node2):
    if node1.next == None:
        if node1 == node2:
            return node1
    
    intersection = dive(node1.next, node2.next)
    if node1 == node2:
        return node1 
    else:
        return intersection

def find_intersection(ll1, ll2):
    size1, tail1 = get_tail_and_size(ll1)
    size2, tail2 = get_tail_and_size(ll2)

    if tail1 != tail2:
        return None
    else:
        if size1 < size2: 
            strim_head_ll(ll2, size2 - size1)
        else:
            strim_head_ll(ll1, size1 - size2)

    return dive(ll1.head, ll2.head)

nodes = []
data = [0, 1, 2,3, 4, 5, 6,7 ,8 ,9]

for dt in data:
    nodes.append(Node(dt))

ll1 = SingleLinkedList()
ll2 = SingleLinkedList()

n1s= [0, 1, 3, 4, 7, 8, 9]
n2s = [2, 5, 6, 7]

for n1 in n1s:
    ll1.add_node_tail(nodes[n1])

for n2 in n2s:
    ll2.add_node_tail(nodes[n2])

ll1.print_list()
ll2.print_list()

intersection = find_intersection(ll1, ll2)
print(intersection.data)