bilangan = int(input("Masukkan bilangan yang mau diketahui prima atau tidak : "))

prima = True
for n in range (2, bilangan):
    if(bilangan % n == 0):
        prima = False
        break
    
if(prima == True):
    print(f"{bilangan} adalah bilangan prima")
else:
    print(f"{bilangan} bukan bilangan prima")