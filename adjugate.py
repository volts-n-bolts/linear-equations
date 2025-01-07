import determinant

def generate(matrix):
    size = len(matrix)  # This is used in multiple places in the method.
    adjugate_matrix = []  # Stores all determinants of each minor to be returned.
    minor_determinants = []  # All the determinants after looping through the matrix of minors.

    # Calculates and appends each determinant to the list of `minor_determinants`.
    for i in range(size):
        for j in range(size):
            value = determinant.calculate(matrix[i][j])
            if (i + j) % 2 == 1:
                value *= -1
            minor_determinants.append(value)

    # Transposes all the calculated determinants of each minor to be returned as the adjugate matrix.
    for i in range(size):
        adjugate_row = []
        for j in range(size):
            adjugate_row.append(minor_determinants[size * j + i])
        adjugate_matrix.append(adjugate_row)

    return adjugate_matrix
