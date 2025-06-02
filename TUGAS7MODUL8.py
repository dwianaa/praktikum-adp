def data_awal():
    data_buku = [
        "9781111111111,Python Dasar Pemograman,Aisyah,10,50000,75000",
        "9782222222222,Calculus,Bima,3,60000,95000",
        "9783333333333,AI untuk Pemula,Celsi,15,70000,100000",
        "9784444444444,Data Science,Dwi,8,55000,85000",
        "9785555555555,Algoritma dan Pemograman,Fadil,2,45000,70000",
        "9786666666666,Geometri Analitik,Kevin,20,40000,60000",
        "9787777777777,Jaringan Komputer,Hadi,5,65000,90000",
        "9788888888888,Aljabar Linear Elementer,Jenny,7,60000,80000",
        "9789999999999,Discrete Mathematics,Sandy,4,58000,85000",
        "9780000000001,Web Programming,Vania,6,55000,80000"
    ]
    with open("inventaris_buku.txt", "w") as file:
        for baris in data_buku:
            file.write(baris + "\n")

def baca_simpan():
    buku_list = []
    with open("inventaris_buku.txt", "r") as file:
        for baris in file:
            isbn, judul, penulis, stok, harga_beli, harga_jual = baris.strip().split(",")
            buku = {
                "ISBN": isbn,
                "Judul": judul,
                "Penulis": penulis,
                "Stok": int(stok),
                "Harga Beli": int(harga_beli),
                "Harga Jual": int(harga_jual)
            }
            buku_list.append(buku)
    return buku_list

def hitung_potensi(buku_list):
    for buku in buku_list:
        buku["Potensi Keuntungan"] = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
    with open("laporan_inventaris.txt", "w") as file:
        for buku in buku_list:
            file.write(f'{buku["ISBN"]},{buku["Judul"]},{buku["Penulis"]},{buku["Stok"]},'
                       f'{buku["Harga Beli"]},{buku["Harga Jual"]},{buku["Potensi Keuntungan"]}\n')

def analisis(buku_list):
    max_buku = buku_list[0]
    min_buku = buku_list[0]
    total_nilai = 0
    kurang_dari_5 = []

    for buku in buku_list:
        if buku["Potensi Keuntungan"] > max_buku["Potensi Keuntungan"]:
            max_buku = buku
        if buku["Potensi Keuntungan"] < min_buku["Potensi Keuntungan"]:
            min_buku = buku
        total_nilai += buku["Stok"] * buku["Harga Beli"]
        if buku["Stok"] < 5:
            kurang_dari_5.append(buku)

    print("Buku dengan potensi keuntungan TERTINGGI:", max_buku["Judul"], "-", max_buku["Potensi Keuntungan"])
    print("Buku dengan potensi keuntungan TERENDAH:", min_buku["Judul"], "-", min_buku["Potensi Keuntungan"])
    print("Total Nilai Inventaris (berdasarkan Harga Beli): Rp", total_nilai)
    print("\nBuku yang stoknya kurang dari 5:")
    for buku in kurang_dari_5:
        print("-", buku["Judul"], "(Stok:", buku["Stok"], ")")

data_awal()
data = baca_simpan()
hitung_potensi(data)
analisis(data)