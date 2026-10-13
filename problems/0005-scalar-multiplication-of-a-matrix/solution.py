def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    """
    Multiply each element of a matrix by a scalar.

    Args:
        matrix: A 2D matrix of numbers.
        scalar: The number to multiply each element by.

    Returns:
        The resulting matrix.
    """
    result = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        result.append(new_row)

    return result


# Example usage
matrix = [[1, 2], [3, 4]]
scalar = 2

print(scalar_multiply(matrix, scalar))