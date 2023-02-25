## [문화재 복원을 위한 DCGAN 기반 Image Completion 시스템 ](2022.1~2022.10)

`#Python` `#Pandas` `#Tensorflow` `#Keras` `#DCGAN` `#Image Completion` 

### 요약

<p align="center">
  <img src="https://user-images.githubusercontent.com/80941367/220962507-6a597f00-dfd2-434c-be6d-20299b52101a.PNG" width="800">
</p></br>

2008년 대한민국 국보1호 숭례문 화재 사건과 미륵사지 석탑의 복원 실패 사례로 문화재 보존과 복원의 중요성이 강조되었습니다. </br>
현재 인공지능 기술의 발전으로 다양한 방법으로 문화재 복원이 이루어지고 있습니다. </br>

해당 프로젝트는 DCGAN(Deep Convolutional Generatice Adversarial Network)과 Image Completion 기술을 이용한 문화재 복원을 제안합니다. </br>
복원은 Image Completion 기술로 훼손된 부분만을 복원하는 것을 목표로 합니다. </br>
실험은 학습시키지 않은 문화재의 원본이 남아 있는 데이터를 원본이 유실, 회손 되었다고 가정하여 진행하였습니다. </br>
최종 목표는 loss값이 0.3정도에 수렴중인 현재 모델을 지속적으로 학습하고, </br>
개선시켜 0.1에 가까워 질 때 까지 학습을 진행시켜 복원의 완성도를 높이는 것으로 합니다. </br>
이후에 실제로 원본이 남아있지 않아 복원에 어려움을 겪는 전문가에게 복원 형태를 제안하는 것을 목표로 합니다.</br>

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
