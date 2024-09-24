list = dict()

for i in range (1,4):
    buah = input("Buah yang mau dijual: ")
    if(buah == "stop"):
        break

    harga = input("Harga jual buah ini: ")
    if(harga == "stop"):
        break

    print()
    list[harga] = buah
for harga_list, buah_list in list.items():
    print(f"{buah_list} harganya {harga_list}")

print()
