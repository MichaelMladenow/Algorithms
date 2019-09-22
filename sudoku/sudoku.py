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

qwidth  = 3               # Quadrant Width
qheight = 3               # Quadrant Height
nums    = list(range(1,10))  # Possible Numbers


def get_quadrant(matrix, row, col):
    """Get all elements in a cell's quadrant."""
    numbers   = nums[:]
    col_start = qheight * (col // qheight)
    col_end   = col_start + qheight
    row_start = qwidth * (row // qwidth)
    row_end   = row_start + qwidth
    return [row[col_start:col_end] for row in
            matrix[row_start:row_end]]


def get_quadrant_options(matrix, row, col):
    """Get all available options in a cell's quadrant."""
    numbers    = nums[:]
    sub_matrix = get_quadrant(matrix, row, col)
    for row in sub_matrix:
        for item in row:
            if item in numbers:
                numbers.pop(numbers.index(item))
    return numbers


def get_row_options(matrix, row):
    """Get all available numbers in a row."""
    numbers = nums[:]
    for item in matrix[row]:
        if item in numbers:
            numbers.pop(numbers.index(item))
    return numbers


def get_col_options(matrix, col):
    """Get all available numbers in a column."""
    numbers = nums[:]
    for row in matrix:
        if row[col] in numbers:
            numbers.pop(numbers.index(row[col]))
    return numbers


def intersected_items(*args):
    """Returns items, present in all iterables.
    param args - arbitrary number of python lists."""
    intersection = []
    for item in args[0]:
        for item_set in args[1:]:
            if item not in item_set:
                break
        else:
            intersection.append(item)
    return intersection


def find_next_empty_cell(matrix):
    """Returns the index of the first cell with
    a values of zero from the 2D matrix."""
    for row in range(9): 
        for col in range(9): 
            if(matrix[row][col]==0):
                return (row, col)
    return False


def print_matrix(matrix):
    """Renders the matrix to the console, using
    dividers to separate quadrants."""
    for ix,x in enumerate(matrix):
        if not (ix % 3):
            print("-"*(len(x)+4))
        out_line = []
        for iy,y in enumerate(x):
            if (iy == 0) or (iy == len(x)) or not (iy % 3):
                out_line.append("|")
            out_line.append(str(y))
        out_line.append("|")
        print("".join(out_line))
    print("-"*(len(matrix[0])+4))   


def get_valid_opts(matrix, row, col):
    """Get the valid options for a cell in a
    sudoku matrix."""
    row_opts  = get_row_options(matrix, row)
    col_opts  = get_col_options(matrix, col)
    quad_opts = get_quadrant_options(matrix, row, col)
    return intersected_items(row_opts, col_opts, quad_opts)


def check_sudoku(matrix):
    next_cell = find_next_empty_cell(matrix)
    
    if not next_cell:
        return True

    row,col = next_cell
    opts    = get_valid_opts(matrix, row, col)
    for opt in opts:
        matrix[row][col] = opt
        if check_sudoku(matrix):
            return True
        matrix[row][col] = 0

    return False
        
    
if check_sudoku(sudoku_matrix):
    print_matrix(sudoku_matrix)
else:
    print("Can't find a solution")
    

