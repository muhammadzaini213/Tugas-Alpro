jumlah_deret = int(input("Masukkan jumlah deret: "))
penjabaran = ""
total = 0

for i in range(1, jumlah_deret+1):
    total += 1/i
    if(i == jumlah_deret):
        penjabaran = f"{penjabaran}1/{i}"
        break
    elif(i == 1):
        penjabaran = f"{penjabaran}1 + "
        continue
    penjabaran = f"{penjabaran}1/{i} + "
    
print(f"{penjabaran} = {total}")