#Q.15 FIND THE NUMBER THAT APPEARS ONCE IN AN ARRAY WHERE OTHERS APPEAR TWICE
#BRUTE - linear search - O(n^2), SC = O(1)
def appearsOnceBrute (arr):
    n = len(arr)
    for i in range (n):
        count = 0
        for j in range (n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return None
# Example usage
arr = [2,3,5,4,5,3,4]
print("Number that appears once in the array (Brute):", appearsOnceBrute(arr))

#better - use map / hashing - O(n), SC = O(n)
def appearsOnceHashing (arr):
    n = len(arr)
    hash = {}
    for i in range (n):
        hash[arr[i]] = hash.get(arr[i], 0) + 1 #count frequency of each element, if not present, set to 0 and add 1
    for key in hash:
        if hash[key] == 1:
            return key
    return None
# Example usage
arr = [2,3,5,4,5,3,4]
print("Number that appears once in the array (Hashing):", appearsOnceHashing(arr))

#optimal - using xor - O(n), SC = O(1)
def appearsOnceOR (arr):
    n = len (arr)
    xor = 0
    for i in range (n):
        xor = xor ^ arr[i]
    return xor
# Example usage
arr = [2,3,5,4,5,3,4]
print("Number that appears once in the array (Optimal):", appearsOnceOR(arr))