## penerjemah_protein_pro_max.py

<pre><code>kodon = input("Masukkan Kodon yang ingin diterjemahkan: ")</code></pre>
Saat program dimulai, program akan meminta input kodon yang ingin anda terjemahkan kemudian memasukkannya kedalam variabel 'kodon'.

<pre><code>pengantar_hasil = "Nama protein tersebut adalah"</code></pre>
Ini adalah variabel yang akan digunakan sebagai awalan dari output protein yang diterjemahkan, digunakan agar tidak perlu menulis kata ini di setiap hasil terjemahan protein secara manual atau satu-satu.

<pre><code>teks_hijau = ":\033[32m"</code></pre>
Variabel ini akan ditambahkan dalam output untuk mengubah warna output menjadi berwarna hijau.

<pre><code>if(kodon == "AUG"):
 print(pengantar_hasil, teks_hijau, "Methionime")</code></pre>
Awalan dari percabangan program, jika kodon diisi dengan 'AUG' maka akan memberikan output "Methionime" ditambah dengan pengantar_hasil dan teks_hijau.

<pre><code>elif(kodon == "UUU" or kodon == "UUC"):
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
 print(pengantar_hasil, teks_hijau, "Tryptophon")</code></pre>
Kumpulan percabangan yang berdasar pada isi dari variabel 'kodon' beserta berbagai output yang dihasilkan.

<pre><code>else:
 print("\033[31mTidak dapat menerjemahkan Kodon yang anda masukkan.")</code></pre>
Mengeluarkan output berwarna merah yang menjelaskan jika input yang dimasukkan oleh pengguna tidak dapat diterjemahkan nama proteinnya.


## persamaan_akar_kuadrat.py

<pre><code>print("Selamat datang di program pencari persamaan akar kuadrat!")
print("Silahkan masukkan nilai nilai dari persamaan sesuai instruksi.\n")</code></pre>
Output awal yang dikeluarkan agar pengguna tahu apa maksud dan fungsi dari program ini.

<pre><code>a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))</code></pre>
Program meminta pengguna untuk memasukkan input numerik yang dibutuhkan ke variabel a, b, c.

<pre><code>D = b**2 - 4*a*c</code></pre>
Program menghitung nilai D menggunakan rumus.

<pre><code>pengantar_hasil = "Maka akar persamaannya adalah"</code></pre>
Hanya sebuah kata awal untuk hasil program, dibuat agar tidak perlu berkali-kali menulis ini di tiap output.

<pre><code>print("Nilai D adalah:", D)</code></pre>
Program menampilkan nilai D agar pengguna tahu berapa nilai D yang didapatkan

<pre><code>if (D < 0):
 print(pengantar_hasil, "akar imajiner")</code></pre>
Jika nilai D ada di bawah nol, maka output akan menunjukkan bahwa akar persamaannya adalah akar imajiner.

<pre><code>elif (D == 0):
 print(pengantar_hasil, "X1 = X2, yang didapat dari -b/2a yang hasilnya adalah:", (-b)/2*a)</code></pre>
Jika nilai D adalah nol, maka output akan menjelaskan hasil dapat didapat menggunakan rumus -b/2a serta hasilnya.

<pre><code>elif (D > 0):
 print(pengantar_hasil, "dua akar, yaitu  X1 = (-b+D^0.5)/2*a dan X2 = (-b-D^0.5)/2*a), yang menghasilkan")
 print("X1 =", (-b+D**0.5)/2*a, "dan", "X2 =", (-b-D**0.5)/2*a)</code></pre>
Jika nilai D lebih besar dari nol, maka program akan menunjukkan bahwa persamaan itu memiliki dua akar dan menunjukkan kedua akar tersebut

<pre><code>else:
 print("Error, anda memasukkan input yang salah")</code></pre>
Kondisi ini kemungkinan tidak akan dijangkau, namun mungkin saja ada user yang memasukkan input yang salah sehingga kondisi ini tercapai.


## pencari_keganjilan.py

<pre><code>bilangan_input = int(input("Masukkan batas bilangan ganjil: "))</code></pre>
Program akan meminta input yang akan digunakan sebagai batas bilangan ganjil.

<pre><code>string_bilangan = ""</code></pre>
Variabel ini akan digunakan untuk menyimpan string dari urutan bilangan ganjil.

<pre><code>print("Bilangan ganjil dibawah bilangan ini adalah:")</code></pre>
Output untuk menjelaskan pada pengguna bahwa program ini menunjukkan bilangan ganjil.

<pre><code>while(bilangan_input > 0):
  if(bilangan_input % 2 != 0):
    string_bilangan = f"{string_bilangan}{bilangan_input} "

  bilangan_input -= 1</code></pre>
Disaat variabel bilangan_input lebih besar dari nol, maka program akan menjalankan hal di dalam while.

<pre><code>if(bilangan_input % 2 != 0):
    string_bilangan = f"{string_bilangan}{bilangan_input} "</code></pre>
Program ini ada di dalam while yang memastikan jika bilangan tersebut tidak habis dibagi dua (ganjil) maka program akan memasukkan bilangan tersebut kedalam variabel string_bilangan.

<pre><code>bilangan_input -= 1</code></pre>
Dijalankan setelah program memastikan apakah bilangan_input tidak habis dibagi dua, baris ini akan mengurangi variabel bilangan_input sebanyak 1 sebelum program while diulangi.

<pre><code>print(string_bilangan)</code></pre>
Setelah program while selesai, maka program akan mengeluarkan output urutan bilangan ganjil tersebut dari yang terbesar hingga terkecil.


## nilai_faktorial.py

<pre><code>bilangan_input = int(input("Masukkan bilangan yang ingin dicari nilai faktorialnya: "))</code></pre>
Program akan meminta pengguna untuk memasukkan bilangan bulat yang ingin dicari nilai faktorialnya.

<pre><code>output = f"{bilangan_input}! ="</code></pre>
Variabel ini akan menyimpan dan menyusun output akhir yang disusun dengan input yang ditambahkan tanda seru dan sama dengan (Cth: input = 5 => 5! =)

<pre><code>penjabaran = ""</code></pre>
Variabel ini akan menyimpan penjabaran faktorial (Cth: 4x3x2x1)

<pre><code>hasil_faktorial = 1</code></pre>
Variabel ini akan menyimpan nilai hasil faktorial, diisi dengan satu agar bilangan pertama tidak dikalikan dengan nol dan merusak hasil (akan dijelakan nanti)

<pre><code>if(bilangan_input == 0 or bilangan_input < 0):
 print("Input harus lebih besar dari nol!")</code></pre>
Jika bilangan lebih kecil atau sama dengan nol, maka batalkan operasi dan ingatkan pengguna bahwa input harus lebih besar dari nol.

<pre><code>else:
 while(bilangan_input >= 0):
  hasil_faktorial = hasil_faktorial * bilangan_input
  if(bilangan_input == 1):
   penjabaran = f"{penjabaran}{bilangan_input}"
  else:
   penjabaran = f"{penjabaran}{bilangan_input} x "
  bilangan_input -= 1
 print(output, penjabaran, "=", hasil_faktorial)</code></pre>
Jika kondisi sebelumnya tidak terpenuhi, maka jalankan program ini.

<pre><code>while(bilangan_input => 0):
 hasil_faktorial = hasil_faktorial * bilangan_input
 if(bilangan_input == 1):
  penjabaran = f"{penjabaran}{bilangan_input}"
 else:
  penjabaran = f"{penjabaran}{bilangan_input} x "
 bilangan_input -= 1</code></pre>
Program while ini akan melakukan perulangan selama variabel bilangan_input belum bernilai nol.

<pre><code>hasil_faktorial = hasil_faktorial * bilangan_input</code></pre>
Variabel ini akan menyimpan total hasil faktorial atau kali berulangnya.

<pre><code>if(bilangan_input == 1):
   penjabaran = f"{penjabaran}{bilangan_input}"</code></pre>
Jika bilangan_input sudah bernilai 1, akhir dari variabel penjabaran tidak perlu diberikan tanda x (kali).

<pre><code>else:
   penjabaran = f"{penjabaran}{bilangan_input} x "</code></pre>
Jika kondisi diatas belum terpenuhi, maka tambahkan penjabaran dengan bilangan input disertai tanda x (kali) dibelakangnya.

<pre><code>bilangan_input -= 1</code></pre>
Sebelum while diulangi, variabel bilangan_input akan dikurangi dengan 1

<pre><code>print(output, penjabaran, "=", hasil_faktorial)</code></pre>
Setelah program while selesai, output akan ditampilkan, lengkap dengan penjabaran dan hasil dari faktorial bilangan yang di input.

