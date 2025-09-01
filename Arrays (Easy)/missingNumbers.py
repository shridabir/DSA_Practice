#Q.13 FIND THE MISSING NUMBER IN THE ARRAY
#brute force - linear search - TC = O(n^2), SC = O(1)
def missingNumberBrute (arr):
    n = len(arr)
    for i in range (1, n+1):
        if i not in arr:
            return i
    return None
# Example usage
arr = [1,2,3,5]
print("Missing number in the array (Brute):", missingNumberBrute(arr))

#Better approach - hashing - TC = O(n) and SC = O(n)
def missingNumberHashing (arr):
    n = len(arr)
    hashArr = [0] * (n + 1) #create a hash array of size n+1
    for i in range (n):
        hashArr[arr[i] - 1] = 1 #mark the elements present in arr
    for i in range (n + 1):
        if hashArr[i] == 0:
            return i + 1
    return None

# Example usage
arr = [1,2,3,5]
print("Missing number in the array (Hashing):", missingNumberHashing(arr))

#optimal - use sum formula - TC = O(n), SC = O(1)
def missingNumberOptimal (arr):
    n = len(arr) + 1 #since one number is missing
    summ = (n * (n + 1)) // 2 #sum of first n natural numbers
    arrSum = sum(arr)
    return summ - arrSum

# Example usage
arr = [1,2,3,5]
print("Missing number in the array (Optimal):", missingNumberOptimal(arr))

#optimal M-2: use XOR - TC = O(n), SC = O(1)
def missingNumberXOR (arr):
    n = len(arr) + 1 #since one number is missing
    xor1 = 0
    xor2 = 0
    for i in range (1, n + 1):
        xor1 = xor1 ^ i #XOR of all elements from 1 to n
    for i in range (len(arr)):
        xor2 = xor2 ^ arr[i] #XOR of all elements in arr
    return xor1 ^ xor2 #XOR of both will give the missing number
# Example usage
arr = [1,2,3,5]
print("Missing number in the array (XOR):", missingNumberXOR(arr))
        
