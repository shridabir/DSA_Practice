#Q.4 FIND MAXIMUM SUBARRAY SUM - KADANE'S ALGORITHM
#brute force - linear search to form subarray and find their sum - TC - O(n^2), SC = O(1)
def maxSubarraySumBrute (arr):
    n = len(arr)
    maxSum = float("-inf")
    for i in range (n):
        currSum = 0
        for j in range (i, n):
            currSum += arr[j]
            maxSum = max (maxSum, currSum)
    return maxSum
#Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum is:", maxSubarraySumBrute(arr))

#optimal - Kadane's Algorithm - TC = O(n) and SC = O(1)
#traverse through the array and add each element to the sum. if sum < 0 consider it 0 and if sum > maxi, maxi = sum
def kadaneMaxSubarraySum (arr):
    n = len(arr)
    maxSum = float ("-inf")
    currSum = 0
    for i in range (n):
        currSum += arr[i]
        if currSum > maxSum:
            maxSum = currSum
        if currSum < 0:
            currSum = 0
    if maxSum < 0: #if all elements are negative, return 0
        maxSum = 0
    return maxSum
#Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum is:", kadaneMaxSubarraySum(arr))

#Q.5 EXTENDED VERSION OF KADANE'S - PRINT ONE OF THE SUBARRAY WITH MAXIMUM SUM
def kadanesPrintSubarray (arr):
    n = len(arr)
    maxSum = float ("-inf")
    currSum = 0
    arrStart = 0
    arrEnd = 0
    start = 0
    for i in range (n):
        currSum += arr[i]
        if currSum > maxSum:
            maxSum = currSum
            arrStart = start #potential start of the subarray because currSum is greater than maxSum
            arrEnd = i #end of the subarray
        
        if currSum < 0:
            currSum = 0
            start = i + 1 #potential start of the subarray because currSum is 0 now
    print("One of the subarray with maximum sum is:", arr[arrStart:arrEnd + 1])
    return maxSum
#Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum is:", kadanesPrintSubarray(arr))
   