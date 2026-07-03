def runLengthEncoding(string):
    # Write your code here.
    #keep track of run in list and keep track of length of run (min len is 1)
    runChars = []
    currentRunLength = 1

    for i in range (1, len(string)):
        #check for condition to append run in list
        currentCharacter = string[i]
        prevCharacter = string[i - 1]

        if currentCharacter != prevCharacter or currentRunLength == 9:
            runChars.append(str(currentRunLength)) #append length as string
            runChars.append(prevCharacter)
            #reset length to 0
            currentRunLength = 0
        #if not the condition, increase the length
        currentRunLength += 1

    #handle last character manually
    #append current length and last character of string in list
    runChars.append(str(currentRunLength))
    runChars.append(string[len(string) - 1])

    #convert list to string
    return "".join(runChars)
