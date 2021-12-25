"""
iter 함수
"""
list = [1, 2, 3]
ir = iter(list)

while True:
    try:
        print(next(ir))
    except StopIteration:
        print('raise StopIteration')
        break

ir = iter(list) # iterator객체 init

while True:
    try:
        print(next(ir))
    except StopIteration:
        print('raise StopIteration')
        break

print('\n')

"""
iterator, iterable object
"""

list = [1, 2, 3]
tuple = (1, 2, 3)
string = 'Hello'

# iterable객체 판별법1 : iter함수
# list, tuple, string은 모두 iter함수를 통해서 iterator객체를 반환하였기에 iterable객체에 해당한다.
print(type(iter(list)))
print(type(iter(tuple)))
print(type(iter(string)))

# iterable객체 판별법2 : dir함수
dir_ = dir(list)
print(dir_)
print(*[f'find : {i}' for i in dir_ if i == '__iter__'])

# iterable객체 판별법3 : hasattr함수
print(hasattr(list, '__iter__'))


print('\n')

"""
special method
"""
list = [1, 2, 3]
ir = list.__iter__()
print(ir.__next__())
print(ir.__next__())


"""
for loop & Iterable obj
"""

for i in [1, 2, 3]:
    print(i, end = ' ')

# for loop internal code
ir = iter([1, 2, 3])
while True:
    try:
        i = next(ir)
        print(i, end = ' ')
    except StopIteration:
        break

#
for i in iter([1, 2, 3]):
    print(i, end = ' ')

print('\n')

test_list = [1, 2, 3] # init list
test_iter0 = iter(test_list) # iter's arge = list
test_iter1 = iter(test_iter0) # iter's arge = iter
print(id(test_list)) # 2540659168136
print(id(test_iter0)) # 2540661600072
print(id(test_iter1)) # 2540661600072
