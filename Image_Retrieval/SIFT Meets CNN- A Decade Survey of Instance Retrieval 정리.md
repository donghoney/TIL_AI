## SIFT Meets CNN: A Decade Survey of Instance Retrieval

### Abstract

초기에는 콘텐츠 기반 이미지 검색 (CBIR)이 글로벌 기능으로 연구되었습니다.
2003 년 이래로 로컬 변환 자 (사실상 SIFT)를 기반으로 한 이미지 검색은 이미지 변환을 처리 할 때 SIFT의 이점으로 인해 10여 년 동안 광범위하게 연구되었습니다.
최근에는 CNN (Convolutional Neural Network)을 기반으로 한 이미지 표현이 커뮤니티에 대한 관심을 높이고 인상적인 성능을 보였습니다.
급속한 진화가 이뤄지면서 이 기사에서는 지난 10 년 동안의 인스턴스 검색에 대한 포괄적인 survey를 제공합니다.
SIFT 기반 및 CNN 기반 방식의 두 가지 범주가 제시됩니다.
전자의 경우 코드북 크기에 따라 문헌을 큰 / 중형 / 소형 코드북을 사용하여 구성합니다.
후자의 경우, 세 가지 방법, 즉 사전 훈련 또는 미세 조정 된 CNN 모델 및 하이브리드 방법을 사용하여 논의합니다.
첫 번째 두 개는 이미지를 네트워크로 단일 패스 (pass)하고, 마지막 카테고리는 패치 기반 피쳐 추출 방식을 사용합니다.
이 설문 조사는 현대의 인스턴스 검색에서 이정표를 제시하고, 다양한 카테고리의 이전 작품을 광범위하게 검토하며, SIFT와 CNN 기반 방법 간의 연결에 대한 통찰력을 제공합니다.
여러 데이터 세트에서 여러 카테고리의 검색 성능을 분석하고 비교 한 후 일반 및 특수 인스턴스 검색에 대한 유망한 방향을 논의합니다.

## 1. INTRODUCTION

CONTENT 기반 이미지 검색 (CBIR)은 컴퓨터 비전 사회에서 오랫동안 연구 주제였습니다.
1990 년대 초, CBIR에 대한 연구가 시작되었습니다.
이미지는 텍스쳐와 컬러와 같은 시각적 신호에 의해 인덱싱되었고 무수히 많은 알고리즘과 이미지 검색 시스템이 제안되었습니다.
간단한 전략은 글로벌 디스크립터를 추출하는 것이다.
이 아이디어는 1990 년대와 2000 년대 초반에 이미지 검색 커뮤니티를 지배했습니다.
그러나 잘 알려진 문제는 전역 시그니처가 조명, 변환, 교합 및 절단과 같은 이미지 변경에 대한 불변 예측에 실패 할 수 있다는 것입니다.
이러한 차이는 검색 정확도를 떨어 뜨리고 전역 설명자의 응용 범위를 제한합니다.
이 문제는 로컬 피처 기반 이미지 검색을 발생 시켰습니다. 이 survey의 초점은 인스턴스 수준 이미지 검색입니다. 이 작업에서는 특정 객체 / 장면 / 아키텍처를 묘사하는 쿼리 이미지가 주어지면 동일한 이미지를 포함하는 이미지를 검색하는 것이 목표입니다.
인스턴스 검색은 쿼리를 사용하여 동일한 클래스의 이미지를 검색하는 것을 목표로 클래스 검색 [1]에서 출발합니다.
다음에서 지정하지 않으면 “이미지 검색(image retrieval)"과 “인스턴스 검색(instance retrieval)"이 혼용됩니다.
지난 몇 년 동안의 인스턴스 검색의 목표는 그림 1에 제시되어있다.

1에서 SIFT 기반 및 CNN 기반 방법의 시간이 강조 표시됩니다.
전통적인 방법의 대부분은 Smeulders 등이 CBIR에 대한 포괄적인 survey를 발표했을 때 “2000 년 말에" 끝났다고 볼 수 있다.
3 년 후 (2003 년) Bag-of-Words (BoW) 모델이 이미지 검색 커뮤니티 [3]에 소개되었고 2004 년 SIFT 디스크립터에 의존 [5]하는 이미지 분류 [4]에 적용되었습니다.
검색 커뮤니티는 이후 많은 개선이 제안 된 10 년 동안 BoW 모델의 중요성을 목격했습니다.
2012 년 Krizhevsky 등 [6]은 AlexNet과 함께 ILSRVC 2012에서 최첨단 인식 정확도를 달성하여 이전의 최상의 결과를 큰 폭으로 초과했습니다.
그 이후로, 연구 초점은 심층적 인 학습 기반의 방법들, 특히 convolutional 신경 네트워크 (CNN)로 옮겨지기 시작했다 [7, 8].
SIFT 기반 방법은 주로 BoW 모델에 의존합니다.. 
BoW는 원래 텍스트를 단어로 파싱하기 때문에 문서를 모델링하기 위해 제안되었습니다.
단어 응답을 전역 벡터로 누적하여 문서에 대한 단어 히스토그램을 작성합니다.
이미지 도메인에서 SIFT (scale-invariant feature transform) [5]의 도입은 BoW 모델을 실현 가능하게 만든다.
원래 SIFT는 탐지기와 디스크립터로 구성되었지만 현재는 격리되어 사용됩니다. 이 survey에서 SIFT는 지정되지 않은 경우 일반적으로 커뮤니티에서 일반적인 관행 인 128-dim 설명자를 참조합니다.
사전 훈련 된 코드북 (어휘)을 사용하여 로컬 기능을 시각적 단어로 양자화합니다.
따라서 이미지는 문서와 비슷한 형태로 표현 될 수 있으며 고전 가중치 부여 및 인덱싱 체계가 활용 될 수 있습니다.
최근 몇 년 동안, SIFT 기반 모델의 인기는 많은 비전 작업에서 손으로 만들어진 features을 능가하는 것으로 보인 계층적 구조 인 CNN (convolutional neural network)에 의해 압도되었습니다.
검색에서, CNN 벡터가 짧은 경우에도 BoW 모델에 비해 경쟁력있는 성능이 보고 되었습니다 [10, 16, 17].

![Fig. 1: Milestones [5], [6], [7], [8], [9], [10], [11], [12], [13], [14] of BoW based image retrieval. Times for BoW models based on SIFT or CNN features are covered in blue and red, respectively, marked by the pioneering work of Krizhevsky et al. [8].](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/6d902439b736a7546dd8872b307fb760087ca629/2-Figure1-1.png)

CNN 기반 검색 모델은 일반적으로 압축 표현을 계산하고 유클리드 거리 또는 일부 근사 이웃 (ANN) 검색 방법을 검색에 사용합니다. 현재 문헌은 사전 훈련 된 CNN 모델을 직접 사용하거나 특정 검색 작업을 위해 미세 조정(fine-tunning)을 수행 할 수 있습니다.
이러한 방법의 대부분은 descriptor를 얻기 위해 이미지를 네트워크로 한 번만 보냅니다(feed).
일부는 SIFT와 비슷한 방식으로 네트워크에 여러 번 전달되는 패치를 기반으로 합니다. 우리는 이 survey에서 하이브리드 방식으로 분류합니다.

#### 1.1 Organization of This Paper

이 논문은 변경된 시점에 SIFT 기반 및 CNN 기반 인스턴스 검색 방법에 대한 포괄적인 문헌 조사를 제공합니다.
먼저 섹션 2에서 분류 방법론을 제시합니다.
그런 다음 섹션 3과 섹션 4에서 두 가지 주요 메소드 유형을 각각 설명합니다.
여러 벤치 마크 데이터 세트에서 섹션 5는 SIFT와 CNN 기반 방법의 비교를 요약합니다.
6 절에서 우리는 두 가지 가능한 미래 방향을 지적한다.
이 조사는 7 절에서 결론 지을 것이다.

### 2 CATEGORIZATION METHODOLOGY

다양한 시각적 표현에 따르면이 설문 조사는 검색 문헌을 SIFT 기반 및 CNN 기반의 두 가지 유형으로 분류합니다.
SIFT 기반의 방법은 대형, 중형 또는 소형 코드북(large, medium-sized or small codebooks)을 사용하는 세 가지 클래스로 구성됩니다.
코드북 크기는 인코딩 방법의 선택과 밀접한 관련이 있습니다.
CNN 기반의 방법은 하이브리드 방법뿐만 아니라 사전 훈련 된 또는 미세 조정 된 CNN 모델을 사용하여 분류됩니다.
이들의 유사점과 차이점은 표 1에 요약되어 있습니다.

![image-20190731023924478](/Users/donghoon/Library/Application Support/typora-user-images/image-20190731023924478.png)

SIFT 기반의 방법은 2012 년 이전에 주로 연구되었다 (좋은 연구가 최근 몇 년 간 등장한다) [18].
이 방법의 라인은 일반적으로 하나의 타입의 검출기, 예를 들어 Hessian-Affine 및 하나의 타입의 디스크립터 (예를 들어, SIFT)를 사용한다.
인코딩(Encoding)은 로컬 feature을 벡터에 매핑합니다.
인코딩 과정에서 사용 된 코드북의 크기를 기반으로 SIFT 기반 방법을 다음과 같은 세 가지 범주로 분류합니다.

- 작은 코드북 사용. 
  시각적 단어(visual word)는 수천 개 미만입니다. 
  컴팩트 벡터는 차원(dimension) 감소 및 코딩 전에 생성된다 [14,15].
- 중형 코드북 사용. 
  BoW의 희소성과 시각적 단어의 낮은 차별성을 고려할 때, 역 색인(inverted index)과 이진 서명(binary signatures)이 사용된다 [13]. 
  정확도(accuracy)와 효율성(efficiency) 사이의 절충이 주요한 영향을 미치는 요인이다 [20].
- 대형 코드북 사용. 
  BoW 히스토그램과 시각적 단어의 높은 판별 능력을 고려할 때 역 색인(inverted index)과 메모리 친화적 인 서명(memory-friendly signatures)이 사용된다 [21]. 
  근사 방법은 코드북 생성 및 인코딩 [11], [12]에서 사용된다.

CNN 기반 메서드는 CNN 모델을 사용하여 features을 추출합니다.
일반적으로 소형 (고정 길이) 표현이 작성됩니다.
세 가지 classes가 있습니다.

* 하이브리드 방식(Hybrid methods)
  * 이미지 패치는 특징 추출을 위해 CNN에 여러 번 공급된다 [7].
    인코딩과 인덱싱은 SIFT 기반의 방법과 유사하다 [22].

* 사전 훈련 된 CNN 모델 사용
  * 특징(Features)은 ImageNet과 같은 일부 대규모 데이터 세트에서 사전 훈련 된 CNN을 사용하여 단일 패스(single pass)에서 추출됩니다 [23].
    Compact Encoding / pooling 기법이 사용된다 [9, 10].

* 미세 조정된(fine-tuned) CNN 모델 사용.
  * CNN 모델 (예 : ImageNet에서 사전 교육)은 이미지가 대상 데이터베이스와 유사한 분포를 공유하는 교육 세트에서 미세 조정됩니다 [8].
  * CNN 기능은 CNN 모델에 대한 단일 통과를 통해 종단 간 방식으로 추출 할 수 있습니다.
  * 시각적 표현은 향상된 식별 능력을 나타낸다 [17,24].

### 3 SIFT-BASED IMAGE RETRIEVAL

#### 3.1 Pipeline

SIFT 기반 검색의 파이프 라인은 그림 2의 로컬 피쳐(Local feature) 추출에서 소개된다.

![Fig. 2: Pipeline of the Bag-of-Words (BoW) model. For the three method types, feature detection and description are performed in different manners which will be described in Section 3. These local features are quantized to visual words pre-defined in a codebook (Section 4). The inverted index or feature encodings are used for retrieval efficiency, to be covered in Section 5.](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/6d902439b736a7546dd8872b307fb760087ca629/3-Figure2-1.png)

우리가 N 개의 이미지로 구성된 갤러리 G를 가지고 있다고 가정합니다.
feature detector가 주어지면, 우리는 희소한 관심 지점이나 조밀한 패치 주위의 지역에서 local descriptors를 추출합니다.
우리는 이미지에서 D개의 검출된 영역의 로컬 디스크립터를 s로 나타낸다.

#####코드북 교육(codebook training)

SIFT 기반의 방법은 코드북을 오프라인에서 훈련시킵니다.
코드북의 각 시각적 단어는 “보로노이 셀 (Voronoi cell)"이라고 불리는 부분 공간의 중심에 있다.
큰 코드북은 더 세분화 된 분할에 해당하며, 그 결과 더 판별적인 시각적 단어가 생기고 그 반대도 마찬가지입니다.
로컬 디스크립터 s이 레이블이 지정되지 않은 트레이닝 세트로부터 계산된다고 가정하십시오.
베이스 라인 접근법, 즉, kmeans는 M 포인트를 K 클러스터로 분할한다; 따라서, K 개의 시각적 단어는 크기 K의 코드북을 구성한다.

##### Feature 인코딩.

로컬 디스크립터 s는 feature 부호화 과정 s를 통해 피쳐 임베딩s으로 사상된다.

k-means 클러스터링을 사용하면 s는 visual words와의 거리에 따라 인코딩 될 수 있습니다.
대형 코드북의 경우 하드(hard) [11], [12] 및 소프트 양자화(soft quantization) [25]가 좋은 선택입니다.
전자의 경우, 결과물 인 embedding s는 단지 하나의 0이 아닌 엔트리를 가진다; 후자에서, s는 소수의 시각적 단어로 양자화 될 수있다.
global signature은 로컬 피처의 모든 embeddings을 sum-pooling 한 후에 생성됩니다.
중형 코드북의 경우 원본 정보를 보존하기 위해 추가 바이너리 서명(additional binary signatures)을 생성 할 수 있습니다.
작은 코드북을 사용할 때, 널리 사용되는 부호화(encoding) 체계는 VLAD (vector of locally aggregated descriptors) [15], Fisher vector(FV)[14] 를 포함한다.

#### 3.2 Local Feature Extraction

local invariant features은 이미지 사이의 지역 구조(local structures)를 정확하게 일치시키는 것을 목표로 한다 [26].
SIFT 기반의 방법은 일반적으로 특징 검출기(detector)와 디스크립터(descriptor)로 구성된 유사한 특징 추출 단계를 공유한다.


##### 로컬 탐지기(Local detector)

관심 지점 검출기는 다양한 이미징 조건 하에서 안정한 지역 집합을 안정적으로 위치시키는 것을 목표로합니다.
검색(retrieval) 커뮤니티에서 아핀-공변(affine-covariant) 영역을 찾는 것을 선호합니다.
검출된 영역의 모양이 아핀 변환에 따라 변해서 영역 내용 (descriptors)은 불변이 될 수 있어서 “공변 (covariant)"이라고 불립니다.
이러한 종류의 검출기는 Hessian 검출기 [27]와 같은 키포인트 중심 검출기와 다르며, the difference of Gaussians (DoG) [5] 검출기와 같은 스케일 불변 영역에 초점을 맞추는 센서와는 다릅니다.
국소 강도 패턴(local intensity patterns)에 적응되는 타원형 영역(Elliptical regions)은 아핀 검출기(detectors)에 의해 생성된다.
이는 동일한 로컬 구조가 관점 변화에 의해 야기되는 변형 하에서 보장되는 것을 보장한다. 예를 들어 인스턴스 검색에서 종종 발생하는 문제, 마일스톤(milestone) 작업 [3], MSER (Maximally Stable Extremal Region) 탐지기 [28] 및 아핀 확장 된 Harris- 라플라스 검출기가 사용되며, 둘 다 아핀 불변 영역 검출기이다.
MSER는 몇 가지 후속 연구 [11, 29]에서 사용된다.
Hessianaffine 검출기 [30]는 검색에 널리 채택되어 왔으며, Gaussians (DoG) 검출기 [13,31]의 차이점보다 우수한 것으로 나타 났으며, 큰 시야 변화하는 지역 구조.
이러한 아핀 - 공변량 영역(affine-covariant regions)의 방향 모호성을 수정하기 위해 중력 가정이 만들어졌다 [32].
오리엔테이션(orientation) 추정을 무시한 관행은 이후의 연구 [33, 34]에서 사용되었고, 객체가 일반적으로 직립(upright)인 아키텍처 데이터 집합에 일관된 향상을 보여줍니다.
다른 비 아핀(non-affine) 탐지기는 [35]에서 사용 된 Laplacian of Gaussian (LOG) 및 Harris 탐지기와 같은 검색에서도 테스트되었습니다.
표면이 매끄러운 물체의 경우 관심 지점이 거의 감지되지 않으므로 물체 경계는 지역 설명을위한 좋은 후보가됩니다.
다른 한편으로, 일부는 고밀도 영역 검출기를 사용한다.
조밀하게 샘플 된 이미지 패치와 검출 된 패치 사이의 비교에서, Sicre 등 [37]은 전자의 우월성을보고했다.
고밀도 샘플링의 회전 불변성(rotation invariance)을 복구하기 위해 패치의 주된 각도는 [38]에서 추정된다.
다양한 고밀도 샘플링(dense sampling) 전략, 관심 지점(interest point) 탐지기 및 그 사이의 포괄적 인 비교는 [39]에서 액세스 할 수 있습니다.

##### 로컬 디스크립터(Local Descriptor)

탐지 된 영역 세트를 사용하여 descriptors는 로컬 컨텐츠를 인코딩(encode)합니다.
SIFT [5]가 기본 디스크립터로 사용되었습니다.
128-Dim 벡터는 일치하는 정확도로 경쟁 디스크립터를 능가하는 것으로 나타났습니다 [40].
확장에서 PCA-SIFT [41]는 피처 계산과 고유성 손실에서 더 많은 시간을 들여 매칭 프로세스의 속도를 높이기 위해 차원을 128에서 36으로 줄입니다.
또 다른 개선점은 RootSIFT [33]이다. 두 단계로 계산된다 : 1) SIFT 기술자를 정규화한다. 2) 각 요소를 제곱한다.
RootSIFT는 현재 SIFT 기반 검색에서 루틴으로 사용되며 SURF [42]도 널리 사용됩니다.
그것은 Hessian-Laplace detector와 local gradient histogram의 local descriptor를 결합합니다.
적분 이미지는 가속(acceleration)에 사용됩니다.
SURF는 SIFT와 비교할만한 일치 정확도를 가지고 있으며 계산이 더 빠릅니다.
SIFT, PCA-SIFT 및 SURF 간의 비교는 [43]을 참조하십시오.
매칭 속도를 더 가속화하기 위해, 바이너리 디스크립터(binary descriptors) [44]는 유클리드 거리를 매칭(matching) 중에 해밍 거리(Hamming distance)로 대체한다.
hand-crafted descriptors와 별도로 일부는 로컬 descriptors의 판별 능력을 향상시키는 학습 방법을 제안합니다.
예를 들어, Philbin et al [45]은 비선형 변환을 제안하여 투영 된 SIFT 서술자가 진정한 일치에 대해 더 작은 거리를 산출한다.
Simoyan et al [34]은 풀링 영역과 선형(linear) 디스크립터 투영법(projection)을 학습함으로써이 과정을 개선한다.

#### 3.3 Retrieval Using Small Codebooks

작은 코드북은 수천, 수백 또는 그 이하의 visual words를 가지므로 코드북 생성 및 인코딩의 계산 복잡성은 보통입니다.
대표적인 작품으로는 BoW [3], VLAD [15], FV [14]가 있습니다.
우리는 주로 VLAD와 FV를 논의하고 BoW 컴팩트 벡터의 포괄적 인 평가를 위해 [46]을 독자들에게 소개합니다.

##### 3.3.1 Codebook Generation

클러스터링 복잡성은 코드북 크기에 크게 의존합니다. VLAD [15] 또는 FV [14]에 기초한 작업에서, 코드북 크기는 일반적으로 작다 (예를 들어, 64, 128, 256).
VLAD의 경우, 플랫 k-means이 코드북 생성에 사용됩니다.
FV에 대해, 가우시안 혼합 모델 (GMM), 즉, K가 가우시안 혼합물의 수인 경우, 최대 우도 추정(maximum likelihood estimation)을 사용하여, $$u_\lambda(x) = \sum_{i=1}^Kw_iv_i(x)$$를 트레이닝한다.

GMM describes the feature space with a mixture of K Gaussian distributions, and can be denoted as s, where s , s and s represent the mixture weight, the mean vector and the covariance matrix of Gaussian ui , respectively.

#### 3.3.2 Encoding 

작은 코드북 크기 덕분에, 상대적으로 복잡하고 정보를 보존하는 인코딩 기술을 적용 할 수 있습니다.
우리는 주로이 섹션에서 FV, VLAD 및 개선점을 설명합니다.
사전 훈련 된 GMM 모델을 통해 FV는 로컬 features과 GMM 센터 간의 평균 1 차 및 2 차(the averaged first and second order) 차이를 설명합니다.

그 차원은 $$2pK$$이며, 여기서 p는 로컬 디스크립터의 차원이고, K는 GMM의 코드북 크기이다.
FV는 일반적으로 버스트 니스(burstiness) 문제 (3.4.3 절에서 설명)를 억제하기 위해 파워 노말라이제이션(normalization) [47], [14]를 거친다.
이 단계에서 FV의 각 구성 요소는 매개 변수 α에 의해 특징 지어지는 비선형 변환을 겪습니다. 
$$
x_i :=sign(x_i)||x_i||^\alpha
$$
그런 다음 l2 정규화가 사용됩니다.
나중에 FV는 여러 측면에서 개선되었습니다.
예를 들어, Koniusz 등 [48]은 각 디스크립터(descriptor)를 공간(spatial) 좌표(coordinates)와 관련 튜닝 가능(tunable) 가중치로 보완한다.
[49]에서 더 큰 코드북 (최대 4,096 개)이 생성되어 계산 효율성 측면에서 작은 코드북에 대해 우수한 분류 정확도를 보여줍니다.
Cinbis 등 [50]은 local region이 iid하다는 가정을 수정하기 위해 버스트 효과를 줄이고 power normalization보다 수율을 향상시키는 non-iid 모델을 제안한다.
Jégou 등 [15]이 제안한 **VLAD 인코딩 체계는 FV의 단순화 된 버전**으로 생각할 수있다.
코드북에서 가장 가까운 시각적 단어로 지역 특징을 양자화하고 그 차이를 기록합니다.
가장 가까운 이웃 탐색(Nearest neighbor search)은 작은 코드북 크기 때문에 수행된다.
잔여 벡터(residual vectors)는 sum 풀링과 정규화(normalizations)에 의해 집계됩니다.
VLAD의 차원은 $$pK$$입니다.
몇몇 중요한 인코딩 기술의 비교는 [51], [52]에 제시되어있다.
다시 말하지만, VLAD의 개선은 여러 측면에서 비롯됩니다.
[53]에서 Jégou와 Chum은 시각적 단어 동시 발생과 연관성을 없애기 위해 PCA와 화이트닝 (표 5에서 PCAw로 표시) 사용 및 양자화 손실을 줄이기 위한 다중 코드북 교육을 제안합니다.
[54], Arandjelovi’c 등은 VLAD를 세 가지 측면에서 확장합니다 1) 즉 내부 정규화 (intra-normalization)라고 불리는 각각의 거친 클러스터 내의 잔여 합(residual sum)을 정규화하고, 2) 데이터 집합 전송 문제(dataset transfer problem)를 해결하기 위한 어휘 적응과 3) 작은 객체 발견을 위한 multi-VLAD
[54]와 동시에 Delhumeau et al[55]은 잔여 합(residual sums) 대신 각 잔차 벡터(each residual vector)를 정규화(normalize)하는 것을 제안한다. 그들은 또한 치수 감소를 수행하지 않는 각 Voronoi 셀 내의 지역 PCA를 [52] 옹호한다.
최근 연구 [56]에서는 소프트 할당(soft assignment)을 사용하고 하드 양자화(hard quantization)보다 향상된 각각의 랭크에 대해 최적의 가중치를 경험적으로 학습합니다.
VLAD, FV, BoW, 지역 제한적 선형 코딩 (localality-constrained linear coding, LLC) [57] 및 단항 임베딩 (monomial embedding)과 같은 다양한 임베딩 방법을 이용하는 일반적인 기술이 있음을 주목하십시오.
Tolias 등 [58]은 embeddings의 판별적(discriminative) 인 능력을 향상시키기 위해 SIFT 디스크립터와 함께 SIFT 영역의 지배적인 방향을 부호화 하기 위한 방향성 공변 임베딩(orientation covariant embedding)을 제안한다.
유사한 지배적인 방향을 갖는 매칭점이 상향 가중(up-weighted)되도록 반대 영역에서 기하학적 큐를 사용함으로써 약한 기하학적 일관성 (WGC) [13]과 유사한 공분산 속성(covariance property)을 얻습니다.
삼각측량 임베딩(The triangulation embedding) [18]은 입력 벡터의 크기 대신 방향을 고려합니다.
Jégou et al [18]은 또한 매핑된 벡터 간의 간섭을 제한하는 민주적 합산(democratic aggregation)을 제시한다.
Murray와 Perronnin [59]은 민주적인 집단화와 비슷한 개념을 보완하면서 풀링 된 벡터와 각 코딩 표현 사이의 유사성을 균등화함으로써 최적화 된 일반화 된 최대 풀링 (GMP)을 제안한다.
BoW, VLAD 및 FV의 계산 복잡성은 비슷합니다.
우리는 오프라인 교육(offline training) 및 SIFT 추출 단계를 무시합니다.
visual word 할당 중에 각 피쳐는 VLAD (또는 FV)의 모든 시각적 단어 (또는 가우스)와의 거리 (또는 부드러운 할당 계수)를 계산해야 합니다.
따라서 이 단계는 O (pK)의 복잡성을 갖습니다.
다른 단계에서는 복잡도가 O (pK)를 초과하지 않습니다.
Embedding의 펌핑을 고려하면, 인코딩 프로세스는 O (pKD)의 전체적인 복잡성을 가지며, 여기서 D는 이미지의 피쳐 수( the number of features in an image)입니다.
VLAD의 변형 인 Triangulation embedding [18]은 비슷한 복잡성을 가지고있다.
다중 VLAD [54]의 복잡성은 O (pKD)이기도하지만 더 많은 비용이 소요되는 매칭 프로세스가 있습니다.
계층 적 VLAD [60]는 O (pKK0D)의 복잡성을 갖는다. 여기서 K0는 2 차 코드북의 크기이다.
집합 단계에서 GMP [59]와 민주적 집합 [18]은 매우 복잡하다.
GMP의 복잡성은 O (P 2 K)입니다. 여기서 P는 피쳐 내장의 차원이고 민주적 인 집계의 계산 비용은 Sinkhorn 알고리즘에서 비롯됩니다.

#### 3.3.3 ANN Search
VLAD / FV 삽입의 높은 차원 때문에 효율적인 압축(efficient compression)과 ANN 탐색 방법이 사용되었다 [61], [62].
예를 들어, 주성분 분석 (PCA)은 일반적으로 차원 축소에 적용되며, PCA [53] 이후에 검색 정확도가 증가하는 것으로 나타났습니다.
해싱 기반 ANN 방법의 경우, Perronnin 등 [47]은 지역 민감성 해싱(locality sensitive hashing) [63]과 스펙트럼 해싱(spectral hashing) [64]과 같은 표준 이진 인코딩(binary encoding) 기법을 사용한다.
그럼에도 불구하고 SIFT 및 GIST 기능 데이터 세트에서 테스트 할 때 스펙트럼 해싱은 제품 양자화 (Product Quantization, PQ) [61]에 비해 성능이 낮다.
이러한 양자화 기반 ANN 방법에서, PQ는 FLANN [62]과 같은 다른 대중적인 ANN 방법보다 우수함이 입증되었다.
VLAD와 PQ에 대한 자세한 논의는 [65]에서 볼 수있다.
이후 PQ는 여러 가지 작업을 통해 개선되었습니다.
[66]에서 Douze 등은 인접한 중심들이 작은 해밍 거리를 갖도록 클러스터 중심을 재정렬하는 것을 제안한다.
이 방법은 해밍 거리 기반 ANN 검색과 호환되며 PQ에 상당한 속도 향상을 제공합니다.
우리는 ANN 접근법에 대한 조사를 위해 독자들에게 [67]를 추천한다.
또한 새로운 ANN 기술, 즉 그룹 테스트 [68], [69], [70]를 언급한다.

요컨대, 데이터베이스는 그룹으로 분해되며, 각 그룹은 그룹 벡터로 표시됩니다.
쿼리와 그룹 벡터를 비교하면 그룹에 진정한 일치가 얼마나 많이 포함되는지 알 수 있습니다.
그룹 벡터(group vectors)가 데이터베이스 벡터(database vectors)보다 훨씬 적기 때문에 검색 시간이 단축됩니다.
Iscen 등 [69]은 명시 적으로 그룹을 형성하지 않고 데이터베이스를 요약하는 최상의 그룹 벡터를 직접 찾아내어 메모리 소비를 줄이는 방법을 제안한다.

### 3.4 Retrieval Using Large Codebooks

큰 코드북에는 1 백만 개의 [11], [12] 개의 시각적 단어가 포함될 수 있습니다 [71], [72].
일부 주요 단계는 작은 코드북을 사용하는 것과 비교하여 중요한 변화를 겪습니다.

#### 3.4.1 Codebook Generation

근사 방법(Approximate methods)은 많은 수의 클러스터에 데이터를 할당하는 데 중요합니다.

검색(retrieval) 커뮤니티에서 두 대표적인 작품은 그림 1과 그림 3에서와 같이 계층 적 k - 수단hierarchical k-means (HKM) [11]과 근사 k - 수단 approximate k-means (AKM) [12]입니다.
2006 년에 제안 된 HKM은 피쳐 학습에 표준 kmeans를 계층적으로 적용합니다.
먼저 포인트들을 소수의 클러스터들 (e.g,, s) 로 분할 한 다음, 각각의 클러스터를 재귀적으로 다른 클러스터들로 분할한다.
모든 재귀에서 각 점은 클러스터 트리의 깊이가 O (log K) 인 s 클러스터 중 하나에 할당되어야합니다. 여기서 K는 대상 클러스터 번호입니다.
따라서 HKM의 계산 비용은 $$O(\bar{k}MlogK)$$이며, 여기서 M은 훈련 샘플의 수입니다.
K가 클 때 (큰 코드북) 평평한 k-means O (MK)의 복잡성보다 훨씬 작습니다.
큰 코드북 생성의 또 다른 이정표(milestone)는 AKM [12]입니다.
이 방법은 랜덤 k-d 트리의 포레스트를 사용하여 K 클러스터 센터를 인덱싱하므로 할당 단계를 ANN 검색으로 효율적으로 수행 할 수 있습니다.
AKM에서, 할당 비용은 $$O(KlogK+vMlogK)=O(vMlogK)$$로 기재 될 수 있으며, 여기서 v는 k-d 트리에서 액세스 될 가장 가까운 클러스터 후보의 수이다.
따라서 AKM의 계산 복잡도는 HKM과 동등하며 K가 클 때 평면 k-means보다 훨씬 작습니다.
실험 결과에 따르면 AKM은 양자화 오차가 낮기 때문에 HKM보다 우수합니다 (3.4.2 절 참조).
대부분의 AKM 기반 방법에서 ANN 검색의 기본 선택 사항은 FLANN [62]입니다.

#### 3.4.2 Feature Encoding (Quantization)

ANN 검색은 두 구성 요소 모두에서 중요하기 때문에 피처 인코딩(Feature encoding)은 코드북 클러스터링과 인터리빙됩니다.
AKM 및 HKM과 같은 일부 고전적인 방법에서 암시 된 ANN 기술은 클러스터링 및 인코딩 단계 모두에서 사용할 수 있습니다.
대형 코드북에서 핵심적인 트레이드 오프(key trade-off)는 양자화 오차(quantization error)와 계산 복잡성(computational complexity) 사이입니다.
엔코딩 단계에서 FV [14], 스파스 코딩(sparse coding) [73]과 같은 정보 보존 부호화(information-preserving encoding) 방법은 계산상의 복잡성으로 인하여 대부분 불가능하다.
따라서, 양자화 프로세스를 효율적으로 유지하면서 양자화 에러를 감소시키는 방법은 여전히 ​​어려운 문제로 남아있다.
Fro the ANN methods, 가장 초기의 솔루션은 계층적인 트리 구조를 따라 로컬 feature를 양자화하는 것이다.
서로 다른 레벨의 양자화 트리 노드에는 다른 가중치가 할당됩니다.
그러나 매우 불균형 한 트리 구조 때문에 이 방법은 k-d 트리 기반의 양자화 방법보다 성능이 좋지 않다. 빠른 ANN 검색을 위해 코드북에서 빌드 된 k-d 트리를 사용하여 하나의 시각적 단어가 각 로컬 피쳐에 할당된다.
이 하드 양자화 기법(hard quantization scheme)을 개선 한 Philbin 등 [25]은 특징을 몇 개의 가장 가까운 시각적 단어(nearest visual words)로 양자화하여 부드러운 양자화(soft quantization)를 제안한다.
각 할당 된 시각적 단어(visual word)의 가중치(weight)는 $$exp(-\frac{d^2}{2\sigma^2})$$에 의해 특징으로부터의 거리에 역으로 관련된다. 여기서 d는 설명자(descriptor)와 클러스터 중심(cluster center) 간의 거리이다.
소프트 양자화는 Euclidean distance를 기반으로하지만, Mikulik 등 [71]은 감독되지 않은 매칭 피쳐를 통해 각 시각적 단어에 대한 관련 시각적 단어(relevant visual words)를 찾는 것을 제안한다.
확률 론적(probabilistic) 모델을 기반으로 작성된 이러한 대체 단어는 일치하는 기능의 설명자(descriptors)를 포함하는 경향이 있습니다.
Cai 등 [74]은 소프트 양자화(soft quantization)의 메모리 비용과 질의 시각적 단어의 수(the number of query visual words)를 줄이기 위해 로컬 피처가 가장 가까운 시각 단어와 멀리 떨어져있을 때 성능 하락없이 버려질 수 있다(can be discarded)고 제안했다(suggest).
양자화를 더욱 가속화하기 위해 스칼라 양자화(scalar quantization) [75]는 명시 적으로 훈련 된 코드북 없이도 로컬 피처를 양자화 할 것을 제안합니다.
부동 소수점 벡터가 이진화되고 결과 바이너리 벡터의 첫 번째 차원이 시각적 단어로 십진수로 직접 변환됩니다.
큰 양자화 오류(large quantization error) 및 낮은 재현율(low recal)의 경우 스칼라 양자화는 비트 플롭(bit-flop)을 사용하여 로컬 피처에 대해 수백 개의 시각적 단어를 생성합니다.

#### 3.4.3 Feature Weighting

##### TF-IDF

코드북 C의 시각적 단어는 일반적으로 BoW 인코딩과 통합된 용어 빈도 및 역 문서 빈도 (TF-IDF)라고하는 특정 가중치가 할당됩니다.
TF는 다음과 같이 정의됩니다.
$$
TF(c_i^j)= o_i^j
$$
여기서, $$o_i^j$$는 이미지 $$j$$내의 시각적 단어 $$c_i$$의 발생 횟수이다.
따라서 TF는 지역 가중치(local weight)입니다.
한편, IDF는 글로벌 통계를 통해 주어진 시각적 단어의 기여도를 결정합니다.
시각적 단어 $$c_i$$의 기본 IDF 가중치는 다음과 같이 계산됩니다.
$$
IDF(c_i)=log\frac{N}{n_i},when\ n_i=\sum_{j}1(o_i^j>0)
$$
여기서 N은 갤러리 이미지의 수이며, $$n_i$$는 단어 $$c_i$$가 나타나는 이미지 수를 인코딩합니다.
이미지 j에서 시각적 단어 $$c_i$$에 대한 TF-IDF 가중치는 
$$
w(c_i^j)=TF(c_i^j)IDF(c_i)
$$


이다.

##### Improvements(개선)
시각적 단어 가중과 관련된 주요 문제는 버스티니스 (burstiness)이다 [76].
이것은 반복적인 구조가 이미지에 나타나는 현상을 나타냅니다.
이 문제는 이미지 유사성을 지배하는 경향이 있습니다.
Jégou et al [76]은 burstiness를 다루기 위해 몇 가지 TF 변형을 제안한다.
효과적인 전략은 TF에 대한 제곱 연산을 수행하는 것입니다.
Revaud 등 [7]은 동일한 단어 색인을 사용하여 피쳐을 그룹화하는 대신 스코어링 기능에서 다운 웨이트 된 관련없는 이미지에서 자주 발생하는 키포인트 그룹을 검색하는 방법을 제안합니다.
위의 두 가지 방법은 양자화 후에 버스트 그룹(bursty groups)을 검출하지만, Shi 등 [19]은 디스크립터 단계에서 이를 검출한다.
검출된(detected) 버스트 디스크립터(descriptors)는 평균 풀링(average pooling)을 거치며 BoW 아키텍처에 공급됩니다.
Zheng 등 [78]은 IDF의 관점에서 버스트 니스를 다루기위한 $$L_p$$-norm IDF를 제안하고, Murata 등 [79]은 BM25 공식에 나중에 통합되는 지수 IDF를 설계한다.
대부분의 작품이 버스트를 억제하려고 시도 할 때, Torii 등 [80]은 이것을 가상의 특징으로 간주하고 버스트 감지 이후 새로운 유사성 측정(new similarity measurement)을 설계합니다.
또 다른 특징 가중 전략은 데이터베이스 측면에서의 피쳐 보강(feature augmentation)이다 [81, 33].
두 방법 모두 이미지 그래프를 오프라인으로 구성합니다. 두 이미지가 동일한 개체를 공유하는지 여부를 나타내는 가장자리가 있습니다.
[81]의 경우, 기하학적 검증을 통과하는 피처 만 보존되어 메모리 비용을 절감합니다.
그런 다음 기본 이미지의 피쳐가 연결 이미지의 모든 시각적 단어로 보강됩니다.
이 방법은 [33]에서 증강 된 영상에서 보이는 것으로 추정되는 시각적 단어 만 추가함으로써 시끄러운 시각적 단어가 제외 될 수 있도록 개선되었다.

#### 3.4.4 The Inverted Index

역 색인(inverted index)은 효율적인 저장 및 검색을 위해 설계되었으며 대개 대/중형 코드북에서 사용됩니다.
그 구조는 그림 4에 나와있다.

![SIFT Meets CNNì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/6d902439b736a7546dd8872b307fb760087ca629/10-Figure5-1.png)
역 색인(inverted index)은 각 엔트리가 코드북의 시각적 단어에 대응하는 1 차원 구조입니다.
각 단어 항목에는 거꾸로 된 목록이 첨부되고, 거꾸로 된 각 목록에서 색인 된 목록은 색인 된 features 또는 postings 라고합니다.
역 색인은 대형 코드북에서 시각적 단어 히스토그램의 sparse nature을 이용합니다. 
문헌에서 새로운 검색 방법은 역 색인으로 조정할 수 있어야합니다.
baseline [11], [12]에서 이미지 ID와 용어 빈도 (TF)는 posting에 저장됩니다.
다른 정보가 통합되면 크기가 작아야합니다.
예를 들어, [82]에서 메타 데이터는 디스크립터 문맥 가중치, 디스크립터 밀도, 평균 상대 로그 스케일 및 각 포스팅의 평균 방향 차이와 같이 양자화된다.
유사하게, 방향과 같은 양자화 된 공간 정보가 또한 저장 될 수있다 [83, 21].
동시 인덱싱 (co-indexing) [72]에서 역 색인이 전역 적으로 일관된 이웃으로 확장 될 때, 의미 상 고립 된 이미지는 메모리 소비를 줄이기 위해 삭제된다.
[84]에서, 원래의 1 차원 역 색인은 ANN 탐색을 위해 2 차원으로 확장되며, 이는 각 SIFT 서브 벡터에 대한 코드북을 학습한다.
나중에 로컬 색 및 SIFT 설명자를 통합하기 위해 [31]에 의한 인스턴스 검색에 적용됩니다.

### 3.5 Retrieval Using Medium-sized Codebooks

중형 코드북은 10 ~ 200,000 개의 시각적 단어가있는 코드북입니다.
시각적 단어는 중간 감별력(medium discriminative ability)을 나타내며, 일반적으로 역 색인이 구성됩니다.

#### 3.5.1 Codebook Generation and Quantization

큰 코드북 (3.4.1 절)에 비해 상대적으로 작은 계산 비용을 고려할 때, 코드북 생성을 위해 flat k-means가 채택 될 수있다 [85], [20].
또한 클러스터링을 위해 AKM [12]을 사용하는 것은 매우 경쟁력있는 검색 정확도를 제공한다는 [31,32]에서 보여진다.
양자화를 위해, 가장 가까운 이웃 탐색은 코드북에서 가장 가까운 시각적 단어를 찾는 데 사용될 수있다.
연습을하면 엄격한 ANN 알고리즘을 사용하면 경쟁력있는 검색 결과를 얻을 수 있습니다.
따라서 대형 코드북 (3.4.2 절) [25], [71], [74]에서의 양자화에 대한 광범위한 연구와 비교할 때 중소 규모 코드북에서의 양자화 문제에 초점을 맞춘 연구는 상대적으로 적습니다.

#### 3.5.2 Hamming Embedding and its improvements

중간 크기의 코드북에서 시각적 단어의 차별 능력(discriminative ability)은 크고 작은 코드북 사이에 있습니다.
따라서 양자화 중에 정보 손실을 보상하는 것이 중요합니다.
이를 위해, 중요한 작업, 즉 해밍 임베딩 (Hamming embedding, HE)이 지배적으로 사용되었다.
Jégou 등 [13]에 의해 제안 된 그는 중간 크기의 코드북에서 시각적 단어의 차별성을 크게 향상시킨다.
그는 우선 p 차원 공간에서 $$p_b$$차원 공간으로 SIFT 서술자 $$f\in\mathbb{R}^p$$를 매핑한다.
$$
x=P\cdot f=(x_1,...,x_{{p}_{b}})
$$
여기서 $$P\in \mathbb{R_b^p} *p$$ 는 투영 행렬이고, x는 저 차원 벡터이다.
랜덤 가우스 값들의 행렬을 생성하고 그것에 QR 인수를 적용함으로써, 행렬 P는 최종 직교 행렬의 첫 번째 pb 행들로 취해진다.
x를 이진화하기 위해, Jegou et al은 각 보로노이 셀(Voronoi cell) $$c_i $$에 속하는 기술자를 사용하여 저 차원 벡터의 중앙 벡터 $$\bar{x_i}=(\bar{x_1,i},...,\bar{x_{p_b},i})$$를 계산할 것을 제안한다.
주어진 기술자 f와 그것의 투영된 벡터 x, HE는 시각적 단어 $$c_t$$를 계산하고, HE 바이너리 벡터는 다음과 같이 계산됩니다.
$$
b_j(x) = \begin{cases}
1, & \mbox{if }x_j\mbox{ > } \bar{x_j,t}\\
0, & \mbox{ }\mbox{ otherwise}
\end{cases}
$$


여기서 b (x) = (b1 (x), …, bpb (x))는 치수 pb의 결과 HE 벡터이다. 
이진 feature b (x)는 피쳐 매칭( feature matching)를위한 2 차 검사로 사용됩니다.
한 쌍의 로컬 features는 두 가지 기준, 즉 1) 동일한 시각적 단어와 2) HE signatures 간의 작은 해밍 거리가 충족 될 때 진정한 일치입니다.
HE [85]의 확장은 피쳐 f1과 f2 사이의 정합 강도를 지수 함수에 의해 해밍 거리와 역으로 추정한다.
$$
w_{HE}(f_1,f_2)=exp(-\frac{\mathcal{H(b(x_1),b(x_2))}}{2\gamma^2})
$$
여기서, b (x1)와 b (x2)는 각각 f1과 f2의 HE 이진 벡터이고, H (·, ·)는 두 바이너리 벡터 간의 해밍 거리를 계산하며, $$\gamma$$는 가중 파라미터이다.
그림 6에서 볼 수 있듯이 HE [13]와 그 가중 버전 [85]은 2008 년과 2010 년에 상당한 정확도를 향상시킵니다.

![ê´ë ¨ ì´ë¯¸ì§](https://ask.qcloudimg.com/http-save/yehe-1342338/d4h98mcpp6.jpeg?imageView2/2/w/1620)
HE의 응용 프로그램에는 비디오 사본 탐지 [87], 이미지 분류 [88] 및 재 순위 지정 [89]이 포함됩니다.

예를 들어, 이미지 분류에서 패치 매칭 유사성은 선형 커널 기반 SVM [88]에 통합 된 HE에 의해 효율적으로 추정된다.
이미지 재 순위 지정에서 Tolias 등 [89]은 더 낮은 HE 임계 값을 사용하여 RANSAC에서 찾은 것과 유사한 엄격한 대응성(correspondences)을 찾으며 결과 이미지 하위 집합은 쿼리 재구성을위한 진정한 긍정을 포함 할 가능성이 높습니다.
HE에 대한 개선은 특히 매치 커널의 관점에서 많은 작업에서 관찰되었습니다 [20].
질의 측면에서 정보 손실을 줄이기 위해 Jain et al [90]은 벡터 대 바이너리(vector-to-binary) 거리 비교를 제안한다.
역 색인의 효율성을 유지하면서 벡터 - 초평면 거리를 활용합니다.
또한, Qin 등 [91]은 확률 론적 프레임 워크 내에서 고차원 매치 커널을 설계하고 거짓 매치의 거리 분포에 따라 국부적 특징 거리를 적응 적으로 정규화한다.
이 방법은 각 시각적 단어의 이웃 분포에 따라 특징 - 특징 거리(feature-feature distance) [91] 대신에 단어 - 단어 거리(word-word distance)가 정규화되는 [92]와 유사한 정신을 지닌다.
한 단어와 이웃(a word to its neighbors) 사이의 평균 거리는 [92]에서 거의 일정하게 정규화되어 있지만, 개별적인 임베딩의 기여를 민주화(democratizing)하려는 생각은 [18]에서 나중에 사용되었다.
[20]에서 Tolias et al은 VLAD와 그가 유사한 성격을 공유하고 [91]과 유사한 매칭 기능을 사용하여 로컬 특징 집합과 특징 - 특징 매칭(feature-to-feature matching) 사이에서 교환되는 새로운 매치 커널을 제안한다.
그들은 또한 HE에서 더 많은 비트 (예를 들어, 128)를 사용하는 것이 감소 된 효율성을 희생하여 원래의 64 비트 구조보다 우수함을 입증한다.
더 많은 비트 (256)가 [75]에서 사용되었지만,이 방법은 상대적으로 낮은 리콜 (recall)이 발생하기 쉽습니다.

### 3.6 Other Important Issues

#### 3.6.1 Feature Fusion

##### Local-global fusion

SIFT 공간에서의 유사성 때문에 HE가 거부했지만 다른 지역 (또는 지역) 기능이 융합되면이 문제가 해결 될 수 있습니다.
지역 - 지방 융합(local-local fusion)을위한 좋은 선택은 SIFT와 컬러 기술자를 결합하는 것이다.
color-SIFT 서술자의 사용은 불변성(invariance)과 차별성(discriminative ability) 사이의 절충을 부분적으로 다룰 수있다.
평가는 HSV-SIFT [94], HueSIFT [95], OpponentSIFT [93]과 같은 기술자에 대한 여러 인식 벤치 마크 [93]에 대한 평가가 수행되었다.
HSV-SIFT와 HueSIFT는 모두 스케일 불변이고 시프트 변이입니다.
OpponentSIFT는 상대 색상 공간의 모든 채널을 SIFT 설명자를 사용하여 설명하며 밝은 색상 변경에 강합니다.
[93]에서 데이터 집합에 대한 사전 지식이없는 경우 OpponentSIFT가 권장됩니다.
보다 최근의 연구에서, 이진 컬러 서명은 역 색인 [96], [31]에 저장된다.
일부 데이터 세트의 검색 정확도가 우수하더라도 잠재적 인 문제는 조명의 집중적 인 변화가 색상의 효율성을 떨어 뜨릴 수 있다는 것입니다.

##### Local-global fusion. 
로컬 및 글로벌 기능은 서로 다른 측면의 이미지를 설명하며 상호 보완적일 수 있습니다.

