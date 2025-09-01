#Q.1 PRINT THE LARGEST ELEMENT IN AN ARRAY WITHOUT USING THE MAX FUNCTION
def largest_element(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest
# Example usage
arr = [1,2,3,4,5]
print("Largest element in the array is:", largest_element(arr))
# Output: Largest element in the array is: 5