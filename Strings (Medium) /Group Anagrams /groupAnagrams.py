def groupAnagrams(words):
    # Write your code here.
    #M2: preferable - create hash table to keep track
    #TC: O(w * n * log(n)) = sort w strings of length n
    #SC: O(wn) = hashtable

    #keys: sorted version of words = 'sortedWord'
    #values: list of original words that share same signature = list of 'word'
    anagrams = {}
    for word in words:
        #breaks the word into a list of sorted characters and stitches them back together into a single string
        sortedWord = "".join(sorted(word))
        #check if this sorted word is in anagram hash set
        #if yes, store the list of word that correspond to anagram (sortedWord)
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        #if not, we encountered it first time, so store it as new array of word
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())
            
    pass
