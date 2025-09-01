def rightRotate (arr, d):
    n = len(arr)
    d = d % n #to handle cases where d > n
    temp = arr[-d:] #store last d elements in temp array
    #shift all elements to right by d places
    for i in range (n-1, d-1, -1): #start from behind -> n-1 and go until d-1
        arr[i] = arr[i - d]
    #set first d elements to temp's elements
    for i in range (0, d):
        arr[i] = temp[i]
    return arr
# Example usage
arr = [1,2,3,4,5,6,7]
d = 3
print("Array after right rotation by", d, "places:", rightRotate(arr, d))

#Optimal approach using reversal algorithm - TC - O(n) and SC = O(1)
def reverse (arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rightRotateOptimal (arr, d):
    n = len(arr)
    d = d % n #to handle cases where d > n
    #reverse first n-d elements
    reverse(arr, 0, n-d-1)
    #reverse last d elements (n-d to n-1)
    reverse(arr, n-d, n-1)
    #reverse the whole array
    reverse(arr, 0, n-1)
    return arr
# Example usage
arr = [1,2,3,4,5,6,7]
d = 3
print("Array after right rotation by", d, "places (Optimal):", rightRotateOptimal(arr, d))