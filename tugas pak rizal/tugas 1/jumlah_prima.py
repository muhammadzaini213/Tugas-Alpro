batas_awal = int(input("Batas awal bilangan prima : "))
batas_akhir = int(input("Batas akhir bilangan prima : "))

total_prima = 0

if(batas_awal < 2):
    batas_awal = 2
    
for bilangan in range (batas_awal, batas_akhir+1):
    n = 2
    prima = True
    
    for n in range (2, bilangan):
        if(bilangan % n == 0):
            prima = False
            break
        
    if(prima == True):
        total_prima += 1
    
        
print(f"Diantara {batas_awal} dan {batas_akhir} ada {total_prima} bilangan prima")