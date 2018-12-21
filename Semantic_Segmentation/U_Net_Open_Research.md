### U-Net: Convolutional Networks for Biomedical Image Segmentation

Convolutional Neural Network

Segmentation

본문 링크 : http://openresearch.ai/t/u-net-convolutional-networks-for-biomedical-image-segmentation/149



메디컬 이미지 Segmentation 관련해서 항상 회자되는 네트워크 구조가 U-Net 입니다. End-to-End 로 Segmentation하는 심플하고 효과적인 방법입니다.

- 특히, data augmentation을 통해서 효율적으로 학습한다고 주장합니다.
- 제시한 아키텍쳐는 컨텍스트 정보를 잘 사용하면서도, 정확하게 로컬라이즈한다고 주장합니다.
- 다양한 의료 데이터 셋에서 [#sota](http://openresearch.ai/tags/sota) 의 성능을 보였습니다.
- End-To-End 구조로 속도도 빠릅니다.



## Architecture

![image](http://openresearch.ai/uploads/default/optimized/1X/ec0ac2e2d2df8f213b916453375ccee95a254ac3_1_616x500.png)

3x3 Convolution으로 주로 이루어져 있습니다. 각 Convolutional Block은 3x3 Convolution 2개로 이루어져있는데, 그 사이에 Dropout이 있습니다. 위 그림에서는 왼편의 각 Block은 3x3 Convolution 2개로 이루어진 것이 4개가 있는 형태라고 보시면 됩니다. 그리고 각 block은 max pool을 이용해 사이즈를 줄이면서 다음 block으로 넘어가게 됩니다.

반면 오른 편은 Convolutional Block에 up-convolution 이라 불리는 것을 앞에 붙였습니다. 즉, 왼편에서 줄어든 사이즈를 다시 올려가면서 Convolutional Block을 이용하는 형태입니다. 그리고, 아래쪽의 단계에서 얻어진 Feature들과 Concat하여 사용합니다. (요즘 유행하는 Residual 형태는 아닙니다. 이후의 FusionNet 에서는 그렇게 합니다)

즉, Multi Scale의 Object Segmentation을 위해서 다양한 크기의 Feature Map을 Concat할 수 있도록 down-sampling과 up-sampling을 순서대로 반복하는 구조로 되어 있습니다.

그리고, 왼편의 피쳐를 오른 편으로 보낼 때, 중앙 부분을 알맞은 사이즈로 Crop해서 보냅니다. 이는 Convolution을 하면서 border pixel에 대한 정보가 날아가는 것에 대한 양쪽의 보정이라고 합니다.

이러한 구조에 대해서 논문은 아래 레이어에서 얻어진 컨텍스트 정보가 상위 레이어의 피쳐에 Concatenate 되는 구조라고 설명합니다.

## Overlap-Tile Strategy

![image](http://openresearch.ai/uploads/default/optimized/1X/9db500ba287c18df96388b6250d9e6a571c0759b_1_690x375.jpg)

Neural Net Input으로 들어가게될 Patch의 경계 부분이 자연스럽지 않을 수 있으므로 위와 같이 Patch로 부터 나온 결과의 일부만을 사용하도록 합니다. 또 컨텍스트 유지를 위해 패딩은 '미러패딩(Mirror Padding)'을 사용하는데, 위 그림의 경계처럼 바깥 부분을 zero 값으로 채우는 것이 아니라 원본을 그대로 Mirroring 하는 것을 뜻합니다.

## Augmentation

Data Augmentation에서 중요하게 사용된 것은 크게 2가지로 파악됩니다.

### Elastic Deformation

적은 수의 이미지를 가지고 효과적으로 학습하기 위해 이 방식을 사용했다고 합니다. 티슈 조직 등의 실질적인 변형과 유사하다고 합니다.

### Weighted Cross Entropy + Data Augmentation

많은 셀을 세그먼테이션해야하는 문제에서의 도전 과제는 같은 클래스가 서로 인접해 있는 케이스입니다.





image.jpg1344x578 193 KB



위 그림의 A처럼 셀이 인접해 있으면, 각 셀과 배경을 구분하는 것은 쉽지만, 셀 각각을 서로 구분하는 것(instance segmentation)은 어렵습니다. 그래서 이 논문에서는 각 instance의 테두리와 테두리 사이가 반드시 배경이 되도록하는 처리를 합니다. 그러니까, 2개의 셀이 붙어있는 경우라고 하더라도, 그 둘 사이에는 반드시 배경으로 인식되어야할 틈을 만들겠다는 것입니다.

![image](http://openresearch.ai/uploads/default/original/1X/5f404882292f729534593e970b891346fe270f10.png)
[OpenCV : Morphological Transformations 6](https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html)

그렇게 하기 위해서 위와 같은 Morphological 연산을 사용해 위 그림처럼 테두리 부분을 조금 제거하고, 그림 D에서처럼 Weight Map을 만들어 학습이 어려울 수 있는 틈새 등에 가중치를 주도록 합니다. 틈새 들에 집중하게 하여 절대로 인스턴스가 붙지 않도록 하는 것입니다.

## Conclusion

UNet은 EM, ISBI 등의 데이터셋에서 아주 좋은 성능을 보여주었습니다. 좋은 네트워크 아키텍쳐에 Weighted Cross Entropy 라는 방식까지 적용해 Instance 구분까지도 가능하게한, 아주 효과적이고 실용적인 논문입니다.