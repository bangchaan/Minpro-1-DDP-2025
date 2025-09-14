print("\n=== Data Pengiriman Barang ===")

# Data awal (contoh)
data_kirim = ["CHN001", "Joko Tingkir", "Juan", "Sepatu", "dalam negeri"]
data_kirim_dua = [] # Data kosong
# ===== Menu =====
print("\n===== MENU =====")
print("1. Create data pengiriman")
print("2. Read / tampilkan data")
print("3. Update data")
print("4. Delete list (pilih 1/2)")
print("5. Keluar")

pilihan = input("Masukkan nomor pilihan (1-5): ")

# ==================== BUAT DATA ====================
if pilihan == "1":
    resi     = input("Masukkan Nomor Resi: ")
    pengirim = input("Nama Pengirim: ")
    penerima = input("Nama Penerima: ")
    barang   = input("Jenis Barang: ")

    print("dalam_negeri = 1")
    print("luar_negeri  = 2")
    tujuan_num = int(input("Masukkan angka 1 atau 2: "))

    if tujuan_num == 1:
        tujuan_barang = "dalam negeri"
        print("Tujuan berhasil ditambahkan")
    elif tujuan_num == 2:
        tujuan_barang = "luar negeri"
        print("Tujuan berhasil ditambahkan")
    else:
        tujuan_barang = None
        print("Tidak valid!")

    if tujuan_barang is not None:
        print(f"Tujuan pengiriman: {tujuan_barang}")
        data_kirim_dua = [resi, pengirim, penerima, barang, tujuan_barang]
        print("\n=== Data berhasil ditambahkan! ===")
        print(f"List data pertama: {data_kirim}")
        print(f"List data kedua  : {data_kirim_dua}")

# ==================== MENAMPILKAN DATA ====================
elif pilihan == "2":
    print("\n===============================")
    print("     List data pengiriman      ")
    print("===============================")
    cari = input("Masukkan nomor resi yang ingin dicari: ")
    if cari == data_kirim[0]:
        print(f"Data Pengiriman Ditemukan:{data_kirim}")
    elif data_kirim_dua and cari == data_kirim_dua[0]:
        print(f"Data Pengiriman Ditemukan:{data_kirim_dua}")
    else:
        print("Nomor resi tidak ditemukan.")

# ==================== UBAH DATA ====================
elif pilihan == "3":
    print("\n===============================")
    print("          Update data          ")
    print("===============================")

    print('\n----Data ke satu yang diganti----')
    print(f"Data pertama sebelum diupdate: {data_kirim}")
    penerima_baru = input("Masukkan nama penerima baru: ")
    tujuan_baru = input("Masukkan tujuan baru: ")
    data_kirim[2] = penerima_baru
    data_kirim[3] = tujuan_baru
    print(f"Data pertama berhasil diubah: {data_kirim}")

    print('----Data ke dua yang diganti----')
    if data_kirim_dua:   #  CEK DULU
        print(f"Data kedua sebelum diupdate: {data_kirim_dua}")
        penerima_baru = input("Masukkan nama penerima baru: ")
        tujuan_baru = input("Masukkan tujuan baru: ")
        data_kirim_dua[2] = penerima_baru
        data_kirim_dua[3] = tujuan_baru
        print(f"Data kedua berhasil diubah: {data_kirim_dua}")
    else:
        print("List kedua belum ada.")
# ==================== HAPUS ====================
elif pilihan == "4":
    print("\n=============================")
    print("          Hapus list         ")
    print("=============================")
    pilih = input("List data yang ingin dihapus (1/2): ")
    if pilih == "1":
        data_kirim.clear()
        print("List pertama berhasil dihapus:", data_kirim)
    elif pilih == "2":
        data_kirim_dua.clear()
        print("List kedua berhasil dihapus:", data_kirim_dua)
    else:
        print("List tidak ditemukan")

# ==================== KELUAR ====================
elif pilihan == "5":
    print("Program selesai.")

else:
    print("Pilihan tidak dikenal. Program selesai.")
