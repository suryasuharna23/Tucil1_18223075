# Tugas Kecil 1 IF2211 Strategi Algoritma

## Struktur Folder

```
Tucil1_18223075/
│
├── bin/         # File run.bat karena python tidak menghasilkan executeable program
├── doc/         # Dokumen laporan tugas kecil 
├── src/         # Source code utama program
├── test/        # Data uji dan hasil output program
│   ├── input/   # File input untuk pengujian
│   └── output/  # Hasil output dan gambar solusi
├── README.md    # Dokumentasi dan petunjuk penggunaan
```


## Penjelasan Singkat Program
Program ini merupakan implementasi penyelesaian Permainan Queens Linkedin. Tujuan dari gim ini adalah menempatkan queen pada sebuah papan persegi berwarna sehingga terdapat hanya satu queen pada tiap baris, kolom, dan daerah warna. Selain itu, satu queen tidak dapat ditempatkan bersebelahan dengan queen lainnya, termasuk secara diagonal.

## Requirement dan Instalasi
- Python 3.x (disarankan versi terbaru)
- Library tambahan: Pillow (untuk pengolahan gambar)
	- Install dengan perintah: `pip install pillow`

## Cara Menjalankan Program
1. Lakukan cloning repository https://github.com/suryasuharna23/Tucil1_18223075.git
2. Pastikan semua requirement sudah terpasang.
3. Jalankan file `run.bat` yang ada di folder `bin` dengan cara:
	 - Buka Command Prompt atau PowerShell di folder utama.
	 - Jalankan perintah: `bin\run.bat`
4. Antarmuka program akan muncul dan siap digunakan.

## Cara Mengkompilasi Program
Tidak perlu kompilasi, cukup jalankan langsung dengan Python seperti langkah di atas.

## Penjelasan File dan Fungsi Utama

### src/interface.py
- Menyediakan fungsi-fungsi untuk interaksi pengguna:
	- Menampilkan menu utama.
	- Menerima input file dari pengguna.
	- Menampilkan hasil proses (solusi, waktu eksekusi, visualisasi).
	- Menampilkan pesan error jika input tidak valid.
	- Mengatur flow interaksi antara pengguna dan program.

### src/main.py
- Berisi fungsi utama (`main`) sebagai entry point program:
	- Memproses argumen atau input dari pengguna.
	- Memanggil fungsi dari interface untuk mendapatkan input dan menampilkan output.
	- Mengatur pemanggilan algoritma utama (misal: pencarian solusi).
	- Mengatur penyimpanan hasil ke file output jika diperlukan.

### src/utils.py
- Berisi fungsi-fungsi utilitas:
	- Membaca file input dan mengubahnya menjadi struktur data yang sesuai.
	- Menulis hasil ke file output.
	- Validasi data input.
	- Fungsi pendukung lain seperti pengolahan data, konversi format, atau perhitungan tambahan yang dibutuhkan algoritma utama.

## Author

| Nama           | NIM      | Kelas | GitHub           |
|----------------|----------|-------|------------------|
| Surya Suharna  | 18223075 | K01   | @suryasuharna23  |

## Catatan
Pada live update, terdapat penampilan papan bahwa jika kurang dari 0.2 detik (200 milidetik) maka tidak melakukan update tampilan, atau dengan kata lain membatasi update tampilan maksimal 5 kali per detik.