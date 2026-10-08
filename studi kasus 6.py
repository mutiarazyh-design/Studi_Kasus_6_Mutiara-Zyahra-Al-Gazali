import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


while True:
    print("\n=== SISTEM MANAJEMEN INVENTARIS BARANG ===")
    print("1. Lihat Data Barang")
    print("2. Tambah Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    # Read
    if pilihan == "1":
        print("\n=== DATA INVENTARIS BARANG ===")

        for barang in data:
            print("Nama Barang :", barang["nama_barang"])
            print("Stok         :", barang["jumlah"], barang["satuan"])
            print("-----------------------------")

    # Create
    elif pilihan == "2":
        nama_barang = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah stok: "))
        satuan = input("Masukkan satuan barang: ")

        data_baru = {
            "nama_barang": nama_barang,
            "jumlah": jumlah,
            "satuan": satuan
        }

        data.append(data_baru)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Data barang berhasil ditambahkan!")

    # Exit
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia!")