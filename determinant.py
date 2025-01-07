import heaps_algorithm

def calculate(matrix):
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

    permutations_list = heaps_algorithm.generate_permutations(len(matrix))

    determinant_value = 0

    # The index is used to get the current permutation parity even/odd
    for index in range(len(permutations_list)):

        sign = 1  # Determines if the multiplied values are added or subtracted.
        value = 1  # Subsequent elements will be multiplied to this value.

        if index % 2 == 1:
            sign *= -1

        # Looks up the respective column number from the permutations list for each row to calculate the determinant.
        for sub_index in range(len(permutations_list[index])):
            value *= matrix[sub_index][permutations_list[index][sub_index]]

        determinant_value += sign * value

    return determinant_value