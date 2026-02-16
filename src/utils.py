import time
stats = 0
last_print_time = 0

def initial_board(n):
    board = [[0 for i in range(n)] for j in range(n)]
    return board

def is_valid(board, row, col, colored_area):
    n = 0
    for x in board:
        n = n + 1

    # Baris dan kolom
    for i in range(n):
        if i != row and board[i][col] == 1:
            return False
        if i != col and board[row][i] == 1:
            return False
    
    # Diagonal
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                if r != row or c != col:
                    jarak_baris = row - r
                    if jarak_baris < 0:
                        jarak_baris = -jarak_baris
                    jarak_kolom = col - c
                    if jarak_kolom < 0:
                        jarak_kolom = -jarak_kolom
                    if jarak_baris == 1 and jarak_kolom == 1:
                        return False
    
    # Area berwarna
    my_area = None
    for area in colored_area:
        for pos in area:
            if pos[0] == row and pos[1] == col:
                my_area = area
                break
        if my_area: break
    
    if my_area:
        count = 0
        for pos in my_area:
            if board[pos[0]][pos[1]] == 1:
                count += 1
        if count > 1:
            return False

    return True

def data_color(area):
    rows = area.strip().split('\n')
    n = len(rows)
    areas = {}

    for i in range(n):
        rc = rows[i].strip() # rc = color in row i
        
        if not rc: continue
        
        for j in range(len(rc)):
            color = rc[j]
            if color.isalnum():
                if color not in areas:
                    areas[color] = []
                areas[color].append((i,j))

    return list(areas.values())

def load_file(filename):
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

def run_brute_force(board, row, area, raw_lines=None):
    global stats
    n = len(board)

    if raw_lines is not None:
        print_live(board, n, raw_lines)

    if row == n:
        stats += 1
        for r in range(n):
            c = -1
            for k in range(n):
                if board[r][k] == 1:
                    c = k
                    break
            if c == -1: return False
            if is_valid(board, r, c, area)== False:
                return False
        return True

    for col in range(n):
        board[row][col] = 1
        if run_brute_force(board, row + 1, area, raw_lines):
            return True
        board[row][col] = 0
    return False  

def print_board(board, raw_lines, durasi, jumlah_kasus):
    n = len(board)
    txt_res = ""

    for r in range(n):
        row_str = ""

        if r < len(raw_lines):
            str_original = raw_lines[r].strip()
        else:
            str_original = ""*n

        for c in range(n):
            if board[r][c] == 1:
                row_str = row_str + '#'
            else:
                if c < len(str_original):
                    row_str += str_original[c]
                else:
                    row_str += "."
        
        txt_res += row_str + "\n"
    
    waktu_pencarian = "Waktu pencarian: " + str(int(durasi * 1000)) + " ms\n"
    banyak_kasus = "Jumlah kasus yang ditinjau: " + str(jumlah_kasus) + "\n"

    result = txt_res + "\n"+ waktu_pencarian + banyak_kasus

    print(result)

    save = input("Apakah Anda ingin menyimpan hasilnya? (y/n): ")
    if save == 'y' or save == 'Y' or save == 'ya' or save == 'Ya':
        filename = input("Masukkan nama file untuk menyimpan hasil: ")
        with open(f"../test/output/{filename}.txt", 'w') as f:
            f.write(result)
        print("Berhasil disimpan")
    else:
        print("Hasil tidak disimpan")

def print_live(board, n, raw_lines):
    global last_print_time
    
    current_time = time.time()

    if current_time - last_print_time < 0.3:
        return

    last_print_time = current_time

    print("\033[H", end="")
    
    txt_res = ""
    for r in range(n):
        row_str = ""
        if r < len(raw_lines):
            str_original = raw_lines[r].strip()
        else:
            str_original = ""*n
            
        for c in range(n):
            if board[r][c] == 1:
                row_str = row_str + '#'
            else:
                if c < len(str_original):
                    char = str_original[c]
                else:
                    char = "."
                row_str += char + " "
        txt_res += row_str + "\n"

    print(txt_res)
    print("coba kombinasi")