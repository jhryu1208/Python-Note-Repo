"""
dict basic
"""

dict1 = dict(a=1, b=2, c=3)
# 키가 존재할 때
dict1['a'] = 100 # 키값이 수정됨
print(dict1)

# 키가 존재하지 않을 때
dict1['d'] =100 # 키값이 추가됨
print(dict1)

print('\n')

dict2 = dict(a=1, b=2, c=3)

# 존재하는 키의 값을 참조할 때
dict2['a'] += 100
print(dict2)

# 존재하지 않은 키의 값을 참조할 때는 KeyError를 반환한다.
# 따라서 이와 같은 상황을 고려하여 처리를 미리 진행할 필요가 있다.
# 즉, 키가 존재할 때와 존재하지 않을 때의 상황 별 실행 코드를 구분할 필요가 있다.
try:
    dict2['d'] += 100
    print(dict2)
except KeyError:
    print('KeyError')

print('\n')

"""
키가 존재할 때와 존재하지 않을 때의 사전 대처 방법
"""

# 방법1) if~else
str = 'jihyun'

d = {}
for i in str:
    if i in d.keys():
        d[i] += 100
    else:
        d[i] = 999
print(d)

# 방법2) setdefault
str = 'jihyun'

d = dict(y=100)
return_list = []
for i in str:
    x = d.setdefault(i, 999)
    return_list.append(x)

print(return_list)
print(d)

# 방법3) defaultdict

from collections import defaultdict

str = 'jihyun'
d = defaultdict(int) # 참고로 int함수는 받는 인자가 없으면 0을 반환한다.
for i in str:
    d[i] += 100

print(d)
print(d.keys(), d.values())

# 함수 생성 이용
def return_0():
    return 0

str = 'jihyun'
d = defaultdict(return_0)
for i in str:
    d[i] += 100

print(d)
print(d.keys(), d.values())

# lambda 이용
str = 'jihyun'
d = defaultdict(lambda : 0)
for i in str:
    d[i] += 100

print(d)
print(d.keys(), d.values())
