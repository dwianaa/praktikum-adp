jml = int(input("Masukkan Jumlah Mahasiswa Pratikum ADP : "))
data = []

for i in range(jml):
    print("\nData Mahasiswa ke ", i+1)
    nama = input("Nama               : ")
    pretest = float(input("Nilai Pretest      : "))
    posttest = float(input("Nilai Posttest     : "))
    makalah = float(input("Nilai Makalah      : "))

    akhir = (pretest * 40 + posttest * 40 + makalah * 20) // 100  # hasilnya bulat (int)
    data.append([nama, akhir])

print("\n|-------------------------------------|")
print("|        TABEL NILAI MAHASISWA        |")
print("|----------------------|--------------|")
print("| Nama Mahasiswa       | Nilai Akhir  |")
print("|----------------------|--------------|")
for m in data:
    print(f"| {m[0]:<20} | {m[1]:>12} |")
print("|----------------------|--------------|")

total = 0
for n in data:
    total += n[1]
rata= total / jml
print("\nRata-rata nilai akhir kelas:", rata)

maks = data[0][1]
min = data[0][1]
for n in data:
    if n[1] > maks:
        maks = n[1]
    if n[1] < min:
        min = n[1]

print("\n Mahasiswa dengan nilai tertinggi:")
for n in data:
    if n[1] == maks:
        print(n[0], "(", n[1], ")")

print("\n Mahasiswa dengan nilai terendah:")
for n in data:
    if n[1] == min:
        print(n[0], "(", n[1], ")")

print("\n Mahasiswa yang nilainya di atas rata-rata kelas:")
for n in data:
    if n[1] > rata:
        print(n[0], "(", n[1], ")")