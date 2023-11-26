
def sudoko_solver(board):
    def is_valid(num, row, col):
        # check for dupes
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                return False

        return True

    def get_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j

        return None

    def back_tracking():
        empty_cell = get_empty()
        if empty_cell is None:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num

                if back_tracking():
                    return True

                board[row][col] = 0

        return False

    if back_tracking():
        return board
    else:
        return None


board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(sudoko_solver(board))