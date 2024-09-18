harga_asal = int(input("Harga asal rumah: "))
harga_jual = int(input("Harga jual rumah: "))
waktu_perlima_tahun = int(input("Waktu cicilan: 5 tahun x ")) * 5
for tahun in range (waktu_perlima_tahun, 0, -5):
 print(f"Cicilan pertahun untuk {tahun} tahun adalah {harga_jual/tahun} per tahun")
