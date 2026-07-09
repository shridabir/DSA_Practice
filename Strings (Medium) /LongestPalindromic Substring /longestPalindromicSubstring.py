def longestPalindromicSubstring(string):
    # Write your code here.
    #TC: O(n^2) as at each traversal we are checking 2 cases: 1) centered at letter between 2 letters 2) centered between 2 letters
    #SC: O(n) as we store and slice the final string
    
    currentLongest = [0,1] #stores starting and ending index of palindrome initialized to 0, 1 as first letter will be palindrome
    for i in range(1,len(string)): #start from 1 as we know first letter is palindrome and cant expand to left of first
        #odd len palindrome (centred at between prev letter and next letter) e.g 
        #a b a
        odd = getLongestPalindromeFrom(string, i - 1, i + 1) #expands from left (i - 1) and right(i + 1) index
        #even len palindrome(centred between current and previous letter) 
        even = getLongestPalindromeFrom(string, i - 1, i) #expands from left (i - 1) and right(i)
        #a | a
        longest = max(odd, even, key = lambda x: x[1] - x[0]) #check who is longest based on length) by taking differnce betn value at idx 1 and idx 0
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])

    #slice the longest palindrome
    return string[currentLongest[0] : currentLongest[1] + 1]

#implements expansion from middle logic
def getLongestPalindromeFrom(string, leftidx, rightidx):
    #dont expand out of the bounds of string
    while leftidx >= 0 and rightidx < len(string):
        #break if left != right
        if string[leftidx] != string[rightidx]:
            break
        #else if left = right shift ieftidx to left and rightidx to right
        leftidx -= 1
        rightidx += 1

    #return indices
    return [leftidx + 1, rightidx - 1]
