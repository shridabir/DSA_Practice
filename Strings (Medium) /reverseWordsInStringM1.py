def reverseWordsInStringM1(string):
    #M1 - keep track of all the words including spaces
    #TC = O(n)
    #SC = O(n)
    # Write your code here.

    words = [] #list to keep track of all words
    startOfWord = 0 #changes to current idx when it encounters a space

    for idx in range(len(string)):
        character = string[idx]

        #check if character at this idx is a space
        if character == " ":
            #if it is, we have a word which is from startOfWord until current idx(space) but not including currentidx (space)
            words.append(string[startOfWord:idx])
            #update startOfWord to current idx
            startOfWord = idx
        #if character at current idx is not a space but character at startOfWord idx is a space
        elif string[startOfWord] == " ":
            #append thta space in word list
            words.append(" ")
            #move startOfWord to current idx - idx of space
            startOfWord = idx

    #need to add last word in words list - because in this case we won't reach situation where character == " " and last word will not be added
    #therefore add it manually at end
    #if no trailing spaces
    words.append(string[startOfWord:])

    reverseList(words) #reverses this list
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list) - 1

    while start < end:
        list[start], list[end] = list[end], list[start] #swapping
        start += 1
        end -= 1
