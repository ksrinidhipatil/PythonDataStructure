class Node(object): 
    def __init__(self,data, pointer = None): 
        self.data = data
        self.pointer = pointer 

class CircularLinkedList(object): 
    def __init__(self,head = None, tail = None): 
        self.head = head
    
    def insertOne(self, data): 
        current = self.head
        nodeX = Node(data,None)
        if current == None:
            self.head = nodeX
            self.head.pointer = self.head
            self.tail = nodeX
        else: 
            nextX = current
            self.head = nodeX 
            nodeX.pointer = nextX 
            self.tail.pointer = nodeX
    def insertAtPos(self,data,pos): 
        position = 1
        current = self.head 
        nodeX = Node(data, None)
        if pos == 1: 
            self.insertOne(data)
        elif pos > 1: 
            while current.pointer != self.head: 
                prevX = current
                current = current.pointer
                position += 1 
                if position == pos: 
                    break 
             
            if pos == position: 
                nextX = current 
                prevX.pointer = nodeX 
                nodeX.pointer = nextX
                    
            
    def printAll(self):
        current = self.head 
        if current == None: 
            print "empty Man"
        else:
            while current.pointer != self.head: 
                print current.data
                current = current.pointer
            print current.data
        
cl = CircularLinkedList()
cl.insertOne(5)
cl.insertOne(10)
cl.insertAtPos(12,1)
cl.insertAtPos(15,3)



cl.printAll()



            
