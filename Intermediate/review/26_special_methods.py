"""
ex1
"""

t = (1, 2, 3)
print(len(t))
print(t.__len__())

print(iter(t))
print(t.__iter__())

print(str(t))
print(t.__str__())


"""
ex2
"""

class simple:
    def __init__(self, id):
        print('객체가 생성됨')
        self.id = id
    def __len__(self):
        print('len함수가 사용됨')
        return len(self.id)
    def __str__(self):
        print('str함수가 사용됨')
        return '사실은 월요일!'

s = simple('오늘은 금요일')

result0 = len(s)
print(result0)

result1 = str(s)
print(result1)

result2 = len('아무 일도 없지롱')
print(result2)
