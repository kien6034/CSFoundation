class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 
        self.pre = None 

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None   

    def add_tail(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            
            while (tmp.next != None):
                tmp = tmp.next 

            #add 
            tmp.next = node  
    
    def add_node_tail(self, node):
        if self.head == None:
            self.head = node
            
        else:
            tmp = self.head
            
            while (tmp.next != None):
                tmp = tmp.next 
            #add 
            tmp.next = node  

    def add_head(self, data):
        node = Node(data)

        if self.head == None:
            self.head= node
        else:
            node.next = self.head 
            self.head = node 
            
    def remove(self, rdata):
        tmp = self.head 
        if tmp.data == rdata:
            self.head = tmp.next
            tmp = self.head
            return 

        while (tmp.next != None):
            if tmp.next.data == rdata:
                tmp.next = tmp.next.next 
                return
            else:
                tmp = tmp.next 
                

    def print_list(self):
        tmp = self.head
        while(tmp != None):
            print(tmp.data, end = "  ->  ")
            tmp = tmp.next 
        print()
    

class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 
      
    def add_tail(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            tmp = self.head
            
            while (tmp.next != None):
                tmp = tmp.next 

            #add 
            tmp.next = node 
            node.pre = tmp  
    

    def remove(self, rdata):
        tmp = self.head 
        if tmp.data == rdata:
            self.head = tmp.next
            self.head.pre = None 
            tmp = self.head
            return 

        while (tmp.next != None):
            if tmp.next.data == rdata:
                tmp.next = tmp.next.next
                if tmp.next != None:
                    tmp.next.pre = tmp 
                return
            else:
                tmp = tmp.next 
                

    def print_list(self):
        tmp = self.head
        while(tmp != None):
            print(tmp.data, end = "  ->  ")
            tmp = tmp.next 
        print()
    


