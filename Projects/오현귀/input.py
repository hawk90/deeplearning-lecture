import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import pandas as pd
import re

search = input('검색어를 입력하세요 : ')
cnt = int(input('검색할 페이지 건수를  입력하세요 : '))
date = input('검색날짜를 입력하세요(YYYYMMDD-N형식으로) : ')
# 네이버검색
plusUrl = quote_plus(search)

pageNum = 1
lastPage = cnt * 10 - 9
temp1 = []
temp2 = []
temp3 = []
temp4 = []

while pageNum <= lastPage:
    ##단순검색
    # url= f'https://search.naver.com/search.naver?where=kin&sm=tab_jum&query={plusurl}'

    # 페이지별검색
    url = f'https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query={plusUrl}&sm=tab_pge&kin_start={pageNum}'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # contents
    contents = soup.select('.type01 dd')

    j = 1
    for i in contents:

        # 질문날짜
        if (j % 4) == 1:
            temp1.append(i.text)
        # 질문
        if (j % 4) == 2:
            temp2.append(i.text)
        # 대답
        if (j % 4) == 3:
            temp3.append(i.text)
        j += 1

    pageNum += 10

# 데아타프레임 선언
middle = pd.DataFrame()
middle_question = pd.DataFrame()
middle_answer = pd.DataFrame()

# 중학생Q/A전체
middle['date'] = temp1
middle['question'] = temp2
middle['answer'] = temp3

# 중학생질문
middle_question['question'] = temp2
# 중학생대답
middle_answer['answer'] = temp3

print(middle)

path = "./in_data/"
savename = path + search + ' ' + date

# 추출결과 csv파일로 저장하기
middle.to_csv(savename + "(QA).csv", encoding='UTF8', index=False)

# 추출결과 csv파일로 저장하기
middle_question.to_csv(savename + "(질문).csv", encoding='UTF8', index=False)
middle_answer.to_csv(savename + "(대답).csv", encoding='UTF8', index=False)
