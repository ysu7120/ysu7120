## [홈베이스: 모션인식을 활용한 야구훈련 프로그램](https://github.com/geeksbaek/goinside) (2021.3~2021.6)

`#Python` `#Pandas` `#Tensorflow` `#Keras` `#Transfer learning` `#Teachable Machine` `#node.js` `#Text to speach`

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220950687-d3d60fba-e793-479f-9bc3-f07a7ec1b407.PNG" width="800">
</p></br>

전 세계적인 전염병인 코로나 바이러스의 확산으로 인구가 밀집하면 안되는 이유가 생겼으며,정부차원에서 5인이상 집합금지,</br>
운동시설이용제한 등의 제약을 걸었기 때문에 운동인들은 제대로 된 훈련을 할 수 없는 상황에 놓였습니다.</br> 
특히 다수가 필요한 운동과 이를 훈련하기 위한 티칭을 하는 과정에서 방역수칙을 어길 수 밖에 없기 때문에 이를 해결할 방안이 필요합니다.</br>

이러한 문제를 해결하기 위해 언제 어디서든 야구훈련을 받을 수 있는 프로그램을 연구하고 개발하였습니다</br>
해당 연구를 위해 Teachable Machine와 초음파센서를 활용하였습니다. </br>
스마트 베이스볼 트레이닝 프로그램은 웹사이트를 기반으로 제작하였습니다.</br>
카메라에 저장된 이미지센서가 사용자의 모션을 인식하고 해당 자세에 대한 티칭을 하여 훈련을 보조하며</br>
초음파센서를 활용하여 티칭의 정확도를 높였고, 모바일도 연동이 가능해 언제 어디서든 훈련이 가능합니다.</br>

### 프로젝트 진행 과정요약

구글의 티쳐블머신을 활용하고 카카오의 Text to speach APi를 사용하여 사용자가 연습상황을 확인할 수 있게 하였습니다.

1. 티쳐블머신을 활용하여 야구동작의 타격준비, 타격, 실패의 세가지 동작을 학습한 학습모델을 제작합니다.
2. 타격에 성공할때마다 카운트를 더하고 Text to speach APi를 활용하여 소리로 알려줍니다.
3. 웹 페이지에 기능을 이식하고 Netlify를 활용하여 베포하였습니다. </br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/221350769-270cf594-0a2d-4280-98eb-a9a4cbc03cab.PNG" width="400">
</p></br>
