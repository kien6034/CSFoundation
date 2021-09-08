#CIRCULAR LINKED LIST

"""
    Given a circular linked list, implement an algorithm that returns all the node at the beginning of the loop

    EXAMPLE:
        input: 1->2-> 3->5->4->3 
        ans: 3
"""

from ..linkedlist import * 


#METHOD 1: USING HASH TABLE to store the traversed node. If the new node is in the table, return that node 

#METHOD 2: runner up
def find_metting_ponint(cll):
    tmp1 = cll.head 
    tmp2 = cll.head 

    while tmp2 != None:
        tmp1 = tmp1.next 
        if tmp2.next != None:
            tmp2 = tmp2.next.next
        else:
            tmp2 =tmp2.next 

        if tmp1 == tmp2:
            return tmp1

    return None

def find_loop_beginning(cll ,meet_point):
    tmp1 = cll.head
    tmp2 = meet_point

    while tmp1 != tmp2:
        tmp1 = tmp1.next
        tmp2 = tmp2.next 
    return tmp1

#create a circular linked list 
nodes = dict()
data = [1, 2, 3,5, 4, 3]
for dt in data:
    node = Node(dt)
    nodes[dt] = node

cll = SingleLinkedList()

for dt in data:
    cll.add_node_tail(nodes[dt])

meet_point = find_metting_ponint(cll)

ans = find_loop_beginning(cll, meet_point)

print(ans.data)
