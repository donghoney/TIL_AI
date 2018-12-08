## [[Review\] Cascaded FCN - Automatic Liver and Tumor Segmentation of CT and MRI Volumes Using Cascaded Fully Convolutional Neural Networks](http://cdm98.tistory.com/37)

2018.12.07 15:11

![img](https://t1.daumcdn.net/cfile/tistory/9935C93C5C0A0DDA1C)

2017.02.23에 발표된 후 국제 의료영상 심포지움인 **ISBI 2017**에 accept된

**Cascaded FCN**에 대해 리뷰하도록 하겠습니다.



Paper Link : [[Link\]](https://www.google.co.kr/search?ei=oQ4KXLS2Osvn-Aaf3Y6ACw&q=cascaded+fcn&oq=cascaded+fcn&gs_l=psy-ab.3..0i19.1578.66970..67097...1.0..0.171.2752.0j20......0....1..gws-wiz.....0..0j33i160j0i67j0i131j0i10j0i30j0i10i30.xjjEHYYTlOA) / Github Link : **[Github Link]**









**Abstract**

\- 간(liver)과 간에 위치한 병변(hepatic lesions)을 추출(segmentation)하는 것은 정학환 임상 진단과 컴퓨터의 도움을 받는 결정지원시스템(computer-aided decision support systems)을 완성하는 것의 중요한 발판이 됩니다.



\- 이 논문에서는 cascaded fully convolutional neural networks (CFCNs)을 통해 자동적으로 CT와 MRI의 간과 병변을 추출(segment)해주는 방법을 제시합니다.
  \1. 두 개의 FCNs으로 이루어진 CFCNs는 우선 두번째 FCN의 ROI input으로 쓰일 간을 추출하는 FCN을 학습합니다.
  \2. 두번째 FCN은 오직 첫번째 FCN에서 예측한 liver ROIs 내에서만 병변을 segment합니다.



\- 검증(validation) 결과로 각 volume당 100초 미만의 시간 안에 간(liver)에 대한 Dice score가 94% 이상을 달성했습니다.



\- 또한 38개의 MRI liver tumor volumes과 **3DIRCAD** 데이터셋에 대한 robustness를 보입니다.









**1. Introduction**

 

![img](https://t1.daumcdn.net/cfile/tistory/9950504A5C0A141325)

\- Figure 1에서는 두 가지 문제를 확인할 수 있습니다.
  1) 병변의 모양, 크기 그리고 대조의 정도가 다양합니다.

  2) 간과 병변 사이의 값(intensities)의 차이가 크지 않아서 전체적으로 낮은 대조를 갖습니다.



\- 이 논문에서는 Figure 1에서 확인한 두 가지 문제점을 갖고 있는 segmentation task에서 좋은 성능을 보이는 모델을 제시합니다. 논문의 세 가지 contribution은 아래와 같습니다.

  1) 간의 병변(hepatic liver lesions)을 추출(segment)하는 난이도 높은 task에 좋은 성능을 보이는 fully convolutional CNN을 학습하고 적용했습니다.

  2) 상당히 높은 성능을 보이는 cascaded fully convolutional neural network (CFCN)을 제시합니다. CFCN은 CT 단면에 대해서 간과 병변을 연속적으로 segment합니다.

  3) 다른 양식(modality)을 가진 데이터와 다양한 실생활 데이터셋에 대해서도 좋은 성능을 보입니다 (generalization).









**2. Methods**



**- 2.1 Data Preparation**

  : 우선 필요없는 장기와 물체를 제거하기 위해 [-100, 400] 사이의 값을 갖도록 합니다. (-100 미만의 값은 모두 -100으로, 400을 초과하는 값은 모두 400으로 / CT가 아닌 MRI의 경우, HU Windowing 대신에 N4 Bias Correction) 이후 histogram equalization을 통해 대조(contract)를 높여줍니다. 이를 통해 이전보다 더 높은 대조를 갖게 되므로 비정상 간 조직(abnormal liver tissue)을 효과적으로 구분할 수 있습니다. 

   또한 elastic deformation, traslation, rotation, Gaussian noise와 같은 data augmentation을 해줍니다.



![img](https://t1.daumcdn.net/cfile/tistory/996773335C0A1AB830)

\- Figure 3에서 data preparation에서 거친 두 가지 과정의 효과를 확인할 수 있습니다. 왼쪽의 사진은 원본이고 [-100, 400] 사이의 HU 값을 갖도록 처리해준 것이 중간 사진입니다. 이후 histogram equalization을 거친 결과가 오른쪽 사진입니다. 위에서 언급했듯이 두 가지 과정을 통해 낮은 대조를 갖던 사진의 대조를 높여주어 장기간의 구분이 더웃 뚜렷해진 것을 확인할 수 있습니다.



※ Histogram equalization 참고 자료 : **[링크]**





**- 2.2 Cascaded Fully Convolutional Neural Networks**

  : 논문에서는 최신 딥러닝 모델을 시도해보고 최종 결정을 하기까지의 과정을 자세히 설명해두었지만 이 글에서는 생략하고 최종 모델만 다루도록 하겠습니다.



![img](https://t1.daumcdn.net/cfile/tistory/996E62485C0A23FE1A)



Figure 2: 제시된 image segmentation workflow의 구조.

우선 CR/MRI volumes은 각각 **HU-windowing**과 **N4 bias correction**을 통해 **preprocessed**됩니다.

학습(Training) 과정에서는 의료 데이터에서의 노이즈와 변형에 대해 일관성을 유지하기 위해서 학습 데이터를 **augment**하는 단계가 있습니다.

**첫번째 FCN**은 복부(abdomen) CT/MRI scans에서 **간(liver)**을 추출합니다.

여기서 추출된 liver ROI는 **두번째 FCN**의 input으로 사용되어 주어진 segmented liver ROI에서 **병변**을 추출합니다.

최종 결과를 얻기 위해서 3D conditional random field (**3D CRF**)가 사용됩니다.



※ CRF에 대한 참고 자료 : **[링크]**







![img](https://t1.daumcdn.net/cfile/tistory/99571D395C0A9E453C)





조금 더 구체적으로 정리하면,

사실 논문에서 제시하는 모델의 이름은 Cascaded FCN이지만

실제 구조는 2개의 U-Net으로 구성되어 있습니다.



첫번째 U-Net은 비정상 CT scan에서 얻어낸 간을 segment하도록 학습됩니다.

첫번째 U-Net에서 추출된 liver ROI는 전체 인풋 이미지에서 crop된 후,

두번째 U-Net의 input shape으로 re-sampling 해줍니다.

Resampling을 거친 liver ROI는 두번째 U-Net의 input으로 사용됩니다.



이러한 과정을 통해 두번째 U-Net이 오직 간(liver) 영역 내부에서

병변을 segment하도록 함으로써 false positive lesions이 발생할 가능성을 줄여줍니다.





**- 2.3 Effect of Class Balancing**

  : FCN을 학습할 때, 각각의 class의 pixel-wise frequency에 따라 적절한 class balancing을 해주는 것이 중요합니다. 이 논문에서는 class balancing을 거친 결과와 거치지 않은 결과를 비교함으로써 class balancing의 중요성을 강조합니다. CFCN에서는 일반적인 cross entropy loss function에 weighting factor ![img](https://t1.daumcdn.net/cfile/tistory/999B1D465C0A9BB329)를 추가해줌으로써 class balancing을 해결했습니다.





![img](https://t1.daumcdn.net/cfile/tistory/992787485C0A9B290A)



**<Term Explanation>**

※ ![img](https://t1.daumcdn.net/cfile/tistory/9903FF425C0A9C2B10)= voxel i가 foreground에 속할 확률

  **![img](https://t1.daumcdn.net/cfile/tistory/992ACC495C0A9C1932)**= ground truth                         

 ![img](https://t1.daumcdn.net/cfile/tistory/99FC484D5C0A9CDA15)







아래의 그림은 논문에서 시도한 방법 중 하나인 AlexFCN에

**class balancing**을 적용한 것과 적용하지 않은 경우를 비교한 결과입니다.

(3DIRCAD dataset의 간과 병변을 대상으로 학습한 결과)



![img](https://t1.daumcdn.net/cfile/tistory/99A5884C5C0A9DD831)













아래는 U-Net에 학습한 결과입니다.



![img](https://t1.daumcdn.net/cfile/tistory/99879C355C0A9F2922)







**- 2.4 Transfer Learning and Pretraining**

  :  이 논문에서는 pretrained weights로 기존의 U-Net의 weights를 사용했다고 합니다. 또한 논문의 저자는 Github에 학습을 마친 caffe 모델의 weights를 공개해두었습니다. **[링크]**









**3. Experiments and Results**

\- 프레임워크로 Caffe를 사용했습니다.

\- Optimizer로 SGD를 사용했습니다. (learning rate = 0.001, momentum = 0.8, decay = 0.0005)

\- 3D CRF를 적용함으로써 liver segmentation의 Dice score 93.1%에서 94.3%로 향상시켰습니다.

\- 2 fold cross-validation 결과, 병변에 대한 Dice score로 56% (26%의 표준편차)를 얻어냈습니다.





![img](https://t1.daumcdn.net/cfile/tistory/99C649445C0AAC6103)



초록색 영역 : 정확하게 간을 예측한 영역

노란색 영역 : 간을 잘못 예측한 영역 (false negative + false positive)

파란색 영역 : 정확하게 병변을 예측한 영역

빨간색 영역 : 병변을 잘못 예측한 영역 (false negative + false positive)





첫번째 열에서 B와 C를 비교하면 **Single UNet**에 비해 **CFCN**을 사용한 것이

false positive pixels이 적음을 확인할 수 있습니다.



두번째 열에서 E와 F를 비교하면 **3DCRF**를 통해

노란색 영역을 줄이고 초록색 영역이 넓어졌음을 확인할 수 있습니다.

(이 예시의 경우, lesion dice score가 82.3%입니다)











![img](https://t1.daumcdn.net/cfile/tistory/99B2BA505C0AAD7E12)









아래의 예시는 CT가 아닌 DW-MRI 데이터를 예측한 결과입니다.

![img](https://t1.daumcdn.net/cfile/tistory/99C8AF3A5C0AADCB14)









**4. Conclusion**

\- CFCN은 기존의 segmentation이 갖고 있던 치명적인 문제점인 false positive lesions segmentation을 해결하려 노력한 모델입니다. 병변을 segment하기 이전에 병변이 포함된 조직(ex - 간)을 우선적으로 segment한 후 얻어낸 특정 영역에 한해서만 예측이 이루어지도록 하는 방법을 통해 성능을 향상시켰습니다. End-to-end로 학습되지 않는다는 한계가 있지만 메모리 소모가 큰 3D 이미지가 아닌 2D 단면을 가지고도 비교적 높은 성능을 보였다는 장점이 있습니다. CFCN과 3D volume 기반의 segmentation 기법을 합치는 방법을 통해 더욱 성능을 높일 수 있을 것으로 기대됩니다.