from utils import *

def main():
    n = int(input("Masukkan n: "))
    filename = input("Masukkan nama file: ")
    with open(f"../test/input/{filename}.txt", 'r') as f:
        content = f.read()
    
    if n != len(content.strip().split('\n')):
        print("Input tidak sesuai dengan n, silakan cek lagi input")
        return

    colored_content = loadFile(filename)
    print(colored_content)
    print('\n')

    mapColor = getColorData(content)
    print(mapColor)

    board = initial_board(n)

if __name__ == "__main__":
    main()