#Mergesort implementation
#@param {Array-Integer} - array : array to be sorted 
def mergeSort(array): 
    arrLength = len(array) 
    if arrLength > 1: 
        #Finding the mid 
        mid = arrLength/2
        #getting the left and right halfs of the array 
        leftArray = array[:mid]
        rightArray = array[mid:]
        #Reccursively passing the array to the mergeSoft function 
        mergeSort(leftArray) 
        mergeSort(rightArray)
        
        i,j,k = 0,0,0 
        #MergeSort Algorithm 
        #Wile there are elements in the left and right array 
        while i < len(leftArray) and j < len(rightArray):
            #If the first element of the array is less then the first array of rigth Array 
            #place the least element on k index to orignal array 
            if leftArray[i] < rightArray[j]: 
                array[k] = leftArray[i]
                i += 1
                k+= 1
            else: 
                array[k] = rightArray[j]
                j+=1 
                k+=1 
        #Corner case if any elements remains in left or rightArray 
        #append it to the array and increment the k and respective array index 
        while len(leftArray) > i: 
            array[k] = leftArray[i]
            i+=1 
            k+=1
        while len(rightArray) >j: 
            array[k] = rightArray[j]
            k+=1 
            j+=1 
    print "Sorted",array
mergeSort([2,1,5,3,4])
    
        