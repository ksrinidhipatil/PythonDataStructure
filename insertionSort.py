def insertionSort(aList): 
    for i in range(1,len(aList)): 
        currentValue = aList[i]
        position = i
        while position > 0 and currentValue < aList[position -1]: 
            aList[position] = aList[position-1]
            aList[position-1] = currentValue
            position -=1 
    print aList 
    
insertionSort([2,1,34,3,3,1,7,86,4,0,-1,1,2,3,1,1,1,1,2,34,5,6,7,8,6,4,3])
