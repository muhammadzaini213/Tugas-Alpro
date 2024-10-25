nama_file = "file.txt"

file = open(nama_file, 'r')
fileData = file.read()
file.close()

file = open(nama_file, 'w')
no_enter = fileData.replace("\n", "")
file.write(no_enter)
file.close()

print(no_enter)