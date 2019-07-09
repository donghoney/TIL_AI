## 2D Transformation

### 왜 필요할까?

* Detection과 Tracking 문제에서 두 이미지 사이의 매칭 관계를 이미지 평면에서 직접 모델링 할 때 사용



### 어떤 것들이 있을까?

**4가지를 살펴보자** 

* Rigid Transformation
* Similiarity Transformation
* Affine Transformation
* Homography (Projective Transformation)



#### 1. Rigid Transformation

이름 그대로 엄격한(굳어있는) 변환이다. 가장 기본적인 변환이고, 다른 말로 유클리디언 변환(Euclidean Transformation)이라고도 한다. 

* 형태, 크기 유지

* 회전, 평행이동만 변환

  #### 1. 1 . Translation 

  평행이동만을 허용한 경우이다. 크기가 고정이고 회전도 일어나지 않는 경우에는 위치 변화만을 추적하면 된다.
  $$
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix} =
  \begin{bmatrix}
  x \\y
  \end{bmatrix} + \begin{bmatrix}
  t_x \\ t_y
  \end{bmatrix}
  $$

  $$
  t_x = \frac{1}{n}\sum_i(x_i' - x_i)
  \\
  t_y = \frac{1}{n}\sum_i(y_i' - y_i)
  $$

  

  #### 1. 2. Rotation

  회전만을 허용한 경우이다. (x,y)를 반시계 방향으로 $$\theta$$ 라디안 만큼 회전시키는 변환행렬은 다음과 같다.
  $$
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix} =
  \begin{bmatrix}
  cos\theta & - sin\theta \\
  sin\theta & cos\theta
  \end{bmatrix} \begin{bmatrix}
  x \\ y
  \end{bmatrix}
  $$
  회전의 기준은 원점이고 제자리에서 도는것이 아니라, (0,0)을 기준으로 크게 회전한다.

  위의 식을 직접 이용했을 때, 회전변환이 원점을 기준으로 하기 떄문에 만일 두 점의 원점과의 거리가 서로 다르면, 이런 변환은 존재하지 않게 된다.

  그러므로, 스케일 변화까지 고려하여 변환하고 나중에 스케일변화를 제거한다.

  스케일 변화까지 고려한 회전변환은 일반적으로 다음과 같다. 
  $$
  a= s* cos\theta \\b = s * sin\theta
  $$
  
  $$
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix} =
  \begin{bmatrix}
  a & - b \\
  b & a
  \end{bmatrix} \begin{bmatrix}
  x \\ y
  \end{bmatrix}
  $$
  이 식을 전개한 후에, 다시 a, b에 관해 묶으면 다음과 같은 형태로 바꿀 수 있다.
  $$
  \begin{bmatrix}
  x & - y \\
  y & x
  \end{bmatrix} \begin{bmatrix}
  a \\ b
  \end{bmatrix} =
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix}
  $$
  이제 위의 식에 매칭 쌍을 하나만 대입해도 역행렬을 통해 a,b를 구할 수 있다. 만일, 매칭 쌍이 여러 개인 경우에는 다음과 같이 식을 세우고 최소자승법을 이용하면 a,b를 손쉽게 구할 수 있다.
  $$
  \begin{bmatrix}
  x_1 & - y_1 \\
  y_1 & x_1 \\
  x_2 & - y_2 \\
  y_2 & x_2 \\ 
  x_3 & - y_3 \\
  y_3 & x_3 \\ 
  \vdots & \vdots
  \end{bmatrix} \begin{bmatrix}
  a \\ b
  \end{bmatrix} =
  \begin{bmatrix}
  x_1' \\ y_1' \\
  x_2' \\ y_2' \\ 
  x_3' \\ y_3' \\
  \vdots
  \end{bmatrix}
  $$
  

  이렇게 a와 b를 구할 수 있고, 스케일의 s와 회전각이 되는 $$\theta$$ 는 다음과 같이 구할 수 있다.
  $$
  s = \sqrt{a^2+b^2} , cos\theta = \frac{a}{s} , sin\theta= \frac{b}{s}
  $$
  이제 s는 버리고 , $$\theta$$ 만 이용해서 두 점 집합 사이의 매핑 관계를 회전변환만으로 설명할 수 있다.

  물체 크기까지 허용한다면 s도 함께 이용하면 된다.

  #### 1. 3. Rigid 변환

  일반적인 rigid 변환을 행렬식으로 나타내면 다음과 같다.
  $$
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix} =
  \begin{bmatrix}
  a & -b \\ b & a
  \end{bmatrix} \begin{bmatrix}
  x \\ y
  \end{bmatrix} + \begin{bmatrix}
  c \\ d 
  \end{bmatrix}
  $$
  이를 전개하면,
  $$
  ax-by+c = x' \\ 
  bx + ay +d = y'
  $$
  이 되고, 이를 a,b,c,d에 대한 행렬식으로 다시 묶으면
  $$
  \begin{bmatrix}
  x & - y & 1 & 0\\
  y & x & 0 & 1
  \end{bmatrix} \begin{bmatrix}
  a \\ b \\ c \\ d
  \end{bmatrix} =
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix}
  $$
  처럼 된다.

  주어진 매칭쌍들을 
  $$
  (x_1,y_1) -(x_1',y_1') \\ 
  (x_2,y_2) -(x_2',y_2')
  $$
  라 하면, 이 점들을 대입해서 
  $$
  \begin{bmatrix}
  x_1 & - y_1 & 1 & 0\\
  y_1 & x_1 & 0 & 1 \\
  x_2 & - y_2 & 1 & 0\\
  y_2 & x_2 & 0 & 1\\ 
  
  \vdots & \vdots
  \end{bmatrix} \begin{bmatrix}
  a \\ b \\ c \\ d
  \end{bmatrix} =
  \begin{bmatrix}
  x_1' \\ y_1' \\
  x_2' \\ y_2' \\ 
  \vdots
  \end{bmatrix}
  $$
  로 행렬식을 세운다.

  매칭쌍을 가장 잘 근사하는 rigid 변환을 찾을 경우, a,b,c,d를 무사히 결정할 수 있게 된다.

  그리고 s 와 $$cos\theta , sin\theta$$ 값은 a,b,c,d,를 통해 구할 수 있다.마지막으로 이렇게 구한 $$\theta$$ 와 $$c,d$$ 를 
  $$
  \begin{bmatrix}
  x' \\ y'
  \end{bmatrix} =
  \begin{bmatrix}
  a & -b \\ b & a
  \end{bmatrix} \begin{bmatrix}
  x \\ y
  \end{bmatrix} + \begin{bmatrix}
  c \\ d 
  \end{bmatrix}
  $$
  에 대입하면, rigid 변환을 얻을 수 있게 된다.

  여기서 구한 rigid 변환으로부터 실제 물체가 얼마나 평행이동했는지를 알아낼수는 없다고 한다.

  무엇을 기준으로 삼는지에 관계없이 수식적으로 rigid 변환은 유일하게 결정되기 때문에, 결론적으로 rigid 변환식 자체에서는 평행이동량을 구할 수 없다.

  왜냐하면.   $$(x_1,y_1) -(x_1',y_1') \\ 
  (x_2,y_2) -(x_2',y_2') $$   와 같은 매칭 쌍으로 구한 rigid 변환식에 의하면 

  $$(x_3,y_3) $$ 도 동일한 $$(x_3',y_3')$$ 이 나와야 하기 때문이다.



### 2. Similarity Transformation

다음은 similarity 변환인데, 이 변환은 Rigid 변환에서 추가적으로 스케일 변화까지 허용한 변환이다.

* 형태 유지
* 크기, 회전, 평행이동 변환

일반식은 rigid와 동일하게 
$$
\begin{bmatrix}
x' \\ y'
\end{bmatrix} =
\begin{bmatrix}
a & -b \\ b & a
\end{bmatrix} \begin{bmatrix}
x \\ y
\end{bmatrix} + \begin{bmatrix}
c \\ d 
\end{bmatrix}
$$
이다.

similarity의 자유도는 4이며, 이 변환을 유일하게 결정하기 위해서는 2개의 매칭쌍이 필요하다.

여기서 homogeneous 표현법을 통해 회전, 평행이동 , 스케일 변화를 하나의 단일 행렬로 표현할 수 있다.
$$
\begin{bmatrix}
x' \\ y' \\ 1
\end{bmatrix} =
\begin{bmatrix}
a & -b & c\\ b & a & d\\0 & 0 & 1
\end{bmatrix} \begin{bmatrix}
x \\ y \\ 1
\end{bmatrix}
$$
이것으로 회전, 스케일링, 평행이동을 행렬 변환 하나로 표현할 수 있게 되었고,

X' = AX 인 행렬 A는 X에서 X'로의 선형 변환이다. 이렇게 homogeneous 형태의 선형변환으로 표현했을 때 가장 큰 장점은 **여러 변환들을 행렬 곱으로 자유롭게 결합할 수 있다는 점**이다. 

순서대로 행렬곱을 하게 되면 하나의 변환으로 표현이 가능해진다.



### 3. Affine Transformation

Affine 변환은 직선, 길이(거리)의 비, 평행성을 보존하는 변환이며 그 일반식은 다음과 같다.

- 크기, shearing, 반전(reflection), 회전, 평행이동 변환

$$
\begin{bmatrix}
x' \\ y'
\end{bmatrix} =
\begin{bmatrix}
a & -b \\ b & a
\end{bmatrix} \begin{bmatrix}
x \\ y
\end{bmatrix} + \begin{bmatrix}
e  \\ f
\end{bmatrix}
$$

또는 
$$
\begin{bmatrix}
x' \\ y' \\ 1
\end{bmatrix} =
\begin{bmatrix}
a & -b & e\\ b & a & f\\0 & 0 & 1
\end{bmatrix} \begin{bmatrix}
x \\ y \\ 1
\end{bmatrix}
$$
처럼 단일 행렬로도 표현가능하다.

Affine 변환의 자유도는 6이고, 따라서 3개의 매칭쌍이 있으면 affine 변환을 유일하게 결정할 수 있다.

**질문 사항 : 여기서 말하는 자유도가 정확히 어떤 개념인지 궁금하다.**

