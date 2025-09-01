#Q.16 FIND THE LONGEST SUBARRAY WITH GIVEN SUM K - ARRAY WITH ONLY POSITIVE, zero or negative INTEGERS
#brute: find out all subarrays and check if their sum is equal to k. if yes then return its max length - TC = O(n^3) and SC = O(1)
def longestSubarrayWithSumKBrute (arr, k):
    n = len (arr)
    maxLength = 0
    for i in range (n):
        currSum = 0
        for j in range (i, n):
            currSum += arr[j]
            if currSum == k:
                maxLength = max (maxLength, j - i + 1)
    return maxLength
# Example usage
arr = [10,5,2,7,1,9]
k = 15
print("Length of longest subarray with sum k (Brute):", longestSubarrayWithSumKBrute(arr, k))

#brute 
def brute2 (arr, k):
    n = len(arr)
    maxLen = 0
    for i in range (n):
        for j in range (i, n):
            if sum(arr[i:j+1]) == k: #is the sum of subarray from i to j equal to k?
                maxLen = max(maxLen, j-i+1)
    return maxLen
# Example usage
arr = [10,5,2,7,1,9]
k = 15
print("Length of longest subarray with sum k (Brute 2):", brute2(arr, k))

#optimal approach - using prefix sum - TC = O(n^2) and SC = O(n) (for positive and negative integers)
def longestSubarrayWithSumKOptimal (arr, k):
    n = len (arr)
    prefixSum = {}
    maxLen = 0
    currSum = 0
    for i in range (n):
        currSum += arr[i]
        if currSum == k:
            maxLen = max (maxLen, i + 1) #if currSum is equal to k then maxLen is i+1
        #remaining part
        remSum = currSum - k
        if remSum in prefixSum:
            Length = i - prefixSum[remSum] #if remSum is present in prefixSum then maxLen is i - index of remSum
            maxLen = max (maxLen, Length)
        else:
            prefixSum[currSum] = i #if not in prefixsum, store the currSum and its index in prefixSum for future reference
    return maxLen
# Example usage
arr = [10,5,2,7,1,9]
k = 15
print("Length of longest subarray with sum k (Optimal):", longestSubarrayWithSumKOptimal(arr, k))

#optimal approach - using two pointer (sliding window) and greedy approach - TC = O(n) and SC = O(1) (only for positive integers)
def longestSubaarraySumTwoPointer (arr, k):
    n = len(arr)
    left = 0
    right = 0
    currSum = 0
    maxLen = 0
    while (right < n):
        #keep adding right pointer to the sum until it is less than or equal to k
        currSum += arr[right]
        #if currSum > k, then subtract left pointer from the sum until currSum <= k and move it forward
        while left <= right and currSum > k:
            currSum -= arr[left]
            left += 1
        #if currSum == k, then update maxLen
        if currSum == k:
            maxLen = max(maxLen, right - left + 1)
        #move right pointer forward always
        right += 1
    return maxLen
# Example usage
arr = [10,5,2,7,1,9]
k = 15
print("Length of longest subarray with sum k (Two Pointer):", longestSubaarraySumTwoPointer(arr, k))