<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
</head>
<body>
    <h1>Dokumentasi Program Python</h1>
    <p>Berikut adalah dokumentasi untuk beberapa skrip Python yang berbeda. Setiap skrip memiliki fungsionalitas yang spesifik dan menjelaskan bagaimana cara penggunaannya.</p>

    <h2>1. <code>penerjemah_protein_pro_max.py</code></h2>
    <p>Program ini menerjemahkan kodon RNA menjadi nama protein.</p>

    <h3>Cara Kerja</h3>
    <ol>
        <li><strong>Masukkan Kodon</strong>: Pengguna diminta untuk memasukkan kodon RNA yang ingin diterjemahkan.</li>
        <li><strong>Pengantar Hasil</strong>: Variabel <code>pengantar_hasil</code> digunakan untuk menyertakan awalan pada hasil output.</li>
        <li><strong>Warna Teks</strong>: Output ditampilkan dengan teks berwarna hijau jika kodon valid.</li>
        <li><strong>Penerjemahan Kodon</strong>:
            <ul>
                <li><code>AUG</code> → Methionine</li>
                <li><code>UUU</code> atau <code>UUC</code> → Phenylalanine</li>
                <li><code>UUA</code> atau <code>UUG</code> → Leucine</li>
                <li><code>UCU</code>, <code>UCC</code>, <code>UCA</code>, atau <code>UCG</code> → Serine</li>
                <li><code>UAU</code> atau <code>UAC</code> → Tyrosine</li>
                <li><code>UGU</code> atau <code>UGC</code> → Cysteine</li>
                <li><code>UGG</code> → Tryptophan</li>
            </ul>
        </li>
        <li><strong>Pesan Error</strong>: Menampilkan pesan jika kodon tidak dapat diterjemahkan.</li>
    </ol>

    <h3>Kode</h3>
    <pre><code>kodon = input("Masukkan Kodon yang ingin diterjemahkan: ")
pengantar_hasil = "Nama protein tersebut adalah"
teks_hijau = ":\033[32m"

if kodon == "AUG":
    print(pengantar_hasil, teks_hijau, "Methionine")
elif kodon in ["UUU", "UUC"]:
    print(pengantar_hasil, teks_hijau, "Phenylalanine")
elif kodon in ["UUA", "UUG"]:
    print(pengantar_hasil, teks_hijau, "Leucine")
elif kodon in ["UCU", "UCC", "UCA", "UCG"]:
    print(pengantar_hasil, teks_hijau, "Serine")
elif kodon in ["UAU", "UAC"]:
    print(pengantar_hasil, teks_hijau, "Tyrosine")
elif kodon in ["UGU", "UGC"]:
    print(pengantar_hasil, teks_hijau, "Cysteine")
elif kodon == "UGG":
    print(pengantar_hasil, teks_hijau, "Tryptophan")
else:
    print("\033[31mTidak dapat menerjemahkan Kodon yang anda masukkan.")
</code></pre>

    <h2>2. <code>persamaan_akar_kuadrat.py</code></h2>
    <p>Program ini menyelesaikan persamaan kuadrat dari bentuk <code>ax² + bx + c = 0</code> dan menampilkan akarnya.</p>

    <h3>Cara Kerja</h3>
    <ol>
        <li><strong>Input</strong>: Pengguna diminta memasukkan nilai <code>a</code>, <code>b</code>, dan <code>c</code>.</li>
        <li><strong>Hitung Diskriminan</strong>: Menggunakan rumus <code>D = b² - 4ac</code>.</li>
        <li><strong>Jenis Akar</strong>:
            <ul>
                <li>Jika <code>D &lt; 0</code>: Akar imajiner</li>
                <li>Jika <code>D == 0</code>: Satu akar</li>
                <li>Jika <code>D &gt; 0</code>: Dua akar</li>
            </ul>
        </li>
        <li><strong>Pesan Error</strong>: Menampilkan pesan jika input tidak valid.</li>
    </ol>

    <h3>Kode</h3>
    <pre><code>print("Selamat datang di program pencari persamaan akar kuadrat!")
print("Silahkan masukkan nilai-nilai dari persamaan sesuai instruksi.\n")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

D = b**2 - 4*a*c
pengantar_hasil = "Maka akar persamaannya adalah"

print("Nilai D adalah:", D)

if D &lt; 0:
    print(pengantar_hasil, "akar imajiner")
elif D == 0:
    print(pengantar_hasil, "X1 = X2, yang didapat dari -b/2a yang hasilnya adalah:", (-b)/(2*a))
elif D &gt; 0:
    X1 = (-b + D**0.5) / (2*a)
    X2 = (-b - D**0.5) / (2*a)
    print(pengantar_hasil, "dua akar, yaitu X1 = (-b+D^0.5)/2a dan X2 = (-b-D^0.5)/2a), yang menghasilkan")
    print("X1 =", X1, "dan", "X2 =", X2)
else:
    print("Error, anda memasukkan input yang salah")
</code></pre>

    <h2>3. <code>pencari_keganjilan.py</code></h2>
    <p>Program ini mencetak bilangan ganjil yang kurang dari batas yang ditentukan.</p>

    <h3>Cara Kerja</h3>
    <ol>
        <li><strong>Input</strong>: Pengguna memasukkan batas bilangan ganjil.</li>
        <li><strong>Output</strong>: Menampilkan bilangan ganjil dari batas hingga 1.</li>
    </ol>

    <h3>Kode</h3>
    <pre><code>bilangan_input = int(input("Masukkan batas bilangan ganjil: "))
string_bilangan = ""

print("Bilangan ganjil dibawah bilangan ini adalah:")

while bilangan_input &gt; 0:
    if bilangan_input % 2 != 0:
        string_bilangan += f"{bilangan_input} "
    bilangan_input -= 1

print(string_bilangan)
</code></pre>

    <h2>4. <code>nilai_faktorial.py</code></h2>
    <p>Program ini menghitung nilai faktorial dari bilangan positif.</p>

    <h3>Cara Kerja</h3>
    <ol>
        <li><strong>Input</strong>: Pengguna memasukkan bilangan bulat.</li>
        <li><strong>Output</strong>: Menampilkan hasil faktorial dan penjabaran proses perhitungan.</li>
    </ol>

    <h3>Kode</h3>
    <pre><code>bilangan_input = int(input("Masukkan bilangan yang ingin dicari nilai faktorialnya: "))
output = f"{bilangan_input}! ="
penjabaran = ""
hasil_faktorial = 1

if bilangan_input &lt;= 0:
    print("Input harus lebih besar dari nol!")
else:
    while bilangan_input &gt; 0:
        hasil_faktorial *= bilangan_input
        if bilangan_input == 1:
            penjabaran += f"{bilangan_input}"
        else:
            penjabaran += f"{bilangan_input} x "
        bilangan_input -= 1

    print(output, penjabaran, "=", hasil_faktorial)
</code></pre>

</body>
</html>
