"""
Set Type의 집합 연산
"""

A = {'a', 'b', 'c', 'd'}
B = {'b', 'd', 'e', 'f'}

# 차집합
print(A-B)
# 합집합
print(A|B)
# 교집합
print(A&B)
# 대칭차집합
print(A^B)

print('\n')

"""
set
"""

A = set(['a', 'c', 'd', 'f'])
B = {'e', 'f', 'g'}
C = set('fdca')
D = set() # 빈 set

print(A)
print(B)
print(C)
print(D)

"""
list 중복 제거
"""

t = [3, 3, 3, 7, 7, 'z', 'z']
t = list(set(t))
print(t)

print('\n')

"""
set (mutable), frozenset(immutable)
"""
os = {1, 2, 3, 4, 5}

os.add(6) # 6 추가
print(os)

os.discard(1) # 1 삭제
print(os)

os.update({7, 8, 9}) # {7, 8, 9} 원소 추가
print(os)

os &= {2, 4, 6, 8} # {2, 4, 6, 8}과 겹치는 원소만 남김
print(os)

os -= {2, 4} # {2, 4} 원소 삭제
print(os)

os ^= {1, 3, 6} # {1, 3, 6}와 합집합 이후 교집합 삭제
print(os)

"""
set comprehension
"""

s1 = {x for x in range(1, 11)}
print(s1)
