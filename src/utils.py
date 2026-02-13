def initial_board(n):
    board = [[0 for i in range(n)] for j in range(n)]
    return board

def isValid(board, row, col, colored_area):
    # Check column and row
    for i in range(len(board)):
        if (board[row][i] == 1) and (i != col):
            return False
        if (board[i][col] == 1) and (i != row):
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

def move(board, row, colored_area):
    n = len(board)

    if row >= n:
        return True
    for col in range(n):
        if isValid(board, row, col, colored_area):
            board[row][col] = 1
            if move(board, row+1, colored_area):
                return True
            board[row][col] = 0
    return False

def getColor(area):
    rows = area.strip().split('\n')
    n = len(rows)
    areas = {}

    for i in range(n):
        rc = rows[i].strip()
        for j in range(n):
            color = rc[j]
            if color not in areas:
                areas[color] = []
            areas[color].append((i,j))

    return list(areas.values())