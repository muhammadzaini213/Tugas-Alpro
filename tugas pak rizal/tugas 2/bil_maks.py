jumlah = int(input("Masukkan jumlah: "))
angka = []
maks = 0

for i in range (0, jumlah):
  angka.append(int(input(f"Masukkan angka ke {i+1}")))

for j in range (0, jumlah):
  if(angka[j] > maks):
    maks = angka[j]

print(maks)
