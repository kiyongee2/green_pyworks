# requests 모듈
"""
import requests

url = "https://www.python.org"
response = requests.get(url)
#print(response)
html = response.text
print(html)
"""

# BeautifulSoup
"""
from bs4 import BeautifulSoup

html_str = '''
<html>
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
print(first_ul)
print(first_ul.text)

all_li = first_ul.findAll('li')
print(all_li)
print(all_li[1].text)

for li in all_li:
    print(li.text)

"""

# Naver에서 필요한 정보 추출
import requests
from bs4 import BeautifulSoup
"""
url = "http://www.naver.com"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

find_div = html.find('div', attrs={'class':'service_area'})
#print(find_div)
all_a = find_div.findAll('a')
print(all_a[0].text)
first_a = find_div.find('a')
print(first_a.text)
"""

# Naver 증권 > 시장지표 > 환전 고시 환율
url = "https://finance.naver.com/marketindex"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

ul = html.find('ul', attrs={'class':'data_lst'})
#print(ul)
# 첫번째 미국만 추출하기
li = ul.find('li')
#print(li)
#exchange = li.find('span', attrs={'class':'blind'})
#print(exchange)
#value = li.find('span', attrs={'class':'value'})
#print(value)
#print(exchange.text, ':', value.text)

# 전체 횐율 추출하기
all_li = ul.findAll('li')
#print(all_li)
for li in all_li:
    exchange = li.find('span', attrs={'class':'blind'})
    value = li.find('span', attrs={'class':'value'})
    #print(exchange.text, ':', value.text)
    print(exchange.text.split(' ')[-1], ':', value.text)





























































