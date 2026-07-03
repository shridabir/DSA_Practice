def sweetAndSavory(dishes, target):
    # Write your code here.
    #separate sweet and savory dishes and sort them
    #for sweet dishes sort them based on abs values as they are negative

    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0])

    bestPair = [0,0]
    bestDifference = float('inf')
    #pointers
    sweetIndex, savoryIndex = 0,0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        #check current sum
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        if currentSum <= target: #need to add more savory to increase sum, so increment it's index
            #check if the diffference is less than bestDifference. If it is update bestDifference
            currentDifference = target - currentSum
            if currentDifference < bestDifference:
                bestDifference = currentDifference
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]

            savoryIndex += 1
        else:  #if sum > target, add more sweet to reduce it
            sweetIndex += 1

    return bestPair
    return []
