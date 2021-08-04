def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    row = len(matrix)-1
    col_TLBR = row
    col_BLTR = 0

    sum_TLBR = 0
    sum_BLTR = 0

    while (row >= 0):
        sum_TLBR += matrix[row][col_TLBR]
        sum_BLTR += matrix[row][col_BLTR]
        row -= 1
        col_TLBR -= 1
        col_BLTR += 1

    return sum_TLBR + sum_BLTR
