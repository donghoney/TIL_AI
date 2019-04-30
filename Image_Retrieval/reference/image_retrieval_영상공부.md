CVPR 2018 Visual Search and Metric Learning 

Naver Seminar

네이버의 이미지 검색 : 스마트 렌즈 서비스

Image Embedding의 2가지 방식

1. Representation Learning
2. Metric Learning

Similarity Search System

1. Approximate Nearest Neighbor Search
2. PG Encoding
3. Query Expansion and Reranking(RANSAC)



옛날엔 SIFT feature 같은 방식으로 이미지당 많은 feature를 뽑아서 이미지를 찾는 방법이 있었다면, 요즘에는 이미지당 feature를 하나만 뽑아서 이미지를 검색한다. 그 뽑은 하나의 feature를 global descriptor라고 부르고 approximate nearest neighbor search로 찾는 방법을 사용한다.

가장 최신의 연구를 보면, 

CNN을 이용해서 feature를 하나 뽑고 -> 각 레이어마다 feature를 aggregation을 잘해서 하나의 global feature로 표현한다. -> 최종의 나온 feature가 서로 얼마나 비슷한가 -> 이 과정을 end to end 방식으로 진행한다.



Task & Dataset 

Instance Retrieval(소매품) - INSTRE

Instance Retrieval(빌딩, 랜드마크 검색) - ROxford, RParis, Google Landmark(DeLF paper)

Instance Retrieval(패션아이템) - DeepFashion

Person Re-identification - Market-1501, DukeMTMC



광진구 랜드마크 데이터셋을 구축할 때, 위에 빌딩, 랜드마크 검색 데이터셋 ROxford, RParis, Google Landmark를 Benchmark하는 것이 도움이 될듯하다.



* Image Embedding Paper Review

  컨셉 : 이미지를 벡터로!

  * 첫번째 Paper : Group Consistent Similarity Learning via Deep CRF for Person Re-Identification

    Idea : 

    * Additional constraint
    * Exploit mini-batch
    * CRF to model group consistency
    * Estimate a pair of image
    * Similarity from group consistency

    Effect:

    * Achieve SOTA on Market-1501, DukeMTMC





