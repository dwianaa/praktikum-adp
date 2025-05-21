print("--Kalkulator Matriks Sederhana--")
baris = int(input("Masukkan jumlah baris : "))
kolom = int(input("Masukkan jumlah kolom : "))

print("Masukkan elemen matriks A:")
A = []
for i in range(baris):
    barisA = []
    for j in range(kolom):
        elemen = int(input(f"A[{i}][{j}]: "))
        barisA.append(elemen)
    A.append(barisA)

print("Masukkan elemen matriks B:")
B = []
for i in range(baris):
    barisB = []
    for j in range(kolom):
        elemen = int(input(f"B[{i}][{j}]: "))
        barisB.append(elemen)
    B.append(barisB)

while True:
    print("\nPilihan Kalkulator Matriks:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Determinan")
    print("5. Invers")
    print("6. Transpose")
    print("0. END")
    pilihan = input("Pilih menu (0-6): ")
    
    if pilihan == "1":
        print("Hasil Penjumlahan Matriks A + B:")
        for i in range(baris):
            for j in range(kolom):
                print(A[i][j] + B[i][j], end=' ')
            print()

    elif pilihan == "2":
        print("Hasil Pengurangan Matriks A - B:")
        for i in range(baris):
            for j in range(kolom):
                print(A[i][j] - B[i][j], end=' ')
            print()

    elif pilihan == "3":
        if kolom != baris:
            print("Perkalian tidak bisa dilakukan! (jumlah kolom A = jumlah baris B)")
        else:
            print("Hasil Perkalian Matriks A * B:")
            hasil = []
            for i in range(baris):
                barishasil = []
                for j in range(kolom):
                    total = 0
                    for k in range(kolom):
                        total += A[i][k] * B[k][j]
                    barishasil.append(total)
                    print(total, end=' ')
                hasil.append(barishasil)
                print()

    elif pilihan == "4":
        if baris == 2 and kolom == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            print("Determinan Matriks A:", detA)
            print("Determinan Matriks B:", detB)
        else:
            print("Determinan hanya untuk matriks 2x2")

    elif pilihan == "5":
        if baris == 2 and kolom == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            if detA != 0:
                print("Invers Matriks A:")
                for i in range(2):
                    for j in range(2):
                        if i == j:
                            inv = A[1-i][1-j] / detA
                        else:
                            inv = -A[i][j] / detA
                        print(round(inv, 2), end=' ')
                    print()
            else:
                print("Matriks A tidak memiliki invers (karena determinan = 0)")

            if detB != 0:
                print("Invers Matriks B:")
                for i in range(2):
                    for j in range(2):
                        if i == j:
                            invers= B[1-i][1-j] / detB
                        else:
                            invers= -B[i][j] / detB
                        print(round(invers, 2), end=' ')
                    print()
            else:
                print("Matriks B tidak memiliki invers (karena determinan = 0)")
        else:
            print("Invers hanya didukung untuk matriks 2x2")

    elif pilihan == "6":
        print("Transpose Matriks A:")
        for j in range(kolom):
            for i in range(baris):
                print(A[i][j], end=' ')
            print()

        print("Transpose Matriks B:")
        for j in range(kolom):
            for i in range(baris):
                print(B[i][j], end=' ')
            print()
    elif pilihan == "0":
        break

    else:
        print("Pilihan tidak valid.")
        