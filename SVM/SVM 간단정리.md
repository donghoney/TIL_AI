## SVM 간단 정리

glee1228@naver.com

**SVM**

입력 데이터 벡터를 고차원 공간에 매핑함으로써 positive class와 negative class 사이의 마진(Margin)을 최대화 하는 결정 경계(Decision Boundary)를 찾는 분류 알고리즘

**SVM 의 Algorithm**

![ê´ë ¨ ì´ë¯¸ì§](https://1.bp.blogspot.com/-K8qVBF8FKpk/WVnU0CDKPzI/AAAAAAAABy4/X-otWS8WuickSKOu0JNEjergkePulalZQCLcBGAs/s1600/Capture.PNG)

**순서** 

1. **두 가지 케이스 나누기(positive, negative)**

   > 위의 그림에서 초록색 점들은 positive 케이스이고 빨간 점들이 negative 케이스라고 하자. 초록색 점선은 positive를 나누는 경계 결정이 되고, 빨간색 점선은 negative를 분류하는 경계 결정이라고 하고 다음과 같은 식으로 표현해보자.

   $$
   Positive\ Case\ \ \ \ \ \ \ =\ \ \ \ \ \ \ w \cdot x +b \ge 1\\
   Negative\ Case\ \ \ \ \ \ \ =\ \ \ \ \ \ \ w \cdot x +b \le -1
   $$

2. **변수 y를 곱해주어 조건식을 표현**

   > 상태 변수 y 를 양수 음수로 나누어 전체 결정 경계의 식이 양수의 값이 되도록 표현한다.

   $$
   y_j
   \begin{cases}
   +1, & \mbox{if }\ w \cdot x +b\ge \mbox{ 1} \\
   -1, & \mbox{if }\ w \cdot x +b\le \mbox{ -1}
   \end{cases}\\
   
   Confidence\ Level\ \ \ \ \ \ =\ \ \ \ \ \ \ (w \cdot x +b)y_j\\
   $$

3. **Distance(Margin) 최대화**

   >두 결정 경계의 사이 거리가 최대화 되도록 하기에 앞서, 벡터 두개를 정의하고 두개의 벡터를 통해 
   >
   > Decision Rule을 우선 정의하면, 다음과 같다.

   

   $$\bar w$$ :결정 경계선의 법선 벡터

   $$\bar u$$ : $$positive, negative$$ 결정 경계선 위의 $$x_+$$와 $$x_-$$ 의 벡터
   $$
   \bar w \cdot \bar u \ge C\\
   C = -b
   $$
   positive의 경우에서, 
   $$
   f(x) = w \cdot x +b \ge 0
   $$
   으로 표현할 수 있다.

   $$Positive\ Case\ \ \ \ \ \ \ =\ \ \ \ \ \ \ w \cdot x_+ = 1-b\\
   Negative\ Case\ \ \ \ \ \ \ =\ \ \ \ \ \ \ w \cdot x_- = -1 -b$$

   이므로,

   이제 Margin의 Distance 즉, WIDTH는 $$(x_+ - x_-) \cdot \frac{\bar w}{\lVert w \rVert}$$ 로 구할 수 있다.

   그러므로 
   $$
   WIDTH = \frac{2}{\lVert w \rVert}
   $$
   이 된다.

   $$Maximize \frac{1}{\lVert w \rVert} \rightarrow Minimize\ \|w\| \rightarrow Minimize \ \frac{1}{2} \|w\|^2$$ 



4. **라그랑주 승수법으로 정의하고 극값을 찾는다**

   >Loss를 라그랑주 승수법으로 정의하고 미분하여 극댓값 또는 극솟값을 찾는다.
   >
   >w에 대해 편미분 한 값이 0이 될 경우와 b에 대해 편미분한 값이 0이 될 경우를 구해 식에 대입한다.

$$
L = \frac{1}{2}\|\bar w\|^2 - \sum_i^N \alpha_i\left[ y_i(\bar w \cdot \bar x +b)-1 \right]
$$

$$
\alpha_i = 라그랑주\ 승수(0이\ 아닌\ 다른 수)
$$

$$
\bar w = \sum_i \alpha_i \cdot y_i \cdot \bar x_i\\
\sum_i \alpha_iy_i =0\\
L = \frac{1}{2}(\sum_i \alpha_i \cdot y_i \cdot \bar x_i)(\sum_j \alpha_j \cdot y_j \cdot \bar x_j)-\sum_i \alpha_i \cdot y_i \cdot \bar x_i\cdot(\sum_j \alpha_j \cdot y_j \cdot \bar x_j) - \sum_i \alpha_i \cdot y_i \cdot b + \sum_i \alpha_i\\
L = \sum\alpha_i -\frac{1}{2}\sum_i\sum_j\alpha_i\alpha_jy_iy_jx_i\cdot x_j
$$

> 여기서 최종적으로 알 수 있는 것은 Margin은 x+와 x-의 내적값에 따라서만 바뀐다.
>
> 그러므로 여기서 Loss를 최대화할 수 있는 방법은 변환시킨 벡터와 다른 벡터의 내적값이다.

5. **hinge Loss로의 표현**

>positive와 negative의 범주를 구분하면서 데이터와의 거리가 가장 먼 결정경계를 찾기 위해 hinge loss를 사용한다. 위의 y값은 positive일 경우 +1의 값을 갖고, negative일 경우 -1의 값을 가진다고 했는데, 여기서 y는 true값이 되고 wx+b-1과 wx+b+1의 값이 pred 값이 되어 손실함수가 정의된다
>
>y'*y의 값은 위에서 confidence level 로 언제나 양수 값을 취하도록 정의했으므로 loss 그래프는 아래와 같이 그려질 수 있다.

$$
loss = max \{ \ 0,1-(y'*y)\ \}
$$

![img](https://i.imgur.com/J59cih1.png)

6. **Kernel 변환**

>벡터와 다른 벡터의 내적값을 늘이기 위해 다른 차원의 내적값을 알기 위해 Kernel함수를 이용하는데, 
>
>종류는 Linear Kernel, RBF Kernel(Gaussian Kernel) , Polynomial Kernel이 있다.

$$
\Phi(\bar x_i)\cdot\Phi(\bar x_j)\ to \ maximize\\
K(x_i,x_j) = \Phi(\bar x_i)\cdot\Phi(\bar x_j)
$$

* Linear Kernel
  $$
  변환된 \ 내적 \ 값 = (\bar u \cdot \bar v +1)^n
  $$

* Gaussian Kernel
  $$
  변환된 \ 내적 \ 값 = e^{-\frac{\|x_i-x_j\|}{\sigma}}
  $$

6. ****

**사용시 주의사항 **

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
