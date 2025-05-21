def datamahasiswa():
    n = int(input("Masukkan jumlah mahasiswa: "))
    data = []
    for i in range(n):
        print("Masukkan data Mahasiswa :", i + 1)
        nama = input("Nama: ")
        nim = input("NIM: ")
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        data.append([nama, nim, uts, uas, tugas, 0, 0])  
    return data

def nilaiakhir(data):
    for i in range(len(data)):
        uts = data[i][2]
        uas = data[i][3]
        tugas = data[i][4]
        nilai_akhir = 0.35 * uas + 0.35 * uts + 0.30 * tugas
        data[i][5] = round(nilai_akhir, 2)
    return data

def rata2(data, index):
    total = 0
    for i in range(len(data)):
        total += data[i][index]
    return round(total / len(data), 2)

def peringkat(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][5] < data[j][5]:
                data[i], data[j] = data[j], data[i]

    for i in range(len(data)):
        data[i][6] = i + 1  
    return data

def garis():
    print("-" * 88)

def tabel(data):
    garis()
    print("| {:<15} | {:<10} | {:>6} | {:>6} | {:>8} | {:>12} | {:>9} |".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Peringkat"))
    garis()

    for m in data:
        print("| {:<15} | {:<10} | {:>6.1f} | {:>6.1f} | {:>8.1f} | {:>12.2f} | {:>9} |".format(
            m[0], m[1], m[2], m[3], m[4], m[5], m[6]))
    garis()

    print("| {:<15} | {:<10} | {:>6.1f} | {:>6.1f} | {:>8.1f} | {:>12.2f} | {:>9} |".format(
        "Rata-rata", "",
        rata2(data, 2),
        rata2(data, 3),
        rata2(data, 4),
        rata2(data, 5),""))
    garis()


mahasiswa = datamahasiswa()
mahasiswa = nilaiakhir(mahasiswa)
mahasiswa = peringkat(mahasiswa)
tabel(mahasiswa)