
"""
저장 순서가 달라도
내용물이 동일하기에 TRUE반환
"""

dict_a = dict(a=1, b=2, c=3)
dict_b = dict(c=3, a=1, b=2)
print(dict_a == dict_b) # True


"""
OrderedDict 객체의 경우에는
비교에 있어서 저장순서도 중요하다.
"""

from collections import OrderedDict

dict_a = OrderedDict(a=1, b=2, c=3)
dict_b = OrderedDict(c=3, a=1, b=2)
print(dict_a == dict_b) # False


"""
OrderedDict 순서 변경
"""

from collections import OrderedDict

print_dict = lambda dict_obj : [print(i, end = ', ') for i in dict_obj.items()]

dict_c = OrderedDict(a=1, b=2, c=3)
print_dict(dict_c)

print('\n')

dict_c.move_to_end('b')
print_dict(dict_c)

print('\n')

dict_c.move_to_end('b', last = False)
print_dict(dict_c)
