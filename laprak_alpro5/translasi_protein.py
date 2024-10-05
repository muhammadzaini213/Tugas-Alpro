rna = input("Masukkan RNA: ") # Input awal untuk program
length = len(rna) # variabel ini nyimpan panjang dari input yang kita masukkan


# Mengi
kodon = []
protein = []

tampilkan = True

if(length % 3 != 0):
    print("RNA tidak dapat diterjemahkan!")
else:
    for i in range(0, int(length/3)):
        kodon.append(rna[i*3 : (i*3 +3)])

    for j in range(0, len(kodon)):
        if(kodon[j] == "AUG"):
            protein.append("Methionime")
        elif(kodon[j] == "UUU" or kodon[j] == "UUC"):
            protein.append("Phenylalanine")
        elif(kodon[j] == "UUA" or kodon[j] == "UUG"):
            protein.append("Leucine")
        elif(kodon[j] == "UCU" or kodon[j] == "UCC" or kodon[j] == "UCA" or kodon[j] == "UCG"):
            protein.append("Serine")
        elif(kodon[j] == "UAU" or kodon[j] == "UAC"):
            protein.append("Tyrosine")
        elif(kodon[j] == "UGU" or kodon[j] == "UGC"):
            protein.append("Cysteine")
        elif(kodon[j] == "UGG"):
            protein.append("Tryptophan")
        elif(kodon[j] == "UAA" or kodon[j] == "UAG" or kodon[j] == "UGA"):
            print(f"Kodon '{kodon[j]}' ditemukan, program dihentikan.")
            tampilkan = False
            break
        else:
            print(f"Kodon '{kodon[j]}' tidak dapat diterjemahkan")
            tampilkan = False
            break
    if(tampilkan):
        print("Hasil terjemahan:",protein)