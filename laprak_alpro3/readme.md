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
Pengulangan nilai i dari nilai input(x) hingga nol, disetiap pengulangan, string xxx akan dikali dengan nilai i sehingga menghasilkan string yang berulang. Cth("xxxxx")

<pre><code>for i in range(x, 0, -1):
    if(i % 2 == 0):
        print(underscore*i)
    else:
        print(xxx*i)</code></pre>
Pengulangan untuk soal a), batas awal akan menggunakan nilai dari x dan akan terus dikurangi dengan 1 sebelum diulangi.\n
If dan else berfungsi untuk mengecek apakah bilangan tersebut habis dibagi dua atau tidak, jika genap akan menggunakan underscore (_) dan jika ganjil akan menggunakan (x)
