## cicilan_rumah.py

<pre><code>harga_asal = int(input("Harga asal rumah: "))
harga_jual = int(input("Harga jual rumah: "))
waktu_perlima_tahun = int(input("Waktu cicilan: 5 tahun x ")) * 5</code><pre>
Saat program dimulai, pengguna disuruh memasukkan input harga asal, harga jual, serta berapa lama rumah akan dicicil.

<pre><code>for tahun in range (waktu_perlima_tahun, 0, -5):
 print(f"Cicilan pertahun untuk {tahun} tahun adalah {harga_jual/tahun} per tahun")</code></pre
Baris kode ini akan melakukan perulangan berapa cicilan yang akan pembeli bayar per tahun dan mengulanginya lagi untuk 5 tahun dibawahnya hingga cicilan 5 tahun.

## sarangheyo.py

<pre><code>x = int(input("Masukkan nilai: "))</code></pre>
Saat program dimulai, pengguna akan diminta memasukkan input untuk variasi menggunakan bilangan bulat.

<pre><code>xxx = "x"
underscore = "-"
dot = ". "</code></pre>
Baris ini berisi variabel string yang akan diulangi dalam output.

<pre><code>print("\n")<code></pre>
Output yang satu ini berguna untuk menambahkan baris baru sehingga beberapa input tidak menyatu.

<pre><code>for i in range(x, 0 , -1):
    print(xxx*i)</code></pre>
Pengulangan untuk soal a), nilai i dari nilai input(x) hingga nol, disetiap pengulangan, string xxx akan dikali dengan nilai i sehingga menghasilkan string yang berulang. Cth("xxxxx")

<pre><code>for i in range(x, 0, -1):
    if(i % 2 == 0):
        print(underscore*i)
    else:
        print(xxx*i)</code></pre>
Pengulangan untuk soal b), batas awal akan menggunakan nilai dari x dan akan terus dikurangi dengan 1 sebelum diulangi.<br>
If dan else berfungsi untuk mengecek apakah bilangan tersebut habis dibagi dua atau tidak, jika genap akan menggunakan underscore (_) dan jika ganjil akan menggunakan (x)

<pre><code>angka_dari_kecil = ""
angka_dari_besar = ""
for i in range(1, x+1):
    angka_dari_kecil = f"{angka_dari_kecil}{i}"
    print(angka_dari_kecil)

    if(i != x):
      angka_dari_besar = f"{angka_dari_kecil}\n{angka_dari_besar}"
    else:
        print(angka_dari_besar)</code></pre>
Pengulangan untuk soal c), variabel angka i dimulai dari angka 1 dan akan diloop hingga mencapai nilai input(x), variabel angka dari kecil akan menyimpan urutan angka dari yang terkecil, dan menambahkan angkanya setiap pengulangan.<br>
Kemudian, angka dari besar menyusun urutan angka dari yang terbanyak dan berkurang sebanyak satu tiap pengulangan.

<pre><code>for i in range(1, x+1):
    print(xxx*i)
    if(i == x):
        break

for i in range(x-1,0,-1):
    print(xxx*i)
    if(i == x):
        break</code></pre>
Pengulangan untuk soal d), for loop pertama akan mengeluarkan output x dari hanya satu x hingga xxxxx (sesuai dengan input). Kemudian, for loop kedua akan menyusun dari xxxx (sesuai urutan angka) hingga x saja.

<pre><code>for i in range(x, 0 ,-1):
    print(f"{dot*(i-1)}{i}")</code></pre>
Pengulangan untuk soal e), mengulangi i dari nilai input(x) hingga nol dengan menguranginya dengan satu tiap pengulangan, for loop ini akan menyusun dot ( . ) hingga nilai i dikurangi satu, serta nilai i diletakkan setelah dot nya.
