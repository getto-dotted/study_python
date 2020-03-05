


    # str1 = """$#@$aa<img src="aaa">@@@$#@$aa<img src="bbbb">@@@$#@$aa<img src="cc">@@@"""
    # srcList =['img/aa.jpg','img/bb.jpg','img/cc.jpg']

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