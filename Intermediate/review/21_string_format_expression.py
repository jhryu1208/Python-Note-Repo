
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


print('\n')
####################################################################


fs0 = '{0}...{1}...{2}'
fs1 = '{2}...{0}...{1}'

ms0 = fs0.format('Robot', 125, 'Box')
ms1 = fs1.format('Robot', 125, 'Box')
print(ms0)
print(ms1)

fs2 = '{}...{}...{}'
ms2 = fs2.format('첫', '둘', '셋')
print(ms2)

fs3 = '{여기0}...{여기1}...{여기2}'
ms3 = fs3.format(여기0='A', 여기1='B', 여기2 = 'C')
print(ms3)

my = ['A', 'B', 'C']

fs4 = '{}...{}...{}'
ms4 = fs4.format(*my)
print(ms4)


info = [('철수', '남'), ('유리', '여')]
fs5 = \
"""
{0[0]}는 {0[1]}자다.
{1[0]}는 {1[1]}자다.
"""
ms5 = fs5.format(*info)
print(ms5)

info1 = [{'name':'철수', 'sex' : '남'}, {'name':'유리', 'sex' : '여'}]
fs6 = \
"""
{0[name]}는 {0[sex]}자다.
{1[name]}은 {1[sex]}자다.
"""
ms6 = fs6.format(*info1)
print(ms6)

print('\n')

# 파이썬이 '실수'라고 판단 및 출력
print('{0}'.format(3.14))

# 프로그래머가 "실수"라고 직접 알려주는 것
print('{0:f}'.format(3.14))

# 프로그래머가 "정수"라고 직접 알려주는 것
# 실수를 기입할 경우 아무것도 반환하지 않는다.
print('{0:d}'.format(3))


print('{0:.4f}'.format(3.14))
print('{0:.2f}'.format(2.14523))

print('{0:10.4f}'.format(3.14))
print('{0:<10.4f}'.format(3.14))
print('{0:>10.4f}'.format(3.14))
print('{0:^10.4f}'.format(3.14))

print('{0:+10.4f}'.format(3.14))
print('{0:+10.4f}'.format(-3.14))


print('{0:&<10.4f}'.format(3.14))
print('{0:+>10.4f}'.format(3.14))
print('{0:가^10.4f}'.format(3.14))
