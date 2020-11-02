#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:39:44 2020

@author: sehwanyoo
"""

# %% 
# 1.zoo.py 파일에서 'Open 9-5 daily' 문자열을 반환하는 hours 함수를 정의하라. buzz.py에서 hours() 함수를 호출 하라.
#from buzz import hours
from buzz import *

print(hours())




# %% 
# 2. 
#things 리스트를 만들어라. 이 리스트는 "mozzarella", "cinderella", "salomonella" 세 문자열을 요소로 갖는다.
#things 리스트에서 첫 글자를 대문자로 바꿔서 출력하라.
#things 리스트에서 모두 대문자로 바꿔서 출력하라.
#things 리스트에서 마지막 요소를 제거한 뒤 출력하라.
#suprise 리스트를 생성하라. 이 리스트는 "Groucho", "Chico", "Harpo" 세 문자열을 요소로 갖는다.
#suprise 리스트의 마지막 요소를 소문자로 변경하고, 단어를 역전시킨 후, 첫 글자를 대문자로 바꿔라.


things = ['mozzarella', 'cinderella', 'salomonella']

for t in things:
    print(t.capitalize())
    print(t.upper())
    
    
things.pop(-1)

print(things)

suprise = ['Groucho', 'Chico', 'Harpo']

txt = sorted(suprise[2].lower(), reverse=True)
suprise[2] = ''.join(txt)
suprise[2] = suprise[2].capitalize()

print(suprise)


# %% 
# 3. 
#['Harry', 'Ron', 'Hermione'] 리스트를 반환하는 함수를 정의하라.
#
#두 리스트를 짝으로 하는 movies 딕셔너리를 만들어라.
#
#title = ['Creature of Habit', 'Crewel Fate']
#
#plots = ['A turns into a mon ster', 'A haunted yarn shop']
#
#두 리스트를 짝으로 하는 movies2 딕셔너리를 만들어라. (키 값이 비어있을 경우 '' 공백으로 처리)
#
#title = ['Creature of Habit', 'Crewel Fate', 'Apple']
#
#plots = ['A turns into a mon ster', 'A haunted yarn shop']
#
#movies2 딕셔너리를 출력하여라(에러가 날 경우 수정 할 것)
#
#for key in movies2.kesy()
#
#​ print(movies2[key])


def harry_poter_list():
    return ['Harry', 'Ron', 'Hermione'] 

title = ['Creature of Habit', 'Crewel Fate']
plots = ['A turns into a mon ster', 'A haunted yarn shop']

movies = {}

for t, p in zip(title, plots):
    movies[t] = p
    
print(movies)

title = ['Creature of Habit', 'Crewel Fate', 'Apple']
plots = ['A turns into a mon ster', 'A haunted yarn shop']

len_title = len(title)
len_plots = len(plots)

len_max = max(len_title, len_plots)

movies2 = {}

for i in range(len_max): 
    try:
        movies2[title[i]] = plots[i]
    except IndexError as e:
        movies2[title[i]] = '' 
        
for key in movies2.keys():
    print(movies2[key])
