import tkinter as tk
from tkinter import filedialog
import utils
import time

class QueenLinkedIn:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("N-Queens LinkedIn Problem")
        self.window.geometry("500x600")

        self.n = 0
        self.data_file = []
        self.color_area = []
        self.block = []
        self.last_print_time = 0
        self.durasi = 0
        self.solution_board = []

        self.frame_top = tk.Frame(self.window)
        self.frame_top.pack(pady=10)

        self.label_n = tk.Label(self.frame_top, text="Masukkan n:")
        self.label_n.pack(side=tk.LEFT, padx=5)

        self.input_n = tk.Entry(self.frame_top, width=5)
        self.input_n.pack(side=tk.LEFT, padx=5)

        self.btn_open = tk.Button(self.frame_top, text="open file", command=self.open_file, width=15)
        self.btn_open.pack(side=tk.LEFT, padx=5)

        self.btn_search = tk.Button(self.frame_top, text="search", command=self.search, width=15)
        self.btn_search.pack(side=tk.LEFT, padx=5)

        self.label_status = tk.Label(self.window, text="masukkan N lalu pilih file input.")
        self.label_status.pack()

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack(pady=10)

        self.frame_bot = tk.Frame(self.window)
        self.frame_bot.pack()

        self.label_hasil = tk.Label(self.frame_bot, text="", fg="darkgreen")
        self.label_hasil.pack()

        self.frame_save = tk.Frame(self.window)
        self.frame_save.pack(pady=5)

        self.label_save = tk.Label(self.frame_save, text="nama file output:")
        self.label_save.pack(side=tk.LEFT, padx=5)

        self.input_filename = tk.Entry(self.frame_save, width=20)
        self.input_filename.pack(side=tk.LEFT, padx=5)
        self.input_filename.insert(0, "")

        self.btn_save = tk.Button(self.frame_save, text="save", command=self.save_result, width=10)
        self.btn_save.pack(side=tk.LEFT, padx=5)

        self.window.mainloop()
    
    def open_file(self):
        isi_n = self.input_n.get()
        if isi_n == "":
            self.label_status.config(text="error: isi nilai N terlebih dahulu!", fg="red")
            return
        
        if isi_n.isdigit() == False:
            self.label_status.config(text="error: nilai N harus berupa angka!", fg="red")
            return
            
        self.n = int(isi_n)
        
        filename = tk.filedialog.askopenfilename(initialdir="../test/input")
        if filename == "":
            return
        
        f = open(filename, 'r')
        isi_text = f.read()
        f.close()

        temp_data = isi_text.strip().split('\n')
        jumlah_row = len(temp_data)

        if self.n != jumlah_row:
            self.label_status.config(text="error: jumlah baris pada file tidak sesuai dengan N!", fg="red")
            for widget in self.board_frame.winfo_children():
                widget.destroy()
            self.data_file = []
            return

        self.data_file = temp_data
        self.color_area = utils.data_color(isi_text)
        self.solution_board = []

        self.board_ui()
        self.label_status.config(text="file berhasil dibuka, silakan klik search untuk mencari solusi", fg="black")
        self.label_hasil.config(text="")

    def board_ui(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.block = []
        color_list = [
            "#FF9999", "#FFCC99", "#FFFF99", "#99FF99", "#99FFFF", "#9999FF", "#FF99FF", "#E0E0E0",
            "#FFDAB9", "#E6E6FA", "#F0E68C", "#ADD8E6", "#98FB98", "#FFB6C1", "#D3D3D3", "#F5DEB3",
            "#87CEEB", "#FFA07A", "#EE82EE", "#40E0D0", "#F08080", "#9ACD32", "#DA70D6", "#B0E0E6",
            "#FFEFD5", "#D2B48C"
        ]

        for i in range(self.n):
            block_row = []
            txt_row = self.data_file[i].strip()
            for j in range(self.n):
                huruf = txt_row[j]
                
                if huruf.isalpha():
                    color_idx = (ord(huruf.upper()) - 65) % 26
                else:
                    color_idx = 0 
                
                color_bg = color_list[color_idx]

                block_box = tk.Label(self.board_frame, text="", width=4, height=2, bg=color_bg, borderwidth=1, relief="solid", font=("Arial", 12, "bold"))

                block_box.grid(row=i, column=j)
                block_row.append(block_box)
            self.block.append(block_row)
    
    def update_screen(self, board, n, raw_lines):
        current_time = time.time()
        if current_time - self.last_print_time < 0.2:
            return
        
        self.last_print_time = current_time
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    self.block[i][j].config(text="Q", fg="black")
                else:
                    self.block[i][j].config(text="")
        self.label_status.config(text="mencari solusi... langkah ke: " + str(utils.stats), fg="blue")
        self.window.update()
    
    def search(self):
        if self.n == 0:
            self.label_status.config(text="error: silakan buka file terlebih dahulu", fg="red")
            return
        
        if len(self.data_file) == 0:
            self.label_status.config(text="error: file kosong atau tidak valid", fg="red")
            return

        utils.stats = 0
        board = utils.initial_board(self.n)
        utils.print_live = self.update_screen

        self.label_status.config(text="cari solusi...", fg="blue")
        start_time = time.time()
        res = utils.run_brute_force(board, 0, self.color_area, self.data_file)
        end_time = time.time()
        self.durasi = int((end_time - start_time) * 1000)

        if res == True:
            for i in range(self.n):
                for j in range(self.n):
                    if board[i][j] == 1:
                        self.block[i][j].config(text="Q", fg="black")
                    else:
                        self.block[i][j].config(text="")
            
            self.solution_board = board
            self.label_status.config(text="Selesai", fg="green")
            
            pesan = "Waktu pencarian: " + str(self.durasi) + " ms\n"
            pesan = pesan + "Banyak kasus yang ditinjau: " + str(utils.stats) + " kasus"
            self.label_hasil.config(text=pesan)
            
        else:
            self.solution_board = []
            self.label_status.config(text="Tidak ada solusi yang ditemukan.", fg="red")
            self.label_hasil.config(text="Waktu pencarian: " + str(self.durasi) + " ms")

    def save_result(self):
        if self.solution_board == []:
            self.label_status.config(text="error: belum ada solusi untuk disimpan", fg="red")
            return

        filename = self.input_filename.get()
        if filename == "":
            self.label_status.config(text="error: nama file tidak boleh kosong", fg="red")
            return
        
        if filename.endswith(".txt") == False:
            filename = filename + ".txt"
            
        path = "../test/output/" + filename
        
        f = open(path, 'w')
        for i in range(self.n):
            str_row = ""
            txt_original = self.data_file[i].strip()
            for j in range(self.n):
                if self.solution_board[i][j] == 1:
                    str_row = str_row + "#"
                else:
                    if j < len(txt_original):
                        str_row = str_row + txt_original[j]
                    else:
                        str_row = str_row + "."
            f.write(str_row + "\n")
        
        f.write("\n")
        f.write("Waktu pencarian: " + str(self.durasi) + " ms\n")
        f.write("Banyak kasus yang ditinjau: " + str(utils.stats) + " kasus\n")
        f.close()
        
        self.label_status.config(text="berhasil disimpan ke " + path, fg="green")

if __name__ == "__main__":
    app = QueenLinkedIn()