# CNN을 활용한 주요 Model - (4) : Semantic Segmentation

#### 14 Jul 2018 | [CNN](https://reniew.github.io/18/#cnn)

가져온 페이지 주소 : https://reniew.github.io/18/

#### CNN을 활용한 주요 Model - (4) : Semantic Segmentation

CNN을 활용한 최초의 기본적인 Model들 부터 계속해서 다양한 구조를 가지는 많은 모델들이 계속해서 나오고 있다. 이번 포스트에서는 아래의 분류를 기준으로 CNN의 주요 모델들에 대해서 하나씩 알아 보도록 하겠다.

* Modern CNN
  * LeNet
  * AlexNet
  * VGG Nets
  * GoogLeNet
  * ResNet
* Image Detection
  - RCNN
  - Fast RCNN
  - Faster RCNN
  - SPP Net
  - Yolo
  - SDD
  - Attention Net
* Semantic Segmentation
  - **FCN**
  - **DeepLab v1, v2**
  - U-Net
  - ReSeg
* Image Captioning



이번 포스트에서는 Sematic Segmentation을 위해 만들어진 모델들에 대해서 소개한다. Semantic Segmentation 문제에 대해 먼저 소개를 하자. 우선 Segmentation을 먼저 설명하면, Detection이 물체가 있는 위치를 찾아서 물체에 대해 Boxing을 하는 문제였다면, Segmentation이란, Image를 Pixel단위로 구분해 각 pixel이 어떤 물체 class인지 구분하는 문제다.

아래 그림이 Image문제에 대한 분류를 잘 설명했다.![image task](http://ataspinar.com/wp-content/uploads/2017/11/deeplearing_types.png)*출처 : http://ataspinar.com/2017/12/04/using-convolutional-neural-networks-to-detect-features-in-sattelite-images/*

그리고 Segmentation은 두가지로 나뉜다. Semantic Segmentation과 Instance Segmentation로 구분되는데 이번에 소개할 Semantic Segmentation은 pixel단위로 물체를 구분한뒤 각각의 물체가 어떤 class인지만 구분 하는 문제고, Instance Segmentation이란 같은 class이더라도 다른 것이라면 구분하는 문제라 할 수 있다.



![seg](http://research.sualab.com/assets/images/image-recognition-overview-2/segmentation-types.svg)(*출처 : http://research.sualab.com/computer-vision/2017/11/29/image-recognition-overview-2.html*) *Instance Segmentation에서는 각각의 사람들을 다른 사람으로 구분한 것을 볼 수 있다.*

Segmentation은 자율주행 자동차에서 매우 중요한 기술로 많은 모델들이 소개 되었다. 많은 모델 중 몇가지만 알아보도록 한다.

1. **FCN**

FCN이란 Fully Convolutinal Network의 약자로, 2015년 [Fully Convolutional Network for Semantic Semgentation](https://arxiv.org/abs/1411.4038)에서 소개됬다. FCN은 최초의 pixelwise end to end 예측 모델로 많은 의미를 가진다.

FCN에서 가장 중요한 부분은 이름에서 나와있듯 Convolution layer만을 사용했다는 것이다. 기본적으로 CNN 모델에서는 모델 뒤쪽에서 Fully Connected layer가 나오는데, FCN에서는 FC Layer 대신 1x1 Convolution layer를 사용했다는 점이다. 이렇게 사용한 이유에 대해 추측을 해보자면, 우선 Fully Connected layer를 사용하기 위해서는 고정된 input size를 가질 수 밖에 없다. 그리고 FC layer를 지나는 순간 각 pixel에 대한 위치정보는 소실된다. 따라서 FCN은 모든 Network를 Convolution layer만 사용함으로써 input size의 제한을 받지 않고, 위치정보를 보존할 수 있게 되었다.

FCN의 Architecture는 크게 3단계정도로 나뉜다.

![FCN](https://i.imgur.com/uCL3VC5.jpg)

- Feature를 추출하는 Convolution 단계
- 뽑아낸 future에 대해 pixelwise prediction 단계
- classification을 한뒤 각 원래의 크기로 만들기 위한 Upsampling 단계

이러한 단계를 거친 후 각 pixel에 class따라 색칠을 한뒤 Segmentation 결과를 보여준다. 세부적인 Architecture에 대한 소개를 하기보단 여기서 사용된 주요한 개념들에 대해서 소개를 한다.

- **Convolutionalization**

![fcn2](https://i.imgur.com/Vm5oHz0.jpg)

FCN은 Fully Connected Layer를 사용하지 않고 1x1 Convolution Layer를 사용했다고 했는데, 논문에서 이러한 1x1 Convolution을 Convolutionalization이라 표현했다. 그림 중간의 256크기의 matrix가 4096의 크기로 reshape된 것을 볼 수 있다. 이렇게 reshape을 한 후 여기에 1x1 Convolution을 진행한다. 하지만 이렇게 크기를 줄인다면 output dimension이 줄어들어 원래 크기의 image에 대해 segmentation을 할 수 없게 된다. 따라서 다시 크기를 원래 size로 만들어 줘야 한다. 즉 Upsampling 단계가 필요하다.

**Upsampling**

FCN에서 feature extraction을 크기가 줄어 하나의 pixel이 원래 image의 32x32크기를 나타낸다. 여기서 다시 크기를 키우기 위해 32x32의 크기로 바로 만든다면 많은 정보들이 소실되고 정확도 또한 떨이지게 된다. 따라서 여기서는 1/32 크기만을 이용하는 것이 아니라 이전 Layer에서의 1/16크기와 1/8에서의 값도 같이 사용한다. 이전의 layer들의 값을 다른 연산을 거치지 않고 Skip하여 마지막에서 같이 합쳐서 사용하게 된다. 따라서 이러한 과정을 ‘Skip Layer’ 혹은 ‘Skip Connection’이라 부른다.

![fcn3](https://i.imgur.com/A1mCLJO.jpg)

그림을 보면 이전의 Pooling Layer의 값을 가져와 더하는 것을 볼 수 있다. 이렇게 여러 크기의 값들을 Upsampling 한 것들을 합치는 것의 효과는 다음의 그림을 통해 확인하자.




![fcn4](https://i.imgur.com/lAFLKkw.jpg)

1. **DeebLab v1, v2, v3**

최근 Segmentation 분야에서 State-of-art한 성능을 보여주는 DeepLab의 3번 째 versio이 오픈소스로 공개가 되어 많은 사람들의 주목을 받았다.([DeepLab. v3 Github](https://github.com/tensorflow/models/tree/master/research/deeplab))

DeepLab은 2015년 처음으로 나온 DeepLab. v1 인 Semantic Image Segmentation With Deep Convolutional Nets And Fully Connected CRFs([PaPer](http://arxiv.org/pdf/1412.7062.pdf))을 시작으로 2016년 DeepLab v2([Paper](http://arxiv.org/pdf/1606.00915.pdf)), 그리고 올해 오픈소스로 나온 DeepLab v3까지 Semantic Segmentaion분야에서 높은 성능을 보여줬다.

DeepLab v2는 v1과 Atrous Convolution과 Fully Connected CRF(Conditional Random Field)를 사용한다는 점에서 비슷하지만 v2에서는 Atrous spatial pyramid pooling을 사용해서 Multiple sclae에 대응하는 방법이 개선되었다.

여기서는 DeepLab v2만 다룰 예정이다. v1과 v3에 대해서는 위의 링크를 참고하길 바란다.

DeepLab. v2에서 주목했던 문제들은 다음과 같다.

* Reduced feature resolution
  - **Atrous Convolution**
* Reduced Local accuracy
  - **CRF(Conditional Random Field)**
* Existence of objects at multiple scale
  - **Atrous Spatial pyramid pooling**

위 3가지 기술들에 대해 하나씩 살펴보자.

* Atrous Convolution Classification 문제와는 달리 Image를 Pixel별로 구분해야 하는 Segmentaion에서는 CNN의 Layer가 깊어질수록 Feature의 크기가 작아지는 특징이 단점으로 작용했다. 따라서 이러한 Reduced Feature Resolution 문제를 Atrous Convolution을 사용해 해결했다.

Atrous Convolution이란 의미적으로 구멍 뚫린 Convolution이라 해석하면 될 것이다. 아래 논문의 그림을 보자.

![atrous](https://t1.daumcdn.net/cfile/tistory/99107B33598343D524)

그림의 위쪽은 일반적인 Convolution과정이고 아래는 Atrous Convolution을 의미한다. 중간중간 Hole(중간중간을 0으로 만듬)을 만들어서 좀 더 먼 쪽과 Convolution을 진행한다. 이런 과정을 통해 모델은 좀더 Dense한 Feature를 학습한다.

![atours2](https://t1.daumcdn.net/cfile/tistory/99B70033598344A324)

위의 그림을 보면 Atrous Convolution의 효과가 직관적으로 보인다. 아래의 빨간 화살표가 rate=2로 Atrous Conv를 실행한 것인데 위의 일반적인 Conv에 비해 Receptive Field 가 넓어 실제 그림과 비슷한 region을 얻는 것을 볼 수 있다.

- Conditional random field

이제 큰 그림을 줄이면서 각 pixel에 대한 feature를 얻었으니 다시 Segmentation을 위해 다시 image를 늘리는 과정을 해야 한다. 아래 그림과 같이 Bilinear Interpolation만을 수행하면 원래 Image의 Segment를 정확히 얻지 못하는 것을 볼 수 있다.

![aspp](https://i.imgur.com/msrY2vf.jpg)

따라서 Conditinal Ramdom Field를 사용해서 더욱 정확한 Segment를 얻는다. 아래의 그림은 CRF를 반복할 수록 더욱 정확한 Segment를 얻는 과정을 보여준다.![at3](https://t1.daumcdn.net/cfile/tistory/999FF63359834AE52D)

- Atrous spatial pyramid pooling(ASPP)

DeepLab v1에서는 크기가 다른 물체들이 있을 떄 이를 잘 Segmentation하지 못하는 문제가 있었는데 v2에서는 ASPP를 사용해서 이를 해결했다.

ASPP란 특정 레이어 대해서 Atrous Convolution을 여러 rate를 이용해서 진행한 후 결과들을 합치는 방법이다. 아래의 그림을 보자.

![at4](https://t1.daumcdn.net/cfile/tistory/99DCFD33598348311E)

rate 6, 12, 18, 24로 각각 convolution을 한 후 이들을 합치는 과정을 Atrous Spatial Pyramid Pooling 이라 한다.

위의 3가지 방법들을 합친 DeepLab v2의 전반적인 진행과정은 다음 그림과 같다.

![at_final](https://t1.daumcdn.net/cfile/tistory/99ABA333598349D501)

여기까지가 DeepLab에 대한 설명이였다.

출처

- [모두의 연구소 논문 리뷰 블로그](https://modulabs-biomedical.github.io/FCN)
- [라온피플 블로그](https://laonple.blog.me/220991967450)
- [SweetzLab의 기술블로그](http://dogfoottech.tistory.com/169)