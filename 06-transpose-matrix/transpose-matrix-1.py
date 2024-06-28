# Transpose Matrix

def transposeMatrix(matrix):
    # Get the number of rows and columns in the original matrix
    row_count = len(matrix)
    column_count = len(matrix[0])
    
    # Initialize the matrix with the correct dimensions
    transposed_matrix = []    
    for _ in range(column_count):
        new_row = [None] * row_count
        transposed_matrix.append(new_row)
    
    # Fill the transposed matrix
    for i in range(row_count):
        for j in range(column_count):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix