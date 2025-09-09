#Q.3 MAJORITY ELEMENT IN AN ARRAY - FIND THE ELEMENT THAT OCCURS MORE THAN n/2 TIMES
#brute - linear search - TC = O(n^2) and SC = O(1)
def majorityElementBrute (arr):
    n = len(arr)
    for i in range (n):
        cnt = 0
        for j in range (n):
            if arr[i] == arr[j]:
                cnt += 1
        if cnt > n/2:
            return arr[i]
    return -1
#Example usage
arr = [2,2,3,3,1,2,2]
print("Majority element in the array is:", majorityElementBrute(arr))

#better - use hashing - TC = O(n) and SC = O(n)
def majorityElementBetter (arr):
    n = len(arr)
    hash = {}
    for i in range (n):
        hash[arr[i]] = hash.get(arr[i], 0) + 1 # Increment the count of arr[i] in the dictionary; if it doesn't exist, start with 0
    for i in hash:
        if hash[i] > n/2:
            return i
    return -1
#Example usage
arr = [2,2,3,3,1,2,2]
print("Majority element in the array is:", majorityElementBetter(arr))