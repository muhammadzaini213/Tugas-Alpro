def cek_genap(n):
    if(n % 2 == 0):
        return n
    else:
        return 0

def total_genap(awal, akhir):
    total = 0
    for n in range(awal, akhir+1):
        total = total + cek_genap(n)
    print(total)

total_genap(int(input("Batas awal: ")), int(input("Batas akhir: ")))