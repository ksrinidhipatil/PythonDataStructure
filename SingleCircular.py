class Node(object): 
    def __init__(self,data, pointer = None): 
        self.data = data
        self.pointer = pointer 

class CircularLinkedList(object): 
    def __init__(self,head = None, tail = None): 
        self.head = head
    
    #Insert on at head
    #@param {Integer} - Data to be entered
    def insertOne(self, data): 
        current = self.head
        nodeX = Node(data,None)
        #If the LinkedLit is empty Make it the head node
        if current == None:
            self.head = nodeX
            self.head.pointer = self.head
            self.tail = nodeX
        #Make the current node as Node x and Map the previous and next accordingly
        else: 
            nextX = current
            self.head = nodeX 
            nodeX.pointer = nextX 
            self.tail.pointer = nodeX
            
    #Insert at position, 0 is the starting index
    #@param {Integer} data - The data to put in the Node 
    #@param {Integer} Pos - The position of the Node 
    def insertAtPos(self,data,pos): 
        position = 0
        current = self.head 
        #If Position is 0 Call the InserOne Function 
        if pos == 0: 
            self.insertOne(data)
        elif pos >= 1:
            nodeX = Node(data, None)
            #Else increment the current and if Pos == Pos place the Node
            while current.pointer != None: 
                prevX = current
                current = current.pointer
                position += 1 
                if position == pos: 
                    break 
             
            if pos == position: 
                nextX = current 
                prevX.pointer = nodeX 
                nodeX.pointer = nextX
    
    #Delete from Head
    def deleteAtHead(self): 
        current = self.head 
        if current == None: 
            print "Empty Man" 
        else: 
            #Get Next and tail and and point tail to next and current to None
            nextX = current.pointer 
            prevX = self.tail 
            prevX.pointer = nextX 
            self.head = nextX
            
    #Delete from Pos index Starts from 0 
    #@param {Integer} - Pos : position of the Node to be delited
    def deleteFromPos(self,pos): 
        position = 0 
        current = self.head
        index = True
        if pos >= self.sizeOfCL():
            print "Index out of bounds"
            index = False
        if index:
            if pos == 0: 
                self.deleteAtHead()
            else:
                #Loop throuh till you reach the position map prev Node To Next Node
                while current.pointer != None: 
                    if pos > position: 
                        position += 1 
                        prevX = current 
                        current = current.pointer  
                        if pos == position: 
                            break 
                nextX = current.pointer 
                prevX.pointer = nextX
                current = None

    #Print The CirculalLinked List  
    def printAll(self):
        current = self.head 
        if current == None: 
            print "empty Man"
        else:
            #while current.pinter is not head keep on printing
            while current.pointer != self.head: 
                print current.data
                current = current.pointer
            print current.data 
    
    #Size of the CircularLinkedList 
    #return the size of the circularLinkedList
    def sizeOfCL(self): 
        current = self.head
        size = 1
        while current.pointer != self.head: 
            size += 1 
            current = current.pointer 
        return size 
    
        
cl = CircularLinkedList()
cl.insertOne(5)
cl.insertOne(10)
cl.insertAtPos(15,1)
cl.insertAtPos(12,0)
cl.deleteFromPos(4)
cl.printAll()
