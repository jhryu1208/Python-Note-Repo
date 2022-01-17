
s0 = 'My friend %s is %d years old and %fcm tall' % ('Jung', 22, 178.5)
print(s0)

s1 = 'My friend %(name)s is %(age)d years old and %(tall)fcm tall' % {'name' : 'Jung', 'age' : 22, 'tall' : 178.5}
print(s1)

# .precision
print('result : %f' % 3.14)
print('result : %.3f' % 3.14)
print('result : %.2f' % 3.14)

# width
print(('result:%7.f' % 3.14).replace(' ', '#'))
print(('result:%10.3f' % 3.14).replace(' ', '#'))
print(('result: %11.2f' % 3.14).replace(' ', '#'))

print('result:%07.f' % 3.14)
print('result:%010.3f' % 3.14)
print('result: %011.2f' % 3.14)

print(('result:%-7.f' % 3.14).replace(' ', '#'))
print(('result:%-10.3f' % 3.14).replace(' ', '#'))
print(('result: %-11.2f' % 3.14).replace(' ', '#'))

a=3
b=-3

print('num : %+d' % a)
print('num : %+d' % b)
