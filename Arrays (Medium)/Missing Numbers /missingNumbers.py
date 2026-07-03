def missingNumbers(nums):
    # Write your code here.
    #M-1 using set: TC = O(n) | SC = O(n)
    includedNumbers = set(nums)
    solutions = []

    for num in range (1, len(nums) + 3):
        if num not in includedNumbers:
            solutions.append(num)
    return solutions
    return []
