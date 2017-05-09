class Node(object):
    def __init__ (self,value, rPointer = None, lPointer = None):
        self.value = value
        self.rPointer = rPointer 
        self.lPointer = lPointer 
        
class DoubleLinkedList(object):

    def __init__(self,head = None):
        self.head = head
    
    #Function to printall elements in DoubleLinkedLIst
    def printAll(self):
        current = self.head
        if current == None:
            print "Emptry Man"
        else:
            while current.rPointer != None:
                print current.value
                current = current.rPointer
            print current.value
    
    #Enter an element at the head of DoubleLinkedLIst 
    #@param {Integer} - N : Value to be inserted
    def inseretOne(self,N):
        current = self.head
        nodeX = Node(N , None,None)
        nodeX.rPointer = current
        nodeX.lPointer = None
        if current != None: 
            current.lPointer = nodeX 
        self.head = nodeX
    
    #Find An element in DoubleLinkedList
    #@param {Integer} - N : Value to be searched
    def findOne(self,N):
        current = self.head
        position = 1
        found = False 
        #loop over Nodes till the value in node is equal to value inserted
        while ((current.rPointer != None) & (current.value != N)):
            position += 1
            current = current.pointer
        if found:
            print "N found at -> ",position
        else: 
            print "No such node with value = ", N 
            
    #Delete All from likedList 
    def deleteAll(self):
        #Point Self.head to None
        self.head = None

    #Size of Dounle LinkedList 
    def sizeOfLL(self):
        count = 0
        current = self.head
        #loop till the rPointer is None
        while(current.rPointer != None):
            count += 1
            current = current.pointer

        print "This is the total", count
        
    #Delete at Head
    # @param {Integer} - N : value to be delited
    def deleteOne(self,N):
        current = self.head 
        position = 0
        found = False
        #Loop until you find the node which has value N 
        while current.rPointer != None and current.value != N:
            current = current.rPointer 
            position += 1
        #Flag found to True
        if current.value == N: 
            found = True
        if found: 
            if position > 0: 
                #if the node is first or in middile 
                prevX = current.lPointer
                #If the node is correner case
                if current.rPointer != None: 
                    nextX = current.rPointer 
                    nextX.lPointer = prevX 
                    prevX.rPointer = nextX
                else: 
                    self.head = current.rPointer 
                    current.lPointer = None
        if found == False:
            print "No such Value"
    #Delete a Node from a position 
    #@Param {Integer} - The position from where you want to delete 
    def deleteFromPos(self,pos): 
        current = self.head 
        position = 1 
        #If pos is one point the head to the next Node
        if pos == 1: 
            self.head = current.rPointer 
            self.head.lPointer = None
        elif pos > 1:
            
            while current!= None: 
                position += 1
                current = current.rPointer 
                if pos == position: 
                    break 
            prevX = current.lPointer 
            if current.rPointer != None: 
                nextX = current.rPointer 
                prevX.rPointer = nextX 
                nextX.lPointer = prevX 
            else: 
                prevX.rPointer = None
            

l = DoubleLinkedList()
l.inseretOne(5)
l.inseretOne(2)
l.inseretOne(7)
l.deleteFromPos(3)
l.inseretOne(15)
l.printAll()
