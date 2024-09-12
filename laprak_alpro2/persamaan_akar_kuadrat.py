print("Selamat datang di program pencari persamaan akar kuadrat!")
print("Silahkan masukkan nilai nilai dari persamaan sesuai instruksi.\n")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

D = b**2 - 4*a*c

pengantar_hasil = "Maka akar persamaannya adalah"

print("Nilai D adalah:", D)

if (D < 0):
 print(pengantar_hasil, "akar imajiner")
elif (D == 0):
 print(pengantar_hasil, "X1 = X2, yang didapat dari -b/2a yang hasilnya adalah:", (-b)/2*a)
elif (D > 0):
 print(pengantar_hasil, "dua akar, yaitu  X1 = (-b+D^0.5)/2*a dan X2 = (-b-D^0.5)/2*a), yang menghasilkan")
 print("X1 =", (-b+D**0.5)/2*a, "dan", "X2 =", (-b-D**0.5)/2*a) 
else:
 print("Error, anda memasukkan input yang salah")
