from utils import *
import utils
from time import time


def main():
    n = int(input("Masukkan n: "))
    filename = input("Masukkan nama file: ")
    with open(f"../test/input/{filename}.txt", 'r') as f:
        content = f.read()
    
    if n != len(content.strip().split('\n')):
        print("Input tidak sesuai dengan n, silakan cek lagi input")
        return

    content = load_file(filename)
    print(content)
    print('\n')

    colored_area = getColorData(content)

    board = initial_board(n)
    utils.stats = 0

    start_time = time()
    result = run_brute_force(board, 0, colored_area)

    end_time = time()
    durasi = end_time - start_time
    
    if result:
        print_board(board, content, durasi, utils.stats)
    else:
        print("Tidak ada solusi yang ditemukan.")
        print("Waktu pencarian: " + str(int(durasi * 1000)) + " ms")
        print("Jumlah kasus yang ditinjau: " + str(utils.stats))

if __name__ == "__main__":
    main()