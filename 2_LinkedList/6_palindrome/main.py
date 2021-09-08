"""
    Implement a function to check if a linked list is a palindrome 
        - A palindrome is something that is the same when written forwards and backwards: ex: 1->2->3->2->1
"""

from ..linkedlist import * 

def reverse(ll):
    new_ll = SingleLinkedList()

    tmp = ll.head 
    count = 0
    while tmp != None:
        new_ll.add_head(tmp.data)
        count += 1
        tmp = tmp.next 
    return new_ll, count

def is_palindrome(ll):
    '''Reverse the linked list, and compare them'''
    new_ll, length = reverse(ll)
    
    tmp1 = ll.head
    tmp2 = new_ll.head 

    for i in range(int(length/2)):
        if tmp1.data != tmp2.data:
            return False
        tmp1 = tmp1.next
        tmp2 = tmp2.next 
    return True

def dive(node, ll):
    if node.next == None:
        start = ll.head 
        if node.data != start.data:
            return None 
        else:
            return start.next
    
    compare_node = dive(node.next, ll)

    if compare_node == None:
        return None, 0
    else:
        if compare_node.data != node.data:
            return None, 0
        else:
            return compare_node.next

def is_palindrome2(ll):
    node = ll.head 

    compare_node = dive(node, ll)
    if compare_node == None:
        return False
    else:
        return True

def is_palindrome3(ll):
    #iterative
    
    #if the length of the array is unknown, using runner up method 
    '''
        1: craete 2 pointers, pointer 1 move 1 node each time, pointer 2 move 2 nodes each time 
        2: add node of pointer 1 to a stack
        3: When pointer 2 reach the end, means that pointer 1 reach the middle 
        4: compare the values in the stack vs value from middle to end 
    '''
    pass
    
def is_palindrome4(ll):
    #similar to is_palindrome2, but you try to find the midder in recursive inner out (BETTER WAY)
    pass 

data = [1]

sll = SingleLinkedList()

for dt in data:
    sll.add_tail(dt)

if is_palindrome2(sll) != None:
    print("YES")
else:
    print("NO")