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
        print(angka_dari_besar)<code><pre>
Pengulangan untuk soal c), variabel angka i dimulai dari angka 1 dan akan diloop hingga mencapai nilai input(x), variabel angka dari kecil akan menyimpan urutan angka dari yang terkecil, dan menambahkan angkanya setiap pengulangan.<br>
Kemudian, angka dari besar menyusun urutan angka dari yang terbanyak dan berkurang sebanyak satu tiap pengulangan.


