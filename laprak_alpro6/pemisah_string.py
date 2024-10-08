def pemisah_string(teks):
    output = []

    output.append(detektor_alphabet(teks))
    output.append(detektor_angka(teks))
    output.append(detektor_simbol(teks))

    print(output)



def detektor_alphabet(karakter):
    alphabet = ""
    for i in karakter:
        if(i.isalpha()):
            alphabet = f"{alphabet}{i}"
    return alphabet

def detektor_angka(karakter):
    angka = ""
    for i in karakter:
        if(i.isnumeric()):
            angka = f"{angka}{i}"
    return angka

def detektor_simbol(karakter):
    simbol = ""
    for i in karakter:
        if(i.isalnum() == False):
            simbol = f"{simbol}{i}"
    return simbol

pemisah_string(input("Masukkan teks yang ingin anda pisah: "))