def calculate(matrix_a, matrix_b):
    # Ensures that the multiplication obeys the rule that matrix_b has equal the rows as matrix_a has columns.
    if len(matrix_b) != len(matrix_a[0]):
        return []

    matrix_c = []

    for row in matrix_a:
        result = 0

        for index in range(len(row)):
            result += row[index] * matrix_b[index][0]

        matrix_c.append([round(result, 3)])

    return matrix_c