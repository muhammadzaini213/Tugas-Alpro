import random

menu_awal = int(input("Apakah kamu ingin melihat buah keberuntunganmu?\n1. Lihat\n2. Keluar\n>> "))

list_gacha = ["apel", "mangga", "jeruk", "alpukat", "nanas", "bakwan", "semangka", "lemon", "melon"]
print(list_gacha)

list_buah = input("Hilangkan salah satu buah yang tidak anda suka: ")
list_gacha.remove(list_buah)
print(list_gacha, f"{list_buah} <--> telah dihilangkan dari list")

list_buah = input("Tambahkan salah satu buah yang anda suka: ")
list_gacha.append(list_buah)
print(list_gacha, f"{list_buah} <--> telah ditambahkan ke list")

if(menu_awal == 1):
    hasil_gacha = f"\nSelamat anda mendapatkan {list_gacha[random.randint(0,8)]}!\n"
    print(hasil_gacha)
        
elif(menu_awal == 2):
    print("Sampai jumpa lagi nanti!")
else:
    print("Error! Silahkan jalankan program lagi")
