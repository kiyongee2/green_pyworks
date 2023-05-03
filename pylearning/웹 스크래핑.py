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

# find(), findAll() 사용
"""
ul = html.find('ul', attrs={'class':'data_lst'})
#print(ul)
# 첫번째 미국만 추출하기
first_li = ul.find('li')
# print(li)
exchange = first_li.find('span', attrs={'class':'blind'})
print(exchange)
value = first_li.find('span', attrs={'class':'value'})
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
"""
'''
# select(), select_one() 사용
ul = html.select_one('ul.data_lst')
# print(ul)
first_li = ul.select_one('li.on') # USD만 검색
# print(first_ul)
exchange = first_li.select_one('span.blind')
print(exchange.string)
value = first_li.select_one('span.value')
print(value.string)
print(exchange.string, ':', value.string)

all_li = ul.select('ul.data_lst li')
# print(all_li)

for li in all_li:
    exchange = li.select_one('span.blind')
    value = li.select_one('span.value')
    # print(exchange.string, ':', value.string)
    print(exchange.string.split(' ')[-1], ':', value.string)
'''

# 주식 정보
# 주식 1 종목
"""
def getcontent():
    url = 'https://finance.naver.com/item/main.naver?code=086520'
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

content = getcontent()
today = content.find('div', attrs={'class':'today'})
# print(today)
price = today.find('span', attrs={'class':'blind'})
print(price.text)
print(f'에코프로 주가 : {price.text}원')

# 주식 여러 종목
def getcontent(item_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + item_code
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

def getprice(item_code):
    content = getcontent(item_code)
    today = content.find('div', attrs={'class': 'today'})
    price = today.find('span', attrs={'class': 'blind'})
    return price

에코프로 = getprice('086520')
네이버 = getprice('035420')
NCSOFT = getprice('036570')

print(f'에코프로 주가 : {에코프로.text}원')
print(f'에코프로 주가 : {네이버.text}원')
print(f'에코프로 주가 : {NCSOFT.text}원')
"""

# 사진 가져오기(서울 지하철- 위키디피아)
url = 'https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# print(html.head)
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# 지하철 사진 경로
target_img = soup.find('img',
    attrs={'alt':'Seoul Metro 2000 series train on Line 2'})
print(target_img)

# 소스 사진 읽기
target_img_src = target_img.get('src')
print("이미지 경로:", target_img_src)

target_img_response = requests.get('http:' + target_img_src)
print(target_img_response)

# 바이너리 파일 모드로 쓰기
with open('./output/train.jpg', 'wb') as f:
    f.write(target_img_response.content) # 이미지: content
    print("이미지 파일로 저장했습니다.")























































