data_mahasiswa = []

def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = (input("Masukkan nilai mahasiswa: "))
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("Data berhasil ditambahkan!")

def tampilkan():
    if len(data_mahasiswa) == 0:
        print("Belum ada data yang tersimpan.")
    else:
        print("Daftar Nilai Mahasiswa:")
        for i, mahasiswa in enumerate(data_mahasiswa):
            print(f"{i + 1}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

def hapus(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa["nama"] == nama:
            data_mahasiswa.remove(mahasiswa)
            print(f"Data dengan nama {nama} berhasil dihapus!")
            return
    print(f"Data dengan nama {nama} tidak ditemukan.")

def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa["nama"] == nama:
            nilai_baru = (input(f"Masukkan nilai baru untuk {nama}: "))
            mahasiswa["nilai"] = nilai_baru
            print(f"Data dengan nama {nama} berhasil diubah!")
            return
    print(f"Data dengan nama {nama} tidak ditemukan.")

def menu():
    while True:
        print("\n=== Program Daftar Nilai Mahasiswa ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang ingin diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()