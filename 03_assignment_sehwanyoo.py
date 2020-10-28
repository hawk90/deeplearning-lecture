#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:33:36 2020

@author: sehwanyoo
"""

# %% Problem 01

#1. 1시간은 몇 초인가?
#2. 계산한 결과를 seconds_per_hour 변수에 저장
#3. 1일은 몇초인가?  seconds_per_hour 변수를 사용
#4. 계산한 결과를 seconds_per_day 변수에 저장
#5. 나눗셈을 사용해서 sconds_per_day를 seconds_per_hour로 나누기

#from datetime import timedelta 

hour = 1 

seconds_per_hour = hour * 60 * 60  
seconds_per_day = seconds_per_hour * int(24)
seconds_per_day /= seconds_per_hour 


# %% Problem 02

#1. 출생년도에 대한 리스트 year_lists를 만들어라 출생연도를 첫 번째 요소로 하고 1년씩 장가한는 다섯번째 생일까지의 요소를 넣는다. 출생년도가 1980이라고 가정한다.
#2. years_list의 오프셋 3의 생일의 년도는? 참고로 오프셋 0은 출생년도
#3. years_list중 가장 나이가 많을 때의 년도는? if와 max변수를 활용

birth_year = 1987
year_list = [year for year in range(birth_year, birth_year + 5)]

print(year_list[3])

now = 2020
max_v = min(year_list)

for v in year_list:
    
    if (now - max_v) < (now - v):
        max_v = v
        
print(max_v)




# %% Problem 03

#1. 영어-프랑스어 사전을 의미하는 f2e 딕셔너리를 만들어라. 영어의 dog는 프랑스어 chien이고, cat은 chat, walrus는 morse다. 딕셔너리를 출력해보라.
#2. f2e 딕셔너리에서 영어 walrus를 프랑스어로 출력하라.
#3. f2e 딕셔너리를 사용해서 프랑스어 chien을 의미하는 영어를 출력하라.
#4. f2e의 키 값을 출력하라
#5. f2e의 밸류 값을 출력하라. 

f2e = {'dog': 'chein', 'cat': 'chat', 'walrus': 'morse'}

print(f2e)

walrus = [key for key, value in f2e.items() if value == 'chein']

print(walrus)

print(f2e.keys())
print(f2e.values())



# %% Problem 04

#1. 리스트 컴프리헨션을 이용하여 range(10)에서 짝수 리스트를 만들어라
#2. 딕셔너리 컴프리헨션을 이용하여 range(10)의 키 값은 range(10), 밸류 값은 range(10)의 제곱 값

even_list = [e for e in range(10) if e % 2 == 0]

print(even_list) 

dict_list = {ee : pow(ee, 2) for ee in range(10)}

print(dict_list)
