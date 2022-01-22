"""
ex1
"""

class simple:
    pass

s = simple()
print(isinstance(s, simple))

print(isinstance([1,2], list))

"""
ex2
"""

class A:
    pass

class B(A):
    pass

class C(B):
    pass

s = C()
print(isinstance(s, C))
print(isinstance(s, B))
print(isinstance(s, A))


"""
ex3
"""

class simple:
    pass

print(isinstance(simple, object))
print(isinstance([1, 2], object))
print(isinstance(type, object))
