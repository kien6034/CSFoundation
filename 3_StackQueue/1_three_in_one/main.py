import numpy as np 
from ..stack_queue import *
import sys


class FixedMultiStack():
    def __init__(self, arrSize, numberOfStacks) -> None:
        self.numberOfStacks = numberOfStacks
        self.arr = np.empty(arrSize, dtype=np.int16)
        self.stack_range, self.top=  self.determine_stack_range(arrSize, numberOfStacks)

    def determine_stack_range(self, arrSize, numberOfStacks):
        stack_range = []
        slotPerStacks = int(arrSize/ numberOfStacks)
        top = np.zeros(numberOfStacks, dtype=np.int16)


        if numberOfStacks == 0:
            print("number of stack need to be bigger than 0") 

        start = 0
        end = 0
        for i in range(0, numberOfStacks -1):
            start = end 
            end += slotPerStacks
            stack_range.append((start, end))
            top[i] = start -1
        
        stack_range.append((end, arrSize))
        return stack_range, top
    
    def push(self, stack,value):
        if stack not in range(self.numberOfStacks):
            print(f"Stack not should be in range 0 - {self.numberOfStacks}")
            return
        
        if not self.is_full(stack):
            top = self.top[stack] + 1
    
            self.arr[top] = value 
            self.top[stack] = top
        else:
            print(f"Stack {stack} is full")
            return 

    def pop(self, stack):
        if stack not in range(self.numberOfStacks):
            print(f"Stack not should be in range 0 - {self.numberOfStacks}")
            return -1

        if not self.is_empty(stack):
            val = self.arr[self.top[stack]]
            self.top[stack] -=1
            return val 
        else:
            print(f"STack {stack} is full")
            return -1

    def is_empty(self, stack):
        return self.top[stack] == self.stack_range[stack][0] -1

    def is_full(self, stack):
        if self.top[stack] == self.stack_range[stack][1]:
            return True
        else:
            return False

    def print_stack(self, stack):
        start = self.stack_range[stack][0]
        for i in range(start, self.top[stack] + 1):
            print(self.arr[i], end="  -->  ")
        print()


class FlexStack():
    def __init__(self, start, size, capacity) -> None:
        self.start = start 
        self.size= size
        self.cap = capacity

class FlexMultiStack():
    """
        If a stack is full and array still have empty blocks, increase size of that stack and do the shifting 
    """
    def __init__(self, arrSize, numberOfStacks) -> None:
        self.arrSize =arrSize
        self.numberOfStacks = numberOfStacks
        self.arr = np.empty(arrSize, dtype=np.int16)
        self.stacks=  self.determine_stack_range(arrSize, numberOfStacks)
    
    def determine_stack_range(self, arrSize, numberOfStacks):
        stacks = []
        slotPerStacks = int(arrSize/ numberOfStacks)
        top = np.zeros(numberOfStacks, dtype=np.int16)


        if numberOfStacks == 0:
            print("number of stack need to be bigger than 0") 

        start = 0
        end = 0
        for i in range(0, numberOfStacks -1):
            start = end 
            end += slotPerStacks
            top[i] = start -1
            stack = FlexStack(start, 0, slotPerStacks)
            stacks.append(stack)
        
        stacks.append(FlexStack(end, 0, arrSize - end))
        return stacks
    
    def push(self, i, value):
        stack = self.stacks[i]
        if self.is_max_cap(i):
            if self.is_arr_full():
                print("Array is full!")
                return -1 
            else:
                #shifting 
                self.shifting(i)
                self.arr[stack.start + stack.size] = value
                stack.size +=1
        else:
            self.arr[stack.start + stack.size]= value
            stack.size += 1
    
    def shifting(self, i):
        ntf = [] #need to be shift 

        ss = i + 1 # shift stack 
        while self.is_max_cap(ss % self.numberOfStacks):
            ss += 1

        for k in range(ss, i, -1):
            sidx = k % self.numberOfStacks
            stack = self.stacks[sidx]

            for m in range(stack.start + stack.size -1, stack.start -1, -1):
                self.arr[(m+1) % self.arrSize] = self.arr[m%self.arrSize]

        self.stacks[ss %self.numberOfStacks].cap -=1 
        self.stacks[ss % self.numberOfStacks].start = (self.stacks[ss %self.numberOfStacks].start + 1 ) % self.arrSize
        
        self.stacks[i].cap += 1

    def print_all(self):
        print(self.arr)
        for i in range(self.numberOfStacks):
            stack = self.stacks[i]
            print(f"=====================\n Stack {i}||| Start: {stack.start} Size {stack.size} Cap: {stack.cap}")
            
            for i in range(stack.start, stack.start + stack.size):
                print(self.arr[i % self.arrSize], end="  -->  ")
            print()           



    def is_max_cap(self, stack):
        return self.stacks[stack].size == self.stacks[stack].cap
    
    def is_arr_full(self):
        total_size = 0
        for i in range(self.numberOfStacks):
            total_size += self.stacks[i].size 
        
        return total_size == self.arrSize

multiStack = FlexMultiStack(9, 3)
multiStack.push(1, 2)
multiStack.push(1, 3)
multiStack.push(1, 4)
multiStack.push(1, 5)
multiStack.push(2,6)
multiStack.push(2,7)
multiStack.push(1, 8)

multiStack.print_all()