kodon = input("Masukkan Kodon yang ingin diterjemahkan: ")

pengantar_hasil = "Nama protein tersebut adalah"
teks_hijau = ":\033[32m"
if(kodon == "AUG"):
 print(pengantar_hasil, teks_hijau, "Methionime")
elif(kodon == "UUU" or kodon == "UUC"):
 print(pengantar_hasil, teks_hijau, "Phenylalanine")
elif(kodon == "UUA" or kodon == "UUG"):
 print(pengantar_hasil, teks_hijau, "Leucine")
elif(kodon == "UCU" or kodon == "UCC" or kodon == "UCA" or kodon == "UCG"):
 print(pengantar_hasil, teks_hijau, "Serine")
elif(kodon == "UAU" or kodon == "UAC"):
 print(pengantar_hasil, teks_hijau, "Tyrosine")
elif(kodon == "UGU" or kodon == "UGC"):
 print(pengantar_hasil, teks_hijau, "Cysteine")
elif(kodon == "UGG"):
 print(pengantar_hasil, teks_hijau, "Tryptophon")
else:
 print("\033[31mTidak dapat menerjemahkan Kodon yang anda masukkan.")

