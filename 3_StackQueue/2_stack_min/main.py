#STACK MIN 
"""
    How would you design a stack which, in addition to push and pop, have a function that returns the minimum element 
    push, pop and min should all operate in O(1) time 
"""

from ..stack_queue import * 

class StackWithMin(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.min = None 

    def push(self ,node):
        rnode = Node(node)
        super().push(rnode)
        
        if self.min == None:
            min_node = Node(node)
            self.min = rnode 
        else:
            if rnode.data < self.min.data:
                tmp = self.min
                self.min = Node(node)
                self.min.next = tmp 
    
    def pop(self):
        node = super().pop()

        if node == self.min.data:
            self.min = self.min.next 
        return node 
    
    def get_min(self):
        return self.min.data

st = StackWithMin()
st.push(8)
st.push(9)
st.push(4)
st.push(5)
st.push(3)
st.push(7)
st.print_stack()

print(st.get_min())
st.pop()
st.pop()
print(st.get_min())
st.print_stack()
