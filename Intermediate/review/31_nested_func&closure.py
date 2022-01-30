"""
ex1
"""

def maker(m):
    def inner(n):
        return m*n
    return inner

f1 = maker(2)
f2 = maker(3)
print(f1(7))
print(f2(7))

"""
ex2
"""

f3 = maker(101)
f4 = maker(75)

print(f3.__closure__[0].cell_contents)
print(f4.__closure__[0].cell_contents)
