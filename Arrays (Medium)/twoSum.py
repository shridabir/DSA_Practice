#Q.1 TWO SUM PROBLEM - FIND WAYS IF SUM OF ANY TWO NUMBERS IN ARRAY IS EQUAL TO K
#brute force - check all pairs of elements and check if their sum is equal to k - TC = O(n^2) and SC = O(1)
def twoSumBrute (arr, k):
    n = len(arr)
    for i in range (n):
        for j in range (i + 1, n):
            if arr[i] + arr[j] == k:
                return (arr[i], arr[j]) #if indexes then - return (i, j)
    return -1
#Example usage
arr = [2,6,5,8,11]
k = 14
print("Two numbers whose sum is", k, "are:", twoSumBrute(arr, k))

#better approach - using hash set to store elements and check if k - arr[i] exists in set - TC = O(nlogn) and SC = O(n)
def twoSumHashing (arr, k):
    n = len (arr)
    hash = {}
    for i in range (n):
        rem = k - arr[i]
        if rem in hash:
            return (arr[i], rem) #if indexes then - return (i, hash[rem])
        hash[arr[i]] = i #if not in hash, add it to hash. Store this number in the dictionary, and remember the index where I saw it
    return -1
#Example usage
arr = [2,6,5,8,11]
k = 14
print("Two numbers whose sum is", k, "are:", twoSumHashing(arr, k))

#optimal - use two pointers - TC = O(n) and SC = O(1) - ONLY IF WE WANT TO RETURN THR PAIR NOT THE INDEXES
#sort the array and use two pointers. one at start and one at end. if sum of both is equal to k then return the pair.
# if sum is less than k then move left pointer to right. if sum is greater than k then move right pointer to left.
def twoSumTwoPointers (arr, k):
    arr.sort()
    n = len (arr)
    left = 0
    right = n - 1
    while left < right:
        currSum = arr[left] + arr[right]
        if currSum == k:
            return (arr[left], arr[right])
        #sum < k, left pointer forward
        elif currSum < k:
            left += 1
        #sum > k, right pointer backward
        else:
            right -= 1
    return -1
#Example usage
arr = [2,6,5,8,11]
k = 14
print("Two numbers whose sum is", k, "are:", twoSumTwoPointers(arr, k))