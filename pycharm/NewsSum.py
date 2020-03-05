import requests
from bs4 import BeautifulSoup
import json

# 사용할 함수 2종 (bs4객체 생성용/이미지 소스 변경용)
def getSearchList(url, selector):
    response = requests.get(url)
    assert response.status_code is 200

    dom = BeautifulSoup(response.content, "html.parser")
    return dom.select(selector)

def replaceSRC(str1, srcList) :

    if len(srcList) ==0:
        return  str1

    newList = []

    findWord = 'src="'
    str2 = str1
    i =0
    # i< len(srcList)를 넣어주지 않으면 srcList가 1개 일때 범위 오류가 발생한다.
    while str2.find(findWord) != -1 and i< len(srcList):
        startIdx = str2.find(findWord) + len(findWord);
        newList.append(str2[:startIdx])
        newList.append(srcList[i])
        str2 = str2[startIdx:]
        endIdx = str2.find('"');
        str2 = str2[endIdx:]
        i+=1

    newList.append(str2)

    return "".join(newList)
#==============================================================================================================================================================

savepath = 'E:\\node_work2\\public\\news\\'
#저장경로 설정

newsList = []
#json 파일 저장용 리스트

sections = ['politics', 'economy','society', 'life', 'world', 'it']
# 네이버의 주제 태그목록


for i,section in enumerate(sections):
    url = 'https://news.naver.com/'
    url_list = [] # 기사의 링크를 담을 리스트를 주제별로 초기화 해준다.

    head_selector = '#section_{} > div:nth-child(2) > dl:nth-child(1) > dd:nth-child(2) > a:nth-child(1)'.format(section)
    # 각 주제의 1번 헤드라인 기사의 css선택자

    articles = getSearchList(url, head_selector)
    # 각 1번 헤드라인의 정보를 리스트로 가져온다

    if len(articles) ==0: # 헤드라인 기사가 없는 경우도 있으므로 없을때는 pass해준다.
        pass
    else:
        url_list.append(articles[0]['href'])
        # 리스트에서 링크주소에 해당하는 href의 정보를 가져와서 url_list에 담는다.
        # 현재 각 주제의 1번 헤드라인 기사링크까지만 담겨있다.

        #newsTit1 = articles[0].text
        # 1번 헤드라인 기사의 제목을 가져온다.

    
    for j in range(5): # 2~5번 헤드라인 기사를 가져온다.
        selector = '#section_{} > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({}) > a:nth-child(1)'.format(section, j + 1)
        # 각 주제의 2~5번 헤드라인 기사의 css선택자

        sub_articles = getSearchList(url, selector)
        # 각 기사의 정보를 리스트로 가져온다.
        if len(sub_articles) == 0:  # 헤드라인 기사가 없는 경우도 있으므로 없을때는 pass해준다.
            pass
        else:
            url_list.append(sub_articles[0]['href'])
            # 리스트에서 링크주소에 해당하는 href의 정보를 가져와서 url_list에 담는다.
            # 현재 각 주제의 1번 헤드라인 기사링크와 2~5번 링크를 담는 중이다.
            # for문이 모두 돌면 url_list에는 해당 주제의 크롤링할 모든 기사의 링크가 담기게 된다.
            # 현재의 코딩은 각 주제별 링크 5개를 담은 후 출력하고 다음 주제 5개를 담은 후 출력하는 방식이 된다.

            #newsTit_sub = sub_articles[0].text # 2~5번 헤드라인 기사의 제목을 가져온다.


    for k, this_url in enumerate(url_list): # 이제 url_list에는 이번 섹션에서 크롤링할 기사링크들이 모두 담겨있다.
        newsObj = {}  # 기사의 전체 내용을 담을 json 파일용 딕셔너리

        newsUrl = this_url  # json파일에 뉴스링크를 첨부하기 위한 변수선언

        dom = getSearchList(this_url, '#main_content') # url을 크롤링할 해당 기사의 링크로 바꿔주고 페이지중 #main_content 영역을 가져온다.
        pictures = getSearchList(this_url, '#articleBodyContents img') # 기사본문의 이미지들을 가져온다.

        article = dom[0].find_all("div", class_="_article_body_contents") # 해당 기사의 본문 정보를 저장한다.

        title = getSearchList(this_url, '#articleTitle')

        news_title = title[0].text # json파일에 기사제목을 넣기 위한 변수선언

        srcList = []  # 이미지 소스를 담아줄 리스트
        for picture in pictures: # 이미지 파일 저장하기
            src = picture.get('src') # 해당 기사의 이미지 소스를 src로 선언한다.

            response = requests.get(src[:src.index("?")]) # 이미지 소스에서 필요없는 ?뒷부분을 잘라내고 가져온다.
            assert response.status_code is 200

            imgName = "{}{}.jpg".format(section, k+1) # 주제명과 기사 순번으로 사진 이름을 정해서 저장한다.
            srcList.append("news\\" + imgName)
            with open(savepath + imgName, "wb") as fp:
                fp.write(response.content)


        for txt in article: # 해당 기사의 본문에서 문자 정보만 가져온다.
            if len(txt.text) != 0: # 기사의 길이가 0이 아닐때(동영상 1개만 있는 뉴스는 pass) 가져온다.
                del_str ='''// flash 오류를 우회하기 위한 함수 추가
function _flash_removeCallback() {}''' 
                del_str2 = '동영상 뉴스' # 지워야할 단어들 지정
                newsContents = txt.text.replace('다.', '다. \n').replace(del_str, '').replace(del_str2, '').strip() + "\n"
                # newsContents는 본문 앞에 붙은 지저분한 단어들을 제거하고 줄바꿈하여 기사 본문 내용만 가져왔다

                newsSum = txt.text[:txt.text.index('다.')+2].replace('다.', '다. \n').replace(del_str, '').replace(del_str2, '').strip() + "\n"
                # newsSum은 첫번째로 다. 로 끝나는 문장까지를 가져왔다.

                contents = getSearchList(this_url, "div#articleBodyContents")[0]
                # 기사 전체의 태그를 가져온다

                fullContents = replaceSRC(str(contents), srcList)
                # 나중에  비주얼코드에 띄우기 위해 기사 전체의 html태그 중 img src를 내가 저장한 srcList로 변경해 놓는다.

                del_str3 = fullContents[fullContents.index('<!--'):fullContents.index(' // TV플레이어 -->')+15]
                finalContents = fullContents.replace(del_str3,'').strip()
                # 해당 html에서 필요없는 부분을 지운다. html파일이므로 줄바꿈을 위한 변환이 필요 없다.

                contentsFile = '{}{}.html'.format(section, k+1)
                with open(savepath + contentsFile, "w", encoding="utf8") as fp:
                    fp.write(finalContents)

                sumFile = '{}{}s.html'.format(section, k + 1)
                with open(savepath + sumFile, "w", encoding="utf8") as fp:
                    fp.write(newsSum)

        # newsObj에 해당 변수들을 이름을 정하여 넣고 최종적으로 newsList에 담아 json파일로 만든다.

        newsObj['title'] = news_title
        newsObj['link'] = this_url
        newsObj['images'] = srcList
        newsObj['contents'] = "news/" + contentsFile
        newsObj['summary'] = "news/" + sumFile

        newsList.append(newsObj);


with open(savepath + "newsList.json", 'w', encoding='utf8') as fp:
    json.dump(newsList, fp)