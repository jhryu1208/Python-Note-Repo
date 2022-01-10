"""
sort method basic
"""

ns = [3, 1, 4, 2]

ns.sort() # 오름차순, 반환 값은 None이며, 원본 값
print(ns)

ns.sort(reverse=True) # 내림차순, 반환 값은 None이다.
print(ns)

"""
sort method key param
"""

ns = [('B', 3), ('C', 5), ('A', 2)]

first_index_order = lambda t : t[0]
ns.sort(key = first_index_order)
print(ns)

second_index_order = lambda t : t[1]
ns.sort(key = second_index_order)
print(ns)

ns.sort(key = second_index_order, reverse = True)
print(ns)

"""
sort method key param ex1
"""

ns = [('apple', 33), ('mangoooo', 50), ('orangeeeeeeee', 100)]

sort_by_len = lambda x : len(x)
ns.sort(key = sort_by_len)

print(ns)


"""
sort method key param ex2
"""

ns = [(100, 200), (1, 20), (10000, 50000)]

sort_by_sum = lambda x : x[0]+x[1]
ns.sort(key = sort_by_sum, reverse = True)

print(ns)


"""
sorted function
"""

tup = (('mangoooo', 33), ('apple', 50), ('ora', 100))

sort_by_len = lambda x : len(x)
result = sorted(tup, key = sort_by_len, reverse = True)
print(result)
print(tuple(result))
