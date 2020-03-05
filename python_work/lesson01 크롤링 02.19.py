import requests
from bs4 import BeautifulSoup
import time
"""
[크롤링 가능한 기술 : JAVA, Node.js, Python,Kotlin...]

크롤링 수행 단계
1) 지정된 URL에서 HTML 문서를 읽어온다.(requests)
2) 읽어들인 문서를 HTML 페이지로 parsing한다. (html.parser)
3) 파싱된 데이터를 다시 검색 가능한 동적 DOM 형태로 변환한다. (BeautifulSoup)

필요한 모듈
requests : 지정된 url에서 html페이지를 바이트 코드로 불러온다.
lxml 또는 html.parser : lxml은 모듈을 설치해야 사용가능.
BeautifulSoup : CSS나 jQuery의 선택자처럼 사용할 수 있게 해준다.(DOM 형식)

[requests 객체의 중요 모듈]
response.headers : 딕셔너리로 저장된 응답 페이지의 헤더 정보
response.encoding : 인코딩 정보
response.text : 응답페이지의 소스코드 내용(실제 페이지의 소스코드)
response.content : 응답 페이지의 내용을 바이트 코드로 불러온다.
response.json() : JSON 형식으로 불러온다.

뷰티풀 스프 관련 사이트 :  https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/
"""

#print("{:-^50}".format("Hello world"))


# 네이버 실시간 검색 순위


response = requests.get("http://news.naver.com/")
assert response.status_code is 200

#print(response.text)
#print(response.content)

dom = BeautifulSoup(response.content, "html.parser")
print(type(dom))

# 태그를 직접 접근하기
print(dom.title)
print(dom.title.text)
print(dom.title.string)#스트링은 내부태그가 있다면 태그까지 포함된다.
#print(dom.head.text)
print(dom.head.string)

print(type(dom.title.text)) #str
print(type(dom.title.string)) #bs4.element.NavigableString
print(type(dom.title)) #bs4.element.Tag

"""
[태그와 관련된 속성들]
contents : 리스트 형식으로 자식 태그를 가져온다. (dom.태그.contents)
children : 이터레이터 형태로 자식 태그를 가져온다. (dom.태그.children)
parents : 제네레이럴 형태로 부모 태그를 가져온다. (dom.태그.parents)
parent : 바로 위의 부모 태그를 가져온다. (dom.태그.parent)
next_sibling : 다음 형제 태그
previous_sibling : 이전 형제 태그
next_element : 다음 요소 접근
previous_element : 이전 요소 접근

=================================================================================
원하는 데이터 추출하기
<dom객체의 메소드들>
dom.find_all('태그명', class_='') : 원하는 특정 태그들을 리스트로 모두 반환(id, class, 속성, limit기능)
dom.find('태그명') : 원하는 태그 중 제일 첫번째를 반환한다.
dom.select(태그.클래스 혹은 태그#id) : CSS 선택자(Selector)를 그대로 사용한다.(사용법이 jQuery와 유사하다)
dom.extract() : 추출한 결과에서 특정 태그를 제거한다.

"""
response = requests.get("https://news.naver.com/")
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

headline = dom.select("ul.hdline_article_list")[0].find_all("div", class_="hdline_article_tit")
#select()의 결과는 리스트 타입이다
#print(headline[0])
#hdline_list = headline[0].find_all("div", class_="hdline_article_tit")
#print(hdline_list)
for i, element in enumerate(headline):
    print(i, element.find("a").text.strip())
    print(">>>>>", element.find("a")['href'])
    #print(">>>>>", element.find("a").get('href'))

"""[5초마다 한번씩 갱신 시키기]
for문안쪽 제일 마지막에 time.sleep(5)를 넣어준다.

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
"""


"""
결과를 텍스트 파일로 저장하기
파일명, 모드, 인코딩
"""
url = "https://news.naver.com/"
response = requests.get(url)
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

print("===============\n",type(dom.select("ul.hdline_article_list")[0]),"\n===============\n")
"""
※ BeautifulSoup(response.content, "html.parser") 자체는 리스트타입이고
해당 원소에 하나씩 접근해야 bs4.element.Tag로 인식하여 하위 태그 검색이 가능하다.
"""

headline = dom.select("ul.hdline_article_list")[0].find_all("div", class_="hdline_article_tit")

f = open('크롤링.txt', 'w')
for i, element in enumerate(headline):
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
for i, element in enumerate(headline):
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



"""
[========================================================================================]
그림 파일 읽어오기/자주 쓰는 코드 함수화 하기
[========================================================================================]
"""
# url주소와 원하는 선택자를 받아서 해당 url의 DOM객체를 반환하는 함수
# 함수를 다른 파일로 저장하고 import 할 수도 있다.
# ex) from SearchList import getSearchList

def getSearchList(url, selector):
    response = requests.get(url)
    assert response.status_code is 200

    dom = BeautifulSoup(response.content, "html.parser")
    return dom.select(selector)


search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
# 뉴스 메인에서 헤드라인 기사링크 모음을 선택한다.

div_list = search_list[0].find_all('div', class_='hdline_article_tit')
# 헤드라인 모음에서 각각의 헤드라인을 리스트로 담는다.

for i, element in enumerate(div_list): #리스트에 담긴 헤드라인을 태그별로 묶어서 하나씩 꺼낸다.

    imgTags = getSearchList("https://news.naver.com" + element.find("a")["href"], "div#articleBodyContents img") #신문기사 본문에 있는 사진만 가져오기
    # 각 헤드라인 태그에서 a href 태그의 요소(= 링크주소)를 꺼내고 원하는 태그 선택자를 찾아서 DOM객체를 가져온다.

    """
    imgTags의 내용 => 원소가 2개인 리스트
    
    [<img alt="" src="https://imgnews.pstatic.net/image/001/2020/02/19/PYH2020020904340001300_P2_20200219195511090.jpg?type=w647">
    <em class="img_desc">미래통합당 유승민 의원이 2월 9일 오전 서울 여의도 국회 정론관에서 새로운보수당과 자유한국당의 신설합당을 추진하고 
    개혁보수를 위해 총선에 불출마하겠다고 밝히는 기자회견을 한 뒤 정론관을 나서고 있다. [연합뉴스 자료사진]</em></img>, 
    
    <img alt="" src="https://imgnews.pstatic.net/image/001/2020/02/19/PYH2020021922210001300_P2_20200219195511105.jpg?type=w647"><em class="img_desc">
    공천심사 결과 브리핑장 들어서는 김형오(서울=연합뉴스) 하사헌 기자 = 미래통합당 김형오 공천관리위원장이 19일 오후 지금까지의 공천심사 결과를 발표하기 위해 
    서울 여의도 국회 의원회관 간담회실에 들어서고 있다. 2020.2.19 toadboy@yna.co.kr</em></img>]
    
    """
    for j, img in enumerate(imgTags):
        """
        img의 내용 => imgTags에서 가져온 원소1개
        
        <img alt="" src="https://imgnews.pstatic.net/image/001/2020/02/19/PYH2020020904340001300_P2_20200219195511090.jpg?type=w647"><em class="img_desc">
        미래통합당 유승민 의원이 2월 9일 오전 서울 여의도 국회 정론관에서 새로운보수당과 자유한국당의 신설합당을 추진하고 
        개혁보수를 위해 총선에 불출마하겠다고 밝히는 기자회견을 한 뒤 정론관을 나서고 있다. [연합뉴스 자료사진]</em></img>
        """

        # img내부의 내용에 접근하기 위해서 .get('특성명')을 사용하거나 ['특성명']을 사용할 수 있다.
        #src = img.get("src")
        src = img['src']

        # src[:src.index("?")] => src에서 ? 앞부분을 가져온다. / ?의 인덱스 까지를 인덱스 슬라이싱
        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        with open("tmp_img" + str(i) + str(j) + ".jpg", "wb") as fp:
            fp.write(response.content)
        # response.content => img의 src주소에 있는 이미지 파일만을 내용으로 갖는 DOM객체