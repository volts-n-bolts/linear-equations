from src.matrix_operations.determinant import calculate as det_calculate
from src.matrix_operations.minor_matrices import generate as generate_minors
from src.matrix_operations.inverse import calculate as inv_calculate
from src.matrix_operations.adjugate import generate as generate_adjugate
from src.matrix_operations.multiplication import calculate as multiply


#        ###################
#        # End Result Math #
#        ###################


# matrix_a = [
#     [5, 4],
#     [2, 1]
# ]

# matrix_b = [[22], [31]]

# matrix_a = [
#     [5, 4, 1],
#     [2, 1, 2],
#     [1, 2, 3]
# ]

# matrix_b = [[22], [31], [12]]

matrix_a = [
    [1, 3, 5, 4],
    [8, 16, 2, 9],
    [4, 7, 29, 7],
    [25, 16, 11, 18]
]

matrix_b = [[22], [31], [12], [19]]

# matrix_a = [
#     [1, 3, 5, 4, 6],
#     [8, 16, 2, 17, 9],
#     [4, 7, 29, 33, 7],
#     [25, 16, 2, 11, 18],
#     [4, 16, 23, 14, 36]
# ]
#
# matrix_b = [[22], [31], [12], [19], [4]]

# matrix_a = [
#     [84, 23, 45, 67, 89, 12],
#     [32, 65, 87, 19, 43, 76],
#     [55, 88, 22, 44, 66, 99],
#     [91, 13, 57, 79, 24, 46],
#     [47, 69, 92, 14, 58, 80],
#     [26, 48, 71, 93, 16, 59]
# ]

# matrix_b = [[22], [31], [12], [19], [4], [16]]

# matrix_a = [
#     [84, 23, 45, 67, 89, 12, 34],
#     [32, 65, 87, 19, 43, 76, 98],
#     [55, 88, 22, 44, 66, 99, 33],
#     [91, 13, 57, 79, 24, 46, 68],
#     [47, 69, 92, 14, 58, 80, 25],
#     [26, 48, 71, 93, 16, 59, 81],
#     [38, 72, 95, 17, 49, 62, 84]
# ]

# matrix_b = [[22], [31], [12], [19], [4], [16], [10]]

# matrix_a = [
#     [84, 23, 45, 67, 89, 12, 34, 56],
#     [32, 65, 87, 19, 43, 76, 98, 21],
#     [55, 88, 22, 44, 66, 99, 33, 77],
#     [91, 13, 57, 79, 24, 46, 68, 35],
#     [47, 69, 92, 14, 58, 80, 25, 36],
#     [26, 48, 71, 93, 16, 59, 81, 37],
#     [38, 72, 95, 17, 49, 62, 84, 27],
#     [85, 28, 51, 74, 96, 18, 40, 63]
# # ]

# matrix_b = [[22], [31], [12], [19], [4], [16], [10], [8]]

# matrix_a = [
#     [84, 23, 45, 67, 89, 12, 34, 56, 78],
#     [32, 65, 87, 19, 43, 76, 98, 21, 54],
#     [55, 88, 22, 44, 66, 99, 33, 77, 10],
#     [91, 13, 57, 79, 24, 46, 68, 35, 82],
#     [47, 69, 92, 14, 58, 80, 25, 36, 70],
#     [26, 48, 71, 93, 16, 59, 81, 37, 61],
#     [38, 72, 95, 17, 49, 62, 84, 27, 50],
#     [85, 28, 51, 74, 96, 18, 40, 63, 86],
#     [41, 64, 87, 30, 52, 75, 97, 19, 42]
# ]
#
# matrix_b = [[22], [31], [12], [19], [4], [16], [10], [8], [29]]

determinant_of_a = det_calculate(matrix_a)
matrix_of_minors = generate_minors(matrix_a)
adjugate_of_a = generate_adjugate(matrix_of_minors)

# print(determinant_of_a)
# print(adjugate.generate(matrix_of_minors))
inverse_of_a = inv_calculate(adjugate_of_a, determinant_of_a)

print(multiply(inverse_of_a, matrix_b))
