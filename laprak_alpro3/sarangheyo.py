x = int(input("Masukkan nilai: "))

xxx = "x"
underscore = "-"
dot = ". "

for i in range(x, 0 , -1):
    print(xxx*i)
    
print("\n")

for i in range(x, 0, -1):
    if(i % 2 == 0):
        print(underscore*i)
    else:
        print(xxx*i)
        
        
print("\n")

angka_dari_kecil = ""
angka_dari_besar = ""
for i in range(1, x+1):
    angka_dari_kecil = f"{angka_dari_kecil}{i}"
    print(angka_dari_kecil)
    
    if(i != x):
      angka_dari_besar = f"{angka_dari_kecil}\n{angka_dari_besar}"
    else:
        print(angka_dari_besar)

print("\n")

for i in range(1, x+1):
    print(xxx*i)
    if(i == x):
        break
    
for i in range(x-1,0,-1):
    print(xxx*i)
    if(i == x):
        break
    
print("\n")

for i in range(x, 0 ,-1):
    print(f"{dot*(i-1)}{i}")