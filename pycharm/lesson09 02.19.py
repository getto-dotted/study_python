import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/" # 크롤링을 할 기본 url
selector = "ul.hdline_article_list" # 기본 url에서 크롤링을 할 부분 => 선택자 :  "태그명.클래스"

response = requests.get(url) # requests를 통해 url주소의 내용을 가져와서 response라는 이름으로 저장
assert response.status_code is 200 # 상태코드가 200일때만 진행한다 (400,404,500오류등)

dom = BeautifulSoup(response.content, "html.parser")
# BeautifulSoup를 통해 response의 content 영역을 html로 parsing한다. => dom객체로 저장됨

page_list = dom.select(selector)
# dom객체에서 크롤링을 하고자 하는 부분을 선택자를 통해 선택해준다.

url_classes = "hdline_article_tit"
# 크롤링할 부분에서 링크를 통해 해당 링크의 내용을 크롤링할 것이므로 링크가 있는 부분의 클래스를 확인한다.

div_list = page_list[0].find_all('div', class_= url_classes)
# dom객체에서 선택된 부분에서 크롤링을 위해 접속할 링크들을 리스트 형태로 저장한다.

for i, element in enumerate(div_list): # 링크주소를 for문을 통해 하나씩 꺼내와서 접속한다.
    href_list = element.find("a")["href"]
    # 링크 주소중 필요한 부분인 a 태그의 href의 내용만을 선택하여 새로운 변수로 저장한다.

    tagname = "div#articleBodyContents img"
    # 링크를 실행했을때 크롤링할 이미지의 태그와 클래스를 새로운 변수로 저장한다.

    response = requests.get(url+href_list)
    assert response.status_code is 200
    # 이미지를 저장하기 위해서 새로운 링크(기본url + href => 크롤링할 정확한 링크주소)의 내용을 response로 재정의

    dom = BeautifulSoup(response.content, "html.parser")
    # 재정의된 response의 content를 dom객체로 저장한다.

    imgTags = dom.select(tagname)
    # dom객체에서 크롤링할 이미지 태그와 클래스를 선택하여 리스트(연속데이터)로 가져온다.

    for j, img in enumerate(imgTags): # for문을 통해 이미지가 포함된 객체들을 하나씩 꺼내온다.

        #src = img.get("src")
        src = img['src']
        # 이미지 객체에서 이미지 주소인 src부분을 추출한다.

        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200
        # src에서 필요없는 ?type=w647 부분을 제거하고 response객체로 저장한다.
        # 이 상태에서 response객체의 content에는 이미지 정보만 남아있다.

        with open("news_img/크롤링사진{}{}.jpg".format(str(i),str(j)), "wb") as fp:
            fp.write(response.content)

        # jpg형태의 파일을 binary writing할 준비를 하고 response의 content를 불러와서 그대로 작성해준다.

    txtTags = dom.select("div.content")[0].find_all("div", class_="_article_body_contents")
    # 해당 링크에서 content클래스의 div태그 안에서 _article_body_contents클래스의 div내부 내용을 선택한다.

    for k, txt in enumerate(txtTags): # 해당 링크의 div태그 내부의 text파일을 변환하여 가져온다.
        with open("news_img/크롤링글{}{}.txt".format(str(i),str(j)), "w", encoding="utf8") as f:
            f.write(txt.text.replace('. ', '. \n') + "\n")
