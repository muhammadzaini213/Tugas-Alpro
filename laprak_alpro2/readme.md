## penerjemah_protein_pro_max.py

```kodon = input("Masukkan Kodon yang ingin diterjemahkan: ")```
Saat program dimulai, program akan meminta input kodon yang ingin anda terjemahkan kemudian memasukkannya kedalam variabel 'kodon'.

```pengantar_hasil = "Nama protein tersebut adalah"```
Ini adalah variabel yang akan digunakan sebagai awalan dari output protein yang diterjemahkan, digunakan agar tidak perlu menulis kata ini di setiap hasil terjemahan protein secara manual atau satu-satu.

```teks_hijau = ":\033[32m"```
Variabel ini akan ditambahkan dalam output untuk mengubah warna output menjadi berwarna hijau.

```if(kodon == "AUG"):
 print(pengantar_hasil, teks_hijau, "Methionime")```
Awalan dari percabangan program, jika kodon diisi dengan 'AUG' maka akan memberikan output "Methionime" ditambah dengan pengantar_hasil dan teks_hijau.

```elif(kodon == "UUU" or kodon == "UUC"):
 print(pengantar_hasil, teks_hijau, "Phenylalanine")
elif(kodon == "UUA" or kodon == "UUG"):
 print(pengantar_hasil, teks_hijau, "Leucine")
elif(kodon == "UCU" or kodon == "UCC" or kodon == "UCA" or kodon == "UCG"):
 print(pengantar_hasil, teks_hijau, "Serine")
elif(kodon == "UAU" or kodon == "UAC"):
 print(pengantar_hasil, teks_hijau, "Tyrosine")
elif(kodon == "UGU" or kodon == "UGC"):
 print(pengantar_hasil, teks_hijau, "Cysteine")
elif(kodon == "UGG"):
 print(pengantar_hasil, teks_hijau, "Tryptophon")```
Kumpulan percabangan yang berdasar pada isi dari variabel 'kodon' beserta berbagai output yang dihasilkan.

```else:
 print("\033[31mTidak dapat menerjemahkan Kodon yang anda masukkan.")```
Mengeluarkan output berwarna merah yang menjelaskan jika input yang dimasukkan oleh pengguna tidak dapat diterjemahkan nama proteinnya.


## persamaan_akar_kuadrat.py

```print("Selamat datang di program pencari persamaan akar kuadrat!")
print("Silahkan masukkan nilai nilai dari persamaan sesuai instruksi.\n")```
Output awal yang dikeluarkan agar pengguna tahu apa maksud dan fungsi dari program ini.

```a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))```
Program meminta pengguna untuk memasukkan input numerik yang dibutuhkan ke variabel a, b, c.

```D = b**2 - 4*a*c```
Program menghitung nilai D menggunakan rumus.

```pengantar_hasil = "Maka akar persamaannya adalah"```
Hanya sebuah kata awal untuk hasil program, dibuat agar tidak perlu berkali-kali menulis ini di tiap output.

```print("Nilai D adalah:", D)```
Program menampilkan nilai D agar pengguna tahu berapa nilai D yang didapatkan

```if (D < 0):
 print(pengantar_hasil, "akar imajiner")```
Jika nilai D ada di bawah nol, maka output akan menunjukkan bahwa akar persamaannya adalah akar imajiner.

```elif (D == 0):
 print(pengantar_hasil, "X1 = X2, yang didapat dari -b/2a yang hasilnya adalah:", (-b)/2*a)```
Jika nilai D adalah nol, maka output akan menjelaskan hasil dapat didapat menggunakan rumus -b/2a serta hasilnya.

```elif (D > 0):
 print(pengantar_hasil, "dua akar, yaitu  X1 = (-b+D^0.5)/2*a dan X2 = (-b-D^0.5)/2*a), yang menghasilkan")
 print("X1 =", (-b+D**0.5)/2*a, "dan", "X2 =", (-b-D**0.5)/2*a) ```
Jika nilai D lebih besar dari nol, maka program akan menunjukkan bahwa persamaan itu memiliki dua akar dan menunjukkan kedua akar tersebut

```else:
 print("Error, anda memasukkan input yang salah")```
Kondisi ini kemungkinan tidak akan dijangkau, namun mungkin saja ada user yang memasukkan input yang salah sehingga kondisi ini tercapai.


## pencari_keganjilan.py

```bilangan_input = int(input("Masukkan batas bilangan ganjil: "))```
Program akan meminta input yang akan digunakan sebagai batas bilangan ganjil.

```string_bilangan = ""```
Variabel ini akan digunakan untuk menyimpan string dari urutan bilangan ganjil.

```print("Bilangan ganjil dibawah bilangan ini adalah:")```
Output untuk menjelaskan pada pengguna bahwa program ini menunjukkan bilangan ganjil.

```while(bilangan_input > 0):
  if(bilangan_input % 2 != 0):
    string_bilangan = f"{string_bilangan}{bilangan_input} "

  bilangan_input -= 1```
Disaat variabel bilangan_input lebih besar dari nol, maka program akan menjalankan hal di dalam while.

```if(bilangan_input % 2 != 0):
    string_bilangan = f"{string_bilangan}{bilangan_input} "```
Program ini ada di dalam while yang memastikan jika bilangan tersebut tidak habis dibagi dua (ganjil) maka program akan memasukkan bilangan tersebut kedalam variabel string_bilangan.

```bilangan_input -= 1```
Dijalankan setelah program memastikan apakah bilangan_input tidak habis dibagi dua, baris ini akan mengurangi variabel bilangan_input sebanyak 1 sebelum program while diulangi.

```print(string_bilangan)```
Setelah program while selesai, maka program akan mengeluarkan output urutan bilangan ganjil tersebut dari yang terbesar hingga terkecil.


## nilai_faktorial.py

```bilangan_input = int(input("Masukkan bilangan yang ingin dicari nilai faktorialnya: "))```
Program akan meminta pengguna untuk memasukkan bilangan bulat yang ingin dicari nilai faktorialnya.

```output = f"{bilangan_input}! ="```
Variabel ini akan menyimpan dan menyusun output akhir yang disusun dengan input yang ditambahkan tanda seru dan sama dengan (Cth: input = 5 => 5! =)

```penjabaran = ""```
Variabel ini akan menyimpan penjabaran faktorial (Cth: 4x3x2x1)

```hasil_faktorial = 1```
Variabel ini akan menyimpan nilai hasil faktorial, diisi dengan satu agar bilangan pertama tidak dikalikan dengan nol dan merusak hasil (akan dijelakan nanti)

```while(bilangan_input => 0):
 hasil_faktorial = hasil_faktorial * bilangan_input
 if(bilangan_input == 1):
  penjabaran = f"{penjabaran}{bilangan_input}"
 else:
  penjabaran = f"{penjabaran}{bilangan_input} x "
 bilangan_input -= 1```
Program while ini akan memastikan jika bilangan faktorial tidak

