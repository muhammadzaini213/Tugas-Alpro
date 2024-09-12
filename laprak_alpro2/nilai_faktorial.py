bilangan_input = int(input("Masukkan bilangan yang ingin dicari nilai faktorialnya: "))

output = f"{bilangan_input}! ="
penjabaran = ""

hasil_faktorial = 1

if(bilangan_input == 0 or bilangan_input < 0):
 print("Input harus lebih besar dari nol!")
else:
 while(bilangan_input != 0):
  hasil_faktorial = hasil_faktorial * bilangan_input
  if(bilangan_input == 1):
   penjabaran = f"{penjabaran}{bilangan_input}"
  else:
   penjabaran = f"{penjabaran}{bilangan_input} x "
  bilangan_input -= 1
 print(output, penjabaran, "=", hasil_faktorial)

