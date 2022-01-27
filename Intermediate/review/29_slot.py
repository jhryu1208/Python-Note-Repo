"""
객체의 변수를 외부 딕셔너리에 저장하는 경우
"""

class point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)

def main():
    p1 = point3d(1, 1, 1)
    p2 = point3d(2, 2, 2)
    print(p1)
    print(p2)

main()

"""
__slot__을 활용한 객체 내에서 직접 참조
"""

class point3d:
    __slot__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)

def main():
    p1 = point3d(1, 1, 1)
    p2 = point3d(2, 2, 2)
    print(p1)
    print(p2)

main()
