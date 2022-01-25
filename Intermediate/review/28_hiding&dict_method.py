"""
ex1
"""

class person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __str__(self):
        return '{0}: {1}'.format(self.name, self.age)

def main():
    p = person('James', 22)
    print(p)
    p.age -= 1 # 실수 발생
    print(p)

main()

"""
ex2
"""


class person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self.age += a
    def __str__(self):
        return '{0}: {1}'.format(self.name, self.age)

def main():
    p = person('James', 22)
    p.add_age(1)
    print(p)

main()


"""
ex3
"""


class person:
    def __init__(self, n, a):
        self.name = n
        self.__age = a
    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self.__age += a
    def __str__(self):
        return '{0}: {1}'.format(self.name, self.__age)

def main():
    p = person('James', 22)
    print(p.name)
    #print(p.__age)

main()

"""
ex4
"""

class personperson:
    def __init__(self, n, a):
        self.name = n
        self.age = a

def main():
    x = personperson('James', 22)
    print(x.__dict__)
    x.gender = 'M'
    x.name = 'Mic'
    print(x.__dict__)

main()

"""
ex5
"""

class personperson:
    def __init__(self, n, a):
        self.name = n
        self.age = a

def main():
    x = personperson('James', 22)
    x.__dict__['name'] = 'doradora'
    x.__dict__['city'] = 'seoul'
    print(x.__dict__)

main()

"""
ex6
"""

class sample:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

def main():
    s = sample(10, 50)
    print(s.__dict__)

    print(s._sample__x)
    print(s._sample__y)

main()
