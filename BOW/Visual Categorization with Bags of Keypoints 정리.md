#### 2.3.2 Categorization by SVM

- SVM 분류기는 two-class데이터를 분리하는 최대 Margin을 갖는 hyperplane(초평면)을 찾는다.

- Magin = hyperplane과 hyperplane으로부터 가장 가까운 데이터 포인트와의 거리

- 주어진 관측값 X와 대응되는 레이블 Y(+1 or -1)에 대해서, 

![image](https://user-images.githubusercontent.com/26589942/61997987-2b7aa200-b0e4-11e9-86a2-4f194d2c73d8.png)

  여기서 w와 b는 hyperplane의 파라미터이다.

- 일반적으로 데이터는 선형분류가 되지 않기 때문에, SVM은 두가지의 적절한 방법을 사용한다.

  1. 분류 경계로부터의 거리에 비례한 오분류 샘플에 대한 가중 패널티를 상수 C로 부여한다.
  2. mapping 함수는 X의 본래의 데이터 공간에서 또다른 feature 공간으로 만드는 함수이다

  이 feature space는 높거나 무한한 차원을 갖고 있다. SVM의 장점 중 하나는 그것이(???) 완전히 scalar의 관점으로 공식화가 가능하다는 점이다. -> 아마도 실제 데이터를 확장시키지 않고 확장된 feature를 scalar 곱으로 표현할 수 있다는 점이 장점이라는 뜻인 것 같다.

  kernel 함수를 도입해서,
![image](https://user-images.githubusercontent.com/26589942/61997992-36cdcd80-b0e4-11e9-9c97-c9fdc61b5094.png)

  Kernel K와 penalty C는 해결하려는 문제에 의존적이고 사용자에 의해 결정된다.

  Kernel 공식에서, 결정 경계는 

![image](https://user-images.githubusercontent.com/26589942/61997995-40573580-b0e4-11e9-984c-2c143fe1fba0.png)

  로 표현될 수 있다. 

  x_i는 데이터 공간 X상에 존재하는 학습할 feature 이고 y_i 는 x_i 에 대한 레이블이다.

  여기에 파라미터 alpha(알파) 는 전형적으로 대부분 0이다. 동등하게, 그 합계는 소수의 x_i 에 대해 이루어진다. 그 특징 벡터들은 **support vectors**라고 부른다.

  **support vectors** 는 hyperplane 가장 근접하게 놓여있는 벡터들이 될 수 있다.

  이미지 I_i 속 vocabulary V 로부터의 각각 key point v_i 의 출현 횟수로 형성된 histogram이 input feature x_i 가 된다.

  SVM 분류기를 multi-class 문제에 적용하기 위해 one-against-all(OAA또는 OVA)접근방법을 취한다. m-1개의 클래스 j의 이미지와 구별되는 클래스 i의 이미지로 학습한다.

  ![one against all svmì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://courses.media.mit.edu/2006fall/mas622j/Projects/aisen-project/boaa-diagram.png)

  자세한 One-Vs-All Classification 내용은 

  http://www.jmlr.org/papers/volume5/rifkin04a/rifkin04a.pdf

  를 참조해보면 좋을 것 같다. 

  Query Image가 주어지면, 가장 큰 SVM output을 가진 클래스를 query Image에 부여한다.

  

### 3. 실험

- SVM과 Naive Bayes 분류기로 평가를 시행

- 데이터 셋은 in-house seven class 를 사용.
- 1776 이미지, 7개의 클래스(얼굴 792장, 건물 150장, 나무 150장, 차 201장, 전화기 216장, 자전거 125장, 책 142장)가 있음
![image](https://user-images.githubusercontent.com/26589942/61997918-64664700-b0e3-11e9-9db3-cd68d80b78d4.png)


- 많은 양의 배경 혼란이 있는 이미지가 있었고, 간혹 타겟 클래스가 대부분을 차지한 이미지더라도 여러 클래스도 사진에 포함되어있는 경우가 있었다. -> Challenging Dataset임을 말하고 있음.
- 평가는 confusion Matrix를 사용. 



#### 3.1 Naive Bayes 결과

클러스터 개수 K에 따른 Naive Bayes를 사용한 전반적인 에러율은 다음 그림과 같다.

![image](https://user-images.githubusercontent.com/26589942/61997914-59131b80-b0e3-11e9-8f84-f074ad435b36.png)


- K-means 알고리즘의 10번 random trials가 best
- k가 1000부터 2500개 구간 사이에는 에러율이 미세하게 감소했다. 
- 따라서, k=1000였을 때 정확도와 속도 사이의 좋은 trade-off라고 주장한다.

**가장 좋은 vocabulary(k=1000)의 평균 랭크 Confusion Matrix**

![image](https://user-images.githubusercontent.com/26589942/61997936-91b2f500-b0e3-11e9-9a2d-f5743cc186cc.png)



클러스터링 과정에서 , 서로 다른 카테고리의 이미지에는 Interest point 수가 다르므로 편향 될 위험이 있다. 그래서 클러스터링 step에서 랜덤 샘플링을 사용해 각각 샘플링에 5000개의 interest point를 각각 클래스별로 뽑았음. -> **Bootstrapping**과 유사하지만 잘못 분류한 데이터 위주로 더 뽑는 과정은 없으므로 오버피팅을 줄이기 위한 **랜덤 샘플링**이라고 정의할 수 있음.



그 다음 논문에서는 이미지의 interest point를 클러스터링 했을 때 얼마나 잘 정의되는지를 보여준다.

![image](https://user-images.githubusercontent.com/26589942/61997939-98416c80-b0e3-11e9-86f5-781925527270.png)


**Fig. 4** 에서 전화기 이미지의 interest point를 가진 patch들을 clustering했고, 보라색과 노란색은 대표적인 클러스터의 대표 interest point를 가진 patch를 보여준다.




![image](https://user-images.githubusercontent.com/26589942/61997940-9e374d80-b0e3-11e9-8bc5-093c0f2756ca.png)


**Fig. 5**이 알고리즘(descriptor->clustering->select centroid->feature histogram) 하나의 이미지에 동일한 객체가 존재해도 쉽게 분류할 수 있다는 점이라고 언급하고 있다.

**Fig. 6** 은 부분적인 시점에서도 분류되는 이미지들이다.




![image](https://user-images.githubusercontent.com/26589942/61997943-a55e5b80-b0e3-11e9-8355-6aa1c4e5fee8.png)


**Fig. 7**은 배경 혼란으로 interest point가 배경에 높은 비율로 검출되었음에도 불구하고 잘 분류된다고 언급하고 있다.




#### 3.2 SVM 결과

![image](https://user-images.githubusercontent.com/26589942/61999168-6ab1ee80-b0f6-11e9-93a9-ebe6cd06f603.png)

- 예상대로 **SVM이 Naive Bayes보다 성능이 잘 나왔고**, 전반적인 error rate가 28~ 15% 감소했다

- 기하학적인 정보를 담고 있지 않음에도 얼굴 error rate에서 SOTA를 찍었다.
- 그러나 SOTA라고 하기엔 직접적인 비교가 어렵다. 학습 데이터에서 얼굴 데이터 비율이 매우 높았기 때문에~~

- SVM 학습에서, k=1000으로 Naive Bayes와 동일하게 진행했고, linear, quadratic, cubic SVM중에서 linear SVM이 가장 좋은 퍼포먼스를 보여줬다. 파라미터 C=0.005에서 가장 좋은 성능을 보여줬다.



#### 3.3 Results on database

- 또한 5개 클래스로 구성된 데이터(얼굴 450장, 비행기 측면 1074장, 차 앞면 651장, 차 측면 720장, 오토바이 측면 826장) 로 테스트를 진행했다.

![image](https://user-images.githubusercontent.com/26589942/61997949-b4dda480-b0e3-11e9-9c24-80ea047f914e.png)

- 결과는 더 잘 나왔다. 앞서 진행한 table1과 table2과 직접 비교는 할 수 없다. SVM의 classification은 two-class problem으로 분류한 결과이기 때문이다.





#### 3.4 Conclusion

- 이미지 패치의 clustering된 descriptor들로 구성된 feature vector를 사용해서 이미지를 categorization 하는 새로운 방법을 제안

- 배경 혼란에 강인하고 기하학적 정보 없이도 높은 카테고리 분류 퍼포먼스

- SVM 분류기가 Simple Naive Bayes 분류기보다 높은 성능을 보여주었음

- Future work : 

  - 기하학적 정보를 통합한 categorizer
  - 관심 object가 viewpoint에서 작은 부분을 차지한 경우에서의 더 좋은 method
  - point detection, clustering, classification 단계에서 더 좋은 method

  