class Node(object):
    def __init__ (self,value, pointer):
        self.value = value
        self.pointer = pointer

class LinkedList(object):

    def __init__(self,head = None):
        self.head = head

    def printAll(self):
        current = self.head
        if current == None:
            print "Emptry Man"
        else:
            while current.pointer != None:
                print current.value
                current = current.pointer
            print current.value

    def inseretOne(self,N):
        current = self.head
        nodeX = Node(N , None)
        nodeX.pointer = current
        self.head = nodeX
        
    def findOne(self,N):
        current = self.head
        position = 1
        while ((current.pointer != None) & (current.value != N)):
            position += 1
            current = current.pointer

        print "N found at -> ",position

    def deleteAll(self):
        self.head = None

    def sizeOfLL(self):
        count = 0
        current = self.head
        while(current.pointer != None):
            count += 1
            current = current.pointer

        print "This is the total", count
        
    def deleteOne(self,N):
        current = self.head
        position = 1
        while((current.pointer != None) and (current.value != N)):
            prev = current
            current = current.pointer
            position += 1
            
        if position == 1:
            self.head = current.pointer
        else:
            next = current.pointer
            prev.pointer = next 

    def deleteFromPos(self,pos): 
        current = self.head
        position = 1
        while current != None: 
            if pos == 1: 
                self.head = current.pointer 
                current = None
            else:
                if pos > position:
                    position += 1 
                    prevX = current
                    current = current.pointer
                if pos == position: 
                    prevX.pointer = current.pointer 
                    current = None
                    
            
            
        

l = LinkedList()
l.inseretOne(5)
l.inseretOne(2)
l.inseretOne(7)
l.deleteFromPos(1)
l.deleteOne(2)
l.inseretOne(12)
l.printAll()

        
        
                
