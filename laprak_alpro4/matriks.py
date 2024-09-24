print("Selamat datang di program matriks, silahkan masukkan bagian matriks mana yang ingin anda ubah")

list_matriks = [[0,2,3], [0,0,0], [0,0,0]]

baris1 =""
baris2 = ""
baris3 = ""


for i in range (0,3):
        baris1 = f"{baris1}{list_matriks[0]}"

for i in range (0,3):
        baris2 = f"{baris2}{list_matriks[1][i]} "

for i in range (0,3):
        baris3 = f"{baris3}{list_matriks[2][i]} "

print (f"Matriks disimpan: \n{baris1}\n{baris2}\n{baris3}")



print("Apakah anda ingin mengedit matriks?")

option_menu = int(input("1. Edit\n2. Keluar\n>> "))

if(option_menu == 1):
    input_baris = int(input("Edit baris ke: ")) -1
    input_kolom = int(input("Edit kolom ke: ")) -1

    if(input_baris <= 0 or input_baris >= 2 or input_kolom <= 0 or input_kolom >= 2):
        input_edit = int(input(f"Ganti baris ke {input_baris} dan kolom ke {input_kolom} dengan : "))
    else:
        print(("Anda memasukkan angka diluar batas matriks 3x3!"))

    
elif(option_menu == 2):
    print("Terimakasih sudah menggunakan aplikasi matriks!")