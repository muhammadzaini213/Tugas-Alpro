kalimat = input("Masukkan kalimat : ") 

huruf_dibalik = ""
kalimat_dibalik = ""
total_vokal = 0

for i in range (len(kalimat), 0, -1):
    huruf_dibalik = f"{huruf_dibalik}{kalimat[i-1]}"
    
    if(kalimat[i-1] == "a" or kalimat[i-1] == "i" or kalimat[i-1] == "u" or kalimat[i-1] == "e" or kalimat[i-1] == "o"):
        total_vokal += 1

kalimat_dipisah = kalimat.split(" ")

for i in range (len(kalimat_dipisah), 0, -1):
    kalimat_dibalik = f"{kalimat_dibalik} {kalimat_dipisah[i-1]}"

print("Kata dibalikkan:", huruf_dibalik)
print("Kalimat dibalik", kalimat_dibalik)
print("Jumlah huruf vokalnya: ", total_vokal)