def validIPAddresses(string):
    # Write your code here.

    ipAddressFound = [] #stores valid addresses

    #we used min of len(string) and 4 just in case if string is shorter
    for i in range(1, min(len(string), 4)):
        #divide into 4 parts for 4 periods
        currentIPAddressParts = ['', '', '', '']
        #1st part is everything before i
        currentIPAddressParts[0] = string[:i]
        #if not valid we will continue in loop
        if not isValidPart(currentIPAddressParts[0]):
            continue
            
        #if valid check for 2nd period
        for j in range(i + 1, i + min(len(string) - i, 4)): #checks and enforces max len of IP Address part (3 digits) as pyhton's range function is exclusive of upperbound we put 4
            #len(string)-i is remaining part of string after first part
            #part for 2nd period will be from i (where first period is placed till current j)
            currentIPAddressParts[1] = string[i:j]
            #check if its not valid, if not valid we will continue
            if not isValidPart(currentIPAddressParts[1]):
                continue

            #if valid check for 3rd period
            for k in range(j + 1, j + min(len(string) - j, 4)):#checks and enforces max len of IP Address part (3 digits) as pyhton's range function is exclusive of upperbound we put 4
            #len(string)-j is remaining part of string after second part
                #part for 3rd period will be from j (where 2nd period is placed till current k)
                currentIPAddressParts[2] = string[j:k]
                #part after 3rd period will be from where 3rd period is placed until end of string
                currentIPAddressParts[3] = string[k:]
                #check if these parts are valid
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    #if valid we will append all the parts to ipAddressFound joined by '.'
                    ipAddressFound.append('.'.join(currentIPAddressParts))

    return ipAddressFound
            
        
        


#function to check if the part is valid part of IP address
def isValidPart(string):
    #convert string to int
    stringAsInt = int(string) #here any leading 0s will be removed after converting to int e.g 00 will be 0
    if stringAsInt > 255:
        return False

    return len(string) == len(str(stringAsInt)) #checks for leading 0 after conversion back to string
    
        
    return []
