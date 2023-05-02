import re

# match()와 search() 비교
'''
p = re.compile('[a-z]+')
m1 = p.match("afternoon")
print(m1)

m2 = p.match('2020 python')
print(m2)

s = p.search('2020 python')
print(s)
print(s.group())
'''
# findall()을 사용한 문자열 검색 - 리스트로 반환
'''
str = "Two is too"
m1 = re.findall("T[ow]o", str)
print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE)
print(m2)

m3 = re.findall("T[^w]o", str, re.IGNORECASE)
print(m3)
'''

# '*'와 '+'의 차이
'''
p = re.compile('ca*t')
m1 = re.findall(p, 'caat')
print(m1)
m2 = re.findall(p, 'ct')
print(m2)

p2 = re.compile('ca+t')
m3 = re.findall(p2, 'caat')
print(m3)
m4 = re.findall(p2, 'ct')
print(m4)
'''

# finditer()
'''
str = "123?45yy7890 hi 999 Hello"

m2 = re.finditer('[A-Za-z]+', str)
for i in m2:
    print(i)
'''

# match, search 객체의 메서드
'''
p = re.compile('[a-z]+')
m = p.match('hello')

print(m.group())
print(m.start())
print(m.end())
print(m.span())

p = re.compile('[a-z]+')
m = p.search('2023 hello')

print(m.group())
print(m.start())
print(m.end())
print(m.span())

str01 = "lee 010-1234-5678"
p = re.compile('(\w+)\s{1,2}\d+[-]\d+[-]\d+')
m = p.match(str01)
print(m)
print(m.group())
print(m.group(1)) # 소괄호 사용
'''
# 그룹핑된 문자열에 이름 붙이기
p = re.compile('(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
m = p.match('park 010-1234-5678')
print(m.group('name'))
print(m.group('phone'))

# sub() 메서드
p1 = re.compile('blue|red')
s = p1.sub('color', 'blue socks and red shoes')
print(s)

p2 = re.compile('(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')
s1 = p2.sub('\g<name>', 'park 010-3333-5555')
s2 = p2.sub('\g<phone>', 'park 010-3333-5555')
print(s1)
print(s2)

# 참조 번호 사용
data = '''
    kim 871212-1234567
    lee 770707-2345678
'''
# jumin = re.compile("(\d{6})[-]\d{7}")
jumin = re.compile("(\d+)[-]\d+")
print(jumin.sub('\g<1>-*******', data))


