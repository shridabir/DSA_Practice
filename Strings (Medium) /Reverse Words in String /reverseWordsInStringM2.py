def reverseWordsInString(string):
    # Write your code here.
    #M-2: reverse entire list at start
    #TC: O(n)
    #SC: O(n)
    #Reverse words in the list

    #store characters from the string in a list
    characters = [char for char in string]
    #function that reverses the parts of the string - what you want to reverse, start and end
    reverseListInRange(characters, 0, len(characters) - 1)

    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord #idx of eOw = sow
        #increment endOfWord until we find space
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1

        #if thats not the case (not last word), reverse the word we got
        reverseListInRange(characters, startOfWord, endOfWord - 1) #idx of endOfWord can be space therefore - 1 to not include space
        startOfWord = endOfWord + 1 #put startOfWord at idx of endOfWord + 1

    return "".join(characters)

#function that reverses the parts of the string - what you want to reverse, start and end
def reverseListInRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
