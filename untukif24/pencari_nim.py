import re

# Tinggal tempel aja teks list disini
text = '''

'''

# Bagian ini tinggal edit sesuai prodi, angkatan, dan semester kalian
kode_prodi = 11
angkatan = 24
semester = 1

student_names = {
    1: 'Abbie Dzakwan Putra Setyawan',
    2: 'Aditiya Kusuma',
    3: 'Adrian Orlin Vinsensyah',
    4: 'Adrian Tannady',
    5: 'Ahmad Anwar Abdul Qowi',
    6: 'Ahmad Rafif Rafi',
    7: 'Akmal Nuzulla',
    8: 'Aldo Adirajasa Fathoni',
    9: 'Aldy Tri Ramadhani',
    10: 'Alisha Zalfa Safitri',
    11: 'Alisya Duri Azizah',
    12: 'Amalia Rahmanda',
    13: 'Anantha Lokantara',
    14: 'Andi Naufal Nurfadhil',
    15: 'Ariel',
    16: 'Benediktus Aldreno Fabian Wowor',
    17: 'Berlian Mayfarel Rafael',
    18: 'Bhisma Aprian Prayogi',
    19: 'Brian Frisco Simanjuntak',
    20: 'Bryan Fitur Ayni',
    21: 'Chrisella Sefriana Tilukay',
    22: 'Christian Imanuel Admojo',
    23: 'Cindy Aulia Renita',
    24: 'Daniel Juan Haris Hutajulu',
    25: 'Dea Cinta Ramadani',
    26: 'Diva Novaliza Fitriyani',
    27: 'Dylan Sukma Yudha',
    28: 'Fauzan Fayzul Haq',
    29: 'Fazly Pasya Pahlevi',
    30: 'Ferdianta Tarigan',
    31: 'Fikhar Riyazul Islam',
    32: 'Gathan Gafarrel Aqilla',
    33: 'Gian Al Haritz Ueldy Secondri',
    34: 'Giva Asilah Hasnaa Putri',
    35: 'Ibnu Dwiki Hermawan',
    36: 'James Alvaro Gavriel Pulung',
    37: 'Jasmine Aishwarya Wandha',
    38: 'Jasmine Ayu Andini',
    39: 'Kanjeng Adha Nur Asis',
    40: 'Kevin Jonathan Wijaya',
    41: 'Lisa Sapitri',
    42: 'M. Sya\'bani Nur Zain',
    43: 'Maulana Wahid Ramadan',
    44: 'Mayoga Finanda',
    45: 'Mochammad Azriel Albian Putra',
    46: 'Mohammad Mamba\'u Khusnul Umam',
    47: 'Muh. Indra Anugrah',
    48: 'Muhamad Radyt Iksan Pratama',
    49: 'Muhamad Rizal',
    50: 'Muhammad Aditya Putra',
    51: 'Muhammad Afdhalul Adam',
    52: 'Muhammad Fakhrii Julian Noor',
    53: 'Muhammad Farel Alkayis',
    54: 'Muhammad Fauzan Akmal',
    55: 'Muhammad Iqbal',
    56: 'Muhammad Iqbal Ferhan',
    57: 'Muhammad Khairullah Kosasih Zain',
    58: 'Muhammad Nabil Ihyalfikra',
    59: 'Muhammad Rayhant Almunawar',
    60: 'Muhammad Ridho Alfarod',
    61: 'Muhammad Rifqy Dzakwan',
    62: 'Muhammad Rizky Wicaksono',
    63: 'Muhammad Wisnu Wardhana',
    64: 'Muhammad Zaini',
    65: 'Mutia Rahmawati',
    66: 'Nabil Arif Ikhwanul Hakim',
    67: 'Nabilah Al Fadiyah',
    68: 'Nadine Adelia Rizky Kusmanda',
    69: 'Naila Kalsum',
    70: 'Nathanael Prasetyo',
    71: 'Naufal Rifqi Rahman',
    72: 'Nurmuhammad Wahyu Ramadhan',
    73: 'Pandu Restu Adjie',
    74: 'Prima Hafidz Maulana',
    75: 'Rafael Hotdion Lumban Toruan',
    76: 'Rana Afifah Dzikro',
    77: 'Rhadyt Insan Faryabie',
    78: 'Rifat Arifaldo',
    79: 'Sebastian Paskahadi Budiman',
    80: 'Sulthan Farizan Fawwaz',
    81: 'Syahri Nasta’in',
    82: 'Terrano Jazil Fadiatmoko',
    83: 'Thisya Darmala',
    84: 'Thopan Rahman Hakim',
    85: 'Tiara Saparang',
    86: 'Vanessa Marrie Tandiarru',
    87: 'Veronika Thalila Putri',
    88: 'Vincensius Frodo Siregar',
    89: 'Wulan Oktavianty Ajitomo',
    90: 'Yumna Azzahra',
    91: 'Zamir Zulkarnain Litbarsky',
    92: 'Zharif Aziz Zulkarnain Widodo'
}

pattern = re.compile(rf'{kode_prodi}{angkatan}{semester}0([0-9]{{2}})')

matches = set(int(match.group(1)) for match in pattern.finditer(text))

all_numbers = set(range(1, 93))

non_existent = all_numbers - matches

if non_existent:
    print("NIM yang belum list:")
    for num in sorted(non_existent):
        print(f'112410{num:02} - {student_names[num]}')
else:

    print("Udah lengkap cuy")
