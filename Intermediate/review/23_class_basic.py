"""
ex1
"""

class Simple:
    def seti(self, i):
        self.i = i
    def geti(self):
        print(self.i)

s1 = Simple()
s1.seti(200)
s1.geti()

"""
ex2
"""

class Simple:
    def __init__(self):
        self.i = 0
    def seti(self, i):
        self.i = i
    def geti(self):
        print(self.i)


s0 = Simple()
s0.geti()

s1 = Simple()
s1.seti(25)
s1.geti()

"""
ex3
"""

class sosimple:
    def geti(self):
        print(self.i)

ss = sosimple()
ss.i = 27 # 이 순간 변수 ss에 담긴 객체에 i라는 변수가 생성된다.
ss.geti()

ss.add_method = lambda : print('hi')
ss.add_method()

# 클래스 객체 내의 메소드와 변수는 삭제 가능하다.
del ss.i
del ss.add_method

"""
ex4
"""

class simple:
    def __init__(self, i):
        self.i = i
    def geti(self):
        return self.i

simple.n = 100

s1 = simple(3)
print(s1.n, s1.geti(), sep = ', ')
s2 = simple(5)
print(s1.n, s2.geti(), sep = ', ')

"""
ex5
"""

print(type)
print(type([1, 2]))
print(type(list))

class sample():
    pass

print(type(simple))
