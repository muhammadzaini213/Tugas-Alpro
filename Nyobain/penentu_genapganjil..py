print("--------------------------Mulai--------------------------\n")

x = int(input("Masukkan nilai bilangan x: "))

print("\n--------------------------Hasil--------------------------\n")

# Menggunakan if else untuk menentukan genap atau ganjil
if(x % 2 == 0): # Menggunakan modulus untuk mengecek apa bilangan habis dibagi 2
    print(f"{x} adalah bilangan genap")
else:
    print(f"{x} bukan bilangan genap")
    
print("\n--------------------------Selesai--------------------------")