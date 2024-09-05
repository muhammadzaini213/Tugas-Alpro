print("--------------------------Mulai--------------------------\n")

A = int(input("Masukkan bilangan bulat A: "))

B = int(input("Masukkan bilangan bulat B: "))

C = int(0)

print("\n--------------------------Hasil--------------------------\n")

print("Nilai awal semua variabel: ")
print(f"A = {A} \nB = {B} \nC = {C} \n")

# Memasukkan bilangan A ke C
C = A 
print("Memasukkan nilai A ke C")
print(f"A = {A} \nB = {B} \nC = {C} \n")

# Memasukkan nilai B ke A
A = B
print("Memasukkan nilai B ke A")
print(f"A = {A} \nB = {B} \nC = {C} \n")

# Memasukkan nilai C ke B
B = C
print("Memasukkan nilai C ke B")
print(f"A = {A} \nB = {B} \nC = {C} \n")

print("--------------------------Selesai--------------------------")