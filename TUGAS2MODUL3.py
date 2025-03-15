print("--------TEBAK ANGKA BOM--------")
print("\nPemain 1 - Menentukan angka BOM")
n = int(input("Pilih angka positif sampai berapa : "))
k = int(input("Angka BOM: "))

print("\nDeretan angka:")
for i in range (1, n + 1):
    if i%k == 0:
        print("BOM",end= " ")
    else:
        print(i,end= " ")

print("\n\nPemain 2 - Menebak angka BOM")
while True:
    tebak = int(input(f"Tebak angka dari 1 - {n} : "))
    if tebak<1 or tebak>n:
        print("Tebakan di luar batas, COBA LAGI!")
        continue
    elif tebak%k == 0:
        print("Angka", tebak , "adalah BOM, ANDA KALAH!")
        break
    else:
        print("Angka", tebak,"bukan BOM, ANDA MENANG!")
        break
print("\nPERMAINAN SELESAI")