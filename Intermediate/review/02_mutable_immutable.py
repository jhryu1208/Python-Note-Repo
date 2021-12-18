"""
- 수정이 가능한 객체 : mutable 객체 (ex. list, dict)
- 수정이 불가능한 객체 : immutable 객체 (ex. tuple, string)
"""

"""
list의 경우 mutable한 객체이기 때문에,
값을 수정하여도 리스트의 주소가 변경되지 않는다.
"""
list1 = [1, 2, 3]
print(f'result : {list1}, address : {id(list1)}') # list1의 주소 2751202546056
list1 += [4, 5]
print(f'result : {list1}, address : {id(list1)}') # list1의 주소 2751202546056

print('\n')

"""
반면 tuple의 경우 immutable 객체이기 때문에,
값을 수정할 경우 "새로운 tuple이 생성되어 주소가 변경"되는 것을 확인할 수 있다.
"""
tuple1 = (1, 2, 3)
print(f'result : {tuple1}, address : {id(tuple1)}') # tuple1의 주소 1339091106616
tuple1 += (4, 5)
print(f'result : {tuple1}, address : {id(tuple1)}') # tuple1의 주소 1339090787688

print('\n')

"""
아래의 함수에 의해서
list의 경우 원본 값이 변경되었으나,
tuple의 경우 원본 값이 변경되지 않았다.
왜냐하면, 함수내 변수 m의 값은 새로 연산된 덧셈 결과가 반영되었기 때문이며,
기존의 tuple값을 가진 t의 경우 영향을 받지 않았다. (함수에 input되기 전과 후의 주소 값이 모두 동일)
"""
def add_last(m, n):
    m += n

list2 = [1, 2, 3]
add_last(list2, [4, 5])
print(list2) # [1, 2, 3, 4, 5] 원본 값이 변경되었다.

tuple2 = (1, 2, 3)
print(id(tuple2))
add_last(tuple2, (4, 5))
print(tuple2) # (1, 2, 3) 원본 값이 변경되지 않았다.
print(id(tuple2))

print('\n')

"""
따라서, tuple에 값을 추가한 결과를 얻는 함수의 경우 다음과 같이 구성해야한다.
"""
def add_tuple(m, n):
    m += n
    return m # 새로 연산된 튜플 결과가 저장된 m을 리턴시킨다.

tuple3 = (1, 2, 3)
print(id(tuple3))
result_tuple = add_tuple(tuple3, (4, 5))
print(result_tuple)


print('\n')

"""
혹은, list를 다룰 때 원본 값이 변경되는 것을 원치 않을 때는 list의 copy객체를 이용하자.
(하지만, 위에서 확인했듯이 tuple을 다룰 때에는 굳이 copy시킬 필요가 없다.)
"""
def min_max(m):
    copy_m = list(m)
    copy_m.sort() # 복사된 list의 값만 변경되며, 원본 list의 경우 수정되지 않는다.
    return copy_m[0], copy_m[-1]

list3 = [1, 2, 3]
print(f'함수 결과 : {min_max(list3)}, \n원본 리스트 : {list3}')
