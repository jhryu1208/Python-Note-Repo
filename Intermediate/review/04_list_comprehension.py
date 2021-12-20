
"""
1. 기본 list comprehension
"""
r1 = [1, 2, 3, 4, 5]

# 일반 for loop
r2_0 = []
for i in r1:
    r2_0.append(i*10)
print(r2_0)

# list comprehension
r2_1 = [i*10 for i in r1]
print(r2_1)

"""
2. 조건 필터 추가
"""
# 일반 for loop
r3_0 = []
for i in r1:
    if i%2 ==0:
        r3_0.append(i)
print(r3_0)

# list comprehension
r3_1 = [i for i in r1 if i%2==0]
print(r3_1)

"""
3. 중첩 list comprehension
"""

r1 = ['a', 'b', 'c']
r2 = ['1', '2', '3']

# r1과 r2의 요소로 이루어질 수 있는 모든 조합을 생성
r3_0 = []
for p in r1:
    for q in r2:
        r3_0.append(p+q)
print(r3_0)

# list comprehension
r3_1 = [p+q for p in r1 for q in r2]
print(r3_1)

"""
4. 중첩 list comprehension + 조건 필터
"""
# 마지막 for문에 if절 추가
a0 = []
for p in range(2, 10):
    for q in range(1, 10):
        if q%2==0:
            a0.append(p*q)
print(a0)

a1 = [p*q for p in range(2, 10) for q in range(1, 10) if q%2==0]
print(a1)


# for문 사이에 if절 추가
b0 = []
for p in range(2, 10):
    if p%2==0:
        for q in range(1, 10):
            b0.append(p*q)
print(b0)

b1 = [p*q for p in range(2, 10) if p%2==0 for q in range(1, 10)]
print(b1)


# 마지막 for문과 for문 사이에 모두 if절 추가
c0 = []
for p in range(2, 10):
    if p%2==0:
        for q in range(1, 10):
            if q%2==0:
                c0.append(p*q)
print(c0)

c1 = [p*q for p in range(2, 10) if p%2==0 for q in range(1, 10) if q%2==0]
print(c1)
