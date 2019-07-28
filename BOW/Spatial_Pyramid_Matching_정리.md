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

Spatial Pyramid(공간 피라미드) 접근법은 가우시안 스케일 공간 대신에 직사각형 윈도우의 고정된 계층 구조를 정의하는 locally orderless한 이미지의 대안적 공식으로 생각하면 된다. Koenderink와 VanDoorn는 locally orderless한 이미지가 시각적 인식에서 중요한 역할을 한다는 것을 설득력 있게 주장했다. 논문에서의 이미지 검색 실험은 공간 피라미드가 인지함에 있어서 두드러지는 특징들을 제시하고, locally orderless Matching이 이미지들 사이의 전반적인 지각적 유사성을 추정하는 강력한 메카니즘일 수 있다고 제안한다. 









