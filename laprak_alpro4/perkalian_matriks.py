print("Buat matriks pertama: ")
baris1 = int(input("Masukkan jumlah baris: "))
kolom1 = int(input("Masukkan jumlah kolom: "))
matriks1 = []
for i in range(baris1):
    baris_matriks = []
    for j in range(kolom1):
        nilai = int(input(f"Masukkan nilai untuk elemen ({i + 1}, {j + 1}): "))
        baris_matriks.append(nilai)
    matriks1.append(baris_matriks)

print("Matriks pertama yang telah dibuat:")
for baris in matriks1:
    print(baris)

print("Buat matriks kedua: ")
baris2 = int(input("Masukkan jumlah baris: "))
kolom2 = int(input("Masukkan jumlah kolom: "))
matriks2 = []
for i in range(baris2):
    baris_matriks = []
    for j in range(kolom2):
        nilai = int(input(f"Masukkan nilai untuk elemen ({i + 1}, {j + 1}): "))
        baris_matriks.append(nilai)
    matriks2.append(baris_matriks)

print("Matriks kedua yang telah dibuat:")
for baris in matriks2:
    print(baris)

if kolom1 != baris2:
    print("Perkalian matriks tidak dapat dilakukan. Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
else:
    hasil = [[0 for _ in range(kolom2)] for _ in range(baris1)]
    
    for i in range(baris1):
        for j in range(kolom2):
            for k in range(kolom1):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]

    print("Hasil perkalian matriks:")
    for baris in hasil:
        print(baris)
