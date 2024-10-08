def aljabar(awal, akhir):
    for x in range(awal, akhir):
        hasil = 6*(x*x) + 3*x + 2
        print(f"f({x}) = 6({x})^2 + 3({x}) + 2 = {hasil}")

aljabar(-10, 10)