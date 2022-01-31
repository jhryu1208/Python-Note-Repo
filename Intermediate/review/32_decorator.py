
"""
ex1-1
"""

def smile():
    print('^_^')

def confused():
    print('@_@')

smile()
confused()

print()

"""
ex1-2
"""

def deco(func): # 데코레이터 함수, 줄여서 데코레이터라고함
    def df():
        print('emoticon!') # 추가된 기능
        func()             # 원래 갖고 있던 기능
        print('emoticon!\n') # 추가된 기능
    return df              # 보강된 기능의 함수를 반환

smile = deco(smile)
confused = deco(confused)
smile() # 기능이 보강된 smile 함수 호출
confused()

"""
ex2
"""

def adder2(n1, n2):
    return n1+n2

def adder3(n1, n2, n3):
    return n1+n2+n3

def adder_deco(func):
    def ad(*args):
        print(*args, sep = '+', end = ' ')
        print('= {0}'.format(func(*args)))
    return ad

adder2 = adder_deco(adder2)
adder2(10,4)

adder3 = adder_deco(adder3)
adder3(1, 2, 3)

"""
ex3
"""

def adder_deco(func):
    def ad(*args):
        print(*args, sep = '+', end = ' ')
        print('= {0}'.format(func(*args)))
    return ad

@adder_deco
def adder2(n1, n2):
    return n1+n2

@adder_deco
def adder3(n1, n2, n3):
    return n1+n2+n3

def main():
    adder2(10,4)
    adder3(1, 2, 3)

main()

"""
ex4
"""

def deco1(func):
    def inner():
        print('deco1')
        func()
    return inner

def deco2(func):
    def inner():
        print('deco2')
        func()
    return inner


@deco1
@deco2
def simple():
    print('simple')

def main():
    simple()

main()
