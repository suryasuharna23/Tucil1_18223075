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

def getColorData(area):
    rows = area.strip().split('\n')
    n = len(rows)
    areas = {}

    for i in range(n):
        rc = rows[i].strip() # rc = color in row i
        for j in range(len(rc)):
            color = rc[j]
            if color not in areas:
                areas[color] = []
            areas[color].append((i,j))

    return areas

def loadFile(filename):
    with open(f"../test/input/{filename}.txt", 'r') as f:
        content = f.read()
    
    colors = [
        "\033[91m", "\033[92m", 
        "\033[93m", "\033[94m", 
        "\033[95m", "\033[96m",
        "\033[31m", "\033[32m", 
        "\033[33m", "\033[34m", 
        "\033[35m", "\033[36m",
        "\033[91;1m", "\033[92;1m", 
        "\033[93;1m", "\033[94;1m", 
        "\033[95;1m", "\033[96;1m", 
        "\033[37m", "\033[90m", 
        "\033[41m", "\033[42m", 
        "\033[43m", "\033[44m", 
        "\033[45m", "\033[46m"
    ]
    reset = "\033[0m"

    unique_chars = []

    for i in range(len(content)):
        char = content[i]

        if char == '\n':
            continue
        if char == ' ':
            continue

        exist = False
        for j in range(len(unique_chars)):
            if unique_chars[j] == char:
                exist = True
                break
        
        if exist == False:
            unique_chars.append(char)

        r = ""
        for i in range(len(content)):
            char = content[i]
            if char == '\n' or char == ' ':
                r += char
                continue
            
            idx = 0
            for j in range(len(unique_chars)):
                if unique_chars[j] == char:
                    idx = j
                    break
            while idx >= len(colors):
                idx -= len(colors)

            selected = colors[idx]

            r += selected + char + reset
    return r
