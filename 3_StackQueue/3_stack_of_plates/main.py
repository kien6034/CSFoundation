#STACK OF PLATES
"""
    imagine a (literal) stack of plates. If the stack gets too high, it might topple(unbalance)
    There for, in real life, we would like to start a new stack when the previous stack exceeds some threshold. 
    Implement a data structure SetOfStacks that mimics this. Set of stacks should be composed of several stacks and should
    create new stack once the previous one exceeds capacity. 
    Push, pop.. method should behave like a single stack 
""" 
from typing import Set
from ..stack_queue import * 

class StackWithThreshHold(Stack):
    def __init__(self,id, threshold) -> None:
        super().__init__()
        self.size = 0
        self.cap = threshold
        self.id = id
        self.next = None 
        print(f"Stack {self.id} is created! Cap: {threshold}")

    def push(self, node):
        super().push(node)
        self.size += 1

    def pop(self):
        val = super().pop()
        self.size -=1 
        return val

    def is_full(self):
        return self.size == self.cap 

class SetOfStacks:
    def __init__(self, threshold) -> None:
        self.threshold = threshold
        self.stack = StackWithThreshHold(0, threshold)
    
    def push(self, node):
        if self.stack.is_full():
            #create new stack 
            new_stack = StackWithThreshHold(self.stack.id + 1, self.threshold)
            tmp= self.stack 
            self.stack = new_stack
            self.stack.next = tmp
            self.stack.push(Node(node))
        else:
            self.stack.push(Node(node))
    
    def pop(self):
        if self.stack.is_empty():
            self.stack =self.stack.next 
            return self.stack.pop()
        else:
            return self.stack.pop()

    def print_all(self):
        tmp = self.stack 
        
        while tmp != None:
            top = tmp.top 
            while top != None:
                print(top.data, end="  -->  ")
                top = top.next 
            print()
            tmp = tmp.next

data = [1, 2, 3, 4, 5, 6, 7 ,8]

sos = SetOfStacks(3)
for dt in data:
    sos.push(dt)

sos.pop()
sos.pop()
sos.pop()
sos.print_all()