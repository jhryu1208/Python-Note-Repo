
names = ['윤나은', '김현주', '장현지', '이지선', '박선주']

"""
enumerate ex1 : basic
"""

names_asc = sorted(names)
stud_dict = dict()
for num, name in enumerate(names_asc):
    stud_dict[num+1] = name

print(stud_dict)


"""
enumerate ex2 : set start number
"""

names_asc = sorted(names)
stud_dict = dict()
for num, name in enumerate(names_asc, 10):
    stud_dict[num] = name

print(stud_dict)

"""
enumerate ex2 : use lambda
"""

stud_dict = { num : name for num,  name in enumerate(sorted(names), 100)}
print(stud_dict)
