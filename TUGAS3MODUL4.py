print("----------PEMESANAN TIKET BIOSKOP----------")
print()

while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if r >= 4 and c >= 4:
        break
    else:
        print("Melebihi ukuran minimal, silakan masukkan ulang!")

kursi = [[str(i * c + j + 1) for j in range (c)] for i in range (r)]
print("\nLayout Kursi Bioskop:")
for i in range (r):
    for j in range (c):
        print(f"{kursi [i][j]:<4}", end=" ") 
    print()

while True:
    pilih = int(input("\nMasukkan nomor kursi (atau 0 untuk selesai): "))
    if pilih == 0:
        print("Terima kasih telah memesan tiket, Selamat menonton!")
        break
    elif pilih < 1 or pilih > r * c:
        print("Nomor kursi tidak tersedia! Masukkan nomor kursi yang tersedia")
        continue

    baris = (pilih - 1) // c
    kolom = (pilih - 1) % c
    if kursi[baris][kolom] == "X":
        print(f"Kursi {pilih} sudah dipesan! Pilih kursi lain")
    else:
        kursi[baris][kolom] = "X"
        print(f"Kursi {pilih} berhasil dipesan!")

    print("\nLayout Kursi Bioskop:")
    for i in range (r):
        for j in range (c):
            print(f"{kursi [i][j]:<4}", end=" ") 
        print()