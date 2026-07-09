def generateDocument(characters, document):
    # Write your code here.
    '''
    #solution 1: inefficient
    #TC: O(m x (n + m)) m = traverse through document (len of document) and n = len of characters
    #n + m = count of character in document
    #SC: O(1)

    for character in document:
        documentFrequency = countCharFrequency(character, document)
        charactersFrequency = countCharFrequency(character, characters)

        if documentFrequency > charactersFrequency:
            return False
    return True

def countCharFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency

    #solution 2
    #TC = O(c x (n + m)) c = numbe rof unique characters in document (set) and c << m
    #SC = O(c) = to create a set

    #keep track of already counted characters in a set
    alreadyCounted = set()

    for character in document:
        if character in alreadyCounted:
            continue

        documentFrequency = countCharFrequency(character, document)
        charactersFrequency = countCharFrequency(character, characters)

        if documentFrequency > charactersFrequency:
            return False
        #if valid character, add it in the alreadyCounted set
        alreadyCounted.add(character)
    return True

def countCharFrequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1

    return frequency

    return False
'''

    # Solution3.
    #count frequency of character in characters string and compare with documents string
    #we will do this by going through each character in characters string and adding it in dictionary with its count if not already
    #now we will go through characters and check if character in this string is there in characterCounts dictionary, if not we can't create document and return False
    #if yes reduce it's count by 1. If count of any character reaches zero and it's present in characters string, it's an extra character and we can't create document so return FALSE

    #TC: O(n + m): looping through both strings only once
    #SC: O(c) = numbe rof unique characters

    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0 #set the count at the position of character to 0
        characterCounts[character] += 1 #increment the count

    #now go through document string
    for character in document:
        #if character not present in dict or it's count = 0(we used all of these), we cant create the document
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        #if character present in dict and count != 0, reduce it's count by 1
        characterCounts[character] -= 1
        
    return True

