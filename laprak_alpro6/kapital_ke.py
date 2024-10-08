def kapital_ke(teks, ke):
    list_kapital = []
    for i in teks:
        if(teks.isupper()):
            list_kapital.append(i)

    if(ke > len(list_kapital)):
        print("Tidak ditemukan huruf kapital ke", ke)
    else:
        print(list_kapital[ke-1])

kapital_ke(input("Masukkan teks: "), int(input("Cari kapital ke: ")))