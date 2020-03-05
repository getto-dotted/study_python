"""
크롤링 가능한 기술 : JAVA, Node.js, Python,Kotlin...

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

뷰티풀 스프 관련 사이트 :
    https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/
"""

#print("{:-^50}".format("Hello world"))

import requests
from bs4 import BeautifulSoup
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
"""
