#Q.9 FIND THE NEXT PERMUTATION OF AN ARRAY
#next permutation is the next lexicographically greater permutation of the array
#brute force - generate all permutations and sort them, then find the next permutation - TC = O(n!), SC = O(n)
def nextPermutationBrute (arr):
    from itertools import permutations
    n = len(arr)
    perms = sorted(set(permutations(arr))) #Generate all permutations and sort them
    for i in range(len(perms) - 1):
        if perms[i] == tuple(arr):
            return list(perms[i + 1]) #return the next permutation
    return arr #if no next permutation found, return the same array
#Example usage
arr = [2,1,5,4,3,0,0]
print("Next permutation is:", nextPermutationBrute(arr))

#optimal: use permutation algorithm - TC = O(n) and SC = O(1)
#1. Traverse from the end of the array and find the first decreasing element. Let's call its index 'i'.
#2. If no such element is found, it means the array is in descending order. Reverse the array to get the smallest permutation.
#3. If such an element is found, traverse from the end again to find the first element that is greater than arr[i]. Let's call its index 'j'.
#4. Swap arr[i] and arr[j].
#5. Reverse the subarray from i+1 to the end of the array to get the next permutation.
def nextPermutation (arr):
    n = len(arr)
    index = -1
    #step 1 - find the first decreasing element from the end
    for i in range (n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            index = i
            break
    #if no such element found, reverse the array
    if index == -1:
        arr.reverse()
        return arr
    
    #step 2 - find the first element greater than arr[index] from the end
    for j in range (n-1, index, -1):
        if arr[j] > arr[index]:
            #step 3 - swap arr[index] and arr[j]
            arr[index], arr[j] = arr[j], arr[index]
            break
    
    #step 4 - reverse the subarray from index + 1 to the end
    arr[index + 1:] = reversed(arr[index + 1:])
    return arr

#Example usage
arr = [2,1,5,4,3,0,0]
print("Next permutation is:", nextPermutation(arr))