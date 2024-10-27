nama_file = "file.txt"

file = open(nama_file, 'r')
fileData = file.read()
file.close()

list_kata = fileData.split()

posisi_dan_kata = dict()

for i in range (0, len(list_kata)):
    posisi_dan_kata[i+1] = list_kata[i]


file = open("file_baru", 'w')

for key,value in posisi_dan_kata.items():
    file.write(f"{key}: {value}\n")
    print(f"{key}: {value}")

file.close()

