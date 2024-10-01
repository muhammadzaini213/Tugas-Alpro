import random

print("----------------------------Gen Z jokes generator----------------------------")

while True:
    x = int(input("Apakah anda ingin membuat nama random?\n1. Ya\n2. Tidak\n>> "))
    
    if(x == 1):
        list_nama = "Farhan,Aji,Zidan,Joko,Reza"

        list_benda_random = "Kecap,Kebab,Pisang,Kalimantan,Arduino"

        nama = list_nama.split(",")
        benda = list_benda_random.split(",")

        output = f"{nama[random.randint(0, len(nama) -1 )]} {benda[random.randint(0, len(benda) -1)]}"
        print("Nama randommu:", output, "\n")
    else:
        print("Yaudah bye")
        break