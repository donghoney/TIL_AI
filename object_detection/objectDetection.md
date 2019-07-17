**Object Detection History**

- ![object detection historyì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://hoya012.github.io/assets/img/object_detection_first/fig4_paper_trend_2019.PNG)



## YOLO v1

* **Simple is fast.**
  - 빠르다
  - 다른 알고리즘과 비슷한 정확도를 가진다.
  - 다른 도메인에서 좋은 성능을 보인다.

* 평가 지표
  * mAP
  * IoU

* 특징 : One Stage Method

  * R-CNN과 차이점은 한번만 네트워크에 들어간다 (end to end 방식)
  * ![one stage method yoloì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://user-images.githubusercontent.com/24144491/46718835-6d4a7100-cca7-11e8-996c-be10edaab670.png)

* Model

  ![ê´ë ¨ ì´ë¯¸ì§](https://curt-park.github.io/images/yolo/Figure3.JPG)

  * **24 Conv layers.** 앞에 20개의 Conv 레이어는 구글넷의 구성과 동일하고 3x3만 쌓는대신 1x1 reduction conv 레이어를 몇개 추가했다. 그리고 4개의 Conv 레이어를 더 쌓았다. Fast YOLO는 이보다 더 compact한 9개의 conv 레이어를 가진다.
  * 1x1 reduction conv layer
    - 채널 수 조절
    - 계산량 감소
    - 비선형성 증가

* Output

  ![yolo model architectureì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://miro.medium.com/max/1200/1*m8p5lhWdFDdapEFa2zUtIA.jpeg)

* Loss

  ![yolo lossì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://curt-park.github.io/images/yolo/lossFunction.JPG)



## SSD

출처 : https://taeu.github.io/paper/deeplearning-paper-ssd/

* SSD의 알고리즘을 한 문장으로 정리하면 위와 같다. **아웃 풋을 만드는 공간을 나눈다(multi feature map)**. 

* ```
  각 피쳐맵(아웃풋맵)에서 다른 비율과 스케일로 default box를 생성하고 모델을 통해 계산된 좌표와 클래스값에 default box를 활용해 최종 bounding box를 생성
  ```

* Model

![model](https://user-images.githubusercontent.com/24144491/48844097-47eb6f80-eddc-11e8-888c-2ae5d5a51e6a.JPG)

**Multi-scale feature maps for detection**

- 38x38, 19x19, 10x10, 5x5, 3x3, 1x1 의 피쳐맵들을 의미
- Yolo는 7x7 grid 하나뿐이지만 SSD는 전체 이미지를 38x38, 19x19, 10x10, 5x5, 3x3, 1x1의 그리드로 나누고 output과 연결
- 큰 피쳐맵에서는 작은 물체 탐지, 작은 피쳐맵에서는 큰 물체 탐지 (뒤의 2.2 training 부분에서 더 자세히 다룸)



**Convolutional predictiors for detection**

- 이미지부터 최종 피쳐맵까지는 Conv(3x3, s=2)로 연결
- Output과 연결된 피쳐맵은 3 x 3 x p 사이즈의 필터로 컨볼루션 연산. (Yolo v1은 Output과 Fully-Connected. 여기서 시간을 많이 단축시킴)
- 예측된 Output은 class, category 점수와, default box에 대응되는 offset을 구함



**Default boxes and aspect ratios**

- 6개의 피쳐맵(마지막 6개의 피쳐맵, Output과 직결된)은 각각 Conv(3x3x(#bb x (c + offset))) 연산을 통해 Output 형성
- Output은 각 셀당 #bb개의 바운딩박스를 예측

![training0](https://user-images.githubusercontent.com/24144491/48844099-47eb6f80-eddc-11e8-96c6-6c036cf9e4a7.png)

**Ground Truth Box.** 우리가 예측해야하는 정답 박스.

**Predicted Box.** Extra Network의 5 x 5 의 feature map에서 output (predicted box)를 위해 conv 연산을 하면 총 5 x 5 x (6 x (21 + 4))의 값이 형성된다. $$( = grid cell * grid cell * (number\ of \ bounding\ box * ( class + offset)))$$

**Default Box.** 하지만 5x5 feature map은 각 셀당 6개의 default box를 가지고 있다. 이때 default box의 $$w, h$$는 feature map의 scale에 따라 서로 다른 s 값과 서로 다른 aspect ratio인 a 값을 이용해 도출된다. 또 default box의 cx와 cy는 feature map size와 index에 따라 결정된다.



* Loss

![loss1](https://user-images.githubusercontent.com/24144491/48844092-4752d900-eddc-11e8-914b-71b33286b02c.png)

- ![loss2](https://user-images.githubusercontent.com/24144491/48844093-4752d900-eddc-11e8-8b08-2e2ae613ea78.png)
- $$x^p_{ij}$$ = {1,0} i번째 default box와 j번째 ground truth 박스의 category p에 물체 인식 지표. p라는 물체의 j번째 ground truth와 i번째 default box 간의 IOU 가 0.5 이상이면 1 아니면 0.
- $$N$$ 은 # of matched default boxes
- $$l$$ 은 predicted box (예측된 상자)
- $$g$$ 는 ground truth box
- $$d$$ 는 default box.
- $$cx$$, $$cy$$는 그 박스의 x, y좌표
- $$w, h$$는 그 박스의 width, heigth
- $$\alpha$$는 1 (교차 검증으로부터 얻어진)
- loss fucntion 은 크게 2부분, 클래스 점수에 대한 loss와 바운딩 박스의 offset에 대한 loss로 나뉜다.

![loss3](https://user-images.githubusercontent.com/24144491/48844095-4752d900-eddc-11e8-8b0c-2c7688f4d76e.png)

- 우리가 예측해야할 predicted box의 $$l^m_i(cx,cy,w,h)$$값들은 특이한 g햇 값들을 예측
- 이때 $$\hat{g}$$의 $$cx,cy$$는 default box의 $$cx$$와 $$w,h$$로 normalize된 것을 볼 수 있다.
- 이미 $$IoU$$가 0.5 이상만 된 것 부분에서 고려하므로, 상대적으로 크지 않은 값들을 예측해야하고 더불어 이미 0.5 이상 고려된 부분에서 출발하므로 비교적 빨리 수렴할 수 있을 것 같다.(이 부분은 주관적인 판단)
- 초기값은 default box에서 시작하지 않을까 싶음
- $$\hat{g}$$의 $$w, h$$도 마찬가지
- 예측된 $$l$$ 값들을 box를 표현할때(마지막 Test Output) 역시 default box의 offset 정보가 필요함.

![loss4](https://user-images.githubusercontent.com/24144491/48844096-47eb6f80-eddc-11e8-97ad-369978fc4c36.png)

- positive(매칭 된) class에 대해서는 softmax
- negative(매칭 되지 않은, 배경) class를예측하는 값으 $$\hat{c}^0_i$$ 값이고 별다른 언급은 없지만 background이면 1, 아니면 0의 값을 가져야함
- 최종적인 predicted class scores는 우리가 예측할 class + 배경 class 를 나타내는지표



**Choosing scales ansd aspect ratios for default boxes**

- default box를 위한 scale. 여래 크기의 default box 생성을 위해 다음과 같은 식 만듦.

![defaultbox](https://user-images.githubusercontent.com/24144491/48844091-4752d900-eddc-11e8-8c25-258bedfdd290.png)

- Smin = 0.2, Smax = 0.9
- 저 식에다 넣으면 각 feature map당 서로 다른 6개의 s 값들(scale 값들)이 나옴
- 여기에 aspect ratio = {1,2,3,1/2,1/3} 설정
- default box의 width는 $$s_k$$ x $$\sqrt{(a_r)}$$
- $$a_r$$ = 1 일경우 $$s’_k$$ = $$\sqrt{(s_k * s(k+1))}$$
- default box의 $$cx,cy$$는 $$k$$ 번째 피쳐맵 크기를 나눠 사용

**Hard negative Mining**

- 대부분의 default box가 배경이므로 $$x^p_{ij} = 0$$인게 많음
- 따라서 마지막 class loss 부분에서 positive : negative 비율을 1:3으로 뽑음 (high confidence로 정렬해서)

**Data augmentation**

- 전체 이미지 사용
- 물체와 최소 IOU가 0.1, 0.3, 0.5, 0.7, 0.9가 되도록 패치샘플
- 랜덤 샘플링하여 패치 구함

