## SVM 간단 정리

glee1228@naver.com



**회귀(regression)**

* **연속** 변수를 예측
* 데이터를 지나는 **추세선**을 찾는 것



**분류(classification)**

* **이산** 변수 또는 **범주**형 변수를 예측
* 데이터를 나누는 **경계선**을 찾는 것

주의) 로지스틱 회귀분석 = 분류



**SVM(Support Vector Machine)**

* 선형 모형: 오차를 줄이는 데 관심
* SVM: 좋은 형태를 찾는데 관심



**SVM과 linear model과의 관계**

* 정규화 선형 모형 -> 오차를 줄이기 + 좋은 형태도 찾기
* SVM -> 좋은 형태+ 오차도 줄이기
* SVM은 Ridge 선형 모형과 비슷함



**SVM 결정경계는 어떻게 결정하는가**

* 가중치 벡터(W)에 직교하면서, margin이 최대가 되는 선형을 찾음.

![svm decision boundaryì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://www.researchgate.net/profile/Doris_Pischedda/publication/301780242/figure/fig2/AS:576318501015556@1514416446139/Illustration-of-the-decision-boundary-of-the-linear-SVM-in-the-simplest-case-with-only.png)

* $$W^TX+b = 0$$ 의 수식을 따르는 선형을 결정경계(Decision Boundary)라고 함.
* 또한 가중치 벡터 W는 결정경계(Decision Boundary)와 직교(90도)해야 한다.



**왜 W와 결정경계는 직교해야 하는가**

* 계산상의 편의를 위해, b=0으로 가정하면, $$W^TX=0$$ 을 결정 경계로 정의할 수 있고 2개의 벡터 내적의 결과가 0이 되는 각도는 90이므로 직교한다고 표현함



**Margin 계산 방식**

* 결정 경계와 가장 가까운 point를 $$x^1, x^2$$ 로 가정하면, (b=0으로 가정)

* $$W^TX^1 = -1, \ W^TX^2= 1$$ 

* $$
  m =W^TX^2 - W^TX^1\\ = \frac{	\left| 1 \right|}{	\left| W \right|}+\frac{	\left| -1 \right|}{	\left| W \right|} \\ =\frac{	\left| 2 \right|}{	\left| W \right|}
  $$

* ![ì ê³¼ ì§ì  ì¬ì´ì ê±°ë¦¬ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](http://cfs14.tistory.com/upload_control/download.blog?fhandle=YmxvZzIzNzk5QGZzMTQudGlzdG9yeS5jb206L2F0dGFjaC8wLzEwMDAwMDAwMDA1NC5wbmc%3D)

* 직선($$ax+by+c =0$$)과 점($$x_1,y_1$$) 사이의 거리 공식

* $$
  d = \frac{	\left| ax_1+by_1+c \right|}{	\left|  \sqrt{a^2+b^2} \right|}
  $$

* $$W^TX=0와 \ X^1과의 \ 거리는 \Rightarrow \frac{	\left| W^TX^1 \right|}{	\left|  \sqrt{W^2} \right|}$$

* $$W^TX=0와 \ X^2과의 \ 거리는 \Rightarrow \frac{	\left| W^TX^2 \right|}{	\left|  \sqrt{W^2} \right|}$$

**Support Vector Regression(SVR)**

* SVM의 회귀 버전
* 가능한 평평한 형태의 추세선을 찾음



**Support Vector Classification(SVC)**

* SVM의 분류 버전
* 클래스가 잘 나뉘는 결정 경계를 찾음



**Caution **

* SVM은 특성의 스케일에 민감함 -> 축에 따른 데이터 분포에 따라서 결정 경계의 기울기가 달라지기 때문에 사이킷런의 StandardScaler를 사용하여 특성의 스케일을 조정하면 성능이 향상됨



**Hardmargin Classification**

* 모든 샘플이 결정경계 도로 바깥 쪽에 올바르게 분류되어 있다면 이를 Hard margin classification이라고 함. 
* 2가지 문제점
  * 데이터가 선형적으로 구분될 수 있어야 제대로 작동
  * 이상치에 민감

**Softmargin Classification**

* Margin Violation과 도로 폭을 가능한 넓게 유지하는 사이에 적절한 균형
* 사이킷런 SVM의 파라미터 중 C값을 높이면 Hard Margin에 가까워지고, C값을 낮추면 Soft Margin에 가까워짐
* 과대적합 모델은 C를 감소시켜 규제할 수 있음



**Kernel trick**

* 현실에서의 많은 문제들은 비선형성을 가지고 있음
* 선으로 경계선을 찾을 수 없음
* 모형을 비선형으로 만들 수 없다면, 데이터를 비선형으로 변환하여 선형 분리가 가능하게 만들기
* 비선형 변환도 어려움. 따라서, 비선형 변환한것처럼 거리를 재정의하여 작동
* 종류 : linear kernel, RBF kernel, polynomial kernel, sigmoid kernel



**라그랑주 승수법 (Lagrange Multiplier Method)**

* 함수의 최댓값 또는 최솟값을 구하는 문제에서 함수를 미분하여 기울기가 0인 지점, 즉 극대 혹은 극소를 찾는 방법을 사용한다. 하지만, 만약 반드시 만족해야 하는 특정 조건이 주어진다면 이 방법을 사용할 경우 오류가 발생할 것이다. 예를 들어, $$f(x) = x^2+5$$ 함수의 최솟값을 구하는데, $$x=3$$ 라는 조건을 반드시 만족해야 한다면, 함수 f의 극소를 찾는 것이 아리나 단순히 $$f(3) = 14$$ 라는 답을 내야 한다. 이와 유사하게 어떤 함수의 최댓값 또는 최솟값을 구하는 문제에서 특정 조건이 주어질 때 사용하는 방법이 바로 라그랑주 승수법이다.

**라그랑주 승수법 아이디어**

* g(x,y) = c라는 제약 조건

* f(x,y)의 최댓값을 어떻게 구할까?

어떤 조건 $$g$$ 를 만족하는 함수 $$f$$ 의 최댓값 또는 최솟값을 구하는 문제에서 찾고자 하는 값이 $$f$$ 와 $$g$$ 의 접점에 존재할 수도 있다는 가능성에서 출발한다. 예를 들어, 2차원 좌표 평면 상에서 f가 직선이라고 가정하고 이 f의 y절편이 최소가 되는 지점을 찾는 문제를 생각해보자. 단, f가 g라는 원 위의 좌표들을 적어도 하나 이상 포함해야 한다는 제약조건이 있다고 가정한다.이러한 경우, 그림에서 볼 수 있듯이 f와 g가 접할 때 f의 절편이 최소가 된다.

![img](https://2.bp.blogspot.com/-ozuFHTskH44/We1NUWwSM0I/AAAAAAAACOo/NGgR8GXrF5sPgo1a12GloK0Sf6NB1gURQCLcBGAs/s320/%25EB%259D%25BC%25EA%25B7%25B8%25EB%259E%2591%25EC%25A3%25BC.PNG)



**라그랑주 승수법의 수식**

최댓값 또는 최솟값을 구해야 하는 x에 대한 함수를 f라고 하고, 미지수 x가 반드시 만족해야 하는 조건을 표현하는 식을 함수 g라고 하자. 이 때 계산 편의를 위해 $$g(x) = 0$$ 인 형태로 정리한다. 예를 들어, $$x=3$$ 인 조건이 있다면  $$g(x) = x-3 =0 $$ 으로 표현한다. 

이를 바탕으로 보조함수 L을 정의한다. $$L(x,\lambda) = f(x) - \lambda g(x)$$ 이다. ($$\lambda$$ 는 임의의 상수)

라그랑주 승수법의 목표는 $$\triangledown L = 0$$ 인 지점을 찾는 것이다. 만약 제약 조건이 N개일 경우에는 다음과 같이 L을 정의한다.
$$
L(x,\lambda_1,\lambda_2,...,\lambda_N) = f(x) - \sum_{i=1}^N{\lambda_i g_i(x)}
$$


**[질문]** 가우시안 커널을 사용한 SVM 분류기에서, 다음과 같이 결정경계를 정할 경우에

![image-20190723145109460](/Users/donghoon/Library/Application Support/typora-user-images/image-20190723145109460.png)

데이터셋에 underfitting 이라고 생각되는데, 

1. $$C$$의 값을 올려야 할지 줄여야 할지?

2. 그리고 $$\sigma^2$$ 를 올려야할지 줄여야할지?