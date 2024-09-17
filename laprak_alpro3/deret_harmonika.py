jumlah_deret = int(input("Masukkan jumlah deret: "))
penjabaran = ""
total = 0

for i in range(1, jumlah_deret+1):
    total += i
    if(i == jumlah_deret):
        penjabaran = f"{penjabaran}{i}"
        break
    penjabaran = f"{penjabaran}{i} + "
    
print(penjabaran, total)