#O(w * h) Time | O(w * h) Space
def transposeMatrix(matrix):
    # Write your code here.
    transposedMatrix = []
    for col in range (len(matrix[0])):
        newRow = []
        for row in range (len(matrix)): #for each row pick the element in current column
            newRow.append(matrix[row][col])  #appends the element at row row and column col from original matrix
        transposedMatrix.append(newRow)
    return transposedMatrix
    return []
