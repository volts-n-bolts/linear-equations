def calculate(matrix, determinant):
    # Prevents a divide by zero scenario.
    if determinant == 0:
        return []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= 1 / determinant

    return matrix
