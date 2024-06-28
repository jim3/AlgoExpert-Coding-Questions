# Transpose Matrix, using a list comprehension

def transposeMatrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])
    
    return transposed
