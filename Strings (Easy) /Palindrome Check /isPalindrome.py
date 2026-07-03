def isPalindrome(string):
    # Write your code here.

    left = 0
    right = len(string) - 1

    #keep checking until left pointer < right pointer - stop the moment they are pointing at same element
    while left < right:
        #if elements at these pointers are not same - return false
        if string[left] != string[right]:
            return False
        #else move left pointer ahead and right pointer behind
        else:
            left += 1
            right -= 1

    return True
