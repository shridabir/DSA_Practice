def arrayOfProducts(array):
    # Write your code here.
    #M-1 brute force
    '''
    products = [1 for _ in range(len(array))]

    for i in range (len(array)):
        runningProduct = 1
        for j in range (len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct

    return products
    pass
    '''

    ''''
    #M-2 optimal TC: O(n) | SC: O(n)
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range (len(array)):
        leftProducts[i] = leftRunningProduct #store current running product in leftarray
        leftRunningProduct *= array[i] #update the running product by multiplying it by current element in array

    #similarly for right
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct #store current running product in rightarray
        rightRunningProduct *= array[i]

    #output array
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]
    return products
    '''

    #M-3 More optimized: no need of right array
    products = [1 for _ in range(len(array))]
    
    leftRunningProduct = 1
    for i in range (len(array)):
        products[i] = leftRunningProduct #store current running product in leftarray
        leftRunningProduct *= array[i] #update the running product by multiplying it by current element in array

    #similarly for right
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct #multiply leftrunningproduct by rightrunningproduct directly
        rightRunningProduct *= array[i]

    return products
