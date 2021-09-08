#QUEUE VIA STACK 
"""
    Implement a MyQueue class which implements a queue using two stacks 
"""

from ..stack_queue import * 


#FIRST APPORACH:
"""
    when pop an element, move each element of stack 1 to stack 2 until reach the oldest element
    pop that element out then remove element from stack 2 to stack 1
"""

#SECOND APPROACH
"""Only shift element when needed, stack 1 keeps the newest element
    Stack 2 keeps the oldest element, when empty, take all element of stack 1
"""
class MyQueue:
    def __init__(self) -> None:
        self.newest = Stack()
        self.oldest = Stack()
    
    def enqueue(self, value):
        node = Node(value)
       
        self.newest.push(node)
    
    def shift_stack(self):
        if self.oldest.is_empty():
            while not self.newest.is_empty():
                self.oldest.push(Node(self.newest.pop()))

    def dequeue(self):
        self.shift_stack() #when the odest stack is empty, move element from newest stack 
        return self.oldest.pop()


myQueue = MyQueue()
data = [1,2 , 3, 4, 5, 6]
for dt in data:
    myQueue.enqueue(dt)


print(myQueue.dequeue())
myQueue.enqueue(8)
print(myQueue.dequeue())
