#two pointer approach O(n^2) time | O(n) space to store triplets
def threeNumberSum(array, targetSum):
    # Write your code here.
    #sort the array: nlogn
    array.sort()
    triplets = []

    for i in range (len(array) - 2): #n - 2 because last number we will traverse in array will be 3rd last as we will sum up atleast 2 other values with current number in array
        left = i + 1 #right next to current num
        right = len(array) - 1 #last element in the array
        while (left < right):
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currSum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets
