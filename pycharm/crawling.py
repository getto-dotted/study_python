from SearchList import getSearchList
import requests
from bs4 import BeautifulSoup
from Tools import replaceSRC
import json


search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')

savepath = 'E:\\node_work2\\public\\news\\'

newsList = []

for i, element in enumerate(div_list):

    newsObj ={}
    newsLink = "https://news.naver.com"
    newsUrl = newsLink + element.find("a")["href"]
    newsTit = element.find("a").text.strip()

    imgTags = getSearchList(newsUrl, "div#articleBodyContents img") #신문기사 본문에 있는 사진만 가져오기
    newsContents = getSearchList(newsUrl, "div#articleBodyContents")[0]

    srcList = []
    for j, img in enumerate(imgTags):
        src = img.get("src")
        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        imgName = "tmp_img" + str(i) + str(j) + ".jpg"
        srcList.append("news\\"+imgName)
        with open(savepath+imgName, "wb") as fp:
            fp.write(response.content)

    newsContents = replaceSRC(str(newsContents), srcList)
    contentsFile = "newsContent" + str(i)  + ".html"
    with open(savepath + contentsFile, "w", encoding="utf8") as fp:
        fp.write(newsContents)

    newsObj['title'] = newsTit
    newsObj['link'] = newsUrl
    newsObj['images'] = srcList
    newsObj['contents'] = newsContents
    newsObj['contentsFile'] = "news/"+contentsFile

    newsList.append(newsObj);

    # 제이슨 저장용 라이브러리

with open(savepath+"newsList.json", 'w', encoding='utf8') as fp:
    json.dump(newsList, fp)