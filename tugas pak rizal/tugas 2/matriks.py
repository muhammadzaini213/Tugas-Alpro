baris_matriks1 = int(input("Berapa jumlah baris matriks1: "))
kolom_matriks1 = int(input("Berapa jumlah kolom matriks1: "))

matriks1 = []
matriks2 = []

hasil = []

for i in range (0, kolom_matriks1):
  matriks1.append([])
  for j in range (0, baris_matriks1):
    matriks1[i].append(int(input(f"Masukkan nilai untuk matriks [{i+1}, {j+1}]: ")))

baris_matriks2 = int(input("Berapa jumlah baris matriks2: "))
kolom_matriks2 = int(input("Berapa jumlah kolom matriks2: "))


for i in range (0, kolom_matriks2):
  matriks2.append([])
  for j in range (0, baris_matriks2):
    matriks2[i].append(int(input(f"Masukkan nilai untuk [{i+1}, {j+1}]: ")))


for i in range (0, kolom_matriks2):
  hasil.append([])
  for j in range(0, baris_matriks2):
    x = 0
    for k in range(0, kolom_matriks1):
      x = x + matriks1[i][k] * matriks2[k][j]
    hasil[i].append(x) 


print(hasil)
