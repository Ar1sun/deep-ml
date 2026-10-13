def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    """
    if not a:
        return []

    return [[a[i][j] for i in range(len(a))]
            for j in range(len(a[0]))]


print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))