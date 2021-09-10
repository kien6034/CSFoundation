class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None 

class Stack:
    def __init__(self) -> None:
        self.top = None  

    def pop(self):
        if not self.is_empty():
            tmp = self.top
            
            self.top = tmp.next 
            data = tmp.data 
            del tmp 
            return data
        else:
            print("The stack is empty!")
            return None

    def push(self, node):
        if self.top == None:
            self.top =node 
        else:
            tmp = self.top
            self.top = node 
            self.top.next = tmp 
    

    def peek(self):
        if not self.is_empty():
            return self.top.data 
        else:
            return None 

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def print_stack(self):
        tmp = self.top 

        while tmp != None:
            print(tmp.data, end= "  ->  ")
            tmp = tmp.next
        print()


class Queue():
    def __init__(self) -> None:
        self.start = None 
        self.end = None 
    
    def enqueue(self, node):
        if self.start == None:
            self.start = node 
            self.end = node 
        else:
            tmp = self.end 
            self.end = node 
            tmp.next =self.end 
    
    def dequeue(self):
        if not self.is_empty():
            tmp = self.start 
            self.start = tmp.next 
            if self.start == None:
                self.end = None 
            
            return tmp.data 
        else:
            return None 

    def is_empty(self):
        return self.start == None 

    def print_queue(self):
        tmp = self.start 
        while tmp != None:
            print(tmp.data, end = "  ->  ")
            tmp = tmp.next 
        print()

    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            return None

# stack = Stack()

# data = [1, 2, 3, 5]
# for dt in data:
#     node = Node(dt)
#     stack.push(node)

# print(stack.peek())

queue = Queue()

data = [1, 2, 3, 5]
for dt in data:
    node = Node(dt)
    queue.enqueue(node)

