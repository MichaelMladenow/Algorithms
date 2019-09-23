"""
    Some settings below.
"""
qwidth  = 3                   # Quadrant Width
qheight = 3                   # Quadrant Height
row_len = 9                   # Row size
col_len = 9                   # Col size
nums    = list(range(1, 10))  # Possible Numbers


def get_quadrant(matrix, row, col):
    """Get a submatrix of the cells quadrant.

    Retrieves a 3x3 submatrix, containing all cells in 
    a cell's quadrant.

    Args:
        int row: Index of the target cell's row.
        int col: Index of the target cell's col.

    Returns:
        list<int>: 3x3 matrix, containing all cells in
        the quadrant.
    """
    col_start = qheight * (col // qheight)
    col_end   = col_start + qheight
    row_start = qwidth * (row // qwidth)
    row_end   = row_start + qwidth
    return [row[col_start:col_end] for row in
            matrix[row_start:row_end]]


def get_quadrant_options(matrix, row, col):
    """Retrieves a 3x3 submatrix, containing the valid sudoku
    numbers in a cell's quadrant as per the rule that numbers
    in a quadrant must not repeat.

    Args:
        int row: Index of the target cell's row.
        int col: Index of the target cell's col.

    Returns:
        list<int>: 3x3 matrix, containing the valid numbers in a
        a cell's quadrant.
    """
    numbers    = nums[:]
    sub_matrix = get_quadrant(matrix, row, col)
    for row in sub_matrix:
        for item in row:
            if item in numbers:
                numbers.pop(numbers.index(item))
    return numbers


def get_row_options(matrix, row):
    """Retrieves all unoccupied options in a sudoku matrix row

    Args:
        int row: Index of the target row.

    Returns:
        list<int>: List of number 1-9 that are unoccupied in this row.
    """
    return [num for num in nums \
            if num not in matrix[row]]


def get_col_options(matrix, col):
    """Retrieves all unoccupied options in a sudoku matrix col.

    Args:
        int col: Index of the target col.

    Returns:
        int array of unoccupied numbers.
    """
    numbers = nums[:]
    for row in matrix:
        if row[col] in numbers:
            numbers.pop(numbers.index(row[col]))
    return numbers


def intersected_items(*args):
    """Filters elements, present in all collections.

    Args:
        list: List of elements. You could pass multiple lists to this function.

    Returns:
        list: Items present in all argument lists.
    """
    intersection = []
    for item in args[0]:
        for item_set in args[1:]:
            if item not in item_set:
                break
        else:
            intersection.append(item)
    return intersection


def find_next_empty_cell(matrix):
    """Find an empty cell in a sudoku matrix.

    Args:
        list<int> matrix: 9x9 sudoku matrix.

    Returns:
        list<int>[2]: [row_index, col_index] of the first free cell found.
        bool False: There's no empty space in the matrix.
    """
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 0:
                return row, col
    return False


def print_matrix(matrix):
    """Prints out a sudoku matrix on the console.

        Args:
            list<int>: 9x9 sudoku matrix.

        Returns:
            void
        """
    row_padding = row_len // qwidth + 1
    for row in range(row_len):
        if not (row % qheight):
            print("-" * (row_len + row_padding))
        out_line = []
        for col in range(col_len):
            if not (col % qwidth):
                out_line.append("|")
            out_line.append(str(matrix[row][col]))
        out_line.append("|")
        print("".join(out_line))
    print("-" * (row_len + row_padding))


def get_valid_opts(matrix, row, col):
    """Get the valid sudoku options(numbers) for a given cell.

    Retrieves all possible numbers 1-9 for a given sudoku cell
    based on the following rules:
        1) Numbers must be unique in each row
        2) Numbers must be unique in each column
        3) Numbers must be unique in each quadrant(3x)

    Args:
        int row: Index of the target cell's row.
        int col: Index of the target cell's col.

    Returns:
        list<int>: All numbers 1-9 that are valid for the
        sudoku cell.
    """
    row_opts  = get_row_options(matrix, row)
    col_opts  = get_col_options(matrix, col)
    quad_opts = get_quadrant_options(matrix, row, col)
    return intersected_items(row_opts, col_opts, quad_opts)


def check_sudoku(matrix):
    """Check a partially filled sudoku matrix for a solution.

    Recursively attempts to fill a sudoku matrix using a backtracking
    algorithm. Potential options are narrowed down as per the sudoku
    rules. If a solution is found it's printed on the console.

    Args:
        list<int> matrix: 9x9 Sudoku matrix. Some numbers can be pre-filled
        and empty cells are marked as 0.

    Returns:
        bool: Result - True if a solution is found and False if no solution
        can be found.
    """
    # Check if there are any free cells(free = 0).
    next_cell = find_next_empty_cell(matrix)

    # In case all cells are filled a solution is found
    if not next_cell:
        return True

    row, col = next_cell

    # Retrieve all seemingly valid options for a cell
    opts    = get_valid_opts(matrix, row, col)
    for opt in opts:
        # Make a prediction for a valid cell value and test it
        matrix[row][col] = opt
        if check_sudoku(matrix):
            return True

        # In case the predicted value cannot yield a solution
        # clear the prediction matrix backwards until we have another
        # option to test.
        matrix[row][col] = 0

    return False


if __name__ == "__main__":
    sudoku_matrix = [  # 0 - means empty cell
        # 1  2  3  4  5  6  7  8  9
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if check_sudoku(sudoku_matrix):
        print_matrix(sudoku_matrix)
    else:
        print("Can't find a solution")