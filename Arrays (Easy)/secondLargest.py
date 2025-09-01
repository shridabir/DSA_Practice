#Q.2 PRINT SECOND LARGEST ELEMENT IN AN ARRAY WITHOUT USING THE MAX FUNCTION OR SORTING
#brute force - sort the array and fix largest. now run a loop from n-2 to 0 and check if element is not equal to largest. 
#first element not equal to largest from behind = secondlargest as it is sorted - TC = O(nlogn) and SC = O(1)
def secondLargestBrute(arr):
    n = len(arr)
    arr.sort()
    largest = arr[-1]
    for i in range(n-2, -1, -1): #start from n-2, go until 0 and reverse iteration
        if arr[i] != largest:
            return arr[i]
# Example usage
arr = [1,2,3,4,5]
print("Second largest element in the array is:", secondLargestBrute(arr))

#better approach - TC = O(2n) and SC = O(1)
def secondLargestBetter(arr):
    n = len(arr)
    arr.sort()
    largest = arr[-1]
    secondLargest = -1
    for i in range(n) :
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest
# Example usage
arr = [1,2,3,4,5]
print("Second largest element in the array is:", secondLargestBetter(arr))

#optinal approach - TC = O(n) and SC = O(1)
def secondLargestOptimal(arr):
    largest = arr[0]
    slargest = -1
    for i in arr:
        if i > largest:
            slargest = largest
            largest = i
        #if arr[i] is smaller than largest compare it with slargest and check if it is not equal to largest
        elif i > slargest and i != largest:
            slargest = i
    return slargest
# Example usage
arr = [1,2,3,4,5]
print("Second largest element in the array is:", secondLargestOptimal(arr))

#Q.4 FIND SECOND SMALLEST ELEMENT IN AN ARRAY WITHOUT USING THE MIN FUNCTION OR SORTING
def secondSmallest (arr):
    n = len(arr)
    smallest = arr[0]
    secsmallest = float('inf')
    for i in range(n) :
        if arr[i] < smallest:
            secsmallest = smallest
            smallest = arr[i]
        elif arr[i] < secsmallest and arr[i] != smallest:
            secsmallest = arr[i]
    return secsmallest
# Example usage
arr = [1,2,3,4,5]
print("Second smallest element in the array is:", secondSmallest(arr))