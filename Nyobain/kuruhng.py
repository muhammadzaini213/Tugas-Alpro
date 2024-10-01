import sys
print(".:: Program Pengecekan Tanda Kurung ::.")
stack = []
input_string = input("Masukkan kalimat : ")
for i in input_string:
 if i in '[{(':
    stack.append(i)
 elif i in ']})':
    if stack:
        if i == ']' and '[' != stack.pop():
            sys.exit("Tanda [] salah !")
        if i == '}' and '{' != stack.pop():
            sys.exit("Tanda {} salah !")
        if i == ')' and '(' != stack.pop():
         sys.exit("Tanda () salah !")
    else:
     sys.exit("Tidak ada tanda kurung di awal !")
print("Kalimat Sudah Benar...")