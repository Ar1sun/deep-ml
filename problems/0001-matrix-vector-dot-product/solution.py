def matrix_dot_vector(a, b):
    # Dimension check: every row must have as many columns as the vector has entries
    if len(a) == 0 or any(len(row) != len(b) for row in a):
        return -1

    return [sum(x * y for x, y in zip(row, b)) for row in a]