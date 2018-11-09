* 기본 GAN의 원리

```
'z' 벡터가 존재하는 공간을 잠재 공간 (Latent Space)라고 부른다.

잠재 공간의 크기는 제한이 없다. 



z ~ p(z) 랜덤 벡터 z를 Generator에 넣어서 가짜 이미지를 생성한다

가짜 이미지는 주기적으로 visualization 된다.

Generator에서 생성된 가짜 이미지는 Discriminator에 들어간다.

Real Data의 진짜 이미지도 Discriminator에 들어간다.



가짜 이미지가 진짜 이미지와 얼마나 가까운지를 측정한다.

Discriminator는 진짜 이미지를 입력하면 1에 가까운 확률값을 출력하고,

가짜 이미지를 입력하면 0에 가까운 확률값을 출력해야 한다.

진짜 이미지를 입력했을 때의 출력값과 1과의 차이

가짜 이미지를 입력했을 때의 출력값과 0과의 차이

두 경우의 합이 Discriminator의 손실 함수다.

Discriminator의 출력 값은 Binary cross entropy 손실 함수(loss function)를 사용한다.

이 손실 함수의 값을 낮추는 것이 Discriminator 모델 학습의 목표가 된다.

Generator와 Discriminator의 매개변수를 손실함수의 값을 낮추는 방향으로 업데이트 하는 최적화 함수는 AdamOptimizer(매개변수마다 업데이트 속도를 조절하는 최적화 기법)를 사용한다.



Generator는 Discriminator를 속이는 것이 목표.

Discriminator에 G에서 나온 가짜 이미지를 넣었을 때 출력값이 1에 가깝게 나오도록 해야한다.

이 값이 1에서 떨어진 정도가 생성자의 손실 함수가 된다. 이를 최소화 시키도록 생성자를 학습시킨다.
```

* 기본 GAN의 입력 데이터(Input Data) : 랜덤 벡터



* DCGAN의 원리

```
기본 GAN의 학습이 어려운 점을 개선시킨 DCGAN

1. Linear Layer와 Pooling Layer를 최대한 배제하고 Convolution과 Fractional-Strided Convolution으로 네트워크 구조를 만든다.
그 이유는, Pooling Layer와 Linear Layer는 불필요한 매개변수의 수를 줄이고 중요한 특징만 골라내는 역할을 하지만, 이미지의 위치 정보를 잃어 버리기 때문에, 배제한다.

2. Batch Normalization을 사용한다.
Batch Normalization은 CNN에서 입력 데이터의 분포가 치우쳐져 있을 때 평균과 분산을 조정해주는 역할을 한다.
이는 역전파(BackProp)가 각 레이어에 쉽게 전달되도록 해 학습이 안정적으로 이뤄지는 데 중요한 역할을 한다.

이 2가지가 기본 GAN과 DCGAN의 차이점이다.
그리고 마지막으로 DCGAN에서는 학습이 잘 이뤄졌는지 확인하기 위한 검증방법이 존재한다.
잠재 공간(Latent Space)에 실제 데이터 특성이 투영됐는지 살펴볼 수 있다.
예를 들어, 성별, 머리 색깔, 선글라스를 썼는지 여부등 의미 있는 단위들이 잠재 공간에 표현된다. Generator의 입력인 'z' 벡터의 값을 바꿔보는 것으로 Generator의 출력인 이미지의 속성을 바꿔볼 수 있다.

'z' 벡터에서 특정 값 변경 -> Generator가 의미있는 부분을 변화시킴 -> 의미적인 속성을 잘 학습함 을 뜻한다.
```

* DCGAN의 입력 데이터 : 랜덤 벡터



* cGAN의 원리

```
이미지를 처음부터 생성하지 않고, 이미 있는 이미지를 다른 영역의 이미지로 변형하고 싶을 때 사용한다.
예를들어 
스케치 -> 채색된 이미지
흑백 사진 -> 컬러 사진
낮 사진 -> 밤 사진  의 경우에 사용한다.

Discriminator는 스케치와 채색된 이미지를 모두 보고 그 채색된 이미지가 과연 스케치에 어울리는지를 판단한다.
Generator는 Discriminator를 속이기 위해 2가지를 해야하는데,
1. 진짜 같은 이미지를 만들어야 한다
2. 스케치에 맞는 이미지를 만들어야 한다

강력한 모델이지만, 입력 이미지와 출력 이미지가 매칭된 데이터를 필요로 한다.
```

* cGAN의 입력 데이터 : 변형시킬 이미지



* WGAN(Wasserstein GAN)

```
GAN에서 실제 데이터 분포와 근사하는 분포가 얼마나 다른지 측정하는 거리 개념을 바꿔 안정적인 학습을 가능하게 만들었다
```

* EBGAN(Energy-based GAN)

```
GAN을 에너지 관점에서 바라봄으로써 역시 더 안정적인 학습을 추구했다
```

* BEGAN(Boundary Equilibrium GAN)

```
WGAN과 EBGAN을 발전시켜 생성하는 이미지의 퀄리티를 획기적으로 높이고 이미지의 퀄리티와 다양성을 컨트롤 할 수 있게 했다.
```

* CycleGAN

```
두 영역의 이미지 데이터셋이 매칭되어 있지 않아도 이미지 변형을 가능하게 한다.
```

* DiscoGAN

```
CycleGAN과 유사하다
```

* StarGAN

```
세 개 이상의 영역 사이의 이미지 변형을 할 수 있다.
```

* SRGAN(Super-Resolution GAN)

```
사진의 해상도를 높이는 GAN
```

* SEGAN(Speech Enhancement GAN)

```
음성 녹음에서 노이즈를 줄여주는 GAN
```



* GAN의 한계점

```
학습의 불안정성 : 생성자와 구분자가 함께 조금씩 발전해야 한다. 한쪽이 너무 급격하게 강력해지면 다른 쪽 씨가 말라버린다 이를 Mode Collapse(모드붕괴)라고 한다.
```



