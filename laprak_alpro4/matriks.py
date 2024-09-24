
baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))
matriks = []
for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            nilai = int(input(f"Masukkan nilai untuk elemen ({i + 1}, {j + 1}): "))
            baris_matriks.append(nilai)
        matriks.append(baris_matriks)

print("Matriks yang telah dibuat:")
for baris in matriks:
    print(baris)