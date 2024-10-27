nama_file = "file.txt"

try:
    file = open(nama_file, 'r')
    fileData = file.read()

    no_enter = fileData.replace("\n", "")

    with open(nama_file, 'w') as file:
        file.write(no_enter)
    print(no_enter)

except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan.")
except IOError:
    print("Terjadi kesalahan saat membaca atau menulis file.")
except Exception as e:
    print(f"Kesalahan tak terduga terjadi: {e}")