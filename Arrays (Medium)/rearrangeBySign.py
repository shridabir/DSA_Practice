#Q.7 ARRANGE ARRAY ELEMENTS BY SIGN ALTERNATIVELY POSITIVE AND NEGATIVE - here there are equal number of positive and negative elements
#rearrange without changing the order
#brute force - create 2 lists to store pos and neg elements. add pos at even places in arr and neg at odd places
#TC - O(2n), SC - O(n)
def rearrangeBySignBrute (arr):
    n = len(arr)
    pos = []
    neg = []
    for i in range (n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range (n//2):
        arr[2*i] = pos[i] #pos at even places
        arr[2*i + 1] = neg[i] #neg at odd places
    return arr

#optimal - two pointer approach - two pointers at arr[0] = pos and arr[1] neg. Traverse through arr if < 0 place on first neg position and += 2. Same for pos
#TC = O(n), SC = O(1)
def rearrangeBySign (arr):
    n = len(arr)
    pos = 0 #pointer for positive elements
    neg = 1 #pointer for negative elements
    ans = [] #to store the rearranged array
    for i in range (n):
        if arr[i] < 0:
            ans.insert(neg, arr[i]) #insert neg element at neg pointer
            neg += 2 #move neg pointer to next odd index
        else:
            ans.insert(pos, arr[i]) #insert pos element at pos pointer
            pos += 2 #move pos pointer to next even index
    return ans
#Example usage
arr = [3,1,-2,-5,2,-4]
print("Array after rearranging by sign is:", rearrangeBySign(arr))

#Q.8 ARRANGE ARRAY ELEMENTS BY SIGN ALTERNATIVELY POSITIVE AND NEGATIVE - here there are unequal number of positive and negative elements
#rearrange without changing the order. If any elements are left, add them at the end of the array without changing the order.
#use brute force approach previously used and then add remaining extra elements
#TC - O(2n), SC - O(n)
def rearrangeBySignUnequal (arr):
    n = len(arr)
    pos = []
    neg = []
    for i in range (n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    #rearrange in new array
    ans = []
    minLength = min(len(pos), len(neg)) #to avoid index out of range error
    for i in range (minLength):
        ans.append(pos[i])
        ans.append(neg[i])
    
    #add remaining elements
    if len(pos) > len(neg):
        ans.extend(pos[minLength:]) #add remaining pos elements
    else:
        ans.extend(neg[minLength:])
    return ans

#Example usage
arr = [3,1,-2,-5,2,-4,6,8]
print("Array after rearranging by sign is:", rearrangeBySignUnequal(arr))
