## 삼성전자 DS부문 TECH DAY

#### 1) AI기술 관련

* A.I 

  * 종합기술원(장우석)

    * 반도체와 AI가 병합 -> SAIT로 병합
    * 딥러닝은 생물학적 구조 position과 유사
    * SAIT LAB 소개
      * 삼성 R&D 허브
      * Computer VIsion LAB
        * 자기중심인식 - selfie ,AT Emoji
        * 생체인식 - 지문, 홍채, 얼굴
        * 자율주행
        * 증강 현실
        * 가상 인간
        * 디지털 트윈

  * 스마트팩토리

    * cycleGAN을 활용해 공장에서 나오는 111개의 센서 feature 데이터와 실측 데이터를 input으로 상관성을 분석하여 생산공정에서 나오는 불량률 판정 예측을 높였다. 

    * Rsq -> 56% (cycleGAN)

    * Generator 모델을 학습하고 거기서 나오는 예측값과 실측값을 비교한 값

    *  Network Structure

    *  cycleGAN Generator Model

      * input -> conv(3x3) -> pooling ————————————> ㅣ——— ㅣ-> 0,1

           l       -> conv(5x5) -> pooling ————————————> ㅣ            ㅣ

           l       -> conv(7x7) -> pooling ————————————> ㅣ            ㅣ

           ㄴ  ——————————————————————— > ㅣ————ㅣ

    * cycleGAN Discriminator Model

      * Generator와 동일하지만 참거짓만 판별

  * 자율주행

    * object Detection, Scene Segmentation, 3D object Detection, Visual Tracking ...
    * 상황(나라, 날씨, corner case 등등..), 속도, 안전성, 하드웨어 제약 -> 고려!!
    * Object Detection
      * Faster R-CNN 기반 앞단에 inception network로 추가 구성(I-FRCNN+)
      * 더 빠르게 하기 위해 SqueezeNet과 InceptionNet을 병합
      * FHD 기준 15fps 달성
      * ROI Ensemble 기법 활용 . 30fps 달성
      * Selective Knowledge Distillation : Teacher Network 를 활용. unlabeled data에서 label 추출 후 선택적으로 활용
    * Segementation
      * Nfs-Seg(Samsung system lsi)
      * SegNet , ENet, PSNet 등등 보다 빠르고 정확한 성능을 보였음. 조사 필요
      * DeepLab V3+가 성능이 2018년 11월 기준으로 가장 정확하다. 
    * 3D Object Detection
    * Visual Tracking



