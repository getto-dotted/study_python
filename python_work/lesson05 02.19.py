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

    response2 = requests.get(url+a)
    assert response2.status_code is 200
    dom2 = BeautifulSoup(response2.content, "html.parser")

    headline2 = dom2.select("div.content")
    headline2_list = headline2[0].find_all("div", class_="_article_body_contents")
    f = open('크롤링{}.txt'.format(i), 'w', encoding="utf8")
    for j, element2 in enumerate(headline2_list):

        print(element2.text.replace('. ','. \n'))
        f.write(element2.text.replace('. ','. \n')+ "\n")
    f.close()



f = open('크롤링3.txt', 'r', encoding="utf8")
lines = f.readlines()
for line in lines:
    line = line[:-1] #line.strip() 끝에 붙은 \n을 뺀다
    print(line)
f.close()

