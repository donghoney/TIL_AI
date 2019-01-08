## 분류 모델(Classification)의 Accuracy Estimation

클러스터링과 분류 모델에 대한 성능 평가 방법은 데이터에 레이블이 있는지 없는지 여부에 따라 갈린다.

클러스터링은 레이블링이 없는 데이터에 주로 사용하고, 레이블이 있다면 분류 모델을 사용한다.

클러스터링 모델에 대한 평가는 레이블링이 안되어있는 상대에서 클러스터링의 응집도를 평가하는데 대부분 정확도는 그리 높지 않다.

그러므로 도메인 지식을 가진 전문가에 의해 휴리스틱한 방식의 평가가 대부분이다.



* 이 내용들은 조대협님의 블로그의 내용을 정리하고 옮긴 내용입니다. 좋은 글 정말 감사드립니다. 

* 조대협 (http://bcho.tistory.com)



### 분류 모델 평가

레이블이 있는 경우, 분류 모델에 대한 모델 평가 방법을 사용한다.

#### Confusion matrix

이진 분류 문제에서 암의 양성과 음성 데이터를 가지고 있는 데이터가 있다고 해보자.

![img](https://t1.daumcdn.net/cfile/tistory/99BE533359E629C823)

만약 모델의 정확도가 100%라면, 양성과 음성 데이터를 100% 잘 구분할 것이다. 아래 그림과 같이 , 양성으로 예측된 영역을 Positive prediction, 음성으로 분리된 영역을 Negative prediction이라고 한다. 

![img](https://t1.daumcdn.net/cfile/tistory/99B5CE3359E629C81D)

그렇지만, 실제 세계에서는 정확도 100%의 모델은 매우 드물고 실제로는 아래 그림과 같이 예측이 되는 경우가 많다.

![img](https://t1.daumcdn.net/cfile/tistory/99FB223359E629C83E)

양성과 음성 데이터가 각각 잘못되는 경우가 있다.

* 양성인데, 양성으로 제대로 검출된 것은 True Positive(TP)
* 음성인데, 음성으로 제대로 검출된것은 True Negative(TN)
* 양성인데, 음성으로 잘못 검출된 것은 False Negative(FN)
* 음성인데, 양성으로 잘못 검출된 것은 False Positive(FP)

라고 하고, 그림으로 표현하면 다음과 같은 그림이 된다.

![img](https://t1.daumcdn.net/cfile/tistory/99EFFA3359E629C82B)

보통 이를 표로 표시하는데, 다음과 같이 표현이 된다.

![img](https://t1.daumcdn.net/cfile/tistory/995C7A3359E629C812)

$$P = TP + FN$$

$$N = FP + TN$$

위의 이 지표를 바탕으로 모델 평가에 사용한다.

어떤 식으로 하는지 살펴보자.



#### Accuracy

가장 대표적으로 사용되는 지표로 전체 데이터중에서, 제대로 분류된 데이터의 비율로
$$
ACC = (TP+TN) / (전체 데이터 수 = P+N)
$$
모델이 얼마나 정확하게 분류를 하는지를 나타낸다.

![img](https://t1.daumcdn.net/cfile/tistory/9925043359E629C811)



#### Error Rate

Error Rate는 Accuracy와 반대로, 전체 데이터 중에서 잘못 분류한 비율을 나타낸다.

![img](https://t1.daumcdn.net/cfile/tistory/99BA513359E629C825)



#### Sensitivity (Recall or True positive Rate)

민감도라고도 하는데, Sensitive 또는 Recall 이라고도 하는데, 원래 Positive 데이터 수에서 Positive로 분류된 수를 이야기한다. 예를 들어, 원본 데이터에 암 양성이 100개 있었는데, 모델에 있어서 90개가 분류되었으면, Sensitive Rate = 0.9가 된다.
$$
SN = (TP) / P
$$
모델이 얼마나 정확하게 Positive 값을 찾느냐를 나타낸다.

Recall(precision의 반댓말)은 질문에 올바르게 답변하는 것이 아니라, 'true'라는 예측이 'true'의 모든 정답들에 모두 대응되게 하는 것에 더 가깝다.

따라서 단순히 'True'라면 100% 리콜한다.

![img](https://t1.daumcdn.net/cfile/tistory/9967C33359E629C832)

#### Precision

Precision(정밀성)은 Positive로 예측한 내용 중에 , 실제 Positive의 비율을 뜻한다.
$$
PREC = TP / (TP+FP)
$$
Precision가 정확하다는 것이다. 일반적인 영어에서 정확한 의미는, 만약 정답을 받았다면, 정답은 매우 정답에 가깝다는 뜻이다. 그래서 심지어 만약 한가지 질문에만 답을 하고 정확하게 답해도 100% 정확하다.



#### Specificity( True negative rate)

Specificity 값은 Negative로 판단한 것 중에, 실제 Negative 값의 비율이다.

![img](https://t1.daumcdn.net/cfile/tistory/99B3523359E629C824)

#### False Positive rate

원래는 Positive 값인데, 잘못해서 Negative로 판단한 비율로
$$
FPR = FP / N
$$
이 된다. 예를 들어, 게임에서 어뷰징 사용자를 검출했을 때 정확도도 중요하지만, FPR 값이 높으면, 정상 사용자를 비정상 사용자로 검출하는 경우가 많다는 의미가 된다. 어뷰징 사용자에 대해서는 계정 정지등 패널티를 주게 되는데, 모델이 아무리 어뷰징 사용자를 잘 찾아낸다 하더라도 FPR값이 높게 되면, 정상적인 사용자를 어뷰징 사용자로 판단하여 선의의 징계를 받게 되서, 전체적인 게임 충성도에 문제가 생길 수 있다. (어뷰징 사용자를 많이 찾아내는 것보다, 정상 사용자가 징계를 받게 되는 경우가 비지니스에 중요할때) 이런 경우에 FPR 값을 레퍼런스 할 수 있다.



그러면, Confusion Matrix를 통해서 계산된 결과를 가지고 모델을 어떻게 평가를 할까? 앞에서 나온 지표중에서 일반적으로 Accuracy 지표가 많이 사용되고, 그외에 ROC, Precision Recall Plot, F-Score등이 많이 사용되는 각각에 대해서 알아보자.

* 여기까지 정리하면서 조대협(http://bcho.tistory.com/tag/F1%20score)님께 다시한번 감사의 말씀을 드립니다.. 너무 간결하고 잘 읽혀서 제가 공부할 내용을 정리하면서도 고칠 내용이 없습니다.. 감사합니다.



#### ROC( Receiver Operating Characteristics)

ROC 그래프는 가로축을 FP Rate(Specificity) 값을 비율로 하고 세로축을 TP Rate(Sensitive)로 하여 시각화 한 그래프이다. 

* ##### Specificity $= TN / TN+FP$

* ##### Sensitive (Recall) $= (TP) / P$



보통 다음과 같은 그래프가 되고

![img](https://t1.daumcdn.net/cfile/tistory/998C8F3359E629C832)

그래프가 위로 갈 수록 좋은 모델, 적어도 Y=X 그래프보다 위에 있어야 쓸모 있는 모델로 볼 수 있다. 아래 그래프는 3개로 결과를 분류하는 모델에 대한 ROC 곡선 그래프이다.

![img](https://t1.daumcdn.net/cfile/tistory/99ABC43359E629C83C)



ROC 그래프가 class 0, class 2, class 1 순서로 높은 것을 볼 수 있다. 즉 이 모델은 class 0 을 제일 잘 분류하고, 그 다음은 2, 1 순서로 잘 분류한다는 의미가 된다.

ROC는 그래프이기 때문에, 모델의 정확도를 하나의 숫자로 나타내기 어려워서 AUC(Area Under Curve)라는 값을 사용하는데, ROC AUC 값은 ROC 그래프의 면적이 된다. 최대값은 1이 된다. 위의 그래프를 보면 모델 0,2,1의 AUC 값은 0.91, 0.79, 0.60이 된다.



### Precision Recall Plot

Precision Recall Plot (이하 PR그래프)의 경우도 ROC 와 유사한데, 주로 데이터 레이블의 분포가 심하게 불균등 할 때 사용한데, 예를 들어 이상 거래 검출 시나리오의 경우 정상 거래의 비율이 비정상 거래에 비해서 압도적으로 많기 때문에, (98%, 2%) 이런 경우에는 ROC 그래프보다 PR 그래프가 분석에 더 유리하다. 

PR그래프는 X축을 Recall 값을, Y축을 Precision 값을 사용한다.

* ##### Sensitive (Recall) $= (TP) / P$

* ##### Precision $= TP / (TP+FP)$

![img](https://t1.daumcdn.net/cfile/tistory/9983FE3359E629C815)

다음은 이진 분류 (binary classification)의 PR 그래프의 예이다. 그래프가 위쪽으로 갈수록 정확도가 높은 모델이고, ROC와 마찬가지로 PR 그래프의 AUC(면적)값을 이요하여 모델의 정확도를 평가할 수있다.

![img](https://t1.daumcdn.net/cfile/tistory/99BC933359E629C839)

그러면 모델이 쓸만한 모델인지 아닌지는 어떤 기준을 사용할까? ROC 그래프의 경우에는 Y=X 그래프를 기준으로 그래프 윗쪽에 있는 경우 쓸만한 모델로 판단을 했는데, PR 그래프의 경우 Base line이라는 것을 사용한다.



##### Base line = $P / ( P+N)$

으로 정하는데, P는 데이터에서 Positive 레이블의 수 , N은 전체 데이터의 수이다. 예를 들어, 암 데이터에서 양성이 300개 이고,. 전체 데이터가 700 이면 Base line은 300/(700+300) = 0.3 이 된다.



위의 PR 그래프에 Base line 을 적용하여 모델이 좋고 나쁜 영역을 판단하는 그림이다.

아래 그림은 두 모델을 비교한 PR 그래프인데, 두 모델 다 베이스라인을 넘어서 쓸만한 모델이기는 하지만, 모델 A가 B모델보다 확연하게 위에 위치하고 있기 때문에, A 모델이 좋다고 이야기 할 수 있다.

![img](https://t1.daumcdn.net/cfile/tistory/9956F73359E629C803)



### F-Score

모델의 성능을 하나의 수로 표현할 때, ROC나 PR 그래프의 AUC를 사용하면 되지만, AUC를 계산하려면 여러 Throughput(처리량이라고 한다.)에 대해서 Precision, Recall, Specificity 값을 측정해야 한다.

그렇다면 Throughput을 이미 알고 있거나 또는 다양한 Throughput에 대해서 어떤 Throughput이 좋은지를 하나의 수로 모델의 성능을 평가하려면 어떻게 해야할 까? 이를 위해서 사용하는 것이 $$F-Score$$라는 값이 있다.

F-Score에 대한 계산은 다음 공식을 이용한다. 큰 의미상으로 보자면 Precision과 Recall에 대한 평균인데, 그냥 평균을 내면, 값의 왜곡 현상이 생기기 때문에 가중치를 주는 평균이라고 이해하면 된다.

특히 $$\beta$$가 1인 경우 (즉 F1)를 F1 Score라고 하고, 모델의 성능 평가 지표로 많이 사용한다.

