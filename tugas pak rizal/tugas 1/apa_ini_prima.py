bilangan = int(input("Masukkan bilangan yang mau diketahui prima atau tidak : "))

prima = 1
for n in range (2, bilangan):
    if(bilangan % n == 0):
        prima = 0
        break
    
if(prima == 1):
    print(f"{bilangan} adalah bilangan prima")
else:
    print(f"{bilangan} bukan bilangan prima")