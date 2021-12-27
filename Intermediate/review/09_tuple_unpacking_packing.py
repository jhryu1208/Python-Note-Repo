"""
tuple packing
"""

tri_1 = (10, 25)
print(tri_1, type(tri_1))

tri_2 = 10, 25
print(tri_2, type(tri_2))

print('\n')

"""
tuple unpacking
"""

tri_3 = (12, 25)
bt, ht = tri_3
print(bt, ht)

print('\n')

nums = (1, 2, 3, 4, 5)

a, b, *others = nums
print(a, b, others)

a, *others, b = nums
print(a, others, b)

*others, a, b = nums
print(others, a, b)

print('\n')

nums = [1, 2, 3, 4, 5]
a, b, *others = nums
print(a, b, others)

print('\n')

"""
packing, unpacking : function
"""

def return_nums():
    return 1, 2, 3, 4, 5 # 튜플의 소괄호 생략 형태

nums = return_nums()
print(nums, type(nums))

a, b, *others = return_nums()
print(a, b, others)


def show_nums(a, b, *other):
    str = \
    f"""
    num : {a}, type : {type(a)}
    num : {b}, type : {type(b)}
    num : {other}, type : {type(other)}
    """
    print(str)

show_nums(1, 2, 3, 4, 5, 6)


def show_man(name, age, height):
    str = \
    f"""
    name : {name},
    age : {age},
    height : {height}
    """
    print(str)

p = ('Ryu', 25, 178)
show_man(*p)

print('\n')

"""
unpacking : tuple in tuple
"""
t = (1, 2, (3, 4))
a, b, (c, d) = t
print(a, b, c, d, sep=', ')

p = 'Hong', (32, 178), '010-1234-5678', 'Korea'
na, (ag, he), ph, ad = p
print(na, he)

p = 'Hong', (32, 178), '010-1234-5678', 'Korea'
na, (_, he), _, _ = p
print(na, he)

print('\n')

"""
unpacking : for loop
"""

ps = [('Lee', 172), ('Jung', 182), ('Yoon', 179)]
for n, h in ps:
    print(n, h, sep = ', ')
