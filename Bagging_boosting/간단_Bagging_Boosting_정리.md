## 앙상블 기법

glee1228@naver.com

**Ensemble** : 동일한 학습 알고리즘을 사용해서 여러 모델을 학습하는 개념 <-> **Stacking** : 서로 다른 모델을 결합하는 방법

**앙상블 기법의 대표적인 종류** : Bagging , Boosting

**Bagging과 Boosting의 비교** 

1. Bagging은 병렬적이며 빠르고, Boosting은 직렬적이며 상대적으로 느리다.
2. Bagging은 모델의 Variance를 줄일 수 있으나, Bias는 줄이지 못한다
3. Boosting은 Variance와 Bias 모두를 줄일 수 있다. Bias를 줄이는데 목적이 있다.

#### Bias와 Variance와의 관계

![Bias-Variance Tradeoff](https://pbs.twimg.com/media/CpWDWuSW8AQUuCk.jpg)



### Bagging  (bootstrap aggregating)

**이해**

데이터 샘플을 여러 번 뽑아 n개의 모델을 학습시켜 결과를 Aggregating 하는 방법

**특징**

* n개의 모델이 독립적으로 동시에 각각의 데이터셋을 학습할 수 있으므로 속도가 빠르다. 병렬적.

* classification과 regression 모두 사용 가능

* overfitting을 방지해주며, Variance를 감소하게 해줌

* 대표적으로 **Random forest** 알고리즘이 있다.

* **Bootstrapping** 으로 샘플링 하는 것이 Bagging의 핵심

```
bootstrapping : 랜덤 샘플링을 통해 Training Data를 늘리는 방법
데이터 셋 내의 데이터 분포가 고르지 않은 경우에 주로 사용된다.
예를 들어, 사과 클래스가 10000개 오렌지 클래스가 500개 있을 경우, 극단적으로 사과 클래스가 많기 때문에 사과만 찍는 분류기도 높은 training 정확도를 보이기 때문에 데이터가 적은 class의 에러가 무시되는 방향으로 트레이닝 되어 데이터가 많은 클래스를 분류하는 방향으로 overfitting 될 우려가 많다.
이럴 때 Boostrapping을 사용하면, overfitting을 줄일 수 있다.
```

**Bootstrapping Algorithm**

1. 전체 학습 샘플 중에서 $$n$$개를 추출하여 모델을 학습시킨다.
   (이 때, $$n$$은 원래 학습 데이터의 크기보다 작아도 된다)
2. 학습된 모델을 이용하여, 학습 샘플을 분류한다.
3. 잘못 분류된 학습 데이터가 샘플로 선택될 가능성을 높이고, 제대로 분류된 데이터가 샘플로 선택될 가능성을 낮춘다. 결과적으로, 매 학습 마다 **“어려운” 샘플의 비율이 커진다.**
4. 다시 1번으로 돌아가서 학습을 반복한다.



> 아래 그림에는 mean으로 최종 값을 결정하는 것으로 되어 있는데,
>
> Classification(Categorical Data)의 경우에는 voting으로, Regression(Continuous Data)의 경우에는 Mean을 최종 값으로 결정한다.

![img](https://t1.daumcdn.net/cfile/tistory/99934E425BE591A716)

>  출처) https://www.youtube.com/watch?v=2Mg8QD0F1dQ

**Random Forest**

> Bagging 계열의 대표적인 예측력 좋은 알고리즘으로 N개의 Decision Tree가 Voting을 통해 결정하는 방식. 예측 결과의 정확성(accuracy)는 개별 Decision Tree의 평균 값으로 유지되는 반면 낮은 안정성(High Variance)는 중심극한 정리에 의해 낮아진다.

![random forestì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://c.mql5.com/2/33/image1__1.png)

> 출처 ) https://www.mql5.com/en/articles/3856

**중심극한정리**(Central Limit Theorem)

동일한 확률 분포를 가진 독립 확률 변수 n개의 평균의 분포는 n이 적당히 크다면 정규분포에 가까워진다는 정리.

증명은 생략 

### Boosting

**Boosting의 이해**

Boosting은 Bagging에서 해결하지 못한 문제(못 맞추는 문제는 여전히 못 맞추는 문제) - 높은 Bias 를 해결하지 위한 방법으로 여러 개의 모델이 순차적으로 생성되어서 다음 모델을 만들 때 마다 앞에 모델에서 잘 분류하지 못했던 데이터를 분류 할 수 있도록 데이터 혹은 가중치를 그 다음 모델에 반영해서 계속 모델을 추가해 가는 방식이다.

1. 첫번째 모델이 기본 데이터셋을 그대로 또는 일부 데이터를 Bagging하여 학습을 한다. 

2. 그 다음 두 번째 모델은 전체 데이터를 학습하되 첫번째 모델이 에러를 일으킨 데이터에 더 큰 중점을 두고 학습을 진행한다. 

3. 세 번째는 앞의 두 모델이 힘을 합쳐도 맞추지 못한 데이터에 중점을 두고 학습을 진행한다. 

**특징**

* 앞 모델의 학습이 끝나야 뒷 모델이 그 결과에 기반하여 가중치를 결정하고 학습을 할 수 있기 때문에 순차적으로 학습해야 한다. 직렬적이고 상대적으로 속도가 느리다.

* 대표적인 알고리즘으로 Adaboost, Gradient Boost,Xgboost 가 있다.



**Adaboost**



****

#### **Bagging, Boosting과 Bias, Variance** 

-**bagging**은 데이터셋을 선별적으로 학습한다, 하지만 여전히 각각의 모델은 모든 data를 동등하게 대한다. 때문에 **못알아보던 data를 알아보게 되지는 않는다**. 다만 여러개의 모델의 평균을 통해 최종결과를 얻기 때문에 그 결과가 **안정적**이다. 



-**boosting**에서 각각의 모델은 feature를 동등하게 대하지 않는다. **못알아보던 feature를 점점 더 중요하게 여기며 가면 갈수록 그것만 공략**하게 된다. 뒷모델은 앞에서 잘알아보는 feature는 고려하지 않는다, 이미 그 feature를 잘인식하는 model은 앞에 많다. 그 feature는 틀리더라도 앞에서 틀린걸 해결하는게 중요하다. 때문에 모델의 기본적인 **정확도, bias**가 개선된다. 마찬가지로 여러 모델이 최종결과를 결정하기 때문에 그 결과가 **안정적**이다.