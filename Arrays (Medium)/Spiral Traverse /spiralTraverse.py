ef spiralTraverse(array):
    # Write your code here.
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    #continue traversing until startRow doesn't pass endRow and startCol doesn't pass endCol
    while startRow <= endRow and startCol <= endCol:
        #top border: start from SC to EC inclusive and append elements in all columns of SR
        for col in range (startCol, endCol + 1):
            result.append(array[startRow][col])

        #right border: go down in SR i.e from startRow + 1 (don't print first element of EC again) until ER inclusive and print elements at every row of EC
        for row in range (startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        #bottom border: now go from right to left in ER, except the last element in ER as it is already printed
        #print element at every col of endRow
        for col in reversed(range(startCol, endCol)): #start from endCol to startCol
            if startRow == endRow:  #avoid double counting single row
                break
            result.append(array[endRow][col])

        #left border: now go from bottom to top (except first element at ER and firstelement in SR) as they are already printed
        #print every element in row of startCol
        for row in reversed(range(startRow + 1, endRow)): #start from endRow to startRow + 1
            if startCol == endCol: #avoid double counting single column
                break
            result.append(array[row][startCol]) 

        startRow += 1 #goes to bottom
        endRow -= 1 #goes upwards
        startCol += 1#goes rightwards
        endCol -= 1 #goes leftwards
        

    return result
