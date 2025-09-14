# Minpro-1-DDP-2025
Nama: AULIA AISYAH AL HUMAIRA NIM: 2509116029 Sistem Informasi A'25

# PENJELASAN PROGRAM
### 1. Awal Program
* Program mulai dengan menampilkan judul: `=== Data Pengiriman Barang ===`.
* Lalu ada data awal: `data_kirim` yang sudah diisi contoh, dan `data_kirim_dua` yang masih kosong.
* Setelah itu, program menampilkan menu utama berisi 4 pilihan:
  1. Buat data (Create)
  2. Tampilkan data (Read)
  3. Ubah data (Update)
  4. Hapus data (Delete)
     lalu pilih menu

### 2. Pilihan 1 = **Buat Data (Create)**

* User diminta mengisi **Nomor Resi, Nama Pengirim, Nama Penerima, Jenis Barang**.
* Lalu ditanya apakah tujuan `dalam negeri (1)` atau `luar negeri (2)`.
* Kalau pilihannya (1 atau 2), tujuan akan disimpan di variabel `tujuan_barang`.
* Setelah itu, data baru dimasukkan ke dalam `data_kirim_dua`.
* Lalu, jika sudah semua program akan menampilkan isi **data pertama** (yang sudah ada dari awal) dan **data kedua** (yang baru dibuat).

### 3. Pilihan 2 = **Tampilkan Data (Read)**

* Program menampilkan judul “List data pengiriman”.
* User diminta memasukkan **Nomor Resi** untuk mencari data.
* Lalu membandingkan:

  * Kalau nomor resi cocok dengan data pertama (`data_kirim[0]`), tampilkan data pertama.
  * Kalau nomor resi cocok dengan data kedua (`data_kirim_dua[0]`), tampilkan data kedua.
  * Kalau nggak ada yang cocok, tampilkan pesan: “Nomor resi tidak ditemukan.”

### 4. Pilihan 3 → **Ubah Data (Update)**

* Program menampilkan judul “Update data”.
* Untuk **data pertama**:
  * Ditampilkan dulu data lama.
  * User diminta mengisi nama penerima baru dan tujuan baru.
  * Data pertama diganti sesuai input user.
* Untuk **data kedua**:
  * Kalau `data_kirim_dua` ada isinya → ditampilkan dulu data lama.
  * User diminta input penerima baru dan tujuan baru.
  * Data kedua diganti sesuai input user.
  * Kalau `data_kirim_dua` kosong, program akan bilang “List kedua belum ada.”

### 5. Pilihan 4 → **Hapus Data (Delete)**

* Program menampilkan judul “Hapus List”.
* User diminta memilih mau hapus list ke berapa (`1` atau `2`).
* Kalau pilih `1`, `data_kirim` dikosongkan.
* Kalau pilih `2`, `data_kirim_dua` dikosongkan.
* Kalau input selain 1/2, program bilang: “List tidak ditemukan.”


