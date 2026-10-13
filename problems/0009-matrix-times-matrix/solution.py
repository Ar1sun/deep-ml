def matrixmul(a, b):
    # Shapes align only if columns of A == rows of B
    if len(a) == 0 or len(b) == 0:
        return -1
    if any(len(row) != len(b) for row in a):
        return -1

    # Columns of B via zip(*b)
    b_cols = list(zip(*b))

    return [[sum(x * y for x, y in zip(row, col)) for col in b_cols] for row in a]