## Beyond Bags of Features : Spatial Pyramid Matching for Recognizing Natural Scene Categories

**Beyond Bags of Features : Spatial Pyramid Matching for Recognizing Natural Scene Categories, CVPR'06**

> 링크 ) https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1641019



### Abstract

이 논문은 근사적인 전역 기하학적 대응(global geometric correspondence)을 기반으로 장면 범주(Scene categories)를 인식하는 방법을 제시한다.이 기법은 이미지를 점점 더 정밀한 하위 영역으로 분할하여 작동한다. 그리고 각 하위 영역안에 있는 local feature들의 히스토그램을 계산한다. 결과의 Spatial Pyramid(공간적인 피라미드)는 orderless한 bag of words 이미지 표현의 간단하고 계산상으로 효율적인 확장 방법이다. 그리고 까다로운(challenging) 장면 분류 작업에 크게 향상된 성능을 보여준다. 특히, 저자에 의해 제안된 방법은 Caltech-101 database에서 SOTA(State of the art)를 달성했고, 15개 자연 경관 카테고리의 대용량 database에서도 높은 정확도를 성취했다. Spatial Pyramid(공간 피라미드) 프레임워크는 Torralba의 gist와 Lowe의 SIFT 기술자를 포함한 최근에 제안된 이미지 기술자들의 성공에 대한 통찰력을 제공한다.



### 1. Instroduction

이 논문에서, 우리는 이미지의 semantic category 인식 문제를 고려한다. 예를 들어, 장면(숲, 거리, 오피스 등등)을 묘사하는 것으로 분류하고 싶거나 특정한 interest object를 포함하는 것으로 나타내는 문제이다. 이러한 전체 이미지 categorization task의 경우,  bag of features 방법은 local feature들의 orderless한 모음으로 이미지를 표현하고 있고, 최근 인상적인 퍼포먼스를 보여주었다. 

그렇지만, 이 방법은 feature들의 공간적 레이아웃(spatial layout)에 대한 모든 정보를 무시하기 때문에, 공간적 레이아웃에 대한 기술능력이 극도로 제한되어 있다. 특히, 그것들은 object를 배경으로부터 분리해 segmentation하거나 모양 자체를 캡쳐할 수 없다 . 불행하게도, 효과적인 구조 object 기술을 구축하기 위한 이러한 한계를 극복하는 것은 특히 인식 시스템이 심한 배경혼란, occulusion, 큰 시점 변화가 있을 때 작동하도록 만들어야 한다. Generative part model과 geometric correspondence 검색에 기반한 접근 방식은 상당한 계산 비용으로 강인함을 확보한다. 약간 더 효율적인 접근 방법은 이웃한 local feature들 간의 pairwise 관계로 기본적인 bag-of-features 표현을 보강하는 것이지만, 이 아이디어의 구현은 결론적이지 않은 결과를 가져왔다. 기하학적 변형에 대한 robustness를 확보하기 위한 또 하나의 전략은 affine-invariant detectors 과 같은 불변성(invaiance) 수준을 증가시키는 것이다. 그러나 최근 대규모 평가는 이 전략이 일반적으로 성과를 거두지 못했다고 말한다. 

> 논문에서는  background clutter , occulusion, 많은 시점 변화에 대한 강인성을 확보하기 위해 local feature들을 쌍으로 묶는 pairwise 관계를 구성해서 특징이 담긴 가방에 대한 표현을 보강하거나 affine 변환에 불변한 검출기를 사용해서 강인성을 확보하는 것을 말하고 있지만 두 가지 모두 좋은 성과를 거두지는 못했다고 말하고 있다.

저자들은 robust하고 기하학적으로 불변인 구조적 object 표현을 개발하려는 목표에 동참하고 있지만, 이 논문에서는 고정되어있는 sub-region에 대한 local feature들의 통계치를 토대로 전역적인 비불변 표현들을 재검토할 것을 제안한다. Grauman과 Darrell의 피라미드 매칭 기법을 적용한 효율적인 근사 기법을 사용하여 전체적인 스케일에서 rough한 기하학적인 Correspondence를 계산하는 커널 기반의 인식방법을 소개한다. 이 방법은 이미지를 반복적으로 세분화하고 점점 더 정밀한 해상도로 local feature의 히스토그램을 계산하는 것을 포함한다. 이 간단한 방법으로 기본 bag-of-feature 표현보다도 성능이 크게 향상되고 상세한 기하하적 correspondence에 기반한 방법에서도 성능이 크게 향상된다. 



이전 연구 결과에 따르면, 총체적인 방식으로 고려된 장면은 그 구성 대상을 분석하지 않고 semantic category에 대한 풍부한 단서를 산출한다. (이미지 전체를 보기 때문에 관심 object를 제외하고도 많은 정보를 담고 있겠죠?) 저자의 실험들에 따르면, 전체적인 장면을 식별하는 것 뿐만 아니라 이미지가 특정 오브젝트를 포함하는 것으로 카테고리화 하는 경우에도 오브젝트가 심하게 어수선하게 embed되어 있고 포즈와 모양이 매우 다를지라도 전역적인 표현(global representation)이 매우 효과적일 수 있음이 확인되었다. 하지만, 저자는 objet recognition을 위한 전역적인 방법을 지지하지 않는다. 대신에, 이 방법의 하위 역할을 상상한다. 이것은 이미지의 'gist'를 포착하고 특정 객체에 대한 후속 검색을 알리는 데 사용될 수 있다.(이미지의 global한 설명이 고속도로 일 가능성이 높은 경우에, toaster가 아닌 자동차를 높은 가능성으로 찾는 것) 게다가, 논문에서는 저자의 방법의 단순성과 효율성은 까다로운 데이터에 대해서 예기치 않게 높은 인식률을 나타냈고, 새로운 데이터셋을 보정하고 더 정교한 인식 접근법을 평가하는 데 좋은 기준이 될 수 있다고 말한다. 



### 2. Previous Work

컴퓨터 비전에서, 이미지 묘사를 위한 방법으로 히스토그램은 오랜 기간동안 사용되어 왔다. Koenderink와 VanDoorn은 orderless한 이미지나 히스토그램 값 스케일 공간에 대해서 히스토그램을 일반화했다.(즉, 주어진 위치와 스케일에서 각 가우스 계수에 대해 locally orderless한 이미지는 그 계수 위에 집계 된 이미지 특징의 히스토그램을 반환한다)

Spatial Pyramid(공간 피라미드) 접근법은 가우시안 스케일 공간 대신에 직사각형 윈도우의 고정된 계층 구조를 정의하는 locally orderless한 이미지의 대안적 공식으로 생각하면 된다. Koenderink와 VanDoorn는 locally orderless한 이미지가 시각적 인식에서 중요한 역할을 한다는 것을 설득력 있게 주장했다. 논문에서의 이미지 검색 실험은 공간 피라미드가 인지함에 있어서 두드러지는 특징들을 제시하고, locally orderless Matching이 이미지들 사이의  전반적인 지각적 유사성을 추정하는 강력한 메카니즘일 수 있다고 제안한다. 

**반복적으로 이미지를 서브 샘플링하고 각각의 새로운 레벨에서 픽셀 값의 글로벌 히스토그램을 계산하는 것을 포함하는 다중 해상도 히스토그램**과 **논문에서 제안된 방법**을 비교하는 것은 중요하다

다시 말하면, 다중 해상도 히스토그램(multi resolution histogram)은 feature가 계산되는 해상도(intensity values)를 변경하지만, 히스토그램 해상도(intensity scale)는 고정된 상태로 유지된다.

feature가 계산되는 해상도를 고정하는 것과 반대되는 방법을 사용하지만, 집계되는 공간 해상도는 다양하다. 그 결과 더 많은 정보를 보존하는 고차원 표현이 된다. 예를 들어, 얇은 검은 색 및 흰색 줄무니로 구성된 이미지는 공간 피라미드(논문에서 제안된 방법)의 모든 level에서 두가지 mode를 유지하지만, 반면에 다중 해상도 히스토그램의 가장 정밀한 Level을 제외한 것들은 균인하게 회색 이미지와 본래 이미지를 구분할 수 없게 된다. 

> 다중 해상도 히스토그램은 level이 높아질 수록 해상도를 점점 높여가기 때문에, 높은 level의 이미지는 세밀하고 정밀한 정보들이 사라진 상태이다. 그리고 히스토그램 형태는 균일하게 유지된다. 
>
> 반면, 공간 피라미드(Spatial Pyramid)를 사용한 방법은 feature가 계산되는 공간의 해상도를 변경하기 때문에, 다양한 공간 해상도의 히스토그램 분포를 얻을 수 있다. 

결론적으로, 다중 해상도 히스토그램과 달리, 공간 피라미드는 적절한 커널이 함께 적용 될때, 대략적인 기하학적 매칭에 사용될 수 있다. 

**Subdivide** 와 **disorder** 의 operation 즉, 이미지를 서브블록들로 분할하고 이러한 서브 블록들의 local feature들의 히스토그램(또는 평균과 같은 히스토그램 통계치)를 계산하는 것은 global한 이미지 설명 과 interest 지역의 local한 설명 두가지 모두를 위해 컴퓨터 비전 영역에서 여러번 사용되어왔다.

그러므로, 이 operation이 근본적인 것 처럼 보이지만, 이전 방법에서는 적절한 subdivision 체계가 무엇인지에 대한 질문을 던지고 (비록 regular 4x4 그리드가 가장 인기있는 구현 선택인 것처럼 보이지만) **subdividing** 과 **disordering** 사이의 적절한 균형점이 무엇인지 질문을 던진다. 

공간 피라미드 프레임워크는 이 문제를 해결할 수 있는 방법을 제시한다. 즉, 여러 해상도가 원칙적으로 결합된 경우 최고의 결과를 달성할 수 있다. 이 사실은 **subdivide and disorder** 기법의 실험적인 성공은 대략적인 geometric matching를 실제로 수행하고 있음을  보여준다.



### 3. Spatial Pyramid Matching

먼저 피라미드의 원래 공식을 설명한다. 그리고 저자들의 공간 피라미드 이미지 표현 애플리케이션을 소개한다.

#### 3.1 Pyramid Match Kernels

d-차원 특징 공간에서 X와 Y를 벡터들의 두 세트라고 하자. Grauman and Darrell 는 두 세트 사이의 대략적인 correspondence를 찾는 pyramid matching을 제안한다. 비공식적으로 피라미드 매칭은 점점 더 거친 그리드의 시퀀스를 배치하여 작동하고 각각 level의 해상도에서 나타난 매치의 수를 가중 합을 취한다. 어떤 고정 해상도에서, 두 점은 그리드의 같은 셀에 떨어지면 일치한다고 말한다. 더 정밀한 해상도에서 발견된 match들은 더 거친 해상도에서 발견된 match들보다 더 많이 가중된다. 구체적으로 말하면, level 0부터 L에서 일련의 그리드 전체 $$D= 2^{dl}$$ 셀의 합계에 대해 각 차원을 따라 $$2^L$$ 개의 셀을 갖도록 한다 .  이 해상도에서 $$H_X^l$$ 과 $$H_Y^l$$ 를 X와 Y의 히스토그램이라고 하면 X와 Y는 그리드의 i번째 셀로 떨어지는 점의 수이다. 그러면 Level에서 match의 개수는 히스토그램 교차 함수에 의해 주어진다. 
$$
\mathcal{I}(H_X^l,H_Y^l)=\sum_{i=1}^Dmin(H_X^l(i),H_Y^l(i))
$$


$$\mathcal{I}(H_X^l,H_Y^l)$$ 를 $$\mathcal{I}^l$$ 로 줄여 쓸 것이다. level $$l$$ 에서 match의 개수는 더 미세한 level $$l+1$$ 에서의 모든 match의 합을 포함한다. 그러므로, level $$l$$ 에서의 새로운 match들의 수는 $$l=0,...,L-1$$ 의 경우일 때 $$\mathcal{I}^l - $$$$\mathcal{I}^{l+1}$$ 로 구할 수 있다 . level $$l$$ 에 연관된 가중치는 해당 level에 셀 너비에 반비례하는 $$\frac{1}{2^{L-l}}$$ 로 설정된다. 직관적으로 우리는 큰 셀(낮은 Level)에서 발견한 match들에 패널티를 부여하고 싶은데 그 이유는 점점 덜 비슷한 특징을 포함하고 있기 때문이다. 모든 조각들을 모아서 **Pyramid Matching Kernel**을 다음과 같이 정의한다. 
$$
\kappa^L(X,Y) = \mathcal{I}^L + \sum_{l=0}^L-1\frac{1}{2^{L-l}}(\mathcal{I}^l-\mathcal{I}^{l+1})\\=\frac{1}{2^L}\mathcal{I}^0 + \sum_{l=1}^L\frac{1}{2^{L-l+1}}\mathcal{I}^l
$$
히스토그램 교차점과 피라미드 매치커널은 둘다 Mercer 커널이다. 



#### 3.2. Spatial Matching Scheme

피라미드 매치 커널은 orderless한 이미지 표현에서 동작한다. 이것은 고차원 특징공간에서 두개의 특징 모음간의 간결한 매칭하는 방법이다. 그렇지만 모든 공간적 정보는 무시한다. 이 논문은 orthogonal 접근방법은 지지하는데, 이것은 2차원 이미지 공간에서 피라미드 매칭을 수행한다. 그리고 특징 공간에서 전통적인 클러스터링 기법을 사용한다. 특히, 모든 특징 벡터를 M 이산 유형으로 양자화하고 동일한 유형의 특징만 서로 매칭시킬 수 있다는 단순화 가정을 한다. 각 채널 m은 각각의 이미지에서 발견되는 m 타입의 특징의 좌표를 나타내는 두 세트의 2차원 벡터의 2개의 세트를 준다. $$X_m, Y_m$$ 으로 표현되고 각 이미지에서 발견된 m 타입의 특징 좌표를 표현하고 있다. 최종 커널은 분리된 채널 커널의 합으로 정의된다. 
$$
K^L(X,Y) = \sum_{m=1}^M\kappa^L(X_m,Y_m)
$$
이 접근 방법은 인기있는 'visual vocabulary' 패러다임에서 연속적인 연구라는 장점이 있다. 사실상, L=0일 때, 기존의(표준의) Bag of Features 으로 줄어든다. 피라미드 매치 커널은 단순하게 히스토그램 교차점의 가중치 합이기 때문에, 그리고 양수에 대해서 $$c\  min(a,b) = min(ca,cb)$$ 이기 때문에, $$K^L$$ 은 모든 해상도에서 모든 채널의 히스토그램을 적절히 가중치로 연결하여 형성된 '긴' 벡터의 단일 히스토그램 교차점으로 구현할 수 있다. L level과 M 채널에 대해서, 결과 벡터는 다음과 같은 차원을 갖게 된다.
$$
M\sum_{l=0}^L 4^l =  M\frac{1}{3}(4^{L+1}-1)
$$
Section 5 부분이 $$M=400,\ L = 3$$ 으로 세팅된 실험이다. 결과적으로 히스토그램 교차점은 34000 차원이었다.  그러나, 이 operation들은 히스토그램 벡터들이 극도로 sparse하기 때문에(커널의 계산 복잡도는 feature의 개수에 선형이기 때문에) 효율적이다. $$M=300,\ L=2$$ 으로 세팅된 히스토그램 교차점이 4200차원이었을 때 비교적 성능을 크게 향상시키지 않았다. 

![spatial pyramid matchingì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/ba8e0bda11af08b6037666b67cf54ae1f780822d/7-Figure1.2-1.png)

위 그림은 3 level 피라미드를 구성한 예시이다. 이미지에는 원, 다이아몬드 및 십자가로 표시된 세가지 피쳐 유형이 있다. 상단에서 3 가지 level 의 해상도로 이미지를 subdivide 한다. 그 다음, resolution과 각 channel의 level에 대해 각 spatial bin에 떨어지는(가까운) feature를 count한다. 마지막으로, 각 spatial 히스토그램에 가중치를 부여한다. 



마지막 구현 이슈는 정규화(Normalize)이다. 최대 연산 효율성을 위해서, 우리는 모든 히스토그램을 이미지에 있는 모든 feature의 전체 weight을 통해서 정규화한다. 사실상 모든 이미지의 총 feature 수가 동일해야 한다. 밀도가 높은 Feature 표현(Section 4 참조)를 사용하므로 clutter로 인한 가짜 Feature 탐지에 대해 걱정할 필요가 없으므로 이 방법은 변하는 이미지 사이즈의 영향을 처리하기에 적절하다. 



#### 4. Feature Extraction

이 Section은 Section5의 실험들에서 사용된 Feature의 두가지를 묘사한다. 첫 번째로, **weak features** 라고 불리는 oriented edge point , 즉 주어진 방향의 기울기 크기가 최소 임계 값을 초과하는 포인트이다. 이 실험에서 저자들은 총 $$M=16$$ 의 채널에 대해서 edge point들을 2개의 스케일과 8개의 방향에서 추출한다. "gist"와 유사한 표현이나 이미지의 전체 SIFT 기술자를 얻기 위해 이러한 특징들을 설계했다. 

차별화된 성능을 위해서 8픽셀 간격으로 그리드에서 계산된 16x16 픽셀 patch의 SIFT 기술자인 상위 차원의 강력한 기능도 활용한다. Interest point 대신 고밀도 규칙 격자를 사용하기로 결정한 것은 Fei Fei와 Perona의 비교 평가에 기반을 두었다. dense한 feature들은 장면 분류에 더 잘 작동합니다. 직감적으로, 하늘 , 차분한 물 또는 노면과 같은 uniform한 영역을 캡쳐하려면 밀도가 높은 이미지 설명이 필요합니다 (대비가 낮은 영역을 처리하기 위해 패치의 전체그래디언트 크기가 너무 약한 경우, 일반 SIFT Normalization 절차를 건너 뜁니다)  우리는 visual vocabulary를 형성하기 위해 학습 데이터셋으로부터 랜덤한 패치의 subset의 k-means 클러스터링을 수행한다. 실험을 위한 일반적인 vocabulary 사이즈는 $$M=200, M=400$$ 이다.

![Fig. 1.3. Example images from the scene category database. The database is publicly available at http://www-cvr.ai.uiuc.edu/ponce grp/data.](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/ba8e0bda11af08b6037666b67cf54ae1f780822d/9-Figure1.3-1.png)

![Table 1.2. Classification results for the Caltech-101 database.](https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/ba8e0bda11af08b6037666b67cf54ae1f780822d/11-Table1.2-1.png)