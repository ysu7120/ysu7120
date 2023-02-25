# Portfolio

이 페이지는 제가 진행한 프로젝트 중 몇 가지를 추려 소개합니다.

## 기술 스택

개인 프로젝트에서 사용한 기술 스택입니다. 숙련된 기술은 **굵게** 강조했습니다.

- Programing Languages
  - **Python**
  - JavaScript (ES2015) / node.js
- Framework/ Library
  - Numpy
  - Pandas
  - **TensorFlow**
  - **Keras**
  - Selenium
  - BeautifulSoup
  - OpenCV
- Cloud
  - **Firebase**
  - **Google Cloud Platform**

***

## Table of Contents

- [Convolutional LSTM 알고리즘 이용한 컴퓨터 비전 센서 기반 사거리 교통체증 예측 시스템(2020.10~2021.11)](https://github.com/ysu7120#convolutional-lstm-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%BB%B4%ED%93%A8%ED%84%B0-%EB%B9%84%EC%A0%84-%EC%84%BC%EC%84%9C-%EA%B8%B0%EB%B0%98-%EC%82%AC%EA%B1%B0%EB%A6%AC-%EA%B5%90%ED%86%B5%EC%B2%B4%EC%A6%9D-%EC%98%88%EC%B8%A1-%EC%8B%9C%EC%8A%A4%ED%85%9C-202010202111)
- [홈베이스: 모션인식을 활용한 야구훈련 프로그램 (2021.3~2021.6)](https://github.com/ysu7120#%ED%99%88%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EB%AA%A8%EC%85%98%EC%9D%B8%EC%8B%9D%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%95%BC%EA%B5%AC%ED%9B%88%EB%A0%A8-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-2021320216)
- [문화재 복원을 위한 DCGAN 기반 Image Completion 시스템 (2022.1~2022.10)](https://github.com/ysu7120#%EB%AC%B8%ED%99%94%EC%9E%AC-%EB%B3%B5%EC%9B%90%EC%9D%84-%EC%9C%84%ED%95%9C-dcgan-%EA%B8%B0%EB%B0%98-image-completion-%EC%8B%9C%EC%8A%A4%ED%85%9C--20221202210)
- [딥러닝 기반 Transfer Learning 모델을 활용한 아보카도 분류 및 예측 시스템 (2022.10~2023.2)](https://github.com/ysu7120#%EB%94%A5%EB%9F%AC%EB%8B%9D-%EA%B8%B0%EB%B0%98-transfer-learning-%EB%AA%A8%EB%8D%B8%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%95%84%EB%B3%B4%EC%B9%B4%EB%8F%84-%EB%B6%84%EB%A5%98-%EB%B0%8F-%EC%98%88%EC%B8%A1-%EC%8B%9C%EC%8A%A4%ED%85%9C20221020232)
- [실시간 인구 데이터 분석을 통한 인파사고 방지 시스템 구축 (2022.12~2022.12)](https://github.com/ysu7120#%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9D%B8%EA%B5%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D%EC%9D%84-%ED%86%B5%ED%95%9C-%EC%9D%B8%ED%8C%8C%EC%82%AC%EA%B3%A0-%EB%B0%A9%EC%A7%80-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%95202212202212)

## [Convolutional LSTM 알고리즘 이용한 컴퓨터 비전 센서 기반 사거리 교통체증 예측 시스템](https://github.com/geeksbaek/pokedex) (2020.10~2021.11)

`#Python` `#Pandas` `#Numpy` `#Tensorflow` `#Keras` `#Data` `#LSTM`

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220953236-1016f9f4-87c1-46dc-b390-05304cb5763a.PNG" width="800">
</p>

전국 교통사고 다발 지역 상위 10곳 중 9곳은 사거리 또는 교차로이며, 교차로의 경우 교통량이 많아 정체가 심화되기 쉽습니다. 또한 교통혼잡비용은 매년 지속해서 증가하고 있으며, 그 규모 면에서 2017년 GDP의 3.4%에 달할 정도로 국가 경제활동에 큰 영향을 미치므로 교통혼잡을 완화하기 위한 지속적인 노력이 필요합니다.

이러한 문제를 해결하기 위하여, 해당 프로젝트는 교통체증을 예측하여 완화 시키는 시스템으로 센서(VDS) 두 개를 설치하여 센서와 센서 사이의 거리, 신호가 바뀌는 주기, 
신호 대기 중인 차량들의 길이와 차량들의 개수로 체증 지수를 측정하고 교통체증 발생 시 해당 차로 및 주변 차로의 시간별 데이터를 데이터 베이스에 저장하고 
C-LSTM 알고리즘을 이용하여 학습 하고 교통체증에 대해 분석 후 교통체증을 예측하여 AI가 스스로 해당 시간대의 체증 지수를 완화시킵니다.


### 프로젝트 진행 과정요약

교통체증을 완화 알고리즘은 서울시 교통데이터를 분석하여 수정하며 진행하였습니다.

1. 서울시 교통데이터의 입출 교통데이터를 전처리하여 학습할 수 있도록 제작합니다.
2. 준비된 데이터를 LSTM 모델에 입력시켜 특정시간의 정보를 예측할 수 있도록 학습시킵니다.
3. 학습시킨 데이터를 활용하여 특정시간의 차량이동량을 예측하고 제작한 알고리즘을 도로교통에 대입시켜 교통체증을 완화합니다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220963211-e1a95d34-d654-4433-874a-6e65897929ec.PNG" width="400">
</p>

## 프로젝트 성과

- 제2회 대학생 동아리 인공지능(AI) 아이디어 경진대회 우수상 / 부산인재평생교육진흥원
- AI 해커톤대회 대상 / 동서대학교
- 춘계 학술대회 논문 발표
- 특허 등록

## [홈베이스: 모션인식을 활용한 야구훈련 프로그램](https://github.com/geeksbaek/goinside) (2021.3~2021.6)

`#Python` `#Pandas` `#Tensorflow` `#Keras` `#Transfer learning` `#Teachable Machine` `#node.js` `#Text to speach`

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220950687-d3d60fba-e793-479f-9bc3-f07a7ec1b407.PNG" width="800">
</p>

전 세계적인 전염병인 코로나 바이러스의 확산으로 인구가 밀집하면 안되는 이유가 생겼으며, 정부차원에서 5인이상 집합금지, 운동시설이용제한 등의 제약을 걸었기 때문에 운동인들은 제대로 된 훈련을 할 수 없는 상황에 놓였습니다. 특히 다수가 필요한 운동과 이를 훈련하기 위한 티칭을 하는 과정에서 방역수칙을 어길 수 밖에 없기 때문에 이를 해결할 방안이 
필요합니다.

이러한 문제를 해결하기 위해 언제 어디서든 야구훈련을 받을 수 있는 프로그램을 연구하고 개발하였으며, 해당 연구를 위해 이미지센서와 초음파센서를 활용하였습니다. 
스마트 베이스볼 트레이닝 프로그램은 웹사이트를 기반으로 실행가능하며 카메라에 저장된 이미지센서가 사용자의 모션을 인식하고 해당 자세에 대한 티칭을 하여 훈련을 보조하며, 
초음파센서를 활용하여 티칭의 정확도를 높일 수 있으며, 모바일도 연동이 가능해 언제 어디서든 훈련이 가능합니다.

### 프로젝트 진행 과정요약

구글의 티쳐블머신을 활용하고 카카오의 Text to speach APi를 사용하여 사용자가 연습상황을 확인할 수 있게 하였습니다.

1. 티쳐블머신을 활용하여 야구동작의 타격준비, 타격, 실패의 세가지 동작을 학습한 학습모델을 제작합니다.
2. 타격에 성공할때마다 카운트를 더하고 Text to speach APi를 활용하여 소리로 알려줍니다.
3. 웹 페이지에 기능을 이식하고 Netlify를 활용하여 베포하였습니다. 


## [문화재 복원을 위한 DCGAN 기반 Image Completion 시스템 ](https://github.com/geeksbaek/ourchess) (2022.1~2022.10)

`#Python` `#Pandas` `#Tensorflow` `#Keras` `#DCGAN` `#Image Completion` 

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220962507-6a597f00-dfd2-434c-be6d-20299b52101a.PNG" width="800">
</p>

2008년 대한민국 국보1호 숭례문 화재 사건과 미륵사지 석탑의 복원 실패 사례로 문화재 보존과 복원의 중요성이 강조되었습니다. 
현재 인공지능 기술의 발전으로 다양한 방법으로 문화재 복원이 이루어지고 있습니다. 

해당 프로젝트는 DCGAN(Deep Convolutional Generatice Adversarial Network)과 Image Completion 기술을 이용한 문화재 복원을 제안합니다. 
복원은 Image Completion 기술로 훼손된 부분만을 복원하는 것을 목표로 합니다. 
실험은 학습시키지 않은 문화재의 원본이 남아 있는 데이터를 원본이 유실, 회손 되었다고 가정하여 진행하였습니다. 
최종 목표는 loss값이 0.3정도에 수렴중인 현재 모델을 지속적으로 학습하고, 개선시켜 0.1에 가까워 질 때 까지 학습을 진행시켜 복원의 완성도를 높이는 것으로 합니다. 
이후에 실제로 원본이 남아있지 않아 복원에 어려움을 겪는 전문가에게 복원 형태를 제안하는 것을 목표로 합니다.

### 프로젝트 진행 과정요약

AI Hub의 문화재 데이터를 활용하여 학습데이터셋을 제작하고 수정하며, DCGAN기반 이미지 복원 알고리즘을 활용하여 문화재 복원을 시도하였습니다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220964066-bf6efda7-b1aa-47ad-bbea-408d8b71796f.PNG" width="800">
</p>

1. AI Hub의 문화재 데이터 중 석탑을 복원타켓으로 잡아 석탑이외의 이미지를 제거하는 전처리 과정을 거쳤습니다.
2. DCGAN을 활용하여 이미지를 학습시키는 과정에서 다양한 활성화 함수(Relu의 여러버전)을 사용하며 정확도를 높혀갔습니다.
3. 여러 석탑의 이미지를 복원하며 가장 정확도가 높고 육안으로 비슷한 이미지가 도출될때까지 반복하여 이미지를 복원하였습니다.

## 프로젝트 성과
- 추계학술대회 논문발표

### [딥러닝 기반 Transfer Learning 모델을 활용한 아보카도 분류 및 예측 시스템](https://github.com/geeksbaek/tesla-model-3-earlybird)(2022.10~2023.2)

`#Python` `#Selenium` `#Pandas` `#Tensorflow` `#Keras` `#Transfer learning` `#Streamlit` `#Ngrok`

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221216628-6896bf4c-c1dd-4579-b64b-aae75848068b.PNG" width="800">
</p>

타임지가 선정한 슈퍼푸드이며, 후숙 과일 중 하나인 아보카도는 현지가격과 국내 유통 가격이 크게 차이가 나는 식품 중 하나입니다. 이러한 아보카도의 분류과정을 자동화한다면 다양한 분야에서 인건비를 줄여 가격을 낮출 수 있을 것입니다.<br/> 
해당 프로젝트에서는 아보카도의 데이터셋을 크롤링을 통하여 제작하고, 딥러닝 기반 전이학습(transfer learning)모델을 다수 사용하여, 최적의 분류모델을 만드는 것을 목표로 합니다.<br/> 
제작한 데이터셋을 딥러닝 기반 전이학습모델에 직접 대입하고, 해당 모델의 하이퍼 파라미터를 Fine-tuning하며 진행하였습니다.<br/> 
제작된 모델은 아보카도의 이미지를 입력하였을 때, 해당 아보카도의 익은 정도를 99% 이상의 정확도로 분류하였으며, 해당 모델을 웹페이지에 입력하고 Ngrok을 통해 배포하여 누구나 사용할 수 있도록 하였습니다.

### 프로젝트 진행 과정요약
Selenium과 BeautifulSoup을 활용하여 데이터를 크롤링하는 방법으로 데이터셋을 제작하고,
전이학습 모델간의 비교를 통해 최적의 학습모델을 제작하였습니다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221218730-2dcd46a9-a6dd-44d1-88cf-f429c5fa1661.PNG" width="800">
</p>

1. 아보카도의 이미지를 크롤링하고 데이터셋을 제작합니다.
2. 아보카도 이미지의 다양한 특징을 추출하고 이를 통해 데이터셋을 전처리합니다.
3. 다양한 전이학습 기법을 비교하며 최적의 학습모델을 제작합니다.
4. 학습모델을 웹페이지에 입력하여 누구나 사용할 수 있도록 베포합니다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221220179-1bbf500c-d2b6-460d-9e8f-1ec3d7287939.PNG" width="800">
</p>

## 프로젝트 성과
- 학회 논문 등록 준비중

### [실시간 인구 데이터 분석을 통한 인파사고 방지 시스템 구축](https://github.com/geeksbaek/tesla-model-3-earlybird)(2022.12~2022.12)

`#Python` `#Selenium` `#BeautifulSoup` `#Pandas` `#Tensorflow` `#Keras` `#LSTM` `#Kakao` `#Ngrok`

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221231573-34d9350c-8a04-4b8f-9749-3e34782dfb3a.PNG" width="800">
</p><br/> 
지난 2022년 10월 29일 이태원 할로윈 축제 당시 많은 사람들의 축제 참가와 지리적 특징으로 인해 인파사고가 발생하였습니다.<br/> 
위험수준의 인구밀집이 예측되었지만 이를 시민에게 효율적으로 전달할 수 있는 시스템의 부재가 사고의 원인이었다는 전문가의 의견의 기사를 통해 도보되었습니다.<br/> 
이를 해결하기 위해 특정 시간/날짜/장소/행사등으로 인구 밀집도와 위험성을 파악하고 데이터를 분석함으로써 비슷한 사고를 예방하기 위해 프로젝트를 진행하였습니다.<br/>

서울시 행정동 단위 생활 인구데이터를 활용하여 전처리하고, **SNS의 메타데이터를 크롤링**하여 워드클라우드로 제작하여 크리스마스에 <br/>
가장 인구가 밀집될만한곳을 확인한 결과 명동이 가장 많은 빈도로 피드되어 명동이 가장 몰릴것으로 예측하였습니다.<br/> 
명동의 인구 밀집정도를 **LSTM**에 제작한 데이터셋을 학습시켜 실제 예측값과 현실에서 모인값을 비교한 결과 **오차율 약 0.1%** 로 예측하였습니다.<br/>
이렇게 예측한 결과를 위험수준에 따라 4단계로 나누고 해당 위치의 위험수준을 <br/>
사용자가 받아서 바로 확인 할 수 있도록 **카카오 메시지API**를 활용하여 결과를 전달하였습니다.<br/>

### 프로젝트 진행 과정요약
행정동 단위 서울 생활 인구데이터를 활용하여 전처리하고, Selenium과 BeautifulSoup을 활용하여 SNS의 메타데이터를 사용하여 특정날에 가장 인구가 몰리는 곳을 WordCloud를 활용하여 찾아내었습니다.

이후 LSTM을 활용하여 인구의 붐빔을 예측하고 붐빔의 정도에 따라 사용자에게 메시지를 보내줍니다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221232149-5dd691ea-3fb3-4893-b620-0e02c0cd1aff.PNG" width="800">
</p>

1. 서울시 행정동 단위 생활 인구데이터를 전처리하고 데이터셋을 제작합니다.
2. SNS의 메타데이터를 크롤링하며 워드클라우드를 제작하여 특정 시간/날짜/장소/행사에 가장 많이 인구가 몰릴 것으로 예측되는 특징을 찾습니다.
3. LSTM모델을 제작하여 데이터를 학습시키고 특정장소 특정시간에 인구가 몰리는 것을 예측합니다.
4. 위험도 수준을 분류하는 알고리즘을 제작하여 인구밀집 위험의 수준을 4단계로 나눕니다.
5. 카카오 메시지API를 활용하여 사용자에게 위험을 전달합니다.
