def generate(matrix):
    """
    Generates all possible sub-matrices by excluding one row and one column at a time.
    For an n×n matrix, this creates an n×n array of (n-1)×(n-1) sub-matrices.
    
    Args:
        matrix: The input matrix (list of lists) to generate sub-matrices.
        
    Returns:
        list: Only if the input matrix is square, then a list of adjugate matrices will be returned -
              where each element is a sub-matrix excluding the corresponding row and column from the original matrix.
    """
    # Ensures the matrix is a square matrix.
    if len(matrix) == len(matrix[0]):
        matrix_size = len(matrix)  # Assuming square matrix
    else:
        return []

    minors = []  # Will store all sub-matrices

    # For each position (row, col) in the resulting array of sub-matrices
    for excluded_row in range(matrix_size):
        row_of_sub_matrices = []
        for excluded_column in range(matrix_size):
            # Create lists of row and column indices to keep
            remaining_rows = [i for i in range(matrix_size) if i != excluded_row]
            remaining_columns = [j for j in range(matrix_size) if j != excluded_column]
            
            # Build the sub-matrix by selecting elements from remaining rows and columns
            sub_matrix = []
            for row_index in remaining_rows:
                new_row = []
                for column_index in remaining_columns:
                    new_row.append(matrix[row_index][column_index])
                sub_matrix.append(new_row)
                
            row_of_sub_matrices.append(sub_matrix)
        minors.append(row_of_sub_matrices)
        
    return minors
