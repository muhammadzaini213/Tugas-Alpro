nama_file = "file.txt"

file = open(nama_file, 'r')
fileData = file.read()
file.close()

list_kata = fileData.split()

posisi_dan_kata = dict()

for i in range (1, len(list_kata)):
    posisi_dan_kata[i] = list_kata[i-1]


file = open("file_baru", 'a')

for key,value in posisi_dan_kata.items():
    file.write(f"{key-1}: {value}\n")
    print(f"{key-1}: {value}")

file.close()

