# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    l = 0
    r = len(array) - 1
    while l < r:
        while l < r and array[r] == toMove:
            r -= 1
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
        l += 1
    return array
    
