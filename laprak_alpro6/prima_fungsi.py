def cari_prima(n):
    prima = True
    for i in range (2, n):
        if(n % i == 0):
            prima = False

    if(prima):
        print(f"Bilangan {n} adalah prima")
    else:
        print(f"Bilangan {n} bukan prima")

cari_prima(int(input("Masukkan bilangan: ")))