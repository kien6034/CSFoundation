"""
    You have two numbers represented by a linked list, where each node contains a single digit. 
    The digit are stored in reverse order, such that 1's digit is at the head of the list. 
    Write a function that adds the two numbers and returns the sum as a linked list 

    EXAMPLE:
        Input:  (7 -> 1 > 6) + (5 -> 9 -> 2) ~~ 617 + 295
        Output: 2 -> 1 -> 9 ~~ (912)

    FOLLOW UP:
        the digits are stored in normal order
        Input:  (6 -> 1 -> 7) ~~ 617
"""

from ..linkedlist import * 


def add_reversed_ll(ll1, ll2):
    print("==========================\n Add reversed")
    tmp1 = ll1.head 
    tmp2 = ll2.head 

    ans = SingleLinkedList()
    surplus = 0 
    while tmp1 != None and tmp2 != None:
        result = tmp1.data + tmp2.data + surplus
        ans.add_tail(result % 10)
        surplus = result // 10
        tmp1 = tmp1.next 
        tmp2 = tmp2.next 
    
    if tmp1 != None:
        result = tmp1.data + surplus
        ans.add_tail(result %10)
        surplus = result // 10
    
    if tmp2 != None:
        result = tmp2.data + surplus
        ans.add_tail(result %10)
        surplus = result // 10

    return ans


def add_ll(node1, node2):
    if node1.next == None:
        rll = SingleLinkedList()
        result = node1.data + node2.data
        rll.add_tail(result%10)
        return rll, result // 10
    
    rll, surplus = add_ll(node1.next, node2.next)
    result = node1.data + node2.data + surplus
    rll.add_head(result %10)
    return rll, result // 10

def add_normal_ll(ll1, ll2):
    print("========================\n Add normal")
    #make two linked list same length 
    tmp1 = ll1.head
    tmp2 = ll2.head 

    while tmp1 != None and tmp2 != None:
        tmp1 = tmp1.next
        tmp2= tmp2.next 
    
    while tmp1 != None:
        tmp1 = tmp1.next 
        nodeo = Node(0)
        nodeo.next = ll2.head
        ll2.head = nodeo 
    
    while tmp2 != None:
        tmp2 =tmp2.next 
        nodeo = Node(0)
        nodeo.next = ll1.head
        ll1.head = nodeo
    
    rll, surplus = add_ll(ll1.head, ll2.head)
    if surplus > 0:
        rll.add_head(surplus)
    return rll

#number are put in reversed order 
num1 = [7, 1, 6] 
num2 = [5, 9, 3, 5]

ll1 = SingleLinkedList()
ll2 = SingleLinkedList()

for n1 in num1:
    ll1.add_tail(n1)

for n2 in num2:
    ll2.add_tail(n2)

ll1.print_list()
ll2.print_list()

ans = add_reversed_ll(ll1, ll2)
ans.print_list()

ans2 = add_normal_ll(ll1, ll2)
ans2.print_list()