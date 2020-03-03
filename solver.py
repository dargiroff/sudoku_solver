

def solve(bo):
    """
    Solves the input sudoku board
    :param bo: list if lists
        A list of lists, each of the latter is a row on the sudoku board
    :return: bool
        True or Solve based on if the sudoku board is successfully solved or not
    """
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    """

    :param bo: list of lists
         A list of lists, each of the latter is a row on the sudoku board
    :param num: int
        A number in a cell of the sudoku board
    :param pos: tuple
        A two-value tuple determining the position of a number entered into the sudoku board
    :return: bool
        True or False based on if the cells are filled with valid numbers
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    """
    A utility function that prints the contents of the sudoku board in the console

    :param bo: list of lists
         A list of lists, each of the latter is a row on the sudoku board
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """
    Finds empty cells on the sudoku board

    :param bo: list of lists
         A list of lists, each of the latter is a row on the sudoku board
    :return: None
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col

    return None
