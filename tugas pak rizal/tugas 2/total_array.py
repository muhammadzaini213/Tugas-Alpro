jumlah = int(input("Masukkan jumlah: "))
angka = []
total = 0

for i in range(0, jumlah):
  angka.append(int(input(f"Masukkan angka ke {i+1} ")))

for j in range(0, jumlah):
  total = total + angka[j]

print(total)
