#TC = O(n) | SC: O(n)
def zeroSumSubarray(nums):
    # Write your code here.
    sums = set([0]) #edge case
    currSum = 0

    #logic used is this: if sum of a long subarray [0,x] is s and sum of subarray [0,y] is also s. Then sum of subarray [x,y] must be 0.
    #so we are looking if a subarray with given sum is there in set if yes we return true (we have xerosum subarray) else we add that sum in set
    for num in nums:
        currSum += num #subarray sum
        #check if we have this subarray sum in set, if yes return true. If not add it in set
        if currSum in sums:
            return True
        sums.add(currSum)

    return False
