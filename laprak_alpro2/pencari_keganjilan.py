bilangan_input = int(input("Masukkan batas bilangan ganjil: "))
string_bilangan = ""
print("Bilangan ganjil dibawah bilangan ini adalah:")

while(bilangan_input > 0):
  if(bilangan_input % 2 != 0):
    string_bilangan = f"{string_bilangan}{bilangan_input} "

  bilangan_input -= 1

print(string_bilangan)
