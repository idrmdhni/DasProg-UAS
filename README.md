# Proyek UAS - Aplikasi Pemesanan Tiket Pesawat
Ini adalah proyek untuk Ujian Akhir Semester (UAS) mata kuliah **Dasar Pemrograman**. Program ini merupakan aplikasi konsol sederhana untuk memesan tiket pesawat, yang dilengkapi dengan sistem login untuk masuk ke aplikasi.

## Deskripsi Proyek
Aplikasi ini memungkinkan pengguna untuk melakukan hal berikut:
1.  **Membuat Akun & Masuk**: Sebelum melakukan pemesanan, pengguna harus mendaftar dan masuk ke dalam sistem. Informasi pengguna akan disimpan dalam file `database.txt`.
2.  **Pemesanan Tiket**: Pengguna dapat memilih kota asal, tujuan, dan waktu keberangkatan dari daftar yang tersedia (Balikpapan, Singapura, Kuala Lumpur).
3.  **Menghitung Biaya**: Sistem akan secara otomatis menghitung total biaya berdasarkan rute yang dipilih dan jumlah penumpang.
4.  **Cetak Tiket**: Setelah pemesanan berhasil, detail penerbangan dan informasi penumpang akan disimpan dalam sebuah file bernama `Tiket.txt`.

## Fitur Utama
* **Sistem Otentikasi**: Terdapat fitur `sign up` untuk pengguna baru dan `sign in` untuk pengguna yang sudah terdaftar.
* **Pemesanan Dinamis**: Pengguna dapat memilih rute dan jadwal penerbangan yang berbeda.
* **Kalkulasi Biaya Otomatis**: Harga tiket dihitung berdasarkan rute dan jumlah penumpang yang dimasukkan.
* **Penyimpanan Data**: Menggunakan file `.txt` sederhana (`database.txt` dan `Tiket.txt`) untuk menyimpan data pengguna dan detail tiket.

## Cara Menjalankan Program
1.  Pastikan Anda memiliki Python terpasang di sistem operasi yang sedang digunakan.
2.  Buka terminal atau command prompt.
3.  Jalankan salah satu file Python utama:
    ```bash
    python "[UAS]Tiket.py"
    ```
4.  Ikuti instruksi yang muncul di terminal untuk membuat akun, masuk, dan memesan tiket.
