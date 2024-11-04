def fixFormat(path):
    dataMahasiswa = open(path, "r")
    data = dataMahasiswa.read()

    with open (path, 'w') as file:
        file.write(data.replace("'", ""))    

def lining(file):
    return file.read().split("\n")

def splitColumn(string):
    return string.split("\t")

def listMatkul(line):
    listMatkul = line[0]
    listMatkul = listMatkul.replace("\t\t", "\t")
    listMatkul = listMatkul.split("\t")
    listMatkul = listMatkul[:-1]
    return listMatkul

def sorting(listSesi):
    listSesiSorted = []
    hari_order = ["Senin", "Selasa","Rabu","Kamis","Jumat"]
    sesi_order = ["1", "2", "3", "4"]
    for i in range (0, len(hari_order)):
        for j in range (0, len(sesi_order)):
            for k in range(0, len(listSesi)):
                if(listSesi[k].startswith(f"{hari_order[i]}, Sesi {sesi_order[j]}") or listSesi[k].startswith(f"{hari_order[i]} Sesi {sesi_order[j]}")):
                    listSesiSorted.append(listSesi[k])

    return listSesiSorted

def menuAwal(pil, listJadwal):
    if(pil == "1"):
        jadwalNIM(listJadwal)
        print("1. Jadwal\n2. Edit Jadwal\n3. Cek List")
        menuAwal(input(""), listJadwal)
    else:
        print("1. Jadwal\n2. Edit Jadwal\n3. Cek List")
        menuAwal(input(""), listJadwal)

path = "mahasiswa/data_if.txt"
fixFormat(path)

def jadwalNIM(listJadwal):
    find = input("Cari NIM/Nama?")
    found = False
    for i in range (0, len(listJadwal), 2):
        if (find.lower() in listJadwal[i].lower()):
            print(f"{listJadwal[i]}")
            for j in range (0, len(listJadwal[i+1])):
                if(listJadwal[i+1][j]):
                    print(listJadwal[i+1][j])
                    found = True
    if(found == False):
        print("Tidak ditemukan.")
    

def jadwalKosong(listJadwal): 
    listJadwalKosong = []
    for kolom in range(1, len(listJadwal),2):
        order = ["Senin, Sesi 1",
        "Senin, Sesi 2",
        "Senin, Sesi 3",
        "Senin, Sesi 4",
        "Selasa, Sesi 1",
        "Selasa, Sesi 2",
        "Selasa, Sesi 3",
        "Selasa, Sesi 4",
        "Rabu, Sesi 1",
        "Rabu, Sesi 2",
        "Rabu, Sesi 3",
        "Rabu, Sesi 4",
        "Kamis, Sesi 1",
        "Kamis, Sesi 2",
        "Kamis, Sesi 3",
        "Kamis, Sesi 4",
        "Jumat, Sesi 1",
        "Jumat, Sesi 2",
        "Jumat, Sesi 3",
        "Jumat, Sesi 4",]
        for i in listJadwal[kolom]:
            for j in order:
                if j in i:
                    order.remove(j)
        listJadwalKosong.append(listJadwal[kolom-1])
        listJadwalKosong.append(order)

    # print(listJadwalKosong)
    jadwalKosongSesi(listJadwalKosong)

def jadwalKosongNIM(jadwalKosong):
    find = input("Cari NIM/Nama?")
    found = False
    for i in range (0, len(jadwalKosong), 2):
        if (find.lower() in jadwalKosong[i].lower()):
            print(f"{jadwalKosong[i]}")
            for j in range (0, len(jadwalKosong[i+1])):
                if(jadwalKosong[i+1][j]):
                    print(jadwalKosong[i+1][j])
                    found = True
    if(found == False):
        print("Tidak ditemukan.")


def jadwalKosongBersama(jadwalKosong):
    order = ["Senin, Sesi 1",
        "Senin, Sesi 2",
        "Senin, Sesi 3",
        "Senin, Sesi 4",
        "Selasa, Sesi 1",
        "Selasa, Sesi 2",
        "Selasa, Sesi 3",
        "Selasa, Sesi 4",
        "Rabu, Sesi 1",
        "Rabu, Sesi 2",
        "Rabu, Sesi 3",
        "Rabu, Sesi 4",
        "Kamis, Sesi 1",
        "Kamis, Sesi 2",
        "Kamis, Sesi 3",
        "Kamis, Sesi 4",
        "Jumat, Sesi 1",
        "Jumat, Sesi 2",
        "Jumat, Sesi 3",
        "Jumat, Sesi 4",]
    count = []
    for i in range(0,20):
        count.append(0)

    for i in range(0, len(order)):
        for j in range(1, len(jadwalKosong),2):
            for k in jadwalKosong[j]:
                # print(jadwalKosong[j])
                if(order[i] in k):
                    count[i] = count[i] + 1

    for list in range(0,20):
        print(f"{order[list]}: {count[list]} mahasiswa kosong")
    
def jadwalKosongSesi(jadwalKosong):
    order = ["Senin, Sesi 1",
        "Senin, Sesi 2",
        "Senin, Sesi 3",
        "Senin, Sesi 4",
        "Selasa, Sesi 1",
        "Selasa, Sesi 2",
        "Selasa, Sesi 3",
        "Selasa, Sesi 4",
        "Rabu, Sesi 1",
        "Rabu, Sesi 2",
        "Rabu, Sesi 3",
        "Rabu, Sesi 4",
        "Kamis, Sesi 1",
        "Kamis, Sesi 2",
        "Kamis, Sesi 3",
        "Kamis, Sesi 4",
        "Jumat, Sesi 1",
        "Jumat, Sesi 2",
        "Jumat, Sesi 3",
        "Jumat, Sesi 4",]
    for i in range(1, len(jadwalKosong), 2):
        if(order[2] in jadwalKosong[i]):
            print(jadwalKosong[i-1])

with open(path, 'r') as file:
    line = lining(file)
    matkul = listMatkul(line)

    listJadwal = []
    for mahasiswa in range (1, len(line)):
        column = splitColumn(line[mahasiswa])
        nim = column[0]
        nama = column[1]
        
        matkulDanKelas = []
        listSesi = []

        for sesi in range(3, len(column), 2):
            listSesi.append(column[sesi])

        for mataKuliah in range (0, len(listSesi)):
            listSesi[mataKuliah] = f"{listSesi[mataKuliah]} {matkul[mataKuliah][:-10]}"

        listKelas = []

        for kelas in range (2, len(column), 2):
            listKelas.append(column[kelas])
        
        
        for matkulKelas in range (0, len(listSesi)):
            matkulDanKelas.append(f"{listSesi[matkulKelas]}{listKelas[matkulKelas]}")

        matkulDanKelas = sorting(matkulDanKelas)
        listJadwal.append(f"{nama} - {nim}")
        listJadwal.append(matkulDanKelas)

    # print("1. Jadwal\n2. Edit Jadwal\n3. Cek List")
    # menuAwal(input(""), listJadwal)
    jadwalKosong(listJadwal)
    # for i in range (0, len(listJadwal), 2):
    #     print(listJadwal[i])
    #     for j in range (0, len(listJadwal[i+1])):
    #         print(listJadwal[i+1][j])
    #     print("\n")



    


        



        
        