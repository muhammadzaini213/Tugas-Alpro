import re

# Tinggal tempel aja teks list disini
text = '''
'''
pattern = re.compile(r'112410([0-9]{2})')

matches = set(int(match.group(1)) for match in pattern.finditer(text))

all_numbers = set(range(1, 93))
non_existent = all_numbers - matches

if non_existent:
    print("NIM yang belum list: ")
    for num in sorted(non_existent):
        print(f'112410{num:02}') 
else:
    print("Udah lengkap cuy")
