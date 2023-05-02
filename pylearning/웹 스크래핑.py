# requests 모듈
import requests
from bs4 import BeautifulSoup
'''
url = "http://www.python.org"
response = requests.get(url)
print(response)
print(response.status_code)
html = response.text
#print(html)

url2 = "http://www.python.org/3"
response = requests.get(url2)
print(response)
print(response.status_code)

urls = ["http://www.python.org/", "http://www.daum.net/"]
filename = "robots.txt"
# print(urls[0] + filename)
for url in urls:
    url_path = url + filename
    print(url_path)
    response = requests.get(url_path)
    print(response)
'''

# html 태그 만들어 연습하기
"""
html_str = '''
<html>
    <head>
    </head>
    <body>
        <ul class='item'>
            <li>인공지능</li>
            <li>Big Data</li>
            <li>로봇</li>
        </ul>
    </body>
</html>
'''
soup = BeautifulSoup(html_str, "html.parser")
first_ul = soup.find('ul', attrs={'class':'item'})
# print(first_ul)
print(first_ul.text)

# 리스트에 저장
all_li = first_ul.findAll('li')
print(all_li)
# print(all_li[1].text)

for li in all_li:
    print(li.text)
"""

# Naver에서 필요한 정보 추출
"""
url = "http://www.naver.com"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

# print(html.head)
print(html.title)
print(html.title.name)
print(html.title.text)

find_div = html.find('div', attrs={'class':'service_area'})
#print(find_div)
first_a = find_div.find('a')
print(first_a.text)

all_a = find_div.findAll('a')
# print(all_a[0])
print(all_a[1].text)

# naver 메뉴 가져오기
menu_ul = html.find('ul', attrs={'class':'list_nav type_fix'})
menu_lis = menu_ul.findAll('li')
# print(menu_lis)
menu_all_a = menu_ul.findAll('a')
# for menu_a in menu_all_a:
#     print(menu_a)
print(menu_all_a[1].text)
"""

# Naver 증권 > 시장지표 > 환전 고시 환율
url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

ul = html.find('ul', attrs={'class':'data_lst'})
#print(ul)
# 첫번째 미국만 추출하기
li = ul.find('li')
# print(li)
exchange = li.find('span', attrs={'class':'blind'})
print(exchange)
value = li.find('span', attrs={'class':'value'})
print(value)
print(exchange.text, ':', value.text)

# 전체 횐율 추출하기
all_li = ul.findAll('li')
# print(all_li)
for li in all_li:
    exchange = li.find('span', attrs={'class':'blind'})
    value = li.find('span', attrs={'class':'value'})
    # print(exchange.text, ':', value.text)
    print(exchange.text.split(' ')[-1], ':', value.text)




























































