def initial_board(n):
    board = [[0 for i in range(n)] for j in range(n)]
    return board

def isValid(board, row, col, colored_area):
    # Check column and row
    for i in range(len(board)):
        if (board[row][i] == 1) and (i != col):
            return False

    # Check diagonals
    for i in range(len(board)):
        if (board[i][j] == 1) and (abs(row - i) == abs(col - j)):
            return False
    
    for area in colored_area:
        queen_in_area = sum(board[x][y] for x, y in area if 0 <= x < len(board) and 0 <= y < len(board))

        if (row, col) in area and queen_in_area > 0:
            return False
    
    return True