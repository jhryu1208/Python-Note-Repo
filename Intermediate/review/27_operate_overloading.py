"""
ex1
"""


class simple1:
    def __init__(self, a):
        self.a = a

x = simple1(10)

try :
    x + 100
    print(x.a)
except TypeError:
    print('error raised')

class simple2:
    def __init__(self, a):
        self.a = a
    def __add__(self, b):
        self.a += b

x = simple2(10)

try :
    x + 100
    print(x.a)
except TypeError:
    print('error raised')

"""
ex2
"""

x = 100
y = 200
z = x + y

print(x, y, z)



"""
ex3
"""

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return vector(self.x+o.x, self.y+o.y)
    def __call__(self):
        return f'vector({self.x}, {self.y})'

v1 = vector(1, 1)
v2 = vector(5, 5)
v3 = v1+v2
print(v3())


"""
ex4
"""

class test1:
    def __init__(self, a):
        self.a = a

x = test1(10)
print(x)

class test2:
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f'test({self.a})'

x = test2(10)
print(x)

"""
ex5
"""
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return vector(self.x+o.x, self.y+o.y)
    def __str__(self):
        return f'vector({self.x}, {self.y})'

v1 = vector(1, 1)
v2 = vector(5, 5)
v3 = v1+v2
print(v3)

"""
ex6
"""

x1 = 10
before_id1 = id(x1)
y1 = 20
x1 += y1
after_id1 = id(x1)
print(before_id1 == after_id1)

x2 = [10]
before_id2 = id(x2)
y2 = [20]
x2 += y2
after_id2 = id(x2)
print(before_id2 == after_id2)

"""
ex7
"""
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, o):
        return vector(self.x+o.x, self.y+o.y)
    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        #return vector(self.x, self.y)
    def __str__(self):
        return f'vector({self.x}, {self.y})'

v1 = vector(1, 1)
v2 = vector(5, 5)
v1 += v2
print(v1)
