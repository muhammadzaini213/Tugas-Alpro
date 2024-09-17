jumlah_fibonacci = int(input("Masukkan jumlah bilangan fibonacci: "))

bilangan_awal = 1
bilangan_akhir = 1
kontainer_bilangan = 0
string_output = "1,1,"

for i in range(1, jumlah_fibonacci+1):
    kontainer_bilangan = bilangan_awal + bilangan_akhir
    if(i == jumlah_fibonacci):
     string_output = f"{string_output}{kontainer_bilangan}"
    else:
     string_output = f"{string_output}{kontainer_bilangan},"
    bilangan_awal = bilangan_akhir
    bilangan_akhir = kontainer_bilangan
    
print(string_output)