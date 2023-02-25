### [딥러닝 기반 Transfer Learning 모델을 활용한 아보카도 분류 및 예측 시스템](2022.10~2023.2)

`#Python` `#Selenium` `#Pandas` `#Tensorflow` `#Keras` `#Transfer learning` `#Streamlit` `#Ngrok`

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221216628-6896bf4c-c1dd-4579-b64b-aae75848068b.PNG" width="800">
</p></br>

타임지가 선정한 슈퍼푸드이며, 후숙 과일 중 하나인 아보카도는 현지가격과 국내 유통 가격이 크게 차이가 나는 식품 중 하나입니다.</br>
이러한 아보카도의 분류과정을 자동화한다면 다양한 분야에서 인건비를 줄여 가격을 낮출 수 있을 것입니다.<br/> 
해당 프로젝트에서는 아보카도의 데이터셋을 크롤링을 통하여 제작하고, 딥러닝 기반 전이학습(transfer learning)모델을 다수 사용하여,</br>
최적의 분류모델을 만드는 것을 목표로 합니다.<br/> 
</br>
제작한 데이터셋을 딥러닝 기반 전이학습모델에 직접 대입하고, 해당 모델의 하이퍼 파라미터를 Fine-tuning하며 진행하였습니다.<br/> 
제작된 모델은 아보카도의 이미지를 입력하였을 때, 해당 아보카도의 익은 정도를 99% 이상의 정확도로 분류하였으며, </br>
해당 모델을 웹페이지에 입력하고 Ngrok을 통해 배포하여 누구나 사용할 수 있도록 하였습니다.

### 프로젝트 진행 과정요약
Selenium과 BeautifulSoup을 활용하여 데이터를 크롤링하는 방법으로 데이터셋을 제작하고,</br>
전이학습 모델간의 비교를 통해 최적의 학습모델을 제작하였습니다.</br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221218730-2dcd46a9-a6dd-44d1-88cf-f429c5fa1661.PNG" width="800">
</p></br>

1. 아보카도의 이미지를 크롤링하고 데이터셋을 제작합니다.
2. 아보카도 이미지의 다양한 특징을 추출하고 이를 통해 데이터셋을 전처리합니다.
3. 다양한 전이학습 기법을 비교하며 최적의 학습모델을 제작합니다.
4. 학습모델을 웹페이지에 입력하여 누구나 사용할 수 있도록 베포합니다.</br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221220179-1bbf500c-d2b6-460d-9e8f-1ec3d7287939.PNG" width="800">
</p>

## 프로젝트 성과
- 학회 논문 등록 준비중
