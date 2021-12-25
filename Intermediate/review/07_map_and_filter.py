"""
map
"""

list1 = [1, 2, 3]
pow_2 = lambda x : pow(x, 2)

# map 사용X
rs1 = [pow_2(list1[0]), pow_2(list1[1]), pow_2(list1[2])]
rs2 = [pow_2(i) for i in list1]
print(rs1)
print(rs2)

# map 사용
map_rs3 = map(pow_2, list1) # 위의 코드보다 더 짧아짐
rs3 = list(map_rs3)
print(f'map_return_type : {type(map_rs3)}')
print(rs3)

"""
map (example1)
"""
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
func = lambda x, y : x*y

rs4 = list(map(func, ls1, ls2))
print(rs4)

"""
map (example2)
"""
str = 'this is example string object'
str_list = str.split(' ')
print(str_list)

func = lambda x : x[::-1]
rs5 = list(map(func, str_list))
print(rs5)


"""
filter(example1)
"""

# 짝수만 반환
ls1 = range(0, 11)
func1 = lambda x : x%2==0
rs1 = list(filter(func1, ls1))
print(rs1)

"""
filter(example2)
"""

# 3의 배수만 반환
ls2 = range(0, 11)
func2 = lambda x : x%3==0
rs2 = list(filter(func2, ls2))
print(rs2)

"""
filter(example3)
"""

# 1~10사이의 수를 제곱하여 3의 배수만 반환
ls3 = range(0, 11)
func3_1 = lambda x : pow(x, 2) # 제곱
func3_2 = lambda x : x%3==0 # 3의 배수만 반환
rs3 = list(filter(func3_2, map(func3_1, ls3)))
print(rs3)

# 하지만 위의 예제의 경우
# list comprehension을 사용하는 것이 더 간결하다.
# map과 filter가 동시에 사용되는 케이스에서는 list comprehension을 선호하도록 하자.
rs4 = [pow(i, 2) for i in ls3 if i%3==0]
print(rs4)
