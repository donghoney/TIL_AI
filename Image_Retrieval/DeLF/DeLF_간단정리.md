## Large-Scale Image Retrieval with Attentive Deep Local Features 논문 정리

출처 : https://arxiv.org/pdf/1612.06321.pdf



glee1228@naver.com



* DELF로 잘 알려진 논문이고 **포항공대 한보형 교수** 팀과 **구글**이 공동 연구 결과.
* v1는 2016년 12월 공개, 구글 랜드마크 데이터셋 공개와 함께 2018년 2월에 v4



### Abstract

* **DELF**(**DE**ep **L**ocal **F**uture) 깊은 지역 특징이라는 이름의 대규모 이미지 검색에 적합한 local descriptor를 제안
* 유용한 local feature를 식별하기 위해 descriptor와 keypoint 선택에 대한 Attention 매커니즘을 제안
* Google Landmark 데이터셋 공개
  * Background clutter, partial occlusion, multiple landmarks, variable scales를 가진 쿼리와 DB
* global과 local descriptor의 sota를 outperform함.



### 1. Introduction

* 데이터셋이 중소형일지라도, 다양한 이유로 대규모 데이터셋 with clutter, occlusion, and variations in viewpoint and illumination 에서 성능을 발휘하지 못함
* Global Descriptor들은 이미지 부분 패치에 대한 정보를 가지지 못함
* 최근 CNN을 사용하면서 이미지 패치를 매칭하기 위한 local feature를 제안하는 트렌드가 있지만, 의미있는 특징을 찾는 능력이 부족하고 정확도도 제한되어 있어 이미지 검색에 최적화되어 있다고 보기는 어려움.
  * 대부분 중소규모의 데이터를 사용한 테스트만 하기 때문에 제대로 하려면 대규모 데이터셋을 사용해야함.
* 그래서 포괄적이고 까다로운 예제로 구성된 대규모 데이터셋을 활용해 통계적으로 의미있는 결과를 도출하고자 함.
* 주요 목표는 CNN기반의 feature Descriptor
* Attention을 사용한 CNN 기반 local feature인데, 패치 레벨의 주석없이 이미지 수준의 클래스 레이블만 활용한 weakly supervised learning을 제안
* Attention model은 동일한 CNN 아키텍쳐를 재사용하고 추가계산을 거의 하지 않고 Attention Score를 만든다. 이 Score를 패스시켜 local descriptor와 keypoint를 모두 추출할 수 있고, 이 DELP Pipeline은 Global Descriptor+Local Descriptor를 하는 기존의 방법에 비해서 상당히 좋은 성능을 보여줌

![delf_1](../../Image/delf_1.png)



### 2. Related Work

* 기존 데이터 : Oxford5k , Paris6k, Flickr100k, INRIA Holiday 데이터셋
* 검색 시스템 : 
  * 예전에는 KD-Tree 또는 vocabulary tree를 사용한 ANN(Approximate nearest neighbor) 검색 방법
  * 오늘날에는 높은 정밀도로 작동해야 할때는 사용하긴 함.
* Local Feature Aggregation 기법 :
  * VLAD
  * Fisher Vector(FV)
* Global Descriptor : 
  * Pretrained된 CNN 또는 훈련된 네트워크([Deep Image
    Retrieval](https://arxiv.org/pdf/1604.01325.pdf), [NetVLAD](https://arxiv.org/pdf/1511.07247.pdf), [CNN Image Retrieval Learns from BoW](https://arxiv.org/pdf/1604.02426.pdf))
  * 위의 Global Descriptor들은 일반적으로 triplet loss로 훈련
  * CNN기반 Global Descriptor를 사용하는 일부 알고리즘은 VLAD 또는 FV와 같은 기존 Aggregation 기법에서 Hand-craft featrue를 deep local feature로 대체함



### 3. Google-Landmarks Dataset

* 기존 데이터셋(Holidays(1491), Oxford5k(5062), Flickr60k(67714), Flickr1M(1M) )보다 더 큰 대규모 데이터셋
* 12,894 랜드마크로 이루어진 이미지 1,060,709장과  111,036의 추가적인 Query 이미지
* 전 세계에서 촬영된 이미지, GPS 좌표와 연결되어 있음

* 기존 데이터셋 이미지는 랜드마크가 중심에 위치해있어서 global descriptor가 잘 작동함
* Foreground/background clutter, occulusion, 부분적으로 볼 수 없는 오브젝트등을 포함
* Visual feature와 GPS 좌표를 사용하여 클러스터를 구성
  * 검색된 이미지와 연관성 있는 cluster 중심점과 query 이미지의 location이 일정 threshold 이하 이면, 두 이미지는 동일한 랜드마크로 간주
* Ground-truth annotation은 매우 까다로운 이유
  1. 랜드마크가 잘 안보임
  2. GPS 에러가 있음
  3. 랜드마크 주변 거리가 너무 긴 경우(Eiffel Tower, Golden Gate Bridge 처럼)
* 그렇지만 Google-Landarks Datasets은 이런 거리의 threshold를 25km로 두어 잘못된 주석을 매우 작게 줄였음. 약간의 에러가 있을지라도 문제가 되지는 않음



### 4. Image Retrieval with DELF

![delf_1](../../Image/delf_1.png)

* 본 논문의 대규모 검색 시스템은 4개의 블락으로 나눌 수 있음
  1. **Dense Localized Feature Extraction**(밀집되어있는 local feature 추출)
  2. **Keypoint Selection**(키포인트 선택)
  3. **Dimensionality reduction**(차원 축소)
  4. **Indexing and Retrieval**(인덱싱 및 검색)
* 이 4번째 섹션에서는 **DELF Feature** 추출 및 **학습 알고리즘**과 **인덱싱** 및 **검색** 절차에 대해 설명한다.



### 4.1. Dense Localized Feature Extraction

* 분류로 학습된 CNN의 특징 추출 레이어로 구성된 Fully Convolutional Network(FCN)을 이용해서 밀집된 특징을 추출한다.(**Backbone Network**)

* ResNet50을 사용(4 번째 conv레이어 아웃풋을 활용)
* Scale Invariant하기 위해 Image Pyramid를 만들어 각 level을 **독립**적으로 FCN에 적용함
  * 한 장의 이미지를 여러 가지 Scale로 변형하고 그 각각의 이미지를 각각의 FCN에 통과시킨 것 같음.
* **BaseLine Backbone**은 **ImageNet으로 학습된 ResNet50 모델**을 사용
* DELF Local Descriptor의 차별성이 부각되도록 하기 위해 **Fine-Tuning**을 시행
  * Fine Tuning 시, 랜드마크 데이터셋을 사용
  * Standard Cross-Entropy 손실 함수를 사용
    * 해당 내용에 대한 설명은 https://curt-park.github.io/2018-09-19/loss-cross-entropy 참고
  * 입력 이미지는 이미지 중심 정사각형 250x250 로 자른 후, 224x224 사이즈로 random Crop하여 사용
  * Object-Level이나, Patch-Level의 레이블은 필요하지 않음. 



### 4.2. Attention-based Keypoint Selection

* 이미지 검색에 조밀하게 추출된 Feature들을 모두 사용하지 않고, feature subset을 선택하는 기법을 사용
* 정확도와 계산 효율성을 위해 키포인트를 선택시킴



### 4.2.1 Learning with Weak Supervision(복습과 관련자료 학습 필요..)

* Local feature Descriptor에 Attention 점수를 매기는 훈련방식을 제안
* Attention Network에 의해 예측된 가중치(Weight)들의 합에 의해 Local feature는 pooling된다

![delf_3](../../Image/delf_3.png)

* 이 훈련 절차는 4.1의 학습 방법들(손실 함수, 데이터셋)과 유사하고 위의 그림(b)에 대한 설명이다.
* 노란색 블록 부분 : Attention 부분
  *  소프트맥스 기반의 랜드마크 분류기를 학습하기 위해 사용된 전체 이미지 데이터에 대한 임베딩을 만들어낸다.

$$
y = W \left( \sum_n\alpha(f_n;\theta)\cdot f_n\right), \qquad (1)
$$

* $$\alpha(f_n;\theta) $$ 는 각각 feature에 대한 score 함수이고 이 때 파라미터는 $$\theta$$ 가 된다.
* output logit $$y$$ 는 feature 벡터들의 가중합에 의해 만들어 진다.
* $$\mathbf{W}$$ 는 $$\mathbf{W} \in R^{M \times d}$$ ,  $$M$$ 은 클래스 갯수
* cross entropy loss를 학습에 사용

$$
\mathcal{L} = -y^*\cdot \left( \frac{exp(y)}{1^Texp(y)}  \right), \qquad (2)
$$

* $$y $$ 는 원-핫 표현의 ground-truth이고, $$1$$ 은 한개의 벡터이다.

* 스코어 함수 $$\alpha(\cdot )$$ 의 파라미터는 역전파에 의해 학습되며, 기울이는 다음과 같다. 

$$
\frac{\partial\mathcal{L}}{\partial\mathcal{\theta}}=\frac{\partial\mathcal{L}}{\partial y}\sum_n\frac{\partial y}{\partial\alpha_n}\frac{\partial\alpha_n}{\partial \theta}=\frac{\partial \mathcal{L}}{\partial y}\sum_nW\mathcal{f}_n\frac{\partial\alpha_n}{\partial\theta}, \qquad (3)
$$

* $$\theta$$ 에 대한 출력점수 $$\alpha_n \equiv \alpha(f_n;\theta)$$ 의 역전파는 기본 MLP와 동일하다. 

* 여기서 $$\alpha(\cdot)$$ 은 음수가 되지 않도록 강제한다.

* 실제로 score 함수 구현은 2개의 conv 레이어와 softplus 비선형 함수로 구현되어 있다.
  * 이 때 1x1 conv 필터를 사용하게 된다.



### 4.2.2 Training Attention

* Descriptor와 Attention model 둘 다 **이미지-level로 학습**한다.
* 하지만, 학습과정에서 까다로운 게 몇 가지 있다.
  * feature representation과 score function이 joint하게(동시에) 역전파에 의해 학습될 수 있는데, 이 과정이 실질적으로 weak한 모델을 생성한다는 사실을 발견했다.
* 그래서 **two-step 학습 전략**을 적용시켰고 다음과 같다.
  1. Descriptor를 fine-tuning 한다.(4.1 참조)
  2. Score function을 fixed된 descriptor 환경에서 학습시킨다.
* 또 다른 기여(contribution)도 있는데, 그건 attention 학습할 때, **random하게 이미지를 rescaling하는 것**이다.
  * Attention model이 scale invariant하게 돕는다.
  * **Random Rescale** 과정은 다음과 같다.
    1. 처음 정방형 이미지를 만들기 위해 가운데를 center-crop하고, 900 x 900 로 rescale한다.
    2. 그리고 720 x 720 크기로 랜덤하게 crop한다.
    3. 마지막으로 임의로 $$y \le 1$$ 범위로 rescale한다.



### 4.2.3 Characteristics

* 비전통적인 측면의 키포인트 선택은 **Descriptor 추출 후 키포인트 선택**이 이루어진다.
  * 키포인트가 먼저 감지되어 나중에 설명되는 기존 기술(**SIFT 및 LIFT**)과는 다르다.
* 기존 키포인트 탐지기는 low-level feature 기반으로 반복적인 키포인트를 감지하는 데 중점을 둠
  * 그러나, **이미지 검색과 같은 high-level의 인식 작업에서는 서로 다른 인스턴스(객체)를 구분할 수 있는 키포인트를 선택하는 게 중요하다.**
* 제안된 방법은 feature map으로부터 이전보다 높은 수준의 정보들을 가려낸다.



### 4.3. Dimensionality Reduction

* 검색 정확도를 개선시기 위해, 선택된 feature들의 차원을 줄인다.
* L2 norm을 적용 후 PCA로 40차원까지 줄인다.
* 마지막으로, 다시 L2 norm를 거친다.



### 4.4. Image Retrieval System

* 쿼리와 DB 데이터로부터 Descriptor를 추출한다
  * 여기서, 가장 높은 Attention Score를 가진 local feature의 개수를 가진 이미지이다.
* 검색 시스템은 nearest neighbor search를 기반으로 하고, KD-tree와 Product Quantization(PQ)의 콤비네이션으로 구현.
* PQ를 사용해서, 40-dim의 feature descriptor를 50bit로 인코딩.
  * 40-dim feature descriptor를 10개의 동일 차원 서브벡터로 나눈다
  * 서브 벡터당 32($$2^5$$)개의 중심점을 정하고 k-means 클러스터링을 시행하여 50bit($$2^{50}$$)로 인코딩한다.

* Nearest neighbor 검색 정확도 향상
  * Query Descriptor가 인코딩 되지 않은 Asymmetric Distance를 계산한다.
* Nearest neighbor 검색 속도 향상
  * 8K 코드북 사용, Descriptor에 대한 inverted index 구성
  * 인코딩 오류를 줄이기 위해, KD-Tree를 사용하여 voronoi cell을 분할하고 30K개 feature들보다 적은 subtree에 지역적으로 최적화 된 PQ를 사용한다.
  * 쿼리에서 추출된 Local Descriptor에 Approximate nearest neighbor 검색을 수행한 뒤, 가장 가까운 K개의 local Descriptor에 대해 데이터베이스 이미지당 모든 매치되는 것들을 합한다. 
  * 마지막으로, RANSAC 알고리즘을 사용해서 Geometric verification하고, 검색된 이미지에 대한 score를 inlier인 개수로 한다. 이 단계에서 많이 걸러진다.
* 구글 랜드마크 데이터셋에 10억 개의 Desciptor를 indexing하기 위해 8GB 메모리보다 더 적게 필요하다.
* Nearest Neighbor Search 작업에서 CPU 하나를 사용해서 2초보다 적게 걸린다.

* 각 쿼리에 5개 중심을 소프트 할당하고 각 inverted index tree에서 최대 10K개의 리프 노드들을 검색한다.(이 부분 이해가 안됐음)



### 5. Experiments

* 기존의 Global과 local Feature들을 DELF 성능과 비교하는 부분
* 그리고 기존 데이터셋에 DELF를 적용시켜 얼마나 좋은 성능이 나오는지 보여줌.



### 5.1. Implementation Details

* Multi-scale Descriptor Extraction(다중 스케일 디스크립터 추출)

* Training
* Parameters