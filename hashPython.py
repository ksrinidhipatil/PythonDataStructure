class HashMap:
    def __init__(self):
        self.size = 6
        #create an emplty map of size 6
        self.map = [None] * self.size

    #function to get the hash value for the key 
    #This function returns the sum of assci values 
    #input - key && outPut hash value of the key 
    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash%self.size

    #function Put the data to the hasmap based on the hash Index 
    #input - key to hash and value to store & OutPut : True if placed
    def addKeyVal(self,key,val):
        keyHash = self.getHash(key)
        keyVal = [key,val]
        
        #If there is no correlation 
        if self.map[keyHash] is None:
            self.map[keyHash] = list(keyVal)
            return True
        else:
            #If there is correlation, Adding the value to the same hash Index 
            #One of the two methods to solve correlation 
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.map[key_hash].append(keyVal)
            return True
     #To get search for the value from the hashTable by key   
    def get(self,key):
        keyHash = self.getHash(key)
        #If there is more that one pair for a hash key, loop thorugh the pair and get 
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None

    #To delete a vaue from the hashMap 
    #Input the key of the value to be delited & OutPut True if sucess and false for failure 
    def delete(self,key):
        keyHash = self.getHash(key)
        #if there is no value in hasMap for the function then return false 
        if self.map[keyHash] is None:
            return False
        for i in range(0,len(self.map[keyHash])):
            print self.map[keyHash][i]
    #Function to printAll values in HashMap 
    def printAll(self):
        for i in range(0,len(self.map)):
            if self.map[i] is not None:
                if self.map[i][0] == key:
                    print 'hola'


h = HashMap()
h.addKeyVal('apple',5)
h.addKeyVal('orange',6)
h.printAll()
h.delete('apple')
h.printAll()
            
        
