
#Q.14 FIND MAX CONSECUTIVE ONES IN AN ARRAY
#Traverse array and keep count of 1s. If ele is != 1, reset count to 0. Keep track of max count.
#TC - O(n) SC - O(1)
def maxConsecutiveOnes (arr):
    n = len(arr)
    count = 0
    maxCount = 0
    for i in range (n):
        if arr[i] == 1:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 0
    return maxCount
# Example usage
arr = [1,1,0,1,1,1]
print("Maximum consecutive ones in the array is:", maxConsecutiveOnes(arr))