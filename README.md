### [실시간 인구 데이터 분석을 통한 인파사고 방지 시스템 구축](2022.12~2022.12)

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
행정동 단위 서울 생활 인구데이터를 활용하여 전처리하고, Selenium과 BeautifulSoup을 활용하여 SNS의 메타데이터를 사용하여</br>
특정날에 가장 인구가 몰리는 곳을 WordCloud를 활용하여 찾아내었습니다.</br>

이후 LSTM을 활용하여 인구의 붐빔을 예측하고 붐빔의 정도에 따라 사용자에게 메시지를 보내줍니다.</br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221232149-5dd691ea-3fb3-4893-b620-0e02c0cd1aff.PNG" width="800">
</p>

1. 서울시 행정동 단위 생활 인구데이터를 전처리하고 데이터셋을 제작합니다.
2. SNS의 메타데이터를 크롤링하며 워드클라우드를 제작하여 특정 시간/날짜/장소/행사에 가장 많이 인구가 몰릴 것으로 예측되는 특징을 찾습니다.
3. LSTM모델을 제작하여 데이터를 학습시키고 특정장소 특정시간에 인구가 몰리는 것을 예측합니다.
4. 위험도 수준을 분류하는 알고리즘을 제작하여 인구밀집 위험의 수준을 4단계로 나눕니다.
5. 카카오 메시지API를 활용하여 사용자에게 위험을 전달합니다.
