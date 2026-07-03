def majorityElement(array):
    # Write your code here.

    answer = None
    count = 0

    for num in array:
        #when count reaches 0 we have our subarray, put answer as current num and start for new subarray until count reaches 0 again
        if count == 0:
            answer = num
            
        #when found the num which is equal to answer, increment the count
        if num == answer:
            count += 1

        #else, decrement the count
        else:
            count -= 1

    return answer
            
    
    return -1
