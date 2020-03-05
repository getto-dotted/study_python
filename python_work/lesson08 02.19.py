import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
response = requests.get(url)
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

headline = dom.select("ul.hdline_article_list")

hdline_list = headline[0].find_all("div", class_="hdline_article_tit")

#결과를 텍스트 파일로 저장하기
# 파일명, 모드, 인코딩


for i, element in enumerate(hdline_list):
    a = element.find("a")['href'][1:]

    response = requests.get(url+a)
    assert response.status_code is 200
    dom2 = BeautifulSoup(response.content, "html.parser")

    headline2 = dom2.select("div.content")
    headline2_list = headline2[0].find_all("div", class_="_article_body_contents")

    for j, element2 in enumerate(headline2_list):
        src = element2.find('img')['src'][:-10]
        print(src)
        response = requests.get(src)
        assert response.status_code is 200
        with open("크롤링사진{}{}.jpg".format(str(i),str(j)), "wb") as f:
            f.write(response.content)