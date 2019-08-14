- 논문 제목 : Deep metric learning using triplet network

- 논문 링크 : https://arxiv.org/abs/1412.6622

- 논문 내용 : 

  - 목표 : 학습 데이터간의 유사도를 측정할 수 있는 함수를 모델 안에서 직접 학습(즉, Metric Learning) 하여 입력에 유사한 데이터를 찾는 방법을 제안

    - Image Retrieval, Face Recognition 등에 활용 가능 

  - 기존의 연구 및 배경지식

    - Metric Learning : 데이터간 유사도/거리를 측정할 수 있는 함수를 학습하는 알고리즘

    - Siamese Network Architecture : 

      http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf

      - 두 입력에 대해 동일한 아키텍쳐를 이용하여 특징을 추출
      - 두 특징간의 거리를 비교하여 올바른 거리값이 나올때까지 아키텍쳐 학습 (Hinge Loss 이용)   

  - 주요 제안 내용

    - 학습을 위해 3개의 쌍이 필요하다. {(**x**(i)a,**x**(i)p,**x**(i)n)}
    - Triplet Network Architecture (세 쌍둥이 아키텍쳐) (논문 그림 1)
      - Anchor 샘플(입력), positive 샘플, negative 샘플 세가지 입력에서 특징을 추출
        - anchor-positive 샘플간 거리, anchor-negative 샘플간 거리
        - 두 거리 값을 이용하여 상대적인 유사도를 나타낼 수 있음 -> Simaese Network에서 어려웠던 부분을 개선함
        - 두 거리의 비율을 Loss 함수로 이용하여 학습(발표자료 8P 수식)
    - 실험 결과
      - 기존에 알고있던 상위 랭크의 알고리즘들과 비슷한 성능을 보였음

- 설명 보충 자료 :

  - PPT 및 블로그 : 
    - https://pdfs.semanticscholar.org/b1f7/9d796776839aa6ca15b8c552bae1de1029af.pdf
    - https://m.blog.naver.com/PostView.nhn?blogId=4u_olion&logNo=221478534498&categoryNo=50&proxyReferer=https%3A%2F%2Fwww.google.com%2F
  - 오픈소스(torch version) :
    - https://github.com/eladhoffer/TripletNet

- 발전 가능성이 있었던  문제들 / 해당 문제를 해결한 논문들

  - 제안된 논문과 같은 기법에 적용할 학습데이터를 수동으로 제작해야되는 문제가 있음

    - Image Similarity Data Set : https://sites.google.com/site/imagesimilaritydata/download

  - Triplet architecture를 개선한 논문

    - 제목 : Learning Fine-grained Image Similarity with Deep Ranking

    - 링크 : 

      https://arxiv.org/abs/1404.4661

      - 아키텍쳐 내부 구조를 변경
      - 앞단에 Sampling layer를 추가하여 부족한 학습데이터 쌍을 늘림

  - All Pairs 에 대한 학습을 보완한 논문

    - 제목 : [Deep Metric Learning via Lifted Structured Feature Embedding](http://cvgl.stanford.edu/papers/song_cvpr16.pdf)

    - 링크 :

      http://cvgl.stanford.edu/papers/song_cvpr16.pdf

      * non-smooth는 upper bound 식을 도입하여 해결한다.
      * All Pairs 문제는 이전 연구에서 했던 것들과 유사하게 importance sampling 으로 푼다.
      * 샘플링 방식은 3단계로 진행된다.
        * Positive pair 쌍들을 랜덤하게 선정
        * 적당한 Batch 데이터 안에 포함하도록 구성
        * Batch 내부에서 Positive pair에 포함된 각각의 샘플에 대해 hard negative 샘플을 구함.

  - 효율적인 배치 구성을 위해 N-Pair를 제안

    - 제목 : [ Improved Deep Metric Learning with Multi-class N-pair Loss Objective](http://www.nec-labs.com/uploads/images/Department-Images/MediaAnalytics/papers/nips16_npairmetriclearning.pdf) 

    - 링크 :

      http://www.nec-labs.com/uploads/images/Department-Images/MediaAnalytics/papers/nips16_npairmetriclearning.pdf

      * Triplet 구조를 일반화하여 (N+1)-Tuplet 네트워크를 제안함.
      * 1 Anchor, 1 Positive, (N-1) Negative Samples
      * N=2 인 경우 Triplet 과 동일한 모델이 된다.

      ![deep_metric_n_pair_1](/Users/donghoon/GitHub/TIL_AI/Image/deep_metric_n_pair_1.png)

      ![deep_metric_n_pair_2](/Users/donghoon/GitHub/TIL_AI/Image/deep_metric_n_pair_2.png)

  - Mini-Batch 안에서의 Pairs/Triplets로 구성되어 있어 Global Structure를 보지 못하는 문제를 개선

    - 제목 : Deep Metric Learning via Facility Location

    - 링크 :

      http://openaccess.thecvf.com/content_cvpr_2017/papers/Song_Deep_Metric_Learning_CVPR_2017_paper.pdf

      * Facility Location 이라는 방법을 제안
      * 동일한 클래스에 속한 positive pair에 척력(repulsion)이 작용되어 같은 클래스간의 거리가 더 벌어지는 극단적인 예도 존재할 수 있다는 가정.
      * 클러스터 단위로 척력이 작용하는 것으로 해결