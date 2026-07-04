def commonCharacters(strings):
    # Write your code here.
  '''
    #solution 1
    #TC: O(n X m) where n = total number of strings and m = len of longest string
    #SC: O(c) c = total unique characters  in characterCounts
    #dict to store characters and their counts
    characterCounts = {}

    for string in strings:
        #set for unique chars in each string
        uniqueStringChars = set(string)
        for char in uniqueStringChars:
            #if char in set of string is not in the dict, we set it's count to 0 (remove it), else increment it's count
            if char not in characterCounts:
                characterCounts[char] = 0 
            characterCounts[char] += 1

    #list of chars from characterCounts that appear in all strings i.e len(strings) times
    finalChars = []
    for char, count in characterCounts.items():
        if count == len(strings):
            finalChars.append(char)
    return finalChars
    '''

  #solution2: as char needs to be in all strings, we will compare each string with the smallest string and remove the uncommon chars
  #TC: O(n x m): n = total no. of strings, m = convert each string to set so m is len of longest string
  #SC: O(m) m = len of longest string
    #find and convert smallest string to set
    smallestString = getSmallestString(strings)
    potentialCommonChars = set(smallestString)

    for string in strings:
        removeNonexistantChars(string, potentialCommonChars)
        
    return list(potentialCommonChars)

#function that finds smallest string
def getSmallestString(strings):
    smallestString = strings[0]
    for string in strings:
        if len(string) < len(smallestString):
            smallestString = string

    return smallestString


#function to remove characters in each string which are not in potentialCommonChars(set of chars in smallest string)
def removeNonexistantChars(string, potentialCommonChars):
    uniqueStringChars = set(string)
    #as we will be removing from the potentialCommonChars set, better to convert it into list
    for char in list(potentialCommonChars):
        if char not in uniqueStringChars:
            potentialCommonChars.remove(char)
  
