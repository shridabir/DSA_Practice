def sortedSquaredArray(array):
    # Write your code here.
    n = len(array)
    #initialize new array with zeroes
    squaredArray = [0 for _ in array]
    smallerValIndex = 0
    largerValIndex = n - 1

    #traverse from right in array
    for idx in reversed (range(n)):
        #assign values at pointers
        smallerValue = array[smallerValIndex]
        largerValue = array[largerValIndex]
        #if abs(smallerValue) > abs(largerValue) then add square of smallerValue at correponding idx in squaredArray
        if abs(smallerValue) > abs(largerValue):
            squaredArray[idx] = smallerValue * smallerValue
            #move the smallerValIndex forward
            smallerValIndex += 1
        #if abs(largerValue) > abs(smallerValue) then add square of largerValue at correponding idx in squaredArray
        else:
            squaredArray[idx] = largerValue * largerValue
            largerValIndex -= 1
                
    return squaredArray
