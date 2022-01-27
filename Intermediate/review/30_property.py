"""
ex1
"""
class natural:
    def __init__(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n

    def getn(self):
        """
        값을 꺼내는 기능을 하는 메소드를
        보편적으로 getter라고한다.
        """
        return self.__n

    def setn(self, n):
        """
        값을 수정하는 기능의 메소드를
        보편적으로 setter라고 한다.
        """
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n


"""
ex2
"""
class natural:
    def __init__(self, n):
        """
        setn 메소드 호출로 중복된 코드를 대신하였다.
        """
        self.setn(n)

    def getn(self):
        return self.__n

    def setn(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n

def main():
    n1 = natural(1)
    n2 = natural(2)
    n3 = natural(3)
    n1.setn(n2.getn()+n3.getn()) # n1을 n2+n3로 수정하고자함, 하지만 메소드의 호출로인해 n1 = n2+n3보다 복잡해보임
    print(n1.getn())

main()

"""
ex3
"""

class natural:
    def __init__(self, n):
        self.setn(n)
    def getn(self):
        return self.__n
    def setn(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n

    a = property(getn, setn) # property라는 객체를 생성해서 n에 저장

def main():
    n1 = natural(1)
    n2 = natural(2)
    n3 = natural(3)
    n1.a = n2.a + n3.a
    print(n1.a)

main()

"""
ex4
"""

class natural:
    def __init__(self, n):
        self.setn(n)
    p=property() # property객체 생성

    def getn(self):
        return self.__n
    # get메소드를 getter로 등록
    p = p.getter(getn)

    def setn(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n
    # setn메소드를 setter로 등록
    p = p.setter(setn)

"""
ex5
"""

class natural:
    def __init__(self, n):
        self.p = n

    @property
    def p(self):
        return self.__n

    @p.setter
    def p(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n


def main():
    n1 = natural(1)
    n2 = natural(2)
    n3 = natural(3)
    n1.p = n2.p + n3.p
    print(n1.p)

main()
