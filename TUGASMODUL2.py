print("PEMBELIAN TIKET PESAWAT")
print("-----------------------------")
nama = input("Nama :")
umur = int(input("Umur :"))
jk = input("Jenis Kelamin (P/L) :")
print("-----------------------------")

print("\nPilihan Kode Maskapai:")
print("3012 - Padang-Jakarta")
print("4015 - Padang-Batam")
print("4050 - Padang-Bandung")
kode = input("Kode Maskapai (3012/4015/4050): ")
if kode == "3012":
    tujuan = "Padang-Jakarta"
    ekonomi, bisnis, first = 800000, 850000, 900000
    print(f"Tujuan :",tujuan)
elif kode == "4015":
    tujuan = "Padang-Batam"
    ekonomi, bisnis, first = 500000, 550000, 700000
    print(f"Tujuan :",tujuan)
elif kode == "4050":
    tujuan = "Padang-Bandung"
    ekonomi, bisnis, first = 700000, 750000, 850000
    print(f"Tujuan :",tujuan)
else:
    print("Kode tidak valid")

print("\nPilih Kelas Penerbangan:")
print("1. Ekonomi")
print("2. Bisnis")
print("3. First Class")
pilih_kelas = input("Pilihan Kelas (1/2/3): ")
if pilih_kelas == "1":
    kelas = "Ekonomi"
    harga = ekonomi
    print(f"Kelas:",kelas)
elif pilih_kelas == "2":
    kelas = "Bisnis"
    harga = bisnis
    print(f"Kelas:",kelas)
elif pilih_kelas == "3":
    kelas = "First Class"
    harga = first
    print(f"Kelas:",kelas)
else:
    print("Pilihan kelas tidak valid")

jumlah = int(input("\nJumlah tiket : "))
if jumlah > 3:
    totalharga = harga * jumlah
    diskon = totalharga * 0.2
    total = int(totalharga - diskon)
    print(f"Total Harga: Rp",total)
else:
    total = int(harga * jumlah)
    print(f"Total Harga: Rp",total)

print("\n========== STRUK PEMESANAN ===========")
print(f"Nama            :",nama)
print(f"Umur            :",umur)
print(f"Jenis Kelamin   :",jk)
print("-------------------------------------")
print(f"Kode Maskapai   :",kode,(tujuan))
print(f"Jenis Maskapai  :",kelas)
print(f"Jumlah Tiket    :",jumlah)
print(f"Total Harga     : Rp",total)
print("============ SAFE FLIGHT! =============")
