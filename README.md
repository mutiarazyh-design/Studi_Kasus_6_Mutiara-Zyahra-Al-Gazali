Nama: Mutiara Zyahra Al Gazali

NIM: 2609116026

Penjelasan Kode Program:

<img width="1920" height="447" alt="KODE PROGRAM 1" src="https://github.com/user-attachments/assets/7f2ed31a-1dd3-45cb-add2-fe8904816c90" />


import json → Kode ini mengimpor library JSON untuk membaca serta menyimpan data dalam file berformat JSON.

with open("data.json", "r", encoding="utf-8") as f: → Kode ini membuka file data.json dalam mode baca (r) agar data dapat diakses oleh program.

data = json.load(f) → Kode ini membaca data dari file JSON kemudian menyimpannya ke dalam variabel data.

while True: → Kode ini menjalankan program secara terus-menerus sehingga menu dapat ditampilkan berulang kali sampai pengguna memilih pilihan untuk keluar.


<img width="753" height="224" alt="KODE PROGRAM 2" src="https://github.com/user-attachments/assets/31313f9d-daa4-439d-b361-3e4f44893756" />


if pilihan == "1": digunakan untuk menjalankan proses menu 1, yaitu menu Lihat Data Barang, ketika pengguna memilih angka 1.

print("\n=== DATA INVENTARIS BARANG ===") digunakan untuk menampilkan judul bagian data inventaris pada layar.

for barang in data: digunakan untuk melakukan perulangan terhadap setiap data barang yang tersimpan dalam variabel data.

barang["nama_barang"] digunakan untuk mengambil informasi nama barang dari setiap dictionary.

barang["jumlah"] digunakan untuk mengambil informasi jumlah stok yang dimiliki setiap barang.

barang["satuan"] digunakan untuk menampilkan satuan barang, seperti kg, liter, atau pcs.

print("-----------------------------") digunakan untuk memberikan garis pemisah sehingga tampilan data barang menjadi lebih teratur dan mudah dibaca.


<img width="643" height="456" alt="KODE PROGRAM 3" src="https://github.com/user-attachments/assets/1a44eb9c-35ab-492a-aa63-cd829dada2a8" />


data_baru = { ... } digunakan untuk membentuk dictionary baru yang menyimpan informasi berupa nama barang, jumlah, dan satuan.

data.append(data_baru) digunakan untuk memasukkan data barang baru ke dalam list data.

with open("data.json", "w", encoding="utf-8") as f: digunakan untuk membuka file data.json dalam mode tulis (w) agar perubahan data dapat disimpan.

json.dump(data, f, indent=4) digunakan untuk menyimpan seluruh data ke file JSON. Parameter indent=4 digunakan untuk membuat format data JSON lebih terstruktur dan mudah dibaca.

print("Data barang berhasil ditambahkan!") digunakan untuk menampilkan pemberitahuan kepada pengguna bahwa data barang telah berhasil ditambahkan dan disimpan.


<img width="477" height="178" alt="KODE PROGRAM 4" src="https://github.com/user-attachments/assets/c916abc0-284e-44da-a40a-7448aa29db08" />


elif pilihan == "3": digunakan untuk menjalankan menu 3, yaitu menu Keluar, ketika pengguna memilih angka 3.

print("Program selesai.") digunakan untuk memberikan informasi kepada pengguna bahwa program telah selesai dijalankan.

break digunakan untuk menghentikan perulangan while True, sehingga program tidak lagi menampilkan menu dan proses program berakhir.

else: digunakan untuk menangani input yang tidak sesuai dengan pilihan menu 1, 2, atau 3.

print("Pilihan tidak tersedia!") digunakan untuk memberikan peringatan kepada pengguna bahwa pilihan yang dimasukkan tidak terdapat dalam menu.


Data Json:


<img width="466" height="403" alt="DATA JSON 1" src="https://github.com/user-attachments/assets/8a8f8003-c86b-44a4-a24a-eb9b20f17f23" />


<img width="1920" height="1011" alt="DATA JSON 2" src="https://github.com/user-attachments/assets/233b7e9e-0a27-4c8e-a422-627319355950" />


Gambar pertama menunjukkan data awal, sedangkan gambar kedua menunjukkan data setelah pengguna menambahkan barang baru. Hal ini membuktikan bahwa data baru berhasil ditambahkan dan disimpan secara permanen di file data.json.


Output:

<img width="1920" height="1011" alt="Screenshot 2026-10-08 192244" src="https://github.com/user-attachments/assets/406b353c-7b86-4ee9-8931-180c32b4cbda" />

<img width="1920" height="1011" alt="Screenshot 2026-10-08 192258" src="https://github.com/user-attachments/assets/26114941-77bd-43f5-bcea-ea3025b65f43" />

<img width="1920" height="1011" alt="Screenshot 2026-10-08 192311" src="https://github.com/user-attachments/assets/a3de955f-c7c0-4dfc-9209-470a673d4675" />
