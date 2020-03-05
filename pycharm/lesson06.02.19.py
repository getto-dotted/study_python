from SearchList import getSearchList
import requests
from bs4 import BeautifulSoup
from Tools import replaceSRC


search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')

savepath = 'E:\\node_work2\\public\\news\\'

for i, element in enumerate(div_list):
    newsUrl = "https://news.naver.com" + element.find("a")["href"]
    imgTags = getSearchList(newsUrl, "div#articleBodyContents img") #신문기사 본문에 있는 사진만 가져오기
    newsContents = getSearchList(newsUrl, "div#articleBodyContents")[0]

    srcList = []
    for j, img in enumerate(imgTags):
        src = img.get("src")
        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        imgName = "tmp_img" + str(i) + str(j) + ".jpg"
        srcList.append(imgName)
        with open(savepath+imgName, "wb") as fp:
            fp.write(response.content)

    newsContents = replaceSRC(str(newsContents), srcList)
    with open(savepath + "newsContent" + str(i)  + ".html", "w", encoding="utf8") as fp:
        fp.write(newsContents)
