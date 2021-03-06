# Deep Learning Projects

<br >

```bash
├── README.md
└── 윤상덕
    ├── inputs.py           # 데이터 로드
    ├── main.py             #
    ├── model.py            # 뉴럴 네트워크 모델 정의
    ├── predict.py          # 학습된 파라미터를 불러와서 실제 데이터로 predict
    ├── preprocessing.py    # 데이터 전처리
    └── train.py            # comiple, fit
```

<br > 

### 논문 구현해보기(SRGAN>> PROGAN>> ??? - 우민준

SRGAN: http://arxiv.org/pdf/1609.04802.pdf

<br >

### 질문에 답을 웹에서 찾아 대답하기 or 책을 학습한 전문가 chat bot, 한국어 문서 추출요약 - 이낙원.
 규칙 기반 ? https://arxiv.org/pdf/1807.06638v1.pdf

 NLP-progress : https://github.com/sebastianruder/NLP-progress/blob/master/english/summarization.md   
  웹에서 답을 찾는게 웹 크롤링뿐인가요? 아니면 컴이 직접 서핑을 하여 검색할수 있는건지?  https://github.com/SKTBrain/KoBERT
  https://www.quora.com/     https://stackoverflow.com/ 
  https://dacon.io/competitions/official/235671/overview/

  https://m.blog.naver.com/PostView.nhn?blogId=tjdudwo93&logNo=221085844907&proxyReferer=https:%2F%2Fwww.google.com%2F

  https://arxiv.org/ftp/arxiv/papers/1502/1502.04042.pdf

  https://github.com/digicope/ai_nlp/tree/main/03_RNN_LSTM

  Abstract Learning via Demodulation in a Deep
Neural Network   https://arxiv.org/ftp/arxiv/papers/1502/1502.04042.pdf

  On Extractive and Abstractive Neural Document Summarization
with Transformer Language Models  https://arxiv.org/pdf/1909.03186.pdf

<br >

### 웹크링하여 주제분류해보기 - 오현귀

- 네이버에 지식인에서 ''중학생+질문" 이라고 검색어를 입력하여 데이터를 웹크롤링하여 가져온 후 csv파일로 저장하고 가져온 데이터를 형태소만 추출하여 추출한 형태소를 주제분류해보려합니다.
- 현재 네이버 지식인에서 중학생+질문을 검색으로 하여 10000개의 csv파일을 추출을 하였습니다.
- 추출한 데이터에서 okt()함수를 사용하여 형태소를 추출하고 빈도수가 높은 순으로 500까지 추출한 후 불용어를 제거하였습니다.
- 워드클라우드 형태로 단어빈도수가 높은 순으로 글자크기를 크게 나타내는 것까지 완료했습니다.
- 현재 빈도수높은 형태소로 레이블을 만들려고 합니다. 이때 필요한 방법을 무슨 방법으로 해야 할지 찾아야 하구요
- 그리고 데이터를 워드임베딩 해서 학습 시키는 방법을 무엇으로 해야 할지 고민해봐야 합니다.
- LDA 토픽과 TF-IF 부분을 비교해보고 무엇을 선택할지 고민 하고 있습니다
- 100000건 데이터 추출해보기, TF-IF 부분으로 데이터 

<br >

### 초음파 트랜스듀서의 초기 이미지를 평가하여, 합/불을 판단하기 - 민성원

- 초음파 시스템에서 환자에 접촉하는 부분을 트랜스듀서, 혹은 프로브라고 지칭합니다. 프로브를 생산하게 되면 이미지 시스템에 연결하여 초기 이미지를 통해서 제품에 문제가 없는지를 확인 하게 됩니다. 
 문제는 이러한 이미지 판단을 위해서는 수년간의 초음파 임상 경험이 필요하게 됩니다.   

- 목표는 임상 전문가가 판단한 labeled 자료를 학습하여, 합/ 불 판단을 내릴 수 있는 AI를 작성하는 것 입니다. 

- 학습을 위한 이미지 데이터는 직접 준비할 예정이지만, 대량의 데이터를 준비하기가 어려운 현실적 문제가 있습니다. 1차 목표는 수십장의 데이터를 통해 전처리 등 기본적인 network 구조를 구축하는 것 입니다. 

<br >

### Openpose를 사용하여 수화 인식 - 유세환 

- Computer Vision 중 Openpose 기능을 사용하여 사람의 움직임을 감지하여 간단한 수화를 인식하는 기능 구현 
- 참고논문: https://www.researchgate.net/figure/Statistics-of-KETI-sign-language-dataset_tbl1_334150420
- 데이터셋: (이전) AI hub download (https://aihub.or.kr/)
           (변경) https://www.kaggle.com/datamunge/sign-language-mnist

<br >

### 손글씨 데이터 학습을 통한 개인 폰트 제작 - 김태현
:한글 손글씨 데이터를 이용하여 최소한의 입력데이터(대략 210개 정도의 글씨체)를 주게되면 해당 글씨체에 맞는 한글 전체 글씨체(11,172자)를 생성하는 서비스

- 한글, 영어, 숫자를 포함하면 좋겠지만 데이터 및 학습 과정 여부를 고려해 한글로만 한정하여 시도해보고자 합니다.
- 한글 손글씨 데이터와 인쇄 폰트 데이터를 활용하여 학습을 시도하고 모델을 구축합니다.
- 이상적인 최종 결과물은 학습에 필요한 최소한의 자음, 모음, 단어를 입력할 시, 해당 글씨체를 폰트화 시키는 것을 목표로 합니다.


- 사용 데이터셋 : 손글씨체 이미지, 인쇄체 이미지 (AI hub) - https://aihub.or.kr/aidata/133

##### (추가) 음성 데이터 학습을 통해 텍스트 데이터 입력 시, 학습된 목소리로 출력
:한국어 음성 데이터를 가지고 학습을 통해 목소리를 추출합니다. 그래서 최종적으로 특정 텍스트를 입력값으로 주었을 때, 해당 텍스트를 학습된 목소리로 읽는 음성 데이터를 출력하는 것이 목표입니다.

- 위의 프로젝트와 유사한 방식을 통해 구현 가능할 경우 수행합니다.
- 이상적인 최종 결과물은 최소한의 음성데이터를 입력할 시 해당 목소리를 추출하고, 텍스트 입력 시 추출한 목소리로 출력하는 것입니다.

<br >

### Intel RealSense tracking, depth camera를 활용하여 촬영한 이미지를 활용한 자율주행 로봇 구현 or 비트코인 추세 판단 - 하현호

- Intel RealSense 카메라가 있는데 물체와의 거리나, 현재 카메라 위치를 판단하는 등 다양한 기능이 있어 여기에 딥러닝을 같이 적용해보면 좋을 것 같습니다.
- 카메라에서 촬영한 영상이나 사진을 파일로 받아 Dataset으로 사용할 생각입니다.

- 추가로, 가능하다면 특정 비트코인의 과거 데이터들로부터 앞으로의 추세가 어떻게 될 것인지 예측하는 프로그램을 만들어보고 싶습니다.

<br >

### K-Fashin, Imagent 등을 활용하여 사용자가 가지고 있는 옷을 기반으로 어울리는 옷을 추천해주는 모델 - 강찬
- https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset, https://www.aihub.or.kr/aidata/7988 데이터 활용
- instagram과 국내 무신사 스토어 후기 시스템 활용
- 전신 데이터에서 외투, 상의 ,하의, 신발 등으로 분류하여 어울리는 조합을 학습 -> 새로운 하나의 옷 종류에 대하여 어울리는 조합을 추천해주는 프로그램을 만들어보고 싶습니다.

- 추가적으로 가능하다면 GAN으로 새로운 디자인을 만드는 모델까지 가능하다면 해보고 싶습니다.
