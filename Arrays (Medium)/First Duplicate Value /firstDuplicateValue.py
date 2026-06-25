def firstDuplicateValue(array):
    # Write your code here.
    '''
    #M-1 Brute force
    minSecondIndex = len(array)
    for i in range(len(array)):
        value = array[i]
        for j in range(i + 1, len(array)):
            valueToCompare = array[j]
            #if values are equal, we found the duplicate. Store the minIndex
            if value == valueToCompare:
                minSecondIndex = min(minSecondIndex, j)
    #if no duplicates in array
    if minSecondIndex == len(array):
        return -1
    #if duplicates found, return the minIndex
    return array[minSecondIndex]
    '''

    '''
    #M-2 use set TC: O(n) | SC: O(n)
    seen = set()
    for value in array:
        if value in seen:
            return value
        #if not in seen, add it
        seen.add(value)
    return -1 #no duplicates found
    '''

    #M-3: marking values as negative: TC: O(n) | SC: O(1)
    for value in array:
        absValue = abs(value)
        #if the previous value is already marked negative, we found the duplicate. Return the absValue
        if array[absValue - 1] < 0:
            return absValue 
        #if it's not negative, make it negative
        array[absValue - 1] *= -1

    return -1 #if no duplicates found
            

