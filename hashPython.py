class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash%self.size

    def addKeyVal(self,key,val):
        keyHash = self.getHash(key)
        keyVal = [key,val]

        if self.map[keyHash] is None:
            self.map[keyHash] = list(keyVal)
            return True
        else:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
            self.map[key_hash].append(keyVal)
            return True
        
    def get(self,key):
        keyHash = self.getHash(key)
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self,key):
        keyHash = self.getHash(key)
        if self.map[keyHash] is None:
            return False
        for i in range(0,len(self.map[keyHash])):
            print self.map[keyHash][i]
        
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
            
        
