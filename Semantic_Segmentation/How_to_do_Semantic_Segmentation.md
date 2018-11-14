## How to do Semantic Segmentation using Deep Learning 

출처 : https://medium.com/nanonets/how-to-do-image-segmentation-using-deep-learning-c673cc5862ef

### Sementic Segmentation이란?

Semantic segmentation은 거친 추세에서 좋은 추론으로 진행하는 자연스러운 단계이다.

1. 첫 단계는 전체 input에서 예측을 하는 분류로 지정될 수 있다.
2. 다음 단계는 localization / detection 인데, 클래스들 뿐만 아니라, 클래스 각각의 위치에 기반해서 추가적인 정보를 제공한다.
3. 마지막으로, semantic segmentation은 모든 픽셀에 대한 레이블을 추정하여 밀도가 높은 예측을함으로써 세밀한 추론을 달성하므로 각 픽셀은 그 객체를 둘러싸는 객체 영역의 클래스로 레이블링 된다.

![img](https://cdn-images-1.medium.com/max/2000/1*MQCvfEbbA44fiZk5GoDvhA.png)

컴퓨터 비전 분야에서 충분한 기여를 했던, deep network를 리뷰할만한 가치가 있다는 것을 보여주고,

그 networks들은 Semantic segmentation 시스템의 기반이 된다.

아래와 같다.

* AlexNet : 2012 ImageNet Competition에서 84.6%의 정확도로 우승했던 CNN 모델이다. 5개의 convolutional layers와 max-pooling 1개, ReLU로 non-linearities를 표현했고, 3개의 fully-convolutional layer를 가지고 있고, dropout을 사용했다.
* VGG-16 : 이건 옥스포드에서 만든건데, 2013년 ImageNet Competition에서 92.7%의 정확도로 우승했다. 이건 첫번째 레이어에 큰 수용 field들을 가진 적은 레이어대신에, 작은 수용하는 field들을 가진 convolution layer stack을 사용한다. 
* GoogLeNet : 구글 네트워크, 2014년 ImageNet Competition에서 93.3%의 정확도로 우승했던 모델이고, 22개의 레이어를 갖고 있고, 새롭게 inception module을 도입했다. 
* ResNet : 이것은 마이크로 소프트 에서 만들었고, 2016년도 ImageNet Competition에서 96.4%의 정확도로 우승했다. 152개의 layer로 잘 알려져 있고, residual block을 도입했다. Residual blocks는 엄청 깊은 구조에서 학습이 잘 안되는 문제를 레이어들을 다음 레이어의 input으로 붙여넣는 skip connection으로 해결하는 구조이다.

![img](https://cdn-images-1.medium.com/max/1600/1*7UXzOt97gQAmCCOL58hgAw.png)



### 기존 Semantic Segmentation 접근 방법은 뭘까?

일반적인 semantic segmentation 아키텍처는 광범위하게 encoder와 decoder로 이루어진 network로 생각될 수 있다.

* encoder는 보통 VGG/ResNet 같은 pre-trained된 classification 네트워크들이고 decoder가 뒤따른다.
* decoder의 임무는 의미있는 분류를 얻기 위해 encoder에 의해 학습 된 차별적인 특징 (낮은 해상도)을 픽셀 공간 (더 높은 해상도)에 의미적으로 투사하는 것이다.



### 1 - Region-Based Semantic Segmentation

Region-Based method들은 일반적으로 인식을 사용한 segmentation pipline을 따른다. 이 파이프라인은 이미지에서 자유 형식 영역을 추출하고 설명 한 다음 영역 기반 분류를 수행한다.

테스트할 때, 그 영역 기반의 예측은 픽셀 예측으로 변형된다, 가장 높은 스코어를 가진 지역에 포함된 픽셀에 labeling하는 방식이다.

#### R-CNN(Regions with CNN feature)

![img](https://cdn-images-1.medium.com/max/1200/1*ccdPdFdcSqkxRg-7902Uuw.jpeg)

R-CNN은 지역 기반의 가장 대표적인 방법중 하나이다. 이것은 semantic segmentation을 object detection 결과에 기반하여 수행한다. 구체화 하기위해, R-CNN은 처음에 많은 양의 객체 제안을 추출하기 위해 선택적 search를 하고 그로부터 나온 CNN feature들을 계산한다.

마지막으로, 클래스 특정의 선형 SVM을 사용해 각각의 영역을 분류한다. 이미지 분류를 위해 하던 전통적인 CNN구조와 비교했을 때, R-CNN은 object detection과 image segmentation과 같은 더 복잡한 task를 할 수 있다 . 그리고 이것은 두 분야의 중요한 토대가됩니다. 또한 R-CNN은 AlexNet, VGG, GoogLeNet 및 ResNet과 같은 CNN 벤치 마크 구조 위에 구축 될 수 있다.



Image segmentation task를 위해 , R-CNN은 2가지 타입의 특징을 각각의 영역에서 추출하는데,

전역 특징과 전경 특징, 이 두가지가 영역 특징과 함께 결합되면, 더 좋은 성능을 보여준다는 것을 확인했다.

R-CNN은 높은 구분적인 CNN 특징들을 사용해 퍼포먼스 개선을 보여줬다. 그러나, 이것은 segmentation에서 몇가지 단점이 있다.

1. The feature는 segmentation과 호환되지 않는다.
2. The feature는 정확한 테두리 생성을 위한 충분한 공간 정보를 포함하지 않는다.
3. sement 기반의 제안서를 생성하는 것은 시간이 걸리고, 최종 성능에 큰 영향을 준다.

이런 병목 현상들 때문에,이 문제를 해결하기 위한  최근 연구들(SDS, Hypercolumns, Mask R-CNN)이 제안되었다.



### 2  - 	Fully Convolutional Network-Based Semantic Segmentation

![img](https://cdn-images-1.medium.com/max/1200/1*Aa2fKFN2PEKmMQoy8ps-lw.png)

오리지널 Fully Convolutional Network(FCN)은 픽셀에서 픽셀로 mapping하는 것을 학습시킨다. FCN Network 파이프라인은 기본 CNN을 확장시킨다. 주요한 개념은 전통적인 CNN을 