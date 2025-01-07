def generate_permutations(size):
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

    def recursively_generate_subarray(subarray_size):
        if subarray_size == 1:
            return

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
