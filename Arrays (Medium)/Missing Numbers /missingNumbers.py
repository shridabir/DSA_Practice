def missingNumbers(nums):
    # Write your code here.
    '''
    #M-1 using set: TC = O(n) | SC = O(n)
    includedNumbers = set(nums)
    solutions = []

    for num in range (1, len(nums) + 3):
        if num not in includedNumbers:
            solutions.append(num)
    return solutions
    return []
    '''

    #M-2: using sum and averages logic

    #find total of expected range which is from 1 to len(nums) + 2
    total = sum(range(1, len(nums) + 3))

    #subtract total of nums from this
    for num in nums:
        total -= num
    
    averageMissingValue = total // 2 #average of missing values
    foundFirstHalf = 0
    foundSecondHalf = 0

    #traverse through nums array if value is <= avg add it in firstHalf or else add it in secondHalf
    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageMissingValue + 1)) #until avg value
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3)) #from value next to avg value

    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]
    return []
