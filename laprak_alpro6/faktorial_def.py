bilangan= int(input("Masukkan bilangan yang ingin difaktorialkan: "))


def hasil_faktorial(bilangan):
    hasil = 1
    for i in range(bilangan, 0, -1):
        hasil = hasil * i
    return hasil

def penjabaran(bilangan):
    jabar = ""
    for i in range(bilangan, 0, -1):
        jabar = f"{jabar} x {i}"
    return jabar[3:]

print(f"{penjabaran(bilangan)} = {hasil_faktorial(bilangan)}")