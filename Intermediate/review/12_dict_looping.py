"""
dict basic
"""

d = dict([('a', 1), ('b', 2), ('c', 3)])
for k in d.keys():
    print(k, end  = ' ')

print('\n')

for k, v in d.items():
    print(f'key : {k}, value : {v}')

print('\n')

"""
view
"""

d = dict(a=1, b=1, c=1)
v0 = d.items()
for k in v0:
    print(k, end = ' ') # ('a', 1) ('b', 1) ('c', 1)

d['a'] += 5
d['b'] -= 5
print('\n')

for k in v0:
    print(k, end = '') # ('a', 6)('b', -4)('c', 1)

print('\n')

"""
dict comprehension
"""

d1 = dict(a=1, b=2, c=3)
d2 = {k:v*2 for k, v in d1.items()}
d3 = {k:v*2 for k, v in d1.items()}
print(d1)
print(d2)
print(d3)

d4 = {k:v*2 for k, v in d1.items() if v%2==0}
d5 = {k:v*3 for k, v in d1.items() if k!='b'}
print(d4)
print(d5)

kd = ['a', 'b', 'c']
vd = [1, 2, 3]
d6 = {k:v for k, v in zip(kd, vd)}
print(d6)
