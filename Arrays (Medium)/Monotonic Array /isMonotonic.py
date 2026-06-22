#O(n) time | O(1) space
def isMonotonic(array):
    # Write your code here.
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range (1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing  #will be true if one of them is true, false otherwise
    #both will be true only if array has equal elements
    pass
