# 손글씨 데이터 학습을 통한 개인 폰트 제작


### [전체 학습과정 단계]
1) 컴퓨터 폰트로 글씨를 먼저 학습하는 Pre-Train 단계
- 글자 이미지 자체를 학습하는 것
- 글자의 특징을 추출하고, 다시 복원하는 방법을 먼저 학습
- 최종적인 목표는 고딕체의 글자와 폰트 카테고리 정보를 함께 입력받아 폰트가 입혀진 글자를 출력하는 것
![image.png](attachment:image.png)

2) 사람의 손글씨를 학습하는 Transfer Learning 단계
- 손글씨를 학습하는 단계
- 전이학습을 이용해 이전에 컴퓨터 폰트를 베껴내는 사전학습모델을 활용하여 손글씨를 학습
 - 아주 적은 양의 데이터셋으로만 학습하여 11172개의 모든 글자 폰트를 생성하는 것이 목표


### 사용 모델
- 기본적으로 GAN을 사용하여 진행
- original GAN에서 Decoder구조의 부분을 폰트 카테고리를 추가하여 noise를 생성할 수 있도록 변형하여 사용


### 12.01
- AI hub에서 손글씨체 데이터셋과 인쇄체 데이터셋을 모두 사용하여 인쇄체 데이터셋을 사전학습모델에 사용하고 손글씨체 데이터셋을 통해 폰트화 하는 모델 구성을 하려고 했으나, 데이터양이 충분하여 인쇄체 데이터셋만을 가지고 학습하기로 결정

- 여기서 문제는 인쇄체 데이터셋에서는 "어노테이션 바운딩박스"가 없음
- 그래서 crop -> resize -> padding 과정을 위해 어떻게 crop할 것인지가 관건

<json파일 보기좋게 표시하는 참조 코드>

```
>>> import json
>>>
>>> your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
>>> parsed = json.loads(your_json)
>>> print(json.dumps(parsed, indent=4, sort_keys=True))
[
    "foo", 
    {
        "bar": [
            "baz", 
            null, 
            1.0, 
            2
        ]
    }
]
```


### 12.02
- json Parsing
- 링크 : https://www.notion.so/json-Parsing-f174d3ec95dc45859fb5956345ccbcb6

### 12.03
- json Parsing & 데이터 디렉토리로 분류
- 링크 : https://www.notion.so/img-efe4a9d1e3734fdba71ad5865612401e

### 12.09
- 데이터 재분류
- 링크 : https://www.notion.so/3-da7e1922b2654a0fb55052f689e60827

### 12.10
- 데이터 재분류
- 링크 : https://www.notion.so/4-2-2996aba404344997b1a7e7332eaacb56