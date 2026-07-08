def firstNonRepeatingCharacter(string):
    # Write your code here.
    '''
    #solution 1: TC: O(n^2) and SC: O(1)
    for idx in range(len(string)):
        #bolean turns true if duplicate is found
        foundDuplicate = False
        for idx2 in range(len(string)):
            #if value at idx and idx2 is same and idx != idx2, foundDuplicate turns true
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True
        #if it's false, we found first non duplicate so return it's idx
        if not foundDuplicate:
            return idx
    #no non duplicates found
    return -1
    '''

    # solution2: TC: O(n) SC: O(1)
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1 #Get the current count of this character if it exists, otherwise start from 0, then add 1
        #if character in dict, get its value if not set the key and put its value as 0 (default) 
        #if not we will overwrite the key and change it to whatever it was before and make it += 1

    #now go through each letter in string (left to right) and check if it's frequency = 1 if yes return it's idx
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1
        
