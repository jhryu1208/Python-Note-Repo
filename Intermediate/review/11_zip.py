"""
zip
"""
z0 = zip(['a', 'b', 'c'], [1, 2, 3]) # 두 개의 리스트에 저장된 값들을 조합
for i in z0:
    print(i, type(i))

z1 = zip(('a', 'b', 'c'), (1, 2, 3)) # 두 개의 튜플에 저장된 값들의 조합
for i in z1:
    print(i, type(i))

z2 = zip(['a', 'b', 'c'], (1, 2, 3)) # 리스트와 튜플 조합
for i in z2:
    print(i, type(i))


z3 = zip(['a', 'b', 'c'], [1, 2, 3])
print(next(z3))
print(next(z3))
print(next(z3))
try :
    print(next(z3))
except StopIteration:
    print("StopIteration")

# zip으로 생성한 튜플들을 리스트, 튜플, 그리고 딕셔너리에 담을 수 있다.
z4 = zip(['a', 'b', 'c'], [1, 2, 3])
l = list(z4)
z5 = zip('abc', '123')
t = tuple(z5)
z6 = zip('QWE', [1, 2, 3])
d = dict(z6)
print(l)
print(t)
print(d)

# 셋 이상의 조합
z7 = zip('ABC', [1, 2, 3], ('가', '나', '다'))
print(list(z7))
