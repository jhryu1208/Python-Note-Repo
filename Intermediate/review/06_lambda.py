"""
함수 = 객체
"""
def func1(n):
    return n

def func2():
    print('hi')

print(type(func1)) # <class 'function'>
print(type(func2)) # <class 'function'>

# ================================================ #

def say1():
    print('function is also object!')

def caller(func):
    func() # func를 통해 전달된 함수를 호추

caller(say1)

# ================================================ #

def out_func(a):
    def in_func(b):
        return a**b
    return in_func

outfunc = out_func(2) # a**2
print(type(outfunc))
print(outfunc(4)) # 4**2

# ================================================ #
