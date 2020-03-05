import time

import requests
from bs4 import BeautifulSoup



#1초마다 한번씩 갱신 시키기
for cnt in range(5):
    response = requests.get("https://news.naver.com/")
    assert response.status_code is 200

    dom = BeautifulSoup(response.content, "html.parser")

    headline = dom.select("ul.hdline_article_list")

    hdline_list = headline[0].find_all("div", class_="hdline_article_tit")

    for i, element in enumerate(hdline_list):
        print(i, element.find("a").text.strip())
        print(">>>>>", element.find("a")['href'])


    print("{:-^50}".format("5초에 한번씩 갱신한다"))

    time.sleep(5)
