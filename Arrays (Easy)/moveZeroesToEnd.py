#Q.9 Move ALL ZEROS TO END OF ARRAY
#brute force - create a new array and store all non zero elements in it. then fill the rest of the array with 0s.
# TC = O(n) and SC = O(n)
def moveZeroesBrute (arr):
    n = len(arr)
    newArr = []
    for i in range (n):
        if arr[i] != 0:
            newArr.append(arr[i])
    #put those nonzeroes first in arr
    for i in range (len(newArr)):
        arr[i] = newArr[i]
    #fill the rest of arr with 0s
    for i in range (len(newArr), n):
        arr[i] = 0
    return arr

#example usage
arr = [0,1,0,3,12]
print("Array after moving all zeroes to end (Brute):", moveZeroesBrute(arr))

#Optimal approach - TC - O(n) and SC = O(1)
def moveZerosOptimal (arr):
    n = len(arr)
    j = -1 #to check the first zero
    for i in range (n):
        if arr[i] == 0:
            j = i
            break
    if j == -1: #if there are no zeros, retur the arr
        return arr
    #check for nonzero after first zero
    for i in range (j+1, n):
        if arr[i] != 0:
            #swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

#example usage
arr = [0,1,0,3,12]
print("Array after moving all zeroes to end (Optimal):", moveZerosOptimal(arr))