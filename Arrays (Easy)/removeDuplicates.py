#Q.5 REMOVE DUPLICATE ELEMENTS FROM A SORTED ARRAY. DO IT IN PLACE
#brute force  - use set to remove duplicates - TC = O(n) and SC = O(n)
def remove_duplicates(arr):
    sett = list(set(arr))
    return len(sett)
# Example usage
arr = [1,2,3,4,5,5,6]
print("Length of Array after removing duplicates:", remove_duplicates(arr))

#optimal approach - TC = O(n) and SC = O(1) - two pointer approach
def reomove_duplicates_optimal (arr):
    n = len(arr)
    i = 0
    for j in range (1,n):
        if arr[i] != arr[j]:
            #if not equal then shift j in front and increment i
            arr[i+1] = arr[j]
            i += 1
    return i+1
# Example usage
arr = [1,2,3,4,5,5,6]
print("Length of Array after removing duplicates:", reomove_duplicates_optimal(arr))