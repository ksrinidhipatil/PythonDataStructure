#Create a node Class to hold Value and Pointer 
class Node(object):
    def __init__ (self,value, pointer):
        self.value = value
        self.pointer = pointer

class LinkedList(object):

    def __init__(self,head = None):
        self.head = head
    # Print all elements in linkedList
    def printAll(self):
        current = self.head
        if current == None:
            print "Emptry Man"
        else:
            while current.pointer != None:
                print current.value
                current = current.pointer
            print current.value

    /* Insert an element to the head of linkedLIst
    @param {Integer} N - The value to be inserted
    */
    def inseretOne(self,N):
        current = self.head
        nodeX = Node(N , None)
        nodeX.pointer = current
        self.head = nodeX
        retrun True 
    
    /* Find a value in LinkedList
    @param {integer} N - The value to be searched
    */
    def findOne(self,N):
        current = self.head
        position = 1
        #While current is not None and the value at the node is not equal to the input 
        while ((current.pointer != None) & (current.value != N)):
            #Increment position and point the current to the nextNode
            position += 1
            current = current.pointer
        print "N found at -> ",position

    # Delete the LinkedList
    def deleteAll(self):
        self.head = None
    #print the size of the list 
    def sizeOfLL(self):
        count = 0
        current = self.head
        while(current.pointer != None):
            count += 1
            current = current.pointer

        print "This is the total", count
     /* Delete a Node with value N 
    @param {integer} N - Value to be delited 
    */
    def deleteOne(self,N):
        current = self.head
        position = 1
        #Loop throght the LinkedList to find the value 
        while((current.pointer != None) and (current.value != N)):
            prev = current
            current = current.pointer
            position += 1
        #If the position is head, Pass the head to the next Node
        if position == 1:
            self.head = current.pointer
        else:
            #get the prevX, Next X and porint prev pointer to the nextX pointer skipping the current Node 
            next = current.pointer
            prev.pointer = next 

    /* Delete an element from a position
    @param {Integer} Pos - Position of the element in linkedList
    */
    def deleteFromPos(self,pos): 
        current = self.head
        position = 1
        #If the LinkedList is not Emplty 
        while current != None: 
            if pos == 1: 
                #if position is one then point the head to the next Node 
                self.head = current.pointer 
                current = None
            else:
                #loop thorught the node till the position and pos Match 
                if pos > position:
                    position += 1 
                    prevX = current
                    current = current.pointer
                #Point prev to current.pointer to skip the current Node 
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

        
        
                
