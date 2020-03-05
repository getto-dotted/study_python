from uu import encode

str1 = """$#@$aa<img src="aaa">@@@$#@$aa<img src="bbbb">@@@$#@$aa<img src="cc">@@@"""
srcList =['img/aa.jpg','img/bb.jpg','img/cc.jpg']

str2 = str1.split('src=')
str3 = []
str4 = """"""

for i,c in enumerate(str2):
    if i==0:
        str3.append(c)
    else:
        temp_str = c.split('\"')
        temp_str[1]=srcList[i-1]
        str3.extend(temp_str)
        print(str3)
for i,c in enumerate(str3):
    if i==9:
        a= c
    elif i%3==0:
        a= c+ 'src='
    else:
        a= c+ '"'
    str4 += a

print(str4)

#npm install -g express
# open-in-browser/ open in browser/ live server/ node snippets/ 
# 비주얼 스튜디오에서 npm init -y
# npm install --save express
# npm install --save cors
# npm install -g nodemon
# node app.js
# nodemon app.js
# npm install --save serve-static
# npm i -S ejs
# 노드모듈에 에러가 났을때는 노드모듈 폴더를 삭제하고 package.json 파일이 있는 곳에서 npm install을 해준다.
# 그래도 계속 에러가 날 경우에는 npm cache clean --force 를 통해 캐시를 지우고 설치한다.

findWord = 'src="'
str2 = str1

startIdx = str2.find(findWord) + len(findWord);
str2 = str2[startIdx:]
print(str2)
endIdx = str2[startIdx+1:].find('"') +1;
str2 = str2[endIdx:]

print(startIdx, endIdx);
print(str2[:startIdx])
print(str2[endIdx:])
