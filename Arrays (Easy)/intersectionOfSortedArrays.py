#Q.12 FIND INTERSECTION OF TWO SORTED ARRAYS
#brute force - create a new visitor array of size of arr2, initialized with zeroes. Mark it as one if ele of arr1 is in arr2
#append only those elements to result array which are marked as 0
#TC - O(n^2) SC - O(n2)
def intersectionBrute (arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    visited = [0] * n2
    interArr = []
    for i in range (n1):
        for j in range (n2):
            if arr1[i] == arr2[j] and visited[j] == 0:
                interArr.append(arr1[i])
                visited[j] = 1
                break
            if arr2[j] > arr1[i]:
                break #since arrays are sorted, no need to check further
    return interArr
# Example usage
arr1 = [1,2,2,3,4,5]
arr2 = [2,2,3,5,6]
print("Intersection of two arrays is:", intersectionBrute(arr1, arr2))

#optimal - two pointer approach
#Optimal - TC O(n) SC O(1) - two pointer approach
#elements can interesect only when a[i] == b[j] and a[i] > b[j] if these are meet then we can move the pointer of b and add it to our array
def intersectionOptimal (arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i, j = 0, 0
    interArr = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]: #i cant have a partner in arr2
            i += 1 #move i forward
        elif arr2[j] < arr1[i]: #j cant have a partner in arr1
            j += 1 #move j forward
        else: #both are equal we want that element in our intersection array
            if len(interArr) == 0 or arr1[i] not in interArr:
                interArr.append(arr1[i])
                i += 1 #move both forward
                j += 1
    return interArr

# Example usage
arr1 = [1,2,2,3,4,5]
arr2 = [2,2,3,5,6]
print("Intersection of two arrays is (Optimal):", intersectionOptimal(arr1, arr2))