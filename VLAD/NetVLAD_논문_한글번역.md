## NetVLAD : CNN architecture for weakly supervised place recognition

> Relja Arandjelovic´ INRIA ∗ Petr Gronat INRIA∗ Akihiko Torii Tokyo Tech † Tomas Pajdla CTU in Prague ‡ Josef Sivic INRIA∗

논문 링크 : https://arxiv.org/pdf/1511.07247.pdf

### Abstract

​	주어진 쿼리 사진의 위치를 빠르고 정확하게 인식하는 대규모 시각적 장소 인식 문제를 해결합니다. 우리는 다음 세 가지 주요 공헌을 제시합니다. 첫째, 장소 인식 작업을 위해 종단 간 (end-to-end) 방식으로 직접 훈련 가능한 CNN (convolutional neural network) 아키텍처를 개발합니다. 이 아키텍처의 주요 구성 요소 인 NetVLAD는 이미지 검색에 일반적으로 사용되는 "Locally Aggregated Descriptors의 벡터"이미지 표현에서 영감을 얻은 새로운 일반화 된 VLAD 계층입니다. 이 레이어는 CNN 아키텍처에 쉽게 삽입 할 수 있으며 백 프로 파티를 통해 교육을받을 수 있습니다. 둘째, 우리는 약하게 감독 된 새로운 순위 손실을 기반으로하는 훈련 절차를 개발하여 Google Street View Time Machine에서 다운로드 한 시간 경과에 따른 동일한 장소를 묘사하는 이미지에서 종단 간 방식으로 아키텍처 매개 변수를 학습합니다. 마지막으로 우리는 제안 된 아키텍처가 두 가지 어려운 장소 인식 벤치 마크에서 학습되지 않은 이미지 표현과 기성 CNN 설명자를 크게 능가 함을 보여 주며 표준 이미지 검색 벤치 마크에서 현재 최첨단 컴팩트 이미지 표현을 향상시킵니다.



### 1. Introduction

​	컴퓨터 비전 [4,9,10,24,35,63,64,65,66,80,81]과 로봇 공동체 [15, 16, 44]에서 시각적 인 장소 인식은 지난 몇 년 동안 상당한 주목을 받았다. , 46], 자율 주행 [47], 증강 현실 [47] 또는 지리적 위치 파악 기록 영상 [5]에 의해 동기를 부여 받는다. 

​	그러나 장소 인식 문제는 여전히 매우 어려운 과제로 남아 있습니다. 우리는 어떻게 다른 일루미네이션으로 포착되거나 시간이 지남에 따라 외관을 바꿀 수 있다는 사실에도 불구하고 도시 전체 또는 전체 국가의 동일한 거리 구석을 인식 할 수 있습니까? 근본적인 과학적 질문은 비슷하게 보이는 장소를 구별하기에 충분히 부유하지만 아직 전체 도시 나 국가를 대표 할만큼 조밀 한 장소를 적절하게 대표하는 것입니다. 

​	장소 인식 문제는 전통적으로 인스턴스 검색 작업으로 던져 졌는데, 여기에는 큰 지오 태그 데이터베이스 [4, 10, 35, 66, 80, 81]를 쿼리하여 얻은 시각적으로 가장 유사한 이미지의 위치를 사용하여 쿼리 이미지 위치를 추정합니다. . 각각의 데이터베이스 이미지는 SIMO [43]와 같은 로컬 불변 피쳐 [83]를 사용하여 표현되며,이 이미지는 bag-of-visualwords [53,74], VLAD [3,29] 또는 전체 이미지에 대한 단일 벡터 표현으로 집계됩니다 피셔 벡터 [31, 52]. 결과 표현은 보통 압축되고 효율적으로 색인된다 [28, 74]. 이미지 데이터베이스는 정확한 카메라 포즈 [40, 63, 64]의 복구를 가능하게하는 3D 구조에 의해 추가로 보강 될 수 있습니다. 

​	지난 몇 년 동안 CNN (convolutional neural networks) [38, 39]은 객체 분류 [37, 49, 73, 77], 장면 인식 [91] 또는 객체와 같은 다양한 카테고리 수준 인식 작업을위한 강력한 이미지 표현으로 부상했다 탐지 [21]. CNN의 기본 원리는 80 년대에 알려졌으며 [38, 39] 최근의 성공은 GPU 기반 컴퓨팅 성능의 발전과 대형 라벨 이미지 데이터 세트 [37]를 결합한 것입니다. 훈련 된 표현은 인식 작업 [19, 21, 49, 69, 89], 객체 분류를 위해 훈련 된 CNN 표현의 직접적인 적용 [37], 블랙 박스 기술자 추출기 지금까지는 인스턴스 수준 인식 작업에서 성능이 제한적으로 향상되었습니다 [6, 7, 22, 60, 62]. 이 작업에서 우리는 장소 인식을 위해 직접 개발되고 훈련 된 CNN 표현에 의해 성능 차이가 연결될 수 있는지 조사합니다. 이를 위해서는 다음 세 가지 주요 문제를 해결해야합니다. 첫째, 장소 인식을위한 훌륭한 CNN 아키텍처는 무엇입니까? 둘째, 교육을 위해 주석이 달린 충분한 양의 데이터를 수집하는 방법은 무엇입니까? 셋째, 장소 인식 작업에 적합한 최첨단 방식으로 개발 된 아키텍처를 어떻게 훈련 할 수 있습니까? 이러한 과제를 해결하기 위해 우리는 다음 세 가지 혁신을 제시합니다. 

​	먼저, 현재 수행되고있는 손으로 조작 한 객체 검색과 장소 인식 파이프 라인으로부터 배운 교훈을 바탕으로 [2, 3, 25, 80] 우리는 중간 레벨 (conv5) 컨볼 루션 특징을 모으는 장소 인식을위한 컨벌루션 신경망 구조를 개발합니다 효율적인 인덱싱이 가능한 소형 단일 벡터 표현으로 전체 이미지에서 추출됩니다. 이를 달성하기 위해 우리는 이미지 검색 및 장소 인식에서 탁월한 성능을 보인 VLAD (Vector of Locally Aggregated Descriptors) 표현 [29]에서 영감을 얻어 새로운 학습 가능한 일반화 된 VLAD 계층 인 NetVLAD를 설계합니다. 이 레이어는 CNN 아키텍처에 쉽게 삽입 할 수 있으며 백 프로 파티를 통해 교육을받을 수 있습니다. 결과 집합 된 표현은 PCA (Principal Component Analysis)를 사용하여 압축되어 이미지의 최종 압축 설명자를 얻습니다. 

​	둘째, 장소 인식을위한 아키텍처를 교육하기 위해 Google 스트리트 뷰 타임 머신에서 시간 경과에 따라 서로 다른 시점에서 동일한 장소를 묘사하는 여러 파노라마 이미지의 대형 데이터 세트를 수집합니다. 이러한 데이터는 전 세계의 광대 한 지역에서 사용할 수 있지만 약한 형태의 감독 만 제공합니다. 두 개의 파노라마가 (노이즈가 많은) GPS를 기반으로 비슷한 위치에서 캡처되지만 파노라마의 어느 부분이 현장의 같은 부분. 

​	셋째, 우리는 장소 인식을위한 학습 절차를 개발합니다.이 학습 과정은 약하게 레이블이 지정된 Time Machine 이미지에서 장소 인식 작업에 맞게 조정 된 엔드 투 엔드 방식으로 아키텍처의 매개 변수를 학습합니다. 결과 표현은 시점 및 조명 조건의 변화에 강하고 동시에 건물 표면 및 스카이 라인과 같은 이미지의 관련 부분에 초점을 맞추면서 많은 사람들에게 발생할 수있는 자동차 및 사람들과 같은 혼란스러운 요소를 무시합니다. 다른 장소들. 

​	우리는 제안 된 아키텍처가 두 가지 어려운 장소 인식 벤치 마크에서 학습되지 않은 이미지 표현과 CNC 설명자를 훨씬 능가하는 것으로 나타 났으며 표준 이미지 검색 벤치 마크에서 현재의 최첨단 컴팩트 이미지 표현을 향상시킵니다.

#### 1.1 Realated work

더 나은 이미지 검색 [2, 3, 11, 12, 17, 25, 26, 27, 29, 32, 48, 51, 52, 53,54,71,78,79,82] 과 장소 인식 (4, 9, 10, 15, 16, 24, 35, 44, 46, 63, 64, 65, 75, 80, 81)속에 모든 관련 학습 기반 접근법은 다음과 같은 두 가지 범주 중 하나 또는 둘 모두에 속한다. (i) 보조 과제에 대한 학습 (예 : 로컬 기능의 고유 한 형태 [4, 15, 30, 35, 58, 59, 90] , 그리고 (ii) 목표 작업을 위해 미세 조정할 수없는 얕은 수작업 기술 어의 학습 [2, 9, 24, 35, 57]. 이 두 가지 모두 심층 학습의 핵심 아이디어 인 정반대의 학습 인 다양한 인식 작업에서 성능을 크게 향상시키는 핵심 아이디어와 정반대입니다. 우리는 실제로 섹션 5.2에서 엔드 타스크, 장소 인식을위한 교육 표현이 우수한 성능을 얻기 위해 중요하다는 것을 보여줄 것입니다. 

​	수많은 작품들은 지역 디스크립터 나 메트릭을 비교하는 데 집중하지만 [45, 48, 50, 55, 56, 70, 71, 88], 일부는 이미지 검색 결과를 표시하지만 디스크립터는 작업 이미지 검색을 염두에 두지 않고 직접적으로 일치하는 로컬 이미지 패치를 제공합니다. 그들 중 일부는 또한 학습을 부트 스트랩하기 위해, 즉 잡음이 많은 훈련 데이터를 제공하기 위해 수동 조작 된 특징을 이용한다 [45, 48, 50, 55, 71]. 

​	이미지 검색을 위해 CNN 기반 기능을 사용하여 여러 연구가 조사되었습니다. 여기에는 [8, 60]을 연결하거나 풀링 [6, 7, 22]하여 특정 계층의 활성화를 설명자로 직접 처리하는 것이 포함됩니다. 그러나 이러한 작업들 중 어느 것도 실제 작업에서 CNN을 실제로 훈련시키지 않지만 CNN을 블랙 박스 설명자 추출기로 사용합니다. 한 가지 예외는 Babenko et al. [8] 네트워크는 700 개의 랜드 마크를 분류하는 보조 작업에서 미세 조정된다. 그러나 다시 네트워크는 대상 검색 작업에 직접 훈련되지 않습니다. 

​	마지막으로, 최근 [34]와 [41]은 ground-to-aerial 매칭 [41]과 카메라 자세 추정 [34]과는 다르지만 관련된 작업에 대한 end-to-end 학습을 수행했다.

### 2. Method overview

​	현재 장소 인식 시스템 (예 : [4, 10, 35, 63, 64, 65, 66, 80, 81])의 성공을 바탕으로 장소 인식을 이미지 검색으로합니다. 위치를 알 수없는 쿼리 이미지는 큰 위치 정보 태그가 지정된 이미지 데이터베이스를 시각적으로 검색하는 데 사용되며 최상위 이미지의 위치는 쿼리 위치에 대한 제안으로 사용됩니다. 이것은 일반적으로 "이미지 표현 추출기"로 작용하는 함수 f를 설계함으로써 이루어 지는데, 주어진 이미지 Ii는 고정 된 크기의 벡터 f (Ii)를 생성합니다. 함수는 오프라인에서 수행 할 수있는 전체 데이터베이스 {Ii}에 대한 표현을 추출하고 온라인으로 수행 된 쿼리 이미지 2 표현 f (q)를 추출하는 데 사용됩니다. 테스트 시간에 시각 검색은 f (q)와 f (q) 사이의 유클리드 거리 d (q, Ii)를 기반으로 이미지를 정렬하여 쿼리에 가장 가까운 데이터베이스 이미지를 정확하게 또는 가장 근접한 근사 탐색 (Ii). 

​	이전 작품은 주로 수작업으로 표현한 이미지 표현을 사용했지만 (예 : f (I)는 SIFT 기술자를 추출하고 43), bag-of-words 벡터 [74] 나 VLAD 벡터 [29]에 풀링 한 것과 같은데, 여기서 우리는 장소 인식 작업에 직접 최적화 된 종단 간 (end-to-end) 방식으로 표현 f (I)를 학습한다. 표현은 일련의 매개 변수 θ로 매개 변수화되었으며 우리는 fθ (I)로 참조함으로써이 사실을 강조합니다. 유클리드 거리 dθ (Ii, Ij) = kfθ (Ii) - fθ (Ij) k도 같은 매개 변수에 따라 달라진다. 다른 방법으로는 거리 함수 자체를 배우는 것이지만 여기에서는 거리 함수를 유클리드 거리로 고정하고 유클리드 거리에서 잘 작동하는 명시적인 피쳐 맵 fθ를 찾는 것으로 문제를 제기합니다. 

​	3 장에서 우리는 예를 들어 검색을위한 compact aggregated 이미지 디스크립터에서 영감을받은 새로운 deep convolutional neural network architecture에 기반한 제안 된 표현 fθ를 설명한다. 섹션 4에서는 Google 스트리트 뷰 타임 머신의 약하게 감독 된 교육 데이터를 사용하여 종단 간 방식으로 네트워크의 매개 변수 θ를 학습하는 방법을 설명합니다.

### 3. Deep architecture for place recognition

​	이 절에서는 이미지 검색 커뮤니티의 모범 사례에 따라 CNN 아키텍처 fθ에 대해 설명합니다. 대부분의 이미지 검색 파이프 라인은 (i) 로컬 디스크립터를 추출한 다음 (ii) 순서가없는 방식으로 풀링하는 방식을 기반으로합니다. 이 선택 뒤에있는 동기는 번역 및 부분 교합에 대한 상당한 견고성을 제공한다는 것입니다. 라이팅 및 뷰 포인트 변경에 대한 강건 함은 디스크립터 자체에 의해 제공되고 스케일 불변성은 여러 스케일에서 디스크립터를 추출하여 보장됩니다. 

​	표현을 end-to-end로 학습하기 위해 차별화 된 모듈을 통해 통일되고 원칙적인 방식으로 표준 검색 파이프 라인을 모방 한 CNN 아키텍처를 설계합니다. 단계 (i)에서, 우리는 마지막 콘볼 루션 층에서 CNN을 자르고 조밀 한 디스크립터 추출 자로 본다. 이것은 인스턴스 검색 [6, 7, 62]과 텍스쳐 인식 [13]에서 잘 작동하는 것으로 관찰되었다. 즉, 마지막 콘볼 루션 계층의 출력은 H × W 공간 위치에서 추출 된 D 차원 디스크립터 세트로 간주 될 수있는 H × W × D 맵이다. (ii) 단계에서 우리는 추출 된 디스크립터를 고정 된 이미지 표현으로 풀링하고 매개 변수를 역 전파를 통해 학습 할 수있는 VLAD (Locally Aggregated Descriptor) 벡터 [29]에서 영감을 얻은 새로운 풀링 레이어를 설계한다. 이 새로운 풀링 레이어를 "NetVLAD"레이어라고 부르며 다음 섹션에서 설명합니다.

#### 3.1. NetVLAD : A Generalized VLAD layer

​	VLAD (Localally Aggregated Descriptor) [29]의 벡터는 인스턴스 레벨 검색 [29]과 이미지 분류 [22] 모두에서 널리 사용되는 디스크립터 풀링 방법이다. 이미지를 통해 집계 된 로컬 설명 자의 통계에 대한 정보를 캡처합니다. 백과 사전 단어 [14, 74] 집단은 시각적 단어의 수를 유지하지만 VLAD는 각 시각적 단어에 대한 잔차 (설명자와 해당 클러스터 중심 간의 차이 벡터)를 저장합니다. 

​	공식적으로, N 개의 D- 차원 로컬 이미지 기술자 {xi} 및 VLAD 매개 변수로서 K 개의 클러스터 센터 ( "visual words") {ck}가 주어지면, 출력 VLAD 이미지 표현 V는 K × D 차원이다. 편의를 위해 V를 K × D 행렬로 기재 할 것이지만이 행렬은 벡터로 변환되어 정규화 된 후 이미지 표현으로 사용됩니다. V의 (j, k) 요소는 다음과 같이 계산됩니다.
$$
V(j,k) = \sum_{i=1}^Na_k(x_i)(x_i(j)-c_k(j)) \qquad (1)
$$
​	여기서 xi (j)와 ck (j)는 각각 i 번째 설명자와 k 번째 클러스터 중심의 j 번째 차원이다. ak (xi)는 디스크립터 xi 내지 k- 번째 시각 워드의 멤버쉽을 나타내며, 즉, 클러스터 ck가 디스크립터 xi에 가장 가까운 클러스터이면 1이고, 그렇지 않으면 0이다. 직관적으로, V의 각 D 차원 열 k는 클러스터 ck에 할당 된 설명 자의 잔차 합계 (xi -ck)를 기록합니다. 그런 다음 행렬 V는 열 방향으로 L2 정규화 (인트라 정규화 [3])되고, 벡터로 변환되고 마지막으로 전체적으로 L2 정규화된다 [29]. 

​	이미지 검색에서 수년간 지혜를 얻으려면 VLAD를 CNN 프레임 워크에서 모방하고 훈련 가능한 일반화 된 VLAD 레이어 인 NetVLAD를 디자인하는 것이 좋습니다. 그 결과 목표 작업 (우리의 경우 장소 인식)에 대해 철저한 훈련이 가능한 강력한 이미지 표현이 가능합니다. backpropagation을 통한 트레이닝이 가능한 레이어를 구성하려면 레이어의 작업이 모든 매개 변수와 입력에 대해 차이가 있어야합니다. 그러므로 핵심 과제는 VLAD 풀링을 차별화 가능하게 만드는 것입니다. 

​	VLAD에서 불연속성의 원인은 클러스터 중심 ck에 대한 기술자 xi의 하드 할당 ak (xi)이다. 이 연산을 미분 할 수있게하기 위해 우리는 그것을 기술자의 가중치를 할당하는 다중 클러스터로의 유연한 기술자 할당으로 대체한다.
$$
\bar{a_k}(x_i)=\frac{e^{-\alpha||x_i-c_k||^2}}{\sum_{k'}e^{-\alpha||x_i-c_{k'}||^2}} \qquad (2)
$$


클러스터 ck의 근접성에 비례하지만 다른 클러스터 센터에 대한 근접성에 비례한다. ak (xi)는 가장 가까운 클러스터 중심에 가장 높은 가중치를두고 0과 1 사이의 값을가집니다. α는 거리의 크기에 따라 응답 감쇠를 제어하는 매개 변수 (양수 상수)입니다. α → + ∞의 경우이 설정은 가장 가까운 클러스터에 대해 ¯k (xi)가 정확하게 1 일 때와 0 일 때 원래의 VLAD를 정확히 복제합니다. 

![netvladì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://www.di.ens.fr/willow/research/netvlad/images/vlad_cnn.png)

그림 2. **NetVLAD 레이어가있는 CNN 아키텍처** 이 레이어는 표준 CNN 레이어 (convolutions, softmax, L2-normalization)와 구현하기 쉬운 하나의 애그리 게이션 레이어를 사용하여 방정식 비순환 그래프로 결합 된 방정식 (4) ( "VLAD 코어")에서 집계를 수행 할 수 있습니다. 매개 변수는 괄호 안에 표시됩니다.

​	(2)에서 사각형을 확장하면, e -αkxik 2라는 용어가 분자와 분모 사이에서 취소되어 벡터 wk = 2αck와 스칼라 bk = -αkckk 2 인 다음 형태의 연상 할당을 쉽게 볼 수 있습니다 . 
$$
\bar{a_k}(x_i) = \frac{e^{w_k^Tx_i+b_k}}{\sum_{k'}e^{w_{k'}^Tx+b_{k'}}} \qquad (3)
$$


NetVLAD 계층의 최종 형식은 소프트 할당 (3)을 VLAD 디스크립터 (1)에 연결하여 각 클러스터 k에 대해 학습 가능한 매개 변수 집합 인 {wk}, {bk} 및 {ck}을 얻음으로써 얻어집니다. 
$$
V(j,k)=\sum_{i=1}^N\frac{e^{w_k^Tx_i+b_k}}{\sum_{k'}e^{w_{k'}^Tx+b_{k'}}}(x_i(j)-c_k(j)) \qquad (4)
$$


NetVLAD 계층은 원본 VLAD 디스크립터와 마찬가지로 디스크립터 xi의 소프트 할당 aik (xi)가 클러스터 k에 가중치 된 설명자 공간의 다른 부분에 잔차 (xi - ck)의 1 차 통계를 집계합니다. 그러나 NetVLAD 레이어에는 원래 VLAD의 {ck}와 비교하여 {wk}, {bk} 및 {ck} 세 개의 독립 매개 변수 집합이 있습니다. 이는 그림 3에서 설명한 것처럼 원래의 VLAD보다 더 큰 유연성을 가능하게합니다. {ck}에서 {wk, bk}를 분리하는 것은 VLAD를 새로운 데이터 세트에 적용하는 수단으로 [3]에서 제안되었습니다. NetVLAD의 모든 매개 변수는 특정 태스크에 대해 end-to-end 방식으로 학습됩니다.

​	그림 2에서 볼 수 있듯이 NetVLAD 레이어는 직접 비순환 그래프로 연결된 기본 CNN 레이어로 더 분해되는 메타 레이어로 시각화 될 수 있습니다. 첫째, eq. (4)는 soft-max 함수이다. σk (z) = P exp (zk) k0 exp (zk0). 따라서, 디스크립터 xi의 입력 배열을 K 개의 클러스터로 소프트 할당하는 것은 (i) 공간 지원 1 × 1 및 바이어스 {bk}를 갖는 K 개의 필터 {wk}의 세트를 갖는 컨벌루션 }, 출력 sk (xi) = wTkxi + bk를 생성한다; (ii) 그 다음에 컨볼 루션 출력은 soft-max 함수 σk를 통과하여 eq를 구현하는 집계 레이어에서 다른 항에 가중치를 부여하는 최종 소프트 할당 aq (xi)를 얻는다. (4). 정규화 후의 출력은 (K × D) × 1 기술자이다. 

![ê´ë ¨ ì´ë¯¸ì§](http://www.liuxiao.org/wp-content/uploads/2019/02/Screenshot-from-2019-02-19-16-38-47.png)

그림 3. **감독 된 VLAD의 이점.** 빨강 및 녹색 원은 동일한 클러스터 (보로 노이 셀)에 할당 된 두 개의 서로 다른 이미지의 로컬 설명자입니다. VLAD 인코딩에서 두 이미지 간의 유사도 스코어에 대한 기여도는 해당 잔차 간의 스칼라 곱 (최종 VLAD 벡터가 L2- 정규화 됨)이며 잔차 벡터는 설명자와 클러스터 앵커의 차이로 계산됩니다 포인트. 앵커 포인트 ck는 특정 클러스터 k에 로컬 인 새로운 좌표계의 원점으로 해석 될 수 있습니다. 표준 VLAD에서 앵커는 클러스터 센터 (×)로 선택되어 데이터베이스에서 잔차를 균등하게 분산시킵니다. 그러나, 두 개의 디스크립터가 일치하지 않아야하는 이미지에 속하는 것으로 알려진 감독 된 설정에서, 새로운 잔차들 사이의 스칼라 생성을 작게하는 더 나은 앵커 (?)를 배울 수있다.



**다른 방법들과의 관계.** 다른 연구들은 VLAD 또는 Fisher Vectors (FV) [13, 22]를 사용하여 CNN 활성화를 풀링하도록 제안했지만 VLAD / FV 매개 변수 나 입력 설명자를 배우지는 않습니다. 가장 관련있는 방법은 Sydorov et al. 최종 분류 목적을 위해 SVM과 공동으로 FV 파라미터를 학습하는 것을 제안하는 [76]. 그러나 그들의 작업에서 입력 기술 어는 손으로 공학 (SIFT) 할 때 배울 수 없지만 VLAD 계층은 역 전파가 가능하므로 CNN 아키텍처에 쉽게 삽입 할 수 있습니다. "Fisher Networks"[72]는 피셔 벡터 (Fisher Vector) 레이어를 서로 겹쳐 쌓았지만 시스템은 엔드 투 엔드 (end-to-end) 훈련을받지 않았으며 손으로 제작 한 피쳐 만 사용하고 상향식으로 탐욕스럽게 훈련되었습니다. 마지막으로, 우리의 아키텍처는 또한 bilinear 네트워크와 관련이있다. [42], 최근 세분화 된 카테고리 - 레벨 인식의 다른 작업을 위해 개발되었다. 

![Datasets and evaluation methodology â¢ dataset â¢ Pittsburgh (Pitts250k): contains 250k database images downloaded from Goog...](https://image.slidesharecdn.com/201606vlnetvlad-160616113512/95/netvlad-cnn-architecture-for-weakly-supervised-place-recognition-19-638.jpg?cb=1466077388)

그림 4. **Google Street View Time Machine 예제.** 각 열은 다른 시간대에 찍은 인근 위치의 파노라마에서 생성 된 원근 영상을 보여줍니다. 잘 설계된 방법은이 영상 소스를 사용하여 시점 및 조명 (a-c) 및 중재 폐색 (b)의 변화에 변하지 않는 것을 배우는 데 사용할 수 있습니다. 또한 구름 (a), 차량 및 사람들 (b-c)과 같은 혼란스런 시각 정보를 억제하고 식물을 무시하거나 계절에 영향을받지 않는 초목 표현 (a-c)을 배우는 방법을 배울 수 있습니다. 더 많은 예제가 부록 B에 나와 있습니다.



**Max pooling (fmax).** 우리는 또한 H × W 공간 위치 전역에서 D 차원 특성의 Maxpooling을 실험하여 D 차원 출력 벡터를 생성 한 다음 L2 정규화합니다. 이 두 가지 작업은 공용 CNN 패키지의 표준 레이어를 사용하여 구현할 수 있습니다. 이 설정은 [6, 62]의 방법을 반영하지만, [6, 60, 62]는 사전 훈련 된 네트워크만을 사용하는 반면에 우리는 표현 (4 절)을 배울 것이 틀림 없다. 결과는 단순히 CNN을 기성품 [60]으로 사용하면 성능이 떨어지고 최종 작업을위한 교육이 중요하다는 것을 보여줄 것입니다 (5.2 절). 또한 VLAD는 Max-pooling 기준보다 월등합니다.



### 4. Learning from Time Machine data

​	이전 섹션에서는 장소 인식을위한 이미지 표현으로 새로운 CNN 아키텍처를 설계했습니다. 여기서 우리는 장소 인식 작업을 위해 종국적 인 방식으로 매개 변수를 학습하는 방법을 설명합니다. 두 가지 주요 과제는 다음과 같습니다. (i) 주석이 달린 교육 데이터를 수집하는 방법과 (ii) 장소 인식 작업에 적절한 손실이 무엇인지. 이러한 문제를 해결하기 위해 Google 스트리트 뷰 타임 머신에서 시간이 지남에 따라 동일한 장소를 묘사하는 약하게 라벨링 된 이미지를 대량으로 얻을 수 있음을 먼저 보여줍니다. 둘째, Street View Time Machine 이미지의 불완전하고 시끄러운 위치 특수 효과를 처리 할 수있는 새로운 약하게 감독 된 3 중 순위 랭킹을 디자인 할 것입니다. 세부 사항은 아래와 같습니다. 

**타임머신으로부터의 약한 감독.** Google지도의 새로운 장소 인 Google 스트리트 뷰 타임 머신 (Street View Time Machine)을 사용하여 여러 시간에 찍은 여러 거리의 파노라마 이미지를지도상의 가까운 위치에서 제공합니다. 섹션 5.2에서 볼 수 있듯이,이 새로운 데이터 소스는 장소 인식을위한 이미지 표현을 학습하는 데 소중합니다. 그림 4에서 볼 수 있듯이, 동일한 위치가 다른 시간과 계절에 묘사되어 학습 알고리즘에 유용하고 산만 한 기능을 발견하는 데 사용할 수있는 중요한 정보와 이미지 표현이 불변해야하는 변경 사항을 제공하기 위해 학습 알고리즘에 제공됩니다. 좋은 장소 인식 성능을 얻을 수 있습니다. 

​	Time Machine 이미지의 단점은 불완전하고 시끄러운 감독 만 제공한다는 것입니다. 각 Time Machine 파노라마에는 가까운 위치의 파노라마를 식별하는 데 사용할 수있는지도의 대략적인 위치 만 표시하는 GPS 태그가 포함되어 있지만 표시된 장면의 부분 간에는 일치하지 않습니다. 상세하게, 테스트 질의는 카메라 폰으로부터의 투시 이미지이므로, 각 파노라마는 서로 다른 방향 및 두 개의 앙각 [10, 24, 35, 81]에서 고르게 샘플링 된 일련의 투시 이미지로 표현됩니다. 각 투시 영상은 소스 파노라마의 GPS 위치로 표시됩니다. 결과적으로 두 개의 지리적으로 근접한 원근감 이미지는 반드시 서로 다른 방향을 향하게되거나 교합이 발생할 수 있기 때문에 반드시 같은 대상을 묘사하지는 않습니다 (예 : 두 이미지가 서로의 모퉁이를 돌고 있음). 그러므로, 주어진 훈련 질의 q에 대해, GPS 정보는 (i) 잠재 긍정, 즉 지리적으로 질의에 가까운 이미지 및 (ii) 명확한 네거티브 {nqj}의 소스로서 만 사용될 수있다. 즉, 쿼리와 지리적으로 멀리 떨어져 있습니다.

**Weakly supervised triplet ranking loss.** 장소 인식 성능을 최적화하는 fθ 표현을 배우고 싶습니다. 즉, 주어진 테스트 질의 영상 q에 대해서, 데이터베이스의 모든 다른 원거리 영상 Ii보다 근접한 위치로부터 데이터베이스 영상 Ii *를 순위 매김하는 것이 목표이다. 다시 말해, 질의 q와 근접 영상 Ii * 사이의 유클리드 거리 dθ (q, I)가 데이터베이스 Ii에서 멀리 떨어진 영상까지의 거리, 즉 dθ (q, Ii *)보다 작기를 바란다. <dθ (q, Ii),지도상의 질의로부터 일정 거리 이상 떨어진 모든 이미지들에 대하여. 다음으로 우리는이 요구 사항이 훈련 트리플렛 {q, Ii *, Ii} 사이의 랭킹 손실로 어떻게 변환 될 수 있는지 보여줍니다. 

​	구글 스트리트 뷰 타임 머신 데이터로부터, 튜플 (q, {pqi}, {nqj})의 트레이닝 데이터 세트를 얻는데, 각 트레이닝 질의 이미지 q에 대해 우리는 잠재적 인 포지티브 세트 {pqi}와 세트 네거티브 {nqj}. 잠재적 인 긍정적 인 세트는 쿼리와 일치해야하는 적어도 하나의 긍정적 인 이미지를 포함하지만 우리는 어떤 이미지인지를 모릅니다. 이 모호성을 해결하기 위해 각 학습 튜플 (q, {p q i}, {n q j})에 대해 가장 일치하는 잠재적 인 양의 이미지 p q i *를 식별 할 것을 제안한다. 


$$
P_{i*}^q=\underset{P_i^q}{argmin}\ d_\theta(q,p_i^q) \qquad (5)
$$
목표는 훈련 질의 q와 가장 일치하는 잠재적 인 양의 pqi * 사이의 거리 dθ (q, pqi *)가 질의 q와 모든 거리 dθ (q, nqj)보다 작도록 이미지 표현 fθ를 학습하는 것이다. 음의 이미지 qj :


$$
d_\theta(q,p_{i*}^q) < d_\theta(q,n_j^q), \qquad \forall j. \qquad (6)
$$


이 직감에 기초하여, l은 경첩 손실 l (x) = max (x, 0)이고, m은 다음과 같이 훈련 튜플 (q, {pqi}, {nqj})에 대해 약한 감독 된 순위 손실 Lθ를 정의한다. 


$$
L_\theta=\sum_jl \underset{i}({min}d_\theta^2(q,p_i^q)+m-d_\theta^2(q,n_j^q)) \qquad (7)
$$


마진을 제공하는 상수 매개 변수. 방정식 (7)은 네거티브 영상 n q j에 대한 개별 손실의 합이다. 각각의 음수에 대해, 질의와 음수 사이의 거리가 질의와 가장 잘 맞는 양성 사이의 거리보다 마진만큼 큰 경우 손실 l은 0이다. 반대로, 네가티브 이미지까지의 거리와 최상의 매칭 플러스 사이의 마진이 위반되면, 손실은 위반 양에 비례합니다. 위의 손실은 일반적으로 사용되는 triplet loss [67,68,86,87]와 관련이 있지만 다중 인스턴스 학습 [20, 36]과 유사한 공식 (식 (5)에 의해 주어진)을 사용하여 약하게 감독 된 시나리오에 적용된다. , 85]. 우리는 Time Machine 데이터의 대규모 튜플 세트에서 확률 적 경사 (SGD)를 사용하여 표현 fθ의 매개 변수 θ를 학습합니다. 교육 절차의 세부 사항은 부록 A에 나와 있습니다.



### 5. Experiments

​	이 절에서는 사용 된 데이터 집합과 평가 방법론 (5.1 절)을 설명하고 우리의 접근 방식을 검증하기 위해 정량적 (5.2 절) 및 질적 (5.3 절) 결과를 제공합니다. 마지막으로 표준 이미지 검색 벤치 마크 (5.4 절)에서이 방법을 테스트합니다. 

#### 5.1. 데이터 세트 및 평가 방법(Datasets and evaluation methodology)

​	우리는 공개적으로 이용 가능한 두 가지 데이터 세트에 대한 결과를보고합니다. **피츠버그 (Pitts250k) **[81]에는 Google 스트리트 뷰에서 다운로드 한 250,000 개의 데이터베이스 이미지와 스트리트 뷰에서 생성 된 24k 테스트 쿼리가 포함되어 있지만 몇 년씩 서로 다른 시간대에 찍혔습니다. 이 데이터 세트를 훈련, 검증 및 테스트를 위해 대략 3 개의 부분으로 나눕니다. 각각 83k 개의 데이터베이스 이미지와 8k 개의 쿼리가 포함되어 있습니다. 여기에는 해당 세트가 독립적 인 이미지를 포함하도록 지리적으로 수행되었습니다. 더 빠른 훈련을 용이하게하기 위해 일부 실험에서 더 작은 부분 집합 (Pitts30k)이 사용되었으며, 지리적으로 떨어져있는 열차 / 발 (idation) / 테스트 세트 각각에 10k 개의 데이터베이스 이미지가 포함되어 있습니다. 

**도쿄 24/7** [80]에는 휴대 전화 카메라를 사용하여 촬영 한 76k 개의 데이터베이스 이미지와 315 개의 쿼리 이미지가 포함되어 있습니다. 데이터베이스 이미지는 주간, 일몰 및 야간에 가져온 매우 까다로운 데이터 세트입니다. 데이터베이스 이미지는 위에 설명 된대로 Google 스트리트 뷰에서 발생한 주간에만 촬영되었습니다. train / val 세트를 구성하기 위해 Google은 Time Machine 기능을 사용하여 도쿄의 Google Street View 파노라마를 추가로 수집하고이 세트를 **TokyoTM**라고 명명했습니다. 도쿄 24/7 (= 테스트)와 TokyoTM train / val은 모두 지리적으로 떨어져 있습니다. 분할에 대한 자세한 내용은 부록 B 에 나와 있습니다. 

**평가 메트릭.**우리는 표준 장소 인식 평가 절차 [4, 24, 65, 80, 81]를 따른다. 검색된 상위 N 개의 데이터베이스 이미지 중 적어도 하나가 쿼리의 지상 진실 위치에서 d = 25 미터 내에있는 경우 쿼리 이미지가 올바르게 지역화 된 것으로 간주됩니다. 도쿄 대학 24/7의 경우 [80]을 따르고 평가 전에 순위가 매겨진 데이터베이스 이미지에 대해 공간 최대가 아닌 억제를 수행합니다. 

**구현 세부 사항.** Max pooling (fmax) 계층과 NetVLAD (fV LAD) 계층으로 확장 된 두 개의 기본 아키텍처 인 AlexNet [37]과 VGG-16 [73]을 사용합니다. 둘 다 ReLU 이전에 마지막 컨볼 루션 계층 (conv5)에서 잘립니다. NetVLAD의 경우 K = 64를 사용하여 두 기본 아키텍처에 각각 16k 및 32k-D 이미지 표현을 사용합니다. 초기화 절차, 훈련에 사용 된 매개 변수, 훈련 튜플을 샘플링하는 절차 및 기타 구현 세부 사항은 부록 A에 나와 있습니다. 모든 훈련 및 평가 코드와 훈련 된 네트워크는 [1]에서 온라인으로 제공됩니다.

#### 5.2. Results and discussion

**베이스 라인 및 최첨단 기술.** 우리의 접근법의 이점을 평가하기 위해 장소 인식을 위해 훈련 된 표현을 다른 작업에 사전 계획된 "기성품"네트워크와 비교합니다. 즉, conv5에서 기본 네트워크가 절단되면 기준선은 Max pooling (fmax)을 사용하거나 설명자를 VLAD (fV LAD)로 집계하지만 더 이상의 작업 별 교육을 수행하지 않습니다. AlexNet [37], VGG-16 [73]은 AlexNet과 동일한 아키텍처를 재사용하지만 장면 분류를 위해 사전 훈련 된 ImageNet 분류 [18]와 Places205 [91]에 대해 사전 교육을받습니다. Pretrained 네트워크는 최근 인스턴스 검색을위한 off-the-shelf dense descriptor 추출기로 사용되었고 [6, 7, 22, 60, 62] 훈련되지 않은 fmax 네트워크는 [6, 62]의 방법에 해당합니다. 

![Comparison of our methods versus off-the-shelf networks and state-of-the-art.ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/04ed40ce8b1bb2a631a321802738a95eca197cc5/7-Figure5-1.png)

그림 5. **기존 방식의 네트워크와 최첨단 방식의 네트워크 비교.** 기본 CNN 아키텍처는 (A) lexNet 및 (V) GG-16으로 괄호 안에 표시됩니다. AlexNet, Places205, VGG-16의 경우 파란색, 청록색, 녹색), fV LAD (-o-)가 fmax보다 우수합니다 (AlexNet 및 VGG-16의 빨간색과 마젠타 색) VGG-16 기반의 fV LAD + 화이트닝 (- * -) 표현은 모든 데이터 세트에 최첨단 기술을 제공합니다. [80] 방법은 다른 데이터 세트에서 사용할 수없는 깊이 데이터에 의존하기 때문에 도쿄 24/7에서만 평가되었습니다. 추가 결과는 부록 C에 나와 있습니다.

​	

또한, 장소 인식을 위해 훈련 된 CNN 표현을 최첨단의 로컬 피처 기반 컴팩트 디스크립터와 비교한다.이 기술자는 조밀하게 추출 된 RootSIFT [2, 43]의 내부에 정규화 된 VLAD 풀링 [29] ]. 설명자는 미백 및 L2 정규화 [25]와 결합 된 PCA (학습 세트에서 학습 됨)를 사용하여 선택적으로 4096 차원으로 축소됩니다. 이 설정은 뷰 합성과 함께 까다로운 도쿄 24/7 데이터 세트 (c.f. [80])에서 최첨단 결과를 제공합니다. 

​	다음은 피츠버그와 도쿄 24/7 벤치 마크에서 위에 요약 된 기준선에 대한 본 방법의 장소 인식 성능을 비교 한 그림 5에 대해 설명합니다. 차원 감소. 앞에서 설명한 것처럼 VLAD의 차원 축소를 수행하기위한 표준 최첨단 절차를 따릅니다. 즉 4096-D 로의 감소는 미백과 함께 L2- 정규화에 이어 PCA를 사용하여 수행됩니다 [25, 80]. 그림 5는 하위 차원 fV LAD (- * -)가 전체 크기 벡터 (-o-)와 유사하게 수행됨을 보여줍니다.

**차원 감소(Dimensionality reduction). **앞에서 설명한 것처럼 VLAD의 차원 축소를 수행하기위한 표준 최첨단 절차를 따릅니다. 즉 4096-D 로의 감소는 미백과 함께 L2- 정규화에 이어 PCA를 사용하여 수행됩니다 [25, 80]. 그림 5는 하위 차원 fV LAD (- * -)가 전체 크기 벡터 (-o-)와 유사하게 수행됨을 보여줍니다. 

**장소 인식을위한 엔드 투 엔드 교육의 이점(Benefits of end-to-end training for place recognition). **장소 인식의 최종 과제에 대해 교육받은 대표는 두 벤치 마크에서 큰 차이를 보이는 CNN에 의해 지속적으로 outperform합니다. 예를 들어, Pitts250k 테스트에서 우리의 훈련 된 NetVLAD 집계 레이어를 갖춘 AlexNet은 표준 VLAD 집계를 통해 상용 AlexNet에서 얻은 55.0 %와 비교하여 81.0 %의 회수율을 달성했습니다 (즉, 회수율이 상대적으로 향상됨). 47 %. 세 가지 데이터 세트 모두에서 비슷한 개선이 이루어질 수 있습니다. 이것은 (i) 우리의 접근법은 장소 인식을위한 풍부하면서도 간결한 이미지 표현을 습득 할 수 있고, (ii) 미리 만들어진 네트워크를 "기성품"으로 사용하는 대중적인 아이디어 [6, 7, 22, 60, 62]는 대상 또는 장면 분류를 위해 훈련 된 네트워크가 장소 인식의 최종 작업에 적절하지 않아서 최적 이하입니다. 우리는 이것이 "기성품"인 활성화가 유클리드 거리를 사용하여 비교할 수 있도록 훈련되지 않았다는 사실에 기인한다고 생각합니다. 

**최첨단 기술과의 비교(Comparison with state-of-the-art).** 그림 5는 또한 VGG-16 (마젠타 - * -)에 기반한 미백을 사용한 우리의 숙련 된 fV LAD 표현이 RootSIFT + VLAD + 백미 닝과 Torii 외의 방법을 능가하는 것으로 나타남을 보여줍니다. [80], 따라서 모든 벤치 마크에서 압축 된 설명자를위한 최첨단 기술을 설정합니다. 이들은 장소 인식 작업에 대한 대부분의 기성 CNN 기술자를 능가하는 강력한 기준선입니다. 

**VLAD versus Max.** fV LAD (-o-) 메소드를 해당 fmax (-x-) 대응 아이템과 비교하여 VLAD 풀링이 기성품 및 숙련 된 표현 모두에서 최대 풀링보다 훨씬 우수하다는 것이 분명합니다. NetVLAD 성능은 차원 적으로 우아하게 감소합니다. 128-D NetVLAD는 512-D Max (42.9 % 대 38.4 %는 도쿄 24/7의 38 %)와 유사하게 작동하므로 동일한 성능에 비해 4 배 더 작아집니다. 또한 NetVLAD + 화이트닝은 동일한 차원 (60 %)으로 줄 였을 때 맥스 풀링보다 월등히 뛰어납니다. 자세한 내용은 부록 C를 참조하십시오. 

**어떤 레이어를 교육해야합니까?** 표 1에서 우리는 장소 인식의 최종 과제에 대해 서로 다른 계층을 훈련 할 때 얻을 수있는 이점을 연구합니다. 가장 큰 개선 사항은 NetVLAD 레이어를 교육하는 덕분이지만 다른 레이어를 교육하면 추가 개선이 이루어지며 일부 overfitting은 conv2 아래에서 발생합니다.

**Time Machine 교육의 중요성.** 여기에서는 Time Machine (TM) 데이터없이 네트워크를 교육 할 수 있는지 검토합니다. 상세히, 우리는 훈련 데이터베이스 이미지와 동일한 세트로부터 샘플링되도록, 즉 트레이닝에 사용 된 쿼리 및 데이터베이스 이미지의 튜플을 동시에 캡처 한 Pitts30k-train에 대한 트레이닝 쿼리 세트를 수정했다. Alexnet은 33.5 %이고, TM이없는 훈련은 38.7 %로 향상되었습니다. 그러나 TM을 사용한 교육을 통해 68.5 %의 데이터를 얻었으므로 네트워크가 잘되지 않는 경우에도 Time Machine 데이터가 좋은 장소 인식 정확도에 중요합니다. 예를 들어, 네트워크는 장소 인식을 위해 자동차를 인식하는 것이 중요하다는 것을 알게됩니다. 동일한 주차 된 자동차가 모든 장소의 이미지에 나타나기 때문입니다. 

#### 5.3. Qualitative evaluation

​	 장소 인식 아키텍처에서 무엇을 배우고 있는지 시각화하기 위해 Zeiler와 Fergus [89]의 분류 네트워크의 폐색 민감도를 검사하는 방법을 채택합니다. 그림 6에서 볼 수 있듯이, 상용화 된 AlexNet (ImageNet에 사전 교육 된)은 인식 할 수 있도록 훈련 된 범주 (예 : 자동차)와 12 개의 다양한 볼 유형을 구별하는 데 유용한 원형 모양과 같은 특정 모양에 매우 중점을 둡니다 ImageNet 카테고리. 장소 205 카테고리 네트워크는 특정 장소가 아닌 장면 수준 카테고리를 인식하는 것을 목표로하지 않기 때문에 모든 폐색에 상당히 반응하지 않으므로 건물의 특정 부분과 같이 이미지의 중요한 부분이 폐색 되었더라도 여전히 "빌딩 건축물"이미지 설명 자에 해당하는 유사한 출력 기능을 제공합니다. 이 두 가지와는 달리, 특정 장소 인식을 위해 훈련 된 네트워크는 특정 위치에 차별적이지 않은 자동차 및 사람과 같은 혼란스러운 기능을 자동으로 무시하고 건물의 외관 및 스카이 라인을 설명하는 데 초점을 맞 춥니 다. 보다 질적 인 예가 부록 C에 나와 있습니다.

#### 5.4 Image retrieval

표준 피사체 및 이미지 검색 벤치 마크에 대한 이미지 표현을 추출하기 위해 피츠버그에서 완전히 훈련 된 최고의 성능을 발휘하는 네트워크 (VGG-16, fV LAD, 256-D까지 미백 기능 포함)를 사용합니다. 우리의 표현은 옥스포드 5k [53], 파리 6k에서 63.5 %, 73.5 % 및 79.9 %의 mAP를 얻는 세 가지 데이터 세트 모두에서 컴팩트 이미지 표현 (256-D)의 최첨단을 세 가지 데이터 세트로 크게 설정합니다. [54], 휴일 [26]; 예를 들어 옥스포드 5k의 경우 20 %의 상대적 향상을 보입니다. 부록 C에는보다 자세한 결과가수록되어 있습니다. 

### 6. Conclusions

​	우리는 약식으로 감독 된 스트리트 뷰 타임 머신 (Street View Time Machine) 데이터에서 엔드 포인트 방식으로 장소 인식을 위해 훈련 된 새로운 콘볼 루션 뉴럴 네트워크 아키텍처를 설계했습니다. 우리의 훈련 된 표현은 기성품 CNN 모델보다 월등히 뛰어나며 도전적인 24/7 Tokyo 데이터 세트뿐만 아니라 옥스포드 및 파리 이미지 검색 벤치 마크에서 최첨단 기술을 훨씬 능가합니다. 우리 아키텍처의 두 가지 주요 구성 요소 인 (i) NetVLAD 풀링 계층과 (ii) 약한 감독 랭킹 손실은 장소 인식 작업 이외의 일반적인 CNN 빌딩 블록입니다. NetVLAD 계층은 다른 CNN 아키텍처에 쉽게 연결될 수있는 학습 가능한 매개 변수가있는 강력한 풀링 메커니즘을 제공합니다. 약하게 감독 된 순위 손실은 예를 들어 자연 언어로 묘사 된 이미지와 같이 약한 라벨을 붙인 많은 양의 데이터가있는 다른 순위 작업에 대한 종단 간 학습의 가능성을 열어줍니다 [33].



### References

[1] Project webpage (code/networks). http://www.di. ens.fr/willow/research/netvlad/. 6, 11 

[2] R. Arandjelovic and A. Zisserman. Three things everyone ´ should know to improve object retrieval. In Proc. CVPR, 2012. 2, 7 

[3] R. Arandjelovic and A. Zisserman. All about VLAD. In ´ Proc. CVPR, 2013. 1, 2, 3, 4, 7 

[4] R. Arandjelovic and A. Zisserman. DisLocation: Scalable ´ descriptor distinctiveness for location recognition. In Proc. ACCV, 2014. 1, 2, 6 

[5] M. Aubry, B. C. Russell, and J. Sivic. Painting-to-3D model alignment via discriminative visual elements. ACM Transactions on Graphics (TOG), 33(2):14, 2014. 1 

[6] H. Azizpour, A. Razavian, J. Sullivan, A. Maki, and S. Carlsson. Factors of transferability from a generic ConvNet representation. CoRR, abs/1406.5774, 2014. 2, 3, 5, 6, 7, 12, 13 

[7] A. Babenko and V. Lempitsky. Aggregating local deep features for image retrieval. In Proc. ICCV, 2015. 2, 3, 6, 7, 12, 13, 14 

[8] A. Babenko, A. Slesarev, A. Chigorin, and V. Lempitsky. Neural codes for image retrieval. In Proc. ECCV, 2014. 2, 14 

[9] S. Cao and N. Snavely. Graph-based discriminative learning for location recognition. In Proc. CVPR, 2013. 1, 2 

[10] D. M. Chen, G. Baatz, K. Koeser, S. S. Tsai, R. Vedantham, T. Pylvanainen, K. Roimela, X. Chen, J. Bach, M. Pollefeys, B. Girod, and R. Grzeszczuk. City-scale landmark identification on mobile devices. In Proc. CVPR, 2011. 1, 2, 5, 11 

[11] O. Chum, A. Mikulik, M. Perdoch, and J. Matas. Total recall ˇ II: Query expansion revisited. In Proc. CVPR, 2011. 2 

[12] O. Chum, J. Philbin, J. Sivic, M. Isard, and A. Zisserman. Total recall: Automatic query expansion with a generative feature model for object retrieval. In Proc. ICCV, 2007. 2 

[13] M. Cimpoi, S. Maji, and A. Vedaldi. Deep filter banks for texture recognition and segmentation. In Proc. CVPR, 2015. 3, 4 

[14] G. Csurka, C. Bray, C. Dance, and L. Fan. Visual categorization with bags of keypoints. In Workshop on Statistical Learning in Computer Vision, ECCV, pages 1–22, 2004. 3 

[15] M. Cummins and P. Newman. FAB-MAP: Probabilistic localization and mapping in the space of appearance. The International Journal of Robotics Research, 2008. 1, 2 

[16] M. Cummins and P. Newman. Highly scalable appearanceonly SLAM - FAB-MAP 2.0. In RSS, 2009. 1, 2 

[17] J. Delhumeau, P.-H. Gosselin, H. Jegou, and P. P ´ erez. Re- ´ visiting the VLAD image representation. In Proc. ACMM, 2013. 2 

[18] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. FeiFei. ImageNet: A large-scale hierarchical image database. In Proc. CVPR, 2009. 6 

[19] J. Donahue, Y. Jia, O. Vinyals, J. Hoffman, N. Zhang, E. Tzeng, and T. Darrell. DeCAF: A deep convolutional activation feature for generic visual recognition. CoRR, abs/1310.1531, 2013. 1 

[20] J. Foulds and E. Frank. A review of multi-instance learning assumptions. The Knowledge Engineering Review, 25(01):1–25, 2010. 6 

[21] R. B. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich feature hierarchies for accurate object detection and semantic segmentation. In Proc. CVPR, 2014. 1, 13 

[22] Y. Gong, L. Wang, R. Guo, and S. Lazebnik. Multi-scale orderless pooling of deep convolutional activation features. In Proc. ECCV, 2014. 2, 3, 4, 6, 7, 12, 13 

[23] A. Gordo, J. A. Rodr´ıguez-Serrano, F. Perronnin, and E. Valveny. Leveraging category-level labels for instance-level image retrieval. In Proc. CVPR, pages 3045–3052, 2012. 14 

[24] P. Gronat, G. Obozinski, J. Sivic, and T. Pajdla. Learning and calibrating per-location classifiers for visual place recognition. In Proc. CVPR, 2013. 1, 2, 5, 6, 11 

[25] H. Jegou and O. Chum. Negative evidences and co- ´ occurrences in image retrieval: the benefit of PCA and whitening. In Proc. ECCV, 2012. 2, 7 

[26] H. Jegou, M. Douze, and C. Schmid. Hamming embedding ´ and weak geometric consistency for large scale image search. In Proc. ECCV, pages 304–317, 2008. 2, 8, 14 

[27] H. Jegou, M. Douze, and C. Schmid. On the burstiness of ´ visual elements. In Proc. CVPR, Jun 2009. 2 

[28] H. Jegou, M. Douze, and C. Schmid. Product quantization ´ for nearest neighbor search. IEEE PAMI, 2011. 1 

[29] H. Jegou, M. Douze, C. Schmid, and P. P ´ erez. Aggregating ´ local descriptors into a compact image representation. In Proc. CVPR, 2010. 1, 2, 3, 7 

[30] H. Jegou, H. Harzallah, and C. Schmid. A contextual dis- ´ similarity measure for accurate and efficient image search. In Proc. CVPR, 2007. 2 

[31] H. Jegou, F. Perronnin, M. Douze, J. S ´ anchez, P. P ´ erez, and ´ C. Schmid. Aggregating local images descriptors into compact codes. IEEE PAMI, 2012. 1 

[32] H. Jegou and A. Zisserman. Triangulation embedding and ´ democratic aggregation for image search. In Proc. CVPR, 2014. 2, 14 

[33] A. Karpathy and L. Fei-Fei. Deep visual-semantic alignments for generating image descriptions. In Proc. CVPR, 2015. 8 

[34] A. Kendall, M. Grimes, and R. Cipolla. PoseNet: A convolutional network for real-time 6-DOF camera relocalization. In Proc. ICCV, 2015. 2 

[35] J. Knopp, J. Sivic, and T. Pajdla. Avoiding confusing features in place recognition. In Proc. ECCV, 2010. 1, 2, 5, 11 

[36] D. Kotzias, M. Denil, P. Blunsom, and N. de Freitas. Deep multi-instance transfer learning. CoRR, abs/1411.3128, 2014. 6 

[37] A. Krizhevsky, I. Sutskever, and G. E. Hinton. ImageNet classification with deep convolutional neural networks. In NIPS, pages 1106–1114, 2012. 1, 2, 6, 11, 12 

[38] Y. LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard, W. Hubbard, and L. D. Jackel. Backpropagation applied to handwritten zip code recognition. Neural Computation, 1(4):541–551, 1989. 1 

[39] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradientbased learning applied to document recognition. Proceedings of the IEEE, 86(11):2278–2324, 1998. 1 

[40] Y. Li, N. Snavely, D. Huttenlocher, and P. Fua. Worldwide pose estimation using 3D point clouds. In Proc. ECCV, 2012. 1 

[41] T.-Y. Lin, Y. Cui, S. Belongie, and J. Hays. Learning deep 9 representations for ground-to-aerial geolocalization. In Proc. CVPR, 2015. 2 

[42] T.-Y. Lin, A. RoyChowdhury, and S. Maji. Bilinear CNN models for fine-grained visual recognition. In Proc. ICCV, 2015. 4 

[43] D. Lowe. Distinctive image features from scale-invariant keypoints. IJCV, 60(2):91–110, 2004. 1, 3, 7 

[44] W. Maddern and S. Vidas. Towards robust night and day place recognition using visible and thermal imaging. In Proc. Intl. Conf. on Robotics and Automation, 2014. 1, 2 

[45] A. Makadia. Feature tracking for wide-baseline image retrieval. In Proc. ECCV, 2010. 2 

[46] C. McManus, W. Churchill, W. Maddern, A. Stewart, and P. Newman. Shady dealings: Robust, long-term visual localisation using illumination invariance. In Proc. Intl. Conf. on Robotics and Automation, 2014. 1, 2 

[47] S. Middelberg, T. Sattler, O. Untzelmann, and L. Kobbelt. Scalable 6-DOF localization on mobile devices. In Proc. ECCV, 2014. 1 

[48] A. Mikulik, M. Perdoch, O. Chum, and J. Matas. Learning a ˇ fine vocabulary. In Proc. ECCV, 2010. 2 

[49] M. Oquab, L. Bottou, I. Laptev, and J. Sivic. Learning and transferring mid-level image representations using convolutional neural networks. In Proc. CVPR, 2014. 1, 13 

[50] M. Paulin, M. Douze, Z. Harchaoui, J. Mairal, F. Perronnin, and C. Schmid. Local convolutional features with unsupervised training for image retrieval. In Proc. ICCV, 2015. 2 

[51] F. Perronnin and D. Dance. Fisher kernels on visual vocabularies for image categorization. In Proc. CVPR, 2007. 2 

[52] F. Perronnin, Y. Liu, J. Sanchez, and H. Poirier. Large-scale ´ image retrieval with compressed fisher vectors. In Proc. CVPR, 2010. 1, 2 

[53] J. Philbin, O. Chum, M. Isard, J. Sivic, and A. Zisserman. Object retrieval with large vocabularies and fast spatial matching. In Proc. CVPR, 2007. 1, 2, 8, 14 

[54] J. Philbin, O. Chum, M. Isard, J. Sivic, and A. Zisserman. Lost in quantization: Improving particular object retrieval in large scale image databases. In Proc. CVPR, 2008. 2, 8, 14 

[55] J. Philbin, M. Isard, J. Sivic, and A. Zisserman. Descriptor learning for efficient retrieval. In Proc. ECCV, 2010. 2 

[56] D. Qin, X. Chen, M. Guillaumin, and L. V. Gool. Quantized kernel learning for feature matching. In NIPS, 2014. 2 

[57] D. Qin, Y. Chen, M. Guillaumin, and L. V. Gool. Learning to rank bag-of-word histograms for large-scale object retrieval. In Proc. BMVC., 2014. 2 

[58] D. Qin, S. Gammeter, L. Bossard, T. Quack, and L. Van Gool. Hello neighbor: accurate object retrieval with k-reciprocal nearest neighbors. In Proc. CVPR, 2011. 2 

[59] D. Qin, C. Wengert, and L. V. Gool. Query adaptive similarity for large scale object retrieval. In Proc. CVPR, 2013. 2 

[60] A. S. Razavian, H. Azizpour, J. Sullivan, and S. Carlsson. CNN features off-the-shelf: An astounding baseline for recognition. CoRR, abs/1403.6382, 2014. 2, 5, 6, 7, 12, 13 

[61] A. S. Razavian, J. Sullivan, A. Maki, and S. Carlsson. A baseline for visual instance retrieval with deep convolutional networks. CoRR, abs/1412.6574v2, 2014. 14 

[62] A. S. Razavian, J. Sullivan, A. Maki, and S. Carlsson. A baseline for visual instance retrieval with deep convolutional networks. In Proc. ICLR, 2015. 2, 3, 5, 6, 7, 12, 13, 14 

[63] T. Sattler, M. Havlena, F. Radenovic, K. Schindler, and ´ M. Pollefeys. Hyperpoints and fine vocabularies for largescale location recognition. In Proc. ICCV, 2015. 1, 2

[64] T. Sattler, B. Leibe, and L. Kobbelt. Fast image-based localization using direct 2D–to–3D matching. In Proc. ICCV, 2011. 1, 2 

[65] T. Sattler, T. Weyand, B. Leibe, and L. Kobbelt. Image retrieval for image-based localization revisited. In Proc. BMVC., 2012. 1, 2, 6 

[66] G. Schindler, M. Brown, and R. Szeliski. City-scale location recognition. In Proc. CVPR, 2007. 1, 2 

[67] F. Schroff, D. Kalenichenko, and J. Philbin. FaceNet: A unified embedding for face recognition and clustering. In Proc. CVPR, 2015. 6 

[68] M. Schultz and T. Joachims. Learning a distance metric from relative comparisons. In NIPS, 2004. 6 

[69] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus, and Y. LeCun. OverFeat: Integrated recognition, localization and detection using convolutional networks. CoRR, abs/1312.6229, 2013. 1 

[70] E. Simo-Serra, E. Trulls, L. Ferraz, I. Kokkinos, and F. Moreno-Noguer. Fracking deep convolutional image descriptors. CoRR, abs/1412.6537, 2014. 2 

[71] K. Simonyan, A. Vedaldi, and A. Zisserman. Descriptor learning using convex optimisation. In Proc. ECCV, 2012. 2 

[72] K. Simonyan, A. Vedaldi, and A. Zisserman. Deep Fisher networks for large-scale image classification. In NIPS, 2013. 4 

[73] K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition. In Proc. ICLR, 2015. 1, 6, 11 

[74] J. Sivic and A. Zisserman. Video Google: A text retrieval approach to object matching in videos. In Proc. ICCV, volume 2, pages 1470–1477, 2003. 1, 3 

[75] N. Sunderhauf, S. Shirazi, A. Jacobson, E. Pepperell, F. Dayoub, B. Upcroft, and M. Milford. Place recognition with ConvNet landmarks: Viewpoint-robust, condition-robust, training-free. In Robotics: Science and Systems, 2015. 1, 2 

[76] V. Sydorov, M. Sakurada, and C. Lampert. Deep fisher kernels – end to end learning of the fisher kernel GMM parameters. In Proc. CVPR, 2014. 4 

[77] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich. Going deeper with convolutions. In Proc. CVPR, 2014. 1 

[78] G. Tolias, Y. Avrithis, and H. Jegou. To aggregate or not ´ to aggregate: Selective match kernels for image search. In Proc. ICCV, 2013. 2

[79] G. Tolias and H. Jegou. Visual query expansion with or with- ´ out geometry: refining local descriptors by feature aggregation. Pattern Recognition, 2014. 2 

[80] A. Torii, R. Arandjelovic, J. Sivic, M. Okutomi, and T. Pa- ´ jdla. 24/7 place recognition by view synthesis. In Proc. CVPR, 2015. 1, 2, 6, 7, 11, 12, 15 

[81] A. Torii, J. Sivic, T. Pajdla, and M. Okutomi. Visual place recognition with repetitive structures. In Proc. CVPR, 2013. 1, 2, 5, 6, 11, 12 

[82] T. Turcot and D. G. Lowe. Better matching with fewer features: The selection of useful features in large database 10 recognition problems. In ICCV Workshop on Emergent Issues in Large Amounts of Visual Data (WS-LAVD), 2009. 2 

[83] T. Tuytelaars and K. Mikolajczyk. Local invariant feature detectors: A survey. Foundations and TrendsR in Computer Graphics and Vision, 3(3):177–280, 2008. 1 

[84] A. Vedaldi and K. Lenc. Matconvnet – convolutional neural networks for matlab. 2015. 11 

[85] P. Viola, J. C. Platt, and C. Zhang. Multiple instance boosting for object detection. In NIPS, 2005. 6 

[86] J. Wang, Y. Song, T. Leung, C. Rosenberg, J. Wang, J. Philbin, B. Chen, and Y. Wu. Learning fine-grained image similarity with deep ranking. In Proc. CVPR, 2014. 6 

[87] K. Q. Weinberger, J. Blitzer, and L. Saul. Distance metric learning for large margin nearest neighbor classification. In NIPS, 2006. 6 

[88] S. Winder, G. Hua, and M. Brown. Picking the best DAISY. In Proc. CVPR, pages 178–185, 2009. 2 

[89] M. D. Zeiler and R. Fergus. Visualizing and understanding convolutional networks. In Proc. ECCV, 2014. 1, 8, 13 

[90] J. Zepeda and P. Perez. Exemplar SVMs as visual feature ´ encoders. In Proc. CVPR, 2015. 2 

[91] B. Zhou, A. Lapedriza, J. Xiao, A. Torralba, and A. Oliva. Learning deep features for scene recognition using places database. In NIPS, 2014. 1, 6, 12