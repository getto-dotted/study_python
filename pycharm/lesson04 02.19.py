import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/")
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

headline = dom.select("ul.hdline_article_list")

hdline_list = headline[0].find_all("div", class_="hdline_article_tit")

#결과를 텍스트 파일로 저장하기
# 파일명, 모드, 인코딩
f = open('크롤링.txt', 'w')
for i, element in enumerate(hdline_list):
    text1 = element.find("a").text.strip()
    text2 = element.find("a")['href']
    f.write(text1)
    f.write("\n")
    f.write(text2)
f.close()

f = open('크롤링.txt', 'r')
for line in f:
    print(line)
f.close()

f = open('크롤링2.txt', 'w', encoding="utf8")
for i, element in enumerate(hdline_list):
    a = element.find("a")
    data = "{}|{}|{}".format(i, a.text.strip(), a['href'])
    f.write(data + "\n")
f.close()

f = open('크롤링2.txt', 'r', encoding="utf8")
lines = f.readlines()
for  line in lines:
    line = line[:-1] #line.strip() 끝에 붙은 \n을 뺀다
    li = line.split("|")
    print(li[0], li[1])
    print(">>>>>", li[2])
f.close()

