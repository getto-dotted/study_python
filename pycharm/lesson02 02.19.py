"""
원하는 데이터 추출하기
<메소드들>
find_all() : 원하는 특정 태그들을 리스트로 모두 반환(id, class, 속성, limit기능)
find() : 원하는 태그 하나를 반환한다.
select() : CSS 선택자(Selector)를 그대로 사용한다.(사용법이 jQuery와 유사하다)
extract() : 추출한 결과에서 특정 태그를 제거한다.

"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/")
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

headline = dom.select("ul.hdline_article_list")
#select()의 결과는 리스트 타입이다
#print(headline[0])
hdline_list = headline[0].find_all("div", class_="hdline_article_tit")
#print(hdline_list)
for i, element in enumerate(hdline_list):
    print(i, element.find("a").text.strip())
    print(">>>>>", element.find("a")['href'])
    #print(">>>>>", element.find("a").get('href'))