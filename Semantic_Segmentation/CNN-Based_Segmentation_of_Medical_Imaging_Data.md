# [CNN-based Segmentation of Medical Imaging](https://arxiv.org/abs/1701.03056) 논문 리뷰

Date: 01/11/2017

논문 링크 : https://arxiv.org/abs/1701.03056

* 저자는 의료 이미지 세분화(예 : 분류된 데이터 및 클래스 불균형의 희소성)에서 나타나는 특정 문제를 연구하고 다양한 접근법이 이러한 과제를 얼마나 성공적으로 하였는지 파악하는데 동기를 부여합니다.

- 그들은 뼈(손) 세분화 작업 뿐만 아니라 BRATs에 대해 3D UNet 유형 아키텍처를 활용하여 각각에 대한 특정 사항을 연구합니다.

  - 손(Hand) Segmentation를 위해, 그들은 다음을 보았습니다.
    - Jacaard loss을 사용하는 것이 좋습니다. categorical cross entropy보다
      - 두 가지 손실 함수는 데이터 세트에서 상대적으로 공통적인 클래스에서 잘 수행되지만, Jaccard Loss는 빈번하지 않은 클래스에서 훨씬 더 잘 수행됩니다 (테이블은 존재하지 않음)
    - Long Skip Connection을 사용해라 No Skip Connection보다
      - 성능감소를 극적으로 줄여줍니다.
    - 다중 Segmentation map(Upsampling 측면에서)을 결합하여 사용하는 것이 좋습니다. 단일 Segmentation Map을 사용하는 것보다
      - 다중과 단일 segmentation map 모두 validation set에서 비슷한 성능을 보여줬지만, 다중 Segmentation Map은 test set에서 더 나은 성능을 보여주었습니다.
      - 다중 Segmentation Map을 사용하는 Network는 단일 Segmentation Map을 사용하는 Network보다 훨씬 더 빠르게 수렴합니다.
      - 이를 위해 그들은 1x1x1 Convolution들을 추가 Segmentation Map에 summing / Concatenating 하기전에 적용했습니다.
    - Element-wise Summation VS Concatenation of Skip Connection
      - Feature들의 Concatenation은 Summation보다 성능이 좋습니다.
      - 이러한 각 시나리오의 Feature Map을 시각화 하면, 최종 Segmenation Map의 보다 고유하고 더 대표적인 위치를 연결하여 생성된 Feature Map을 보여줍니다.
  - BRATs의 경우, 각 양식을 사용하여 수행한 성과 뿐만 아니라 다양한 방식의 조합을 사용하여 얻은 성과를 살펴보았습니다.
    - 그들은 다른 Modality들이 다른 Feature를 강조 표시하고 모든 클래스에 걸쳐 최상의 성능을 제공하는 단일 조합이 없음을 발견했습니다.

- 기타 네트워크 세부 정보 :

  - Max-Pooling 대신 Stride Convolution이 더 나은 성능을 보였기 때문에 대신 사용되었습니다.
  - 그들은 PReLU 활성화 함수를 사용합니다.
  - Convolution은 최종 Segmentation Map을 생성하는 데 사용되는 것을 제외하고는 모두 3x3x3이며, Deconvolution 이전에 Feature Map의 수를 줄이는 데 사용됩니다.
