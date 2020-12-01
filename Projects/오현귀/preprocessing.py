from konlpy.tag import *          #pip install konlpy 먼저 설치
import matplotlib.pyplot as plt   #pip install matplotlib 먼저 설치
from matplotlib import font_manager as fm
from matplotlib import rc as rc
from wordcloud import WordCloud   #pip install wordcloud 먼저 설치
from collections import Counter

import csv
#import pd
import sys

okt = Okt()
kkma = Kkma()

#input_file ="C:\Users\user\ohg\중학생+질문 20200921-3.csv"             #sys.argv[1]
#output_file ="C:\Users\user\ohg\data\빈도수_중학생+질문 20200921-3.csv" #sys.argv[2]

input_file ="./in_data/중학생+질문 20201005-1(질문).csv"             #sys.argv[1]
output_file ="./out_data/빈도수_중학생+대답 20201005-1(질문).csv" #sys.argv[2]


#CSV파일을 불러와서 형태소를 분석
filereader = open(input_file,encoding = "UTF8").read()
#키워드 추출
keyWord = okt.nouns(filereader)
print("추출된 키워드 : ", keyWord)

#빈도수 추출
cnt = Counter(keyWord)
print("단어별 빈도수 : ", cnt)

#추출된 단어들의 최대500건만
most100 = cnt.most_common(500)
print("단어별 빈도수(500) :", most100)


#불용어 가져오기
sword = open("./stopword/stopword.txt", encoding = "UTF8").read()
#불용어 제거하기
keyWord2 = [each_word for each_word in keyWord if each_word not in sword]
print("불용어제거 된 추출 키워드 :",  keyWord2)

#빈도수 추출
cnt2 = Counter(keyWord2)
print("불용어제거 된 단어별 빈도수 : ", cnt2)

#추출된 단어들의 최대200건만
most2_100 = cnt2.most_common(500)
print("불용어제거 된 단어별 빈도수(100) :", most2_100)

#불용어 단어 제거여부 체크
word = []
word = [ a for a in cnt if a not in cnt2]
print(word)

#워드클라우드 그리기
wordcloud = WordCloud(font_path = 'C:\\Windows\\Fonts\\H2GTRM.TTF',
                     relative_scaling=0.4,
                     background_color ='white',
                     ).generate_from_frequencies(cnt2)
plt.figure(figsize=(20,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

#주요단어들의 빈도를 그래프로 표시하기
from matplotlib import font_manager as fm
from matplotlib import rc as rc
import nltk
from nltk.probability import FreqDist

font_location = 'C:\\Windows\\Fonts\\H2GTRM.TTF'
font_name = fm.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)
plt.figure(figsize =(20,10))

grape = FreqDist(keyWord2)
#가로의 속성 50개 출력
grape.plot(50)

