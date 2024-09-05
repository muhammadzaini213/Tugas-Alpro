n = int(input("Input = "))

ganjil = []
genap = []

for i in range(1, n+1):
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)

print("Ganjil =", ', '.join(map(str, ganjil)))
print("Genap =", ', '.join(map(str, genap)))
