def semordnilap(words):
    # Write your code here.
    #TC: O(nxm) n: number of words in original words, m: len of longest word (reverse every word in array), O(1) to look up in set
    #SC: O(nxm), n: number of words in set and m = len of longest word
    
    #convert words =to set
    wordSet = set(words)
    #list of semordnilap pairs
    pairs = []

    #go through each word in words, reverse it and chec if it's in set
    for word in words:
        reverse = word[::-1]
        #if it's in set and is not a palindrome add the pair of word and its reverse to pairs array
        if reverse in wordSet and reverse != word:
            pairs.append([word, reverse])
            #after adding to pairs, remove them from set
            wordSet.remove(word)
            wordSet.remove(reverse)
    return pairs
