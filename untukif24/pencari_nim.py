import re

# tinggal ganti ganti ini aja wak pas ngelist
text = '''
List yang sudah mengisi: 
1. Gian - 11241033
2. Lisa - 11241041
3. Aditya - 11241050
4. Ariel - 11241015
5. Nabil - 11241058
6. Adit - 11241002
7. Iqbal - 11241055
8. Atha - 11241039
9. Sya'bani - 11241042
10. Nathanael Prasetyo - 11241070
11. Zaini - 11241064
12. Mutia - 11241065
13. Fauzan - 11241028
14. Vero - 11241087
15. Abbie - 11241001
16. Andi - 11241014
17. Rizky - 11241062
18. Christian - 11241022
19. Rana - 11241076
20. Nabil Arif - 11241066
21. Naila Kalsum - 11241069
22. Khairul - 11241057
23. Sulthan - 11241080
24. Yumna -11241090
25. Indra - 11241047
26. James - 11241036
27. Alisha - 11241010
28. Manda - 11241012
29. Yoga - 11241044
30. Chrisella - 11241021
31. Nabilah - 11241067
32. Rehant - 11241059
33. Thisya - 11241083
34. Sebastian - 11241079
35. Wisnu - 11241063
36. Rafa - 11241017
37. Gathan - 11241032
38. Adam - 11241051
39. Vanessa - 11241086
40. Radyt - 11241048
41. Reno - 11241016
42. Zharif - 11241092
43. Fauzan - 11241054
44. Cindy - 11241023
45. Kevin - 11241040
46. Anwar - 11241005
47. Akmal - 11241007
48. Dylan - 11241027
49. Rifat - 11241078
50. Prima - 11241074
51. Kayis - 11241053
52. ⁠Anantha - 11241013
53. Rhadyt insan -11241077
54. Pael - 11241075
55. Jasmine - 11241038
56. Azizah_11241011
57. Fitur_11241020
58. Adrian_11241004
59. ⁠Fikhar - 11241031
60. Juan - 11241024
61. Ferhan -11241056
62. ridho-11241060
63. ⁠Jasmine- 11241037
64. Brian - 11241019
65. Thopan -11241084
66. ⁠dea cinta-11241025
67. Ibnu - 11241035
68. Pandu - 11241073
69. Aldy - 11241009
70. Rifqy - 11241061
71. Ferdi - 11241030
72. Diva - 11241026
73. Aldo - 11241008
74. ⁠Nasta’in - 11241081
75. Naufal -11241071
76. Rafi - 11241006
77. Wulan - 11241089
78. ⁠orlin - 11241003
79. Bhisma - 11241018
80. Fakhrii - 11241052
81. Terra-11241082
82. Tiara - 11241085
83. Zamir - 11241091
84. Frodo- 11241088
85. Pasya- 11241029
86. Azriel - 11241045
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
