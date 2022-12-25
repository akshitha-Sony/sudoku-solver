def find_next_empty(puzzle):
    # a position that isn't filled yet. rep -> -1
    # return row, col tuple
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None # if no spaces left (-1)

def is_valid(puzzle, guess, row, col):
    # return true if valid and false if not
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[r][col] for r in range(9)]
    if guess in col_vals:
        return False

    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    # if we get here then it's valid
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    # if there is no space left then solution exists
    if row is None:
        return True
    for guess in range(1,10):
        # check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # if valid place the guess on the puzzle
            puzzle[row][col]  = guess
            # now recurse using this puzzle!
            if solve_sudoku(puzzle):
                return True
        # if not valid or guess doesn't solve the puzzle, then backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess
    # if none of the numbers that we try work , then this puzzle is unsolvable
    return False

def print_board(puzzle):
    for row in puzzle:
        print(row)

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print_board(example_board)





