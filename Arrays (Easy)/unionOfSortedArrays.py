#Q.11 Find union of two sorted arrays
#brute force - use set to remove duplicates and then take union of both arrays - TC = O(n) and SC = O(n)
def unionBrute (arr1, arr2):
    sett = set(arr1) | set(arr2)
    return list(sett)
# Example usage
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5]
print("Union of two arrays is:", unionBrute(arr1, arr2))

#optimal approach - TC = O(n) and SC = O(1)
#optimal approach - use two pointers. one for arr1 and one for arr2. if arr1[i] < arr2[j] then add arr1[i] to result and increment i.
# if arr1[i] > arr2[j] then add arr2[j] to result and increment j. if both are equal then add either of them and increment both i and j.
# TC = O(n) and SC = O(1)

def unionOptimal (arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i, j = 0, 0
    unionArr = []
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            if len(unionArr) == 0 or arr1[i] not in unionArr:
                unionArr.append(arr1[i])
            i += 1
        else:
            if len(unionArr) == 0 or arr2[j] not in unionArr:
                unionArr.append(arr2[j])
            j += 1
    #add remaining elements of arr1
    while i < n1:
        if len(unionArr) == 0 or arr1[i] not in unionArr:
            unionArr.append(arr1[i])
        i += 1
    #add remaining elements of arr2
    while j < n2:
        if len(unionArr) == 0 or arr2[j] not in unionArr:
            unionArr.append(arr2[j])
        j += 1
    return unionArr

# Example usage
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5]
print("Union of two arrays is (Optimal):", unionOptimal(arr1, arr2))