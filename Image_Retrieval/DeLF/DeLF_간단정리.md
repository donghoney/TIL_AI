## Large-Scale Image Retrieval with Attentive Deep Local Features 논문 정리

출처 : https://arxiv.org/pdf/1612.06321.pdf



glee1228@naver.com

* DELF로 잘 알려진 논문이고 포항공대 한보형 교수 팀과 구글이 공동 연구 결과.
* v1는 2016년 12월 공개, 구글 랜드마크 데이터셋 공개와 함께 2018년 2월에 v4



### Abstract

* DELF(**DE**ep **L**ocal **F**uture) 깊은 지역 특징이라는 이름의 대규모 이미지 검색에 적합한 local descriptor를 제안
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
* 주요 목표는 CNN기반의 feature DescriptoR
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

* 

