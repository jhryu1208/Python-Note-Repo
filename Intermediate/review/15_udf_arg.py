list = [1, 2, 3]
dict = dict(a=1, b=2, c=3)
str = 'abc'
tuple = dict.items()

"""
"""

def test(a, b, c):
    print(a, b, c, sep = ', ')

test(*list)
test(*str)
test(*dict) # Key가 매개변수에 전달된다.
test(**dict) # Value가 매개변수에 전달된다. 단, 키값과 함수인자이름이 동일해야함
test(*tuple)

"""
"""

def test1(*args):
    print(args)

test1(list)
test1(dict)
test1(str)

def test2(**args):
    print(args)

test2(a=1, b=2, c=3)

print('\n')

"""
"""

def test3(*args1, **args2):
    print(args1, args2)

test3()

test3(3)
test3(1, 2)
test3([1,2,3],[1,2,3])

test3(a=1)
test3(a=1, b=1)

test3(1, a=1)
test3(1, 2, 3, a=1, b=2)
test3([1, 2, 3], a=1, b=2, c=3)


def test4(a, *args1, **args2):
    print(a, args1, args2)

def test5(a, b, *args1, **args2):
    print(a, b, args1, args2)

test4(1, 2)
test5(1, 2)

print('\n')

try:
    test4(1)
except TypeError:
    print('Raise TypeError')

try:
    test4(c=1)
except TypeError:
    print('Raise TypeError')

try:
    test4(1, c=1)
except TypeError:
    print('Raise TypeError')

try:
    test5(1, c=1)
except TypeError:
    print('Raise TypeError')
