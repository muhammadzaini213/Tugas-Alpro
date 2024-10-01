A = int(input("Batas awal bilangan prima : "))
B = int(input("Batas akhir bilangan prima : "))

total_prima = 0

if(A < 2):
    A += 1
    
for bilangan in range (A, B+1):
    n = 2
    prima = 1
    
    for n in range (2, bilangan):
        if(bilangan % n == 0):
            prima = 0
            break
        
    if(prima == 1):
        total_prima += 1
    
        
print(f"Diantara {A} dan {B} ada {total_prima} bilangan prima")