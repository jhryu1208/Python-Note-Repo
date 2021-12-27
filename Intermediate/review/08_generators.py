"""
Generator Function
"""

def gen_num():
    print('first_number')
    yield 1
    print('second number')
    yield 2
    print('third number')
    yield 3

gen = gen_num() # generator 객체 생성
print(type(gen))

print('\n')

print(f'첫 번째 next함수 호출 : {next(gen)}')
print(f'두 번째 next함수 호출 : {next(gen)}')
print(f'세 번째 next함수 호출 : {next(gen)}')

print('\n')

print(f'첫 번째 next함수 호출 : {next(gen_num())}')
print(f'두 번째 next함수 호출 : {next(gen_num())}')
print(f'세 번째 next함수 호출 : {next(gen_num())}')

print('\n')

"""
lazy evaluation
"""

def gen_for():
    for i in [1, 2, 3]:
        yield i

g = gen_for()

while True:
    try:
        print(next(g))
    except StopIteration:
        print('StopIteration raised')
        break

print('\n')

"""
advantage of generator
"""

from sys import getsizeof

list_example = list(range(1, 11))

# generator 함수를 사용하지 않은 경우
def normal_func(list):
    result = []
    for i in list:
        result.append(pow(i, 2))
    return result

re_ls0 = normal_func(list_example)
for i in re_ls0:
    print(i, end = ' ')

print(f'\n사용 메모리 사이즈 : {getsizeof(re_ls0)}') # 192

# generator 함수를 사용한 경우
def gen_func(list):
    for i in list:
        yield pow(i, 2)

re_ls1 = gen_func(list_example)
for i in re_ls1:
    print(i, end = ' ')

print(f'\n사용 메모리 사이즈 : {getsizeof(re_ls1)}') # 120

print('\n')

"""
yield from
"""

def gen_nums():
    for i in [1, 2, 3, 4]:
        yield i

g = gen_nums()
while True:
    try:
        print(next(g))
    except StopIteration:
        print('StopIteration raised')
        break

# shorthand
def short_gen_nums():
    yield from [1, 2, 3, 4]

g = gen_nums()
while True:
    try:
        print(next(g))
    except StopIteration:
        print('StopIteration raised')
        break

"""


"""
