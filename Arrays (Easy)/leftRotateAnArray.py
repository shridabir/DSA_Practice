#Q.6 LEFT ROTATE AN ARRAY BY ONE PLACE
#store the first element in a temp variable and shift all elements to left by one. set last element to temp.
def leftRotateByOne (arr):
    n = len(arr)
    temp = arr[0]
    for i in range (1,n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp
    return arr
# Example usage
arr = [1,2,3,4,5]
print("Array after left rotation by one place:", leftRotateByOne(arr))

#Q.6 LEFT ROTATE AN ARRAY BY D PLACES
#store first d elements in temp array and shift all remaining elements to left by d places. set last d elements to temp array.
def leftRotatebyD (arr, d):
    n = len(arr)
    temp = arr[:d] #store first d elements in temp array
    #shift the remaining elements to left by d places
    for i in range (d,n):
        arr[i - d] = arr[i]
    #set last d elements to temp array
    for i in range (n-d, n):
        arr[i] = temp[i - (n - d)]
    return arr
# Example usage
arr = [1,2,3,4,5]
d = 2
print("Array after left rotation by d places:", leftRotatebyD(arr, d))

#Optimal approach using reversal algorithm - TC - O(n) and SC = O(1)
def reverse (arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def leftRotateOptimal (arr, d):
    n = len(arr)
    d = d % n #tp handle cases where d > n
    #reverse first d elements
    reverse (arr, 0, d-1) #[3,2,1,4,5,6,7]
    #reverse last n-d elements (d to n-1)
    reverse (arr, d, n-1) #[3,2,1,7,6,5,4]
    #reverse the whole array
    reverse (arr, 0, n-1) #[4,5,6,7,1,2,3]
    return arr

# Example usage
arr = [1,2,3,4,5,6,7]
d = 3
print("Array after left rotation by d places (Optimal):", leftRotateOptimal(arr, d))
