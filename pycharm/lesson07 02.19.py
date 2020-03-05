import requests
from bs4 import BeautifulSoup
from SearchList import getSearchList

url = "https://news.naver.com/"
selector = "ul.hdline_article_list"

response = requests.get(url)
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")
page_list = dom.select(selector)

url_classes = "hdline_article_tit"

div_list = page_list[0].find_all('div', class_= url_classes)


for i, element in enumerate(div_list):
    tagname = "div#articleBodyContents img"

    imgTags = getSearchList(url + element.find("a")["href"], tagname) #신문기사 본문에 있는 사진만 가져오기

    for j, img in enumerate(imgTags):

        #src = img.get("src")
        src = img['src']

        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        print(src)
        print(type(src))
        print(src[:src.index("?")])
        print('-' * 50)

        with open("크롤링사진{}{}.jpg".format(str(i),str(j)), "wb") as fp:
            fp.write(response.content)