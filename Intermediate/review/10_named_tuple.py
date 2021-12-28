"""
named tuple
"""

from collections import namedtuple

tri = namedtuple('Triangle', ['bottom', 'height']) # 네임드 튜플 클래스 생성
t = tri(12, 15)

print(type(tri)) # <class 'type'>
print(type(t)) # <class '__main__.Triangle'>
print(t[0], t[1]) # 12 15
print(t.bottom, t.height) # 12 15

#t[0]= 15 클래스 이름을 포함한 에러 반환

"""
named tuple unpacking
"""

t =  tri(50, 90)
a, b = t # unpacking
print(a, b)


def return_func(a, b):
    print(a, b)
return_func(*t)
