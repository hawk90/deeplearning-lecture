import pandas as pd
from konlpy.tag import Okt
import re
okt=Okt()

#사이킷런을 이용한 DTM과 TF-IDF
from sklearn.feature_extraction.text import CountVectorizer

#질문을 리스트 선언 및 초기화

##1000건의 데이터
#file = r'C:\Users\user\ohg\in_data\중학생+질문 20201005-1(질문).csv'

#84460건의 데이터
file = r'C:\Users\user\ohg\in_data\중학생+질문 20201202(QA).csv'
df = pd.read_csv(file)


corpus = []
for i in df['question']:
    token=okt.morphs(i)
    corpus.append(token)

vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_) # 각 단어의 인덱스가 어떻게 부여되었는지를 보여준다.

from sklearn.feature_extraction.text import TfidfVectorizer

tfidfv = TfidfVectorizer().fit(corpus)  #코퍼스로부터 각문서의 tfidf
print(tfidfv.transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(tfidfv.vocabulary_) # 각 단어의 인덱스가 어떻게 부여되었는지를 보여준다.
