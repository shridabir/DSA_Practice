def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    first = 0
    second = 0
    smallestDiff = float("inf") #keep track of smallestDiff
    currentDiff = float("inf")  #keep track of currentDiff
    smallestPair = []  #keep track of smallestPair to return

    while (first < len(arrayOne) and second < len(arrayTwo)): #until one of the arrays is exhausted
        firstNum = arrayOne[first]
        secondNum = arrayTwo[second]
        if firstNum < secondNum: 
            currentDiff = secondNum - firstNum
            first += 1 #increment counter of smaller number as we want to keep the difference minimum
        elif secondNum < firstNum:
            currentDiff = firstNum - secondNum
            second += 1 #increment counter of smaller number as we want to keep the difference minimum
        else: #equal: return the pair (smallestDiff = 0)
            return [firstNum, secondNum]

        if currentDiff < smallestDiff:
            smallestDiff = currentDiff #update 
            smallestPair = [firstNum, secondNum]
            
    return smallestPair
      
