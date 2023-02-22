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

- [Convolutional LSTM 알고리즘 이용한 컴퓨터 비전 센서 기반 사거리 교통체증 예측 시스템(2020.10~2021.11)](https://github.com/geeksbaek/portfolio#pokedex-2018)
- [홈베이스: 모션인식을 활용한 야구훈련 프로그램 (2021.3~2021.6)](https://github.com/geeksbaek/portfolio#goinside-20162018)
- [문화재 복원을 위한 DCGAN 기반 Image Completion 시스템 (2022.1~2022.10)](https://github.com/geeksbaek/portfolio#ourchess-2012)
- [딥러닝 기반 Transfer Learning 모델을 활용한 아보카도 분류 및 예측 시스템 (2022.10~2023.2)](https://github.com/geeksbaek/portfolio#etc)
- [실시간 인구 데이터 분석을 통한 인파사고 방지 시스템 구축 (2022.12~2022.12)](https://github.com/geeksbaek/portfolio#etc)

## [Convolutional LSTM 알고리즘 이용한 컴퓨터 비전 센서 기반 사거리 교통체증 예측 시스템](https://github.com/geeksbaek/pokedex) (2020.10~2021.11)

`#Python` `#Pandas` `#Numpy` `#Tensorflow` `#Keras` `#Data` `#LSTM`

### 요약

교통체증으로 인해 생기는 여러가지 문제를 해결하기 위하여, 서울시 교통데이터를 분석하여 시간당 차량이동량을 예측하고 이에 근거하여, 
교통체증을 완화하는 알고리즘을 제작하였습니다.

### 자세히

교통체증을 완화 알고리즘은 서울시 교통데이터를 분석하여 수정하며 진행하였습니다.

<p align="center">
  <img src="https://raw.githubusercontent.com/dialogflow/resources/master/images/overview.png" width="1000">
</p>

1. 서울시 교통데이터의 입출 교통데이터를 전처리하여 학습할 수 있도록 제작합니다.
2. 준비된 데이터를 LSTM 모델에 입력시켜 특정시간의 정보를 예측할 수 있도록 학습시킵니다.
3. 학습시킨 데이터를 활용하여 특정시간의 차량이동량을 예측하고 제작한 알고리즘을 도로교통에 대입시켜 교통체증을 완화합니다.



## [홈베이스: 모션인식을 활용한 야구훈련 프로그램](https://github.com/geeksbaek/goinside) (2021.3~2021.6)

`#Python` `#Pandas` `#Tensorflow` `#Keras` `#Transfer learning` `#Teachable Machine` `#node.js`

### 요약

전 세계적인 전염병인 코로나 바이러스의 확산으로 인구가 밀집하면 안되는 이유가 생겼으며, 정부차원에서 5인이상 집합금지, 운동시설이용제한 등의 제약을 걸었기 때문에 운동인들은 제대로 된 훈련을 할 수 없는 상황에 놓였습니다. 특히 다수가 필요한 운동과 이를 훈련하기 위한 티칭을 하는 과정에서 방역수칙을 어길 수 밖에 없기 때문에 이를 해결할 방안이 
필요합니다.

이러한 문제를 해결하기 위해 언제 어디서든 야구훈련을 받을 수 있는 프로그램을 연구하고 개발하였으며, 해당 연구를 위해 이미지센서와 초음파센서를 활용하였습니다. 
스마트 베이스볼 트레이닝 프로그램은 웹사이트를 기반으로 실행가능하며 카메라에 저장된 이미지센서가 사용자의 모션을 인식하고 해당 자세에 대한 티칭을 하여 훈련을 보조하며, 
초음파센서를 활용하여 티칭의 정확도를 높일 수 있으며, 모바일도 연동이 가능해 언제 어디서든 훈련이 가능합니다.

### 자세히



## [ourchess](https://github.com/geeksbaek/ourchess) (2012)

[![GitHub stars](https://img.shields.io/github/stars/geeksbaek/ourchess.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/geeksbaek/ourchess/stargazers/)

`#javascript` `#nodejs` `#websocket` `#gcp`

### 요약

ourchess는 웹 기반으로 개발된 멀티플레이어 1:1 체스게임입니다. Backend는 node.js, Frontend는 JavaScript와 약간의 jQuery를 사용하여 개발했으며, HTML5 Canvas API로 2D 이미지를 그려 그래픽을 구현하였습니다. UI는 Bootstrap을 사용하여 구성하였으며, 사용자들은 Socket.io의 websocket으로 서로 실시간으로 통신합니다. 현재 [Google Cloud Run](https://ourchess-fyinkdszda-uc.a.run.app/)에서 서비스 중입니다.

### 자세히

멀티플레이어 게임이므로, 사용자들은 각자 방을 생성하여 동시에 게임을 플레이할 수 있습니다. socket.io가 서버에 연결된 소켓들을 네임스페이스로 구분하는 기능을 지원하는 덕분에 방을 쉽게 구현할 수 있었습니다. 방을 생성하면 랜덤한 문자열이 생성되는데, 이 문자열을 네임스페이스로 사용하여 방을 구분 짓습니다.

<p align="center">
  <img src="http://i.imgur.com/XhWvXj2.png" width="170"> <img src="http://i.imgur.com/M5uApvG.png" width="170">
</p>

멀티스크린 지원도 해상도가 변경되면 화면 방향을 계산한 뒤 UI를 재배치하여 모바일 환경에서도 자연스럽게 보이도록 하였습니다. 당시에는 CSS 미디어 쿼리같은 기능이 없었기 때문에 jQuery 기반으로 구현했던 것으로 기억합니다.

이 체스 게임의 주요 특징은 플레이어가 기물을 움직이는 모습이 다른 플레이어에게 실시간으로 전달된다는 것입니다. 이를 자연스럽게 구현하기 위해 크게 두 가지 테크닉을 사용했습니다.

1. 체스판 위에서 기물을 드래그하는 동안 마우스 좌표를 실시간으로 websocket을 통해 브로드캐스트합니다. 현재 코드에서는 mousemove 이벤트가 발생했을 때 좌표 브로드캐스트 하게 되어있는데, 지금 생각해보니 mousemove 이벤트 대신 mousedown, mouseup 같은 이벤트의 리스너에 브로드캐스트를 수행하는 setInterval 함수를 동적으로 생성 및 파괴하는 코드를 구현하는 것이 더 나아 보입니다. mousemove 이벤트는 초당 60회 이상 발생할 수 있는데 그렇게 자주 브로드캐스트 하는 것은 낭비라고 생각됩니다)

2. 좌표를 브로드캐스트 받은 클라이언트들은 기물이 움직이는 것을 구현하기 위해 Canvas를 다시 그려야 합니다. 이때 체스 보드가 그려져 있는 메인 Canvas를 다시 그리는 대신 별도의 Canvas를 생성하여 이곳에 움직일 기물을 그린 뒤 CSS Position을 변경하여 움직이도록 했습니다. Canvas를 초당 60회 이상 다시 그리는 것은 비효율적일뿐더러 그래픽 또한 부자연스럽게 보이기 때문에 이 트릭을 사용하였습니다.

<p align="center">
  <img src="http://i.imgur.com/zqpfsa5.gif" width="400">
</p>

### 비하인드 스토리

온라인 멀티플레이어 체스 게임을 만들기로 한 뒤 제가 가장 중요하게 생각한 목표는 "비록 컴퓨터를 사이에 놓고 두는 체스지만 진짜 사람을 마주보고 있다는 기분을 들게 하자" 였습니다. 어떻게 해야 그런 기분을 들게 할 수 있을지 고민한 끝에 상대가 움직이고 있는 기물의 움직임을 실시간으로 보여주기로 했습니다. 이 아이디어를 실현하기 위해 많은 시행착오를 거치면서 기술을 개선한 끝에 만족스러운 결과를 얻게 되었습니다.

개발에서 시간이 가장 많이 들어간 부분은 기물의 움직임이 체스의 규칙을 위반하는지 검사하는 코드를 작성하는 부분이었습니다. Stalemate, Threefold repetition, Promotion 등 대부분의 체스 규칙을 검사하며, 규칙에 위반되는 움직임은 허용되지 않도록 하였습니다. 사실 이 부분은 서버에서 검사해야 하지만, 개발 편의상 클라이언트에서 검사하게 했습니다. 제대로 서비스하려면 이러한 부분은 보완을 거쳐야 합니다.

이 어플리케이션은 제가 처음으로 개발한 프로그램이어서 의미가 남다릅니다. 대학교 1학년을 마친 뒤 군 휴학 중에 한 달 동안 집에 틀어박혀서 개발했는데, 질문하거나 조언을 구할 사람이 없었기 때문에 모든 것을 혼자서 찾아 배워야 했습니다. 이 과정에서 스스로 문제를 해결하는 능력을 기르고, 혼자서도 하나의 프로젝트를 완성할 수 있다는 자신감을 얻었습니다.

### 사용해보기

[이곳](https://ourchess-fyinkdszda-uc.a.run.app/)에서 직접 플레이해보실 수 있습니다. 플랫폼으로 사용 중인 Google Could Run이 아직 WebSocket을 완전히 지원하지 않아 모든 기능이 동작하지는 않습니다.

## Etc

### [Tesla Model 3 Earlybird](https://github.com/geeksbaek/tesla-model-3-earlybird)

`#react` `#firebase`

테슬라 모델 3의 한국 출시를 기다리며 개발한 서비스입니다. 최신 환율 정보를 바탕으로 예상 구매 가격을 계산해줍니다. 최근 모델 3가 정식 오픈하게 되면서 지원을 중지하게 되었습니다. [여기](https://geeksbaek.github.io/tesla-model-3-earlybird/#/)에서 호스팅은 유지되고 있습니다.

### [Project Arche](https://github.com/geeksbaek/Project-Arche)

`#go` `#web_scraping` `#gcp` `#polymer` `#restful`

아키에이지라는 MMORPG 사용자들에게 도움을 주기 위해 개발한 서비스입니다. 지금은 서비스가 중지된 웹 어플리케이션 버전과 현재 서비스되고 있는 API 버전으로 나누어져 있습니다. [여기](https://project-arche.appspot.com/api/auctions/total/%EB%AA%A9%EC%9E%AC/10)에서 API 버전을 테스트할 수 있습니다.

<p align="center">
  <img src="http://i.imgur.com/hvVFxEz.gif" width="300"> <img src="http://i.imgur.com/YzLMsAp.gif"  width="300">
</p>

### [go-arp-spoofer](https://github.com/geeksbaek/go-arp-spoofer)

`#go` `#network`

대학교에서 "ARP Spoofing을 통한 ID, PASSWORD 파싱" 이라는 주제로 개발한 ARP 스푸핑 툴입니다. Go의 동시성 특징을 적극적으로 활용하여 개발되었습니다. 동시에 복수의 인터페이스, 복수의 세션을 동시에 공격할 수 있는 특징이 있습니다. 자세한 설명은 [PPT](https://onedrive.live.com/redir?resid=75AF0E3BAC6794A2!5977&authkey=!AMk1emIWlg96vk8&ithint=file%2cpptx)에 소개되어 있습니다.

### [go-network-monitoring](https://github.com/geeksbaek/go-network-monitoring)

`#go` `#network`

대학교에서 개발한 네트워크 트래픽 통계 툴입니다. 마찬가지로 Go로 개발하였으며, 네트워크 in-path 구간에서 사용할 수 있습니다. 최적화를 고려하지 않고 간단하게 만들었기 때문에 일정 트래픽 이상이 발생하는 네트워크에서는 정상적인 통계를 내지 못할 수 있습니다.

<p align="center">
  <img src="http://i.imgur.com/FkjatPv.png">
</p>
