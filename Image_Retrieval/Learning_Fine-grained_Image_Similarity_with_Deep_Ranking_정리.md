## Learning Fine-grained Image Similarity with Deep Ranking

논문 링크 : https://arxiv.org/pdf/1404.4661.pdf

출처 : https://umbum.tistory.com/262

**Metric Learning** : 이미지 간의 distance(similarity)를 구하는 방법(함수)를 학습하는 model



#### detection & classification 신경망을 거치는 경우, 그 출력을 그대로 similarity에 사용하면 안되나?

image classification 과 similar image ranking task는 본질적으로 다르다.

출력 뉴런 값들을 저장해놓았다가 distance를 계산하는 방법을 생각해 보았는데, class 내의 두 이미지 P, Q의 비교를 위해, "P,Q 가 다른 class 각각에 속할 확률이 얼마나 되는지" 를 사용하기 때문에 당연히 부정확하다.

detection & classification 신경망의 출력을 K()라고 하면, D(k(P), k(Q))를 구한다는 건데, 어쨌든 k()도 신경망을 통과한 output이기는 하지만 f()는 similarity를 위해 학습한 신경망이고, k()는 classification을 위해 학습한 신경망이다. 따라서 k()를 사용하는 것은 classification을 위해 학습한 신경망의 출력을 그냥 similarity에 가져다 쓰는 것 뿐이라 오히려 더 부정확할 수 있다.



#### 그렇다면 신경망을 하나 더 사용한다고 했을 때, ResNet이나 VGG같은 CNN만 사용해서 similarity를 판정할 수 있나?

신경망의 성격은 어떤 training set을 사용했는가가 결정하니까 image similarity를 판정하도록 training set을 만들어 학습시키면 일반적인 CNN도 similarity 판정에 사용할 수는 있는데 아무래도 성능이 좀 떨어진다. 간단히 예를 들면 input으로 triplet을 받도록 설계하고 $$p_i^+$$ 를 맞추도록 하는 식으로 학습시키는 방법을 생각해볼 수 있다.



### Abstract

이미지로부터 직접 similarity metric을 학습한다.

input으로 triplet을 받기 때문에 논문에 triplet sampling algorithm에 대한 내용도 나와있다.

models based on hand-crafted visual features and deep classification models보다 성능이 좋다.



### 1. Introduction

기존의 hand-crafted features(방법)로 image features(특징)를 뽑아낸 다음 image similarity model을 학습시키는 방법은 hand-crafted features의 성능에 크게 좌우된다. 반면, deep ranking은 features와 similarity model을 동시에 학습한다.

triplet $$t_i = (p_i,p_i^+,p_i^-)$$ 은 query image, positive image, negative image로 이루어진 이미지 묶음이다. Image similarity relationship을 triplet을 이용해 표현하게 된다. 

이 논문의 main contributions는 다음과 같다.

1. Image에서 직접 fine-grained image similarity model을 학습할 수 있는 deep ranking model과 training data를 얻을 수 있는 bootstrapping 방법 제안
2. Multi-scale network structure 제안
3. online triplet sampling algorithm 제안
4. Evaluation dataset publishing



### 2. Related Work

-



### 3. Overview

**최종적인 목표는 image similarity models를 훈련시키는 것이다.**

두 이미지 P와 Q의 similarity D( . , . )는 Euclidean distance의 제곱으로 정의한다.
$$
D(f(P),f(Q)) = ||f(P) - f(Q)||_2^2
$$
$$f( . )$$ 는 이미지를 Euclidean space의 한 점으로 mapping 하는 image embedding function이다.

P, Q가 더 닮아있을 수록, Euclidean space의 두 점 사이의 거리인 $$D( . , . )$$ 값이 더 작아진다.

Euclidean space에서 인접 값을 찾는 문제는 **nearest neighbor search algorithm**으로 해결할 수 있기 때문에 **문제는 f( . )다. f( . ) 가 두 이미지 P, Q가 닮아있는 만큼 둘을 인접한 곳에 mapping 해주면 해결되는 건데, 이 f( . )를 정의하기 위해 보통 hand-crafted features를 사용해 왔지만, 여기서는 deep learning으로 f( . )를 학습한다.**

두 이미지가 얼마나 닮아있느냐를 나타내기 위해 D( . , . ) 를 그대로 사용하는 것이 아니라 relevance score를 사용한다. set of images P 에 속한 두 이미지 $$p_i,p_j$$ 에 대해 relevance score는 다음과 같다.
$$
r_{i,j} = r(p_i,p_j)
$$
$$D(f(p_i),f(p_i^+)) < P(f(p_i),f(p_i^-))$$ 이면 $$r(p_i,p_i^+) > r(p_i,p_i^-)$$ 이다.

triplet $$t_i = (p_i,p_i^+,p_i^-)$$ 에 대한 **hinge loss** 는 다음과 같이 정의된다.
$$
l(p_i,p_i^+,p_i^-) = max{\{ 0, g+D(f(p_i),f(p_i^+))-D(f(p_i),f(p_i^-))\}}
$$


**hinge loss** 는 classifier training에 사용되는 Loss function을 말한다.

원래 $$l(y) = max(0,1-t*y)$$ 형태로 정의되지만, 여러 variation이 존재하며 multiclass classification에서는 위와 같은 형태로 사용한다.

**g** 는 image pairs 사이의 gap을 regularize하기위한 파라미터다.

Hinge loss는 0-1 ranking error loss의 convex approximation이고 모델이 triplet 내의 ranking을 잘못 배열하는지 측정한다. 

결과적으로 최소화해야 하는 object function은 다음과 같다.
$$
min\sum_i\xi_i+\lambda||W||_2^2
$$

$$
s.t . : max{\{0,g+D(f(p_i),f(p_i^+))-D(f(p_i),f(p_i^-))\}<\xi_i}​
$$



