def create_permutations(size: int) -> list:
    """
    Heaps algorithm is used to create permutations, where only 1 swap occurs in a
    single step. Each step swaps 2 values, which each step signifies an even
    or odd permutation. So, even indices, (0, 2, 4, ...) are even permutations,
    and odd indices, (1, 3, 5, ...) are odd permutations.

    Additional Reading:
    https://en.wikipedia.org/wiki/Heap%27s_algorithm
    """

    values = [value for value in range(size)]  # All column index values.
    permutations_list = [values[:]]  # The list of permutations starts with the values in their original order.

    def recursively_generate_subarray(subarray_size) -> list:
        if subarray_size == 1:
            return []

        recursively_generate_subarray(subarray_size - 1)

        for i in range(subarray_size - 1):
            if subarray_size % 2 == 0:  # subarray_size is even
                values[i], values[subarray_size - 1] = values[subarray_size - 1], values[i]
            else:  # subarray_size is odd
                values[0], values[subarray_size - 1] = values[subarray_size - 1], values[0]
            permutations_list.append(values[:])
            recursively_generate_subarray(subarray_size - 1)

    recursively_generate_subarray(size)
    return permutations_list


def calculate_determinant(matrix: list) -> float:
    """
    To find the determinant, the Leibniz formula is used, which works by:
    1. Finding all possible ways to select one element from each row
       (using Heap's algorithm to recursively generate these patterns/permutations)
    2. Each pattern either adds (even indices) or subtracts (odd indices) its
       values to the final result based on how many swaps were needed.

    Heap's algorithm is ideal here because it recursively generates each pattern through
    single swaps, making it easy to track whether to add or subtract each term.
    The permutations are a lookup table for the column number of the matrix.

    Additional Reading:
    https://semath.info/src/determinant-def.html
    https://semath.info/src/determinant-properties.html
    https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants
    """

    permutations_list = create_permutations(len(matrix))

    determinant_value = 0

    # The index is used to get the current permutation parity even/odd
    for index in range(len(permutations_list)):

        sign = 1  # Determines if the multiplied values are added or subtracted.
        value = 1  # Subsequent elements will be multiplied to this value.

        # All odd indices have a subtraction operation.
        if index % 2 == 1:
            sign *= -1

        # Looks up the respective column number from the permutations list for each row to calculate the determinant.
        for sub_index in range(len(permutations_list[index])):
            value *= matrix[sub_index][permutations_list[index][sub_index]]

        determinant_value += sign * value

    return determinant_value


def create_minors(matrix: list) -> list:
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
        matrix_size = len(matrix)  # Assumes a square matrix where rows equal columns in size.
    else:
        return []

    minors = []  # Will store all sub-matrices.

    # For each position (row, col) in the resulting array of sub-matrices.
    for excluded_row in range(matrix_size):
        row_of_sub_matrices = []
        for excluded_column in range(matrix_size):
            # Create lists of row and column indices to keep.
            remaining_rows = [i for i in range(matrix_size) if i != excluded_row]
            remaining_columns = [j for j in range(matrix_size) if j != excluded_column]

            # Build the sub-matrix by selecting elements from remaining rows and columns.
            sub_matrix = []
            for row_index in remaining_rows:
                new_row = []
                for column_index in remaining_columns:
                    new_row.append(matrix[row_index][column_index])
                sub_matrix.append(new_row)

            row_of_sub_matrices.append(sub_matrix)
        minors.append(row_of_sub_matrices)

    return minors


def create_adjugate(matrix: list) -> list:
    size = len(matrix)  # This is used in multiple places in the method.
    adjugate_matrix = []  # Stores all determinants of each minor to be returned.
    minor_determinants = []  # All the determinants after looping through the matrix of minors.

    # Calculates and appends each determinant to the list of `minor_determinants`.
    for i in range(size):
        for j in range(size):
            value = calculate_determinant(matrix[i][j])
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


def calculate_inverse(matrix: list, determinant: float) -> list:
    # Prevents a divide by zero scenario.
    if determinant == 0:
        return []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= 1 / determinant

    return matrix


def multiply(matrix_a: list, matrix_b: list) -> list:
    # Ensures that the multiplication obeys the rule that the number of columns in matrix_a equals
    # the number of rows in matrix_b.
    if len(matrix_b) != len(matrix_a[0]):
        return []

    matrix_c = []

    for row in matrix_a:
        result = 0

        for index in range(len(row)):
            result += row[index] * matrix_b[index][0]

        matrix_c.append([round(result, 3)])

    return matrix_c


MATRIX_A = [
    [1, 3, 5, 4],
    [8, 16, 2, 9],
    [4, 7, 29, 7],
    [25, 16, 11, 18]
]

MATRIX_B = [[22], [31], [12], [19]]

determinant_of_a = calculate_determinant(MATRIX_A)
minor_matrices = create_minors(MATRIX_A)
adjugate_of_a = create_adjugate(minor_matrices)
inverse_of_a = calculate_inverse(adjugate_of_a, determinant_of_a)
resultant = multiply(inverse_of_a, MATRIX_B)

print(resultant)  # This is the end result of solving the system of equations.
