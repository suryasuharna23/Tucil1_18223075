from utils import *
import utils
from time import time

def main():
    n = int(input("Masukkan n: "))
    filename = input("Masukkan nama file: ")
    with open(f"../test/input/{filename}.txt", 'r') as f:
        raw_content = f.read()
    
    raw_lines = raw_content.strip().split('\n')

    if n != len(raw_lines):
        print("Input tidak sesuai dengan n, silakan cek lagi input")
        return

    vis_input = load_file(filename)
    print(vis_input)
    print("\n")

    colored_area = data_color(raw_content)

    board = initial_board(n)
    utils.stats = 0

    start_time = time()
    result = run_brute_force(board, 0, colored_area, raw_lines)
    print_live(board, n, raw_lines)

    end_time = time()
    durasi = end_time - start_time
    
    if result:
        print_board(board, raw_lines, durasi, utils.stats)
    else:
        print("Tidak ada solusi yang ditemukan.")
        print("Waktu pencarian: " + str(int(durasi * 1000)) + " ms")
        print("Jumlah kasus yang ditinjau: " + str(utils.stats))

if __name__ == "__main__":
    main()