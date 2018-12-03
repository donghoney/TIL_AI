[PAPER REVIEW](https://blog.lunit.io/category/paper-review/)[2018년 AUGUST 3일](https://blog.lunit.io/2018/08/03/batch-size-in-deep-learning/)

# Batch Size in Deep Learning

딥러닝 모델의 학습은 대부분 mini-batch Stochastic Gradient Descent (SGD)를 기반으로 이루어집니다. 이 때 batch size는 실제 모델 학습시 중요한 hyper-parameter 중 하나이며, batch size가 모델 학습에 끼치는 영향과 관련한 다양한 연구도 이루어지고 있습니다. 아직까지 명확하게 밝혀진 바는 없지만, 작은 batch size를 사용하면 generalization performance 측면에서 긍정적인 영향을 끼친다는 것이 여러 연구에서 실험적으로 관찰되고 있는 결과입니다.

본 포스트에서는 SGD 및 batch size와 관련한 기본적인 내용을 간단히 리뷰하고, 이 주제에 대해 보다 깊이있게 논의한 아래의 두 가지 논문을 소개합니다.

- D. Masters and C. Luschi, **Revisiting Small Batch Training for Deep Neural Networks**, arXiv 2018
- N. S. Keskar et al., **On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima**,  ICLR 2017

 

### **Recall: Stochastic Gradient Descent (SGD)**

학습하고자 하는 model의 파라미터를 ![\theta](https://s0.wp.com/latex.php?latex=%5Ctheta&bg=ffffff&fg=000000&s=0), 학습 데이터의 example 개수를 ![M](https://s0.wp.com/latex.php?latex=M&bg=ffffff&fg=000000&s=0)이라고 할 때, loss function ![L(\theta)](https://s0.wp.com/latex.php?latex=L%28%5Ctheta%29&bg=ffffff&fg=000000&s=0)는 아래와 같이 전체 학습 데이터에 대한 average로 표현됩니다.

![L(\theta) = \frac{1}{M} \sum_{i=1}^{M} L_i(\theta)](https://s0.wp.com/latex.php?latex=L%28%5Ctheta%29+%3D+%5Cfrac%7B1%7D%7BM%7D+%5Csum_%7Bi%3D1%7D%5E%7BM%7D+L_i%28%5Ctheta%29&bg=ffffff&fg=000000&s=2)

이러한 loss function을 minimize 하기 위한 대표적인 방법이 Gradient Descent 로서, ![L(\theta)](https://s0.wp.com/latex.php?latex=L%28%5Ctheta%29&bg=ffffff&fg=000000&s=0)에 대한 gradient의 반대 방향으로 step size (learning rate) ![\eta](https://s0.wp.com/latex.php?latex=%5Ceta&bg=ffffff&fg=000000&s=0)만큼 parameter를 업데이트 하는 과정을 여러 iteration을 통해 반복하여 최적의 parameter ![\theta^*](https://s0.wp.com/latex.php?latex=%5Ctheta%5E%2A&bg=ffffff&fg=000000&s=0)를 찾아냅니다.

![\theta_{k+1} = \theta_{k} - \eta \nabla L(\theta)](https://s0.wp.com/latex.php?latex=%5Ctheta_%7Bk%2B1%7D+%3D+%5Ctheta_%7Bk%7D+-+%5Ceta+%5Cnabla+L%28%5Ctheta%29&bg=ffffff&fg=000000&s=2)

![1-1](https://bloglunit.files.wordpress.com/2018/08/1-1.gif?w=474&h=356)

이 경우 gradient를 정확하게 계산할 수 있지만, 매 iteration마다 전체 데이터에 대한 loss function을 계산해야 하므로 엄청난 계산량을 필요로 합니다. 이를 개선한 방법이 한 iteration에 하나의 example만 사용하는 Stochastic Gradient Descent 입니다.

![\theta_{k+1} = \theta_{k} - \eta \nabla L_i(\theta)](https://s0.wp.com/latex.php?latex=%5Ctheta_%7Bk%2B1%7D+%3D+%5Ctheta_%7Bk%7D+-+%5Ceta+%5Cnabla+L_i%28%5Ctheta%29&bg=ffffff&fg=000000&s=2)

이 방법의 경우 각 iteration의 계산은 훨씬 빠른 반면 gradient의 추정값이 너무 noise해진다는 단점이 있습니다. 이를 보완한 방법이 매 iteration마다 적당한 크기의 mini-batch에 대한 gradient를 사용하는 Mini-Batch Stochastic Gradient Descent (SGD) 이며, 딥러닝에서 가장 일반적으로 사용되는 기법입니다.

![\theta_{k+1} = \theta_{k} - \eta \frac{1}{m} \sum_{i=1}^{m} \nabla L_i(\theta)](https://s0.wp.com/latex.php?latex=%5Ctheta_%7Bk%2B1%7D+%3D+%5Ctheta_%7Bk%7D+-+%5Ceta+%5Cfrac%7B1%7D%7Bm%7D+%5Csum_%7Bi%3D1%7D%5E%7Bm%7D+%5Cnabla+L_i%28%5Ctheta%29&bg=ffffff&fg=000000&s=2)

이 때 batch size (m)을 어떻게 결정하느냐에 따라 학습 과정에 차이가 발생합니다. Batch size가 클수록 gradient가 정확해지지만 한 iteration에 대한 계산량이 늘어나게 됩니다. 그러나 한 iteration에서 각 example에 대한 gradient ![\nabla L_i(\theta)](https://s0.wp.com/latex.php?latex=%5Cnabla+L_i%28%5Ctheta%29&bg=ffffff&fg=000000&s=0)는 parellel하게 계산이 가능하므로, 큰 batch를 사용하면 multi-GPU 등 parellel computation의 활용도를 높여서 전체 학습 시간을 단축할 수 있습니다. 정리하면, batch size가 SGD에 끼치는 기본적인 영향은 아래와 같습니다.

![comparing_batch_size](https://bloglunit.files.wordpress.com/2018/08/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2018-08-02-e1848be185a9e18492e185ae-3-46-01.png?w=1024&h=220)

### **Revisiting Small Batch Training for Deep Neural Networks (arXiv 2018)**

첫 번째 논문은 딥러닝에서 small batch training의 장점을 다양한 실험을 통해 입증한 논문입니다. 이 논문에서 주장하는 small batch의 장점은 아래 두 가지로 요약될 수 있습니다.

- Generalization performance가 좋아진다.
- Training stability가 좋아진다. 즉, 보다 넓은 범위의 learning rate로 학습이 가능하다.

### Reformulating SGD

앞에서 설명한 Mini-Batch SGD를 다시 쓰면 아래와 같습니다.

![\theta_{k+1} = \theta_{k} + \eta \Delta\theta_k](https://s0.wp.com/latex.php?latex=%5Ctheta_%7Bk%2B1%7D+%3D+%5Ctheta_%7Bk%7D+%2B+%5Ceta+%5CDelta%5Ctheta_k&bg=ffffff&fg=000000&s=2)

![\Delta\theta_k = -\frac{1}{m} \sum_{i=1}^{m} \nabla L_i(\theta)](https://s0.wp.com/latex.php?latex=%5CDelta%5Ctheta_k+%3D+-%5Cfrac%7B1%7D%7Bm%7D+%5Csum_%7Bi%3D1%7D%5E%7Bm%7D+%5Cnabla+L_i%28%5Ctheta%29&bg=ffffff&fg=000000&s=2)

이 때 특정 step에서의 weight update vector ![\eta \Delta\theta_k](https://s0.wp.com/latex.php?latex=%5Ceta+%5CDelta%5Ctheta_k&bg=ffffff&fg=000000&s=0) 를 random variable로 보면, 그 expectation 값은 다음과 같이 표현됩니다.

![\mathbb{E}[\eta \Delta\theta] = -\eta \mathbb{E}[\nabla L_i(\theta)]](https://s0.wp.com/latex.php?latex=%5Cmathbb%7BE%7D%5B%5Ceta+%5CDelta%5Ctheta%5D+%3D+-%5Ceta+%5Cmathbb%7BE%7D%5B%5Cnabla+L_i%28%5Ctheta%29%5D&bg=ffffff&fg=000000&s=2)

이는 한 iteration (m examples)에 대한 weight update 값이므로, 한 example (unit cost of computation)에 해당하는 weight update의 expectation은 아래와 같습니다.

![\frac{1}{m} \mathbb{E}[\eta \Delta\theta] = -\frac{\eta}{m} \mathbb{E}[\nabla L_i(\theta)]](https://s0.wp.com/latex.php?latex=%5Cfrac%7B1%7D%7Bm%7D+%5Cmathbb%7BE%7D%5B%5Ceta+%5CDelta%5Ctheta%5D+%3D+-%5Cfrac%7B%5Ceta%7D%7Bm%7D+%5Cmathbb%7BE%7D%5B%5Cnabla+L_i%28%5Ctheta%29%5D&bg=ffffff&fg=000000&s=2)

따라서 이 값 (the expected value of the weight update per unit cost of computation)을 일정하게 유지하기 위해서는 batch size (m)와 상관 없이 base learning rate ![\tilde{\eta} = \frac{\eta}{m}](https://s0.wp.com/latex.php?latex=%5Ctilde%7B%5Ceta%7D+%3D+%5Cfrac%7B%5Ceta%7D%7Bm%7D&bg=ffffff&fg=000000&s=0) 값을 일정하게 유지해 주어야 하며, 이는 batch size에 linear하게 learning rate를 증가시키는 “linear scaling role”에 해당합니다.

### Benefits of Small Batch Training

Batch size m을 이용하여 n steps의 weight update를 진행한 이후의 weight 값은 아래와 같이 표현할 수 있습니다.

![\theta_{k+n} = - \tilde{\eta}\sum_{j=0}^{n-1} \sum_{i=1}^{m} \nabla L_{i+jm}(\theta_{k+j})](https://s0.wp.com/latex.php?latex=%5Ctheta_%7Bk%2Bn%7D+%3D+-%C2%A0%5Ctilde%7B%5Ceta%7D%5Csum_%7Bj%3D0%7D%5E%7Bn-1%7D+%5Csum_%7Bi%3D1%7D%5E%7Bm%7D+%5Cnabla+L_%7Bi%2Bjm%7D%28%5Ctheta_%7Bk%2Bj%7D%29&bg=ffffff&fg=000000&s=2)

여기서 batch size를 n배 증가시키면, 같은 개수의 training example에 해당하는 weight update는 아래와 같이 표현됩니다.

![\theta_{k+1} = - \tilde{\eta}\sum_{i=1}^{nm} \nabla L_{i}(\theta_k)](https://s0.wp.com/latex.php?latex=%5Ctheta_%7Bk%2B1%7D+%3D+-%C2%A0%5Ctilde%7B%5Ceta%7D%5Csum_%7Bi%3D1%7D%5E%7Bnm%7D+%5Cnabla+L_%7Bi%7D%28%5Ctheta_k%29&bg=ffffff&fg=000000&s=2)

위 두 식을 비교해보면, small batch (m)의 경우 parameter space 상에서 보다 최신 상태의 gradient (![\nabla L_{i+jm}(\theta_{k+j})](https://s0.wp.com/latex.php?latex=%5Cnabla+L_%7Bi%2Bjm%7D%28%5Ctheta_%7Bk%2Bj%7D%29&bg=ffffff&fg=000000&s=0))를 사용할 수 있는 반면, large batch (nm)의 경우 오래 전 상태의 gradient (![\nabla L_{i}(\theta_k)](https://s0.wp.com/latex.php?latex=%5Cnabla+L_%7Bi%7D%28%5Ctheta_k%29&bg=ffffff&fg=000000&s=0))를 계속 사용해야 함을 알 수 있습니다. Deep neural network의 loss function과 같이 복잡한 non-convex function일수록 gradient 값은 parameter 상태에 따라 크게 변하므로, large batch를 사용하면 오래전 gradient로 부정확한 weight update를 하게 될 위험이 커지게 되고, base learning rate를 크게 가져가지 못하는 원인이 될 수 있습니다.

### Results

#### Performance without BN

우선 Batch Normalization (BN)을 제거한 ResNet-8 모델의 CIFAR-10에서의 실험결과는 아래와 같습니다.

![그림1](https://bloglunit.files.wordpress.com/2018/08/e18480e185b3e18485e185b5e186b71.png?w=1400)

Learning rate를 고정하고 batch size를 변화시킨 그래프 (왼쪽)는 작은 batch size에서 보다 높은 test accuracy를 얻을 수 있음을 보여줍니다. 또한 batch size를 고정하고 learning rate를 변화시킨 그래프 (오른쪽)를 보면, 작은 batch를 사용할 경우 더 넓은 범위의 learning rate에서 안정적인 학습이 가능함을 알 수 있습니다.

#### Performance BN

다음으로 Batch Normalization (BN)을 적용한 ResNet-32 모델의 CIFAR-10에서의 실험 결과는 아래와 같습니다.

![그림2](https://bloglunit.files.wordpress.com/2018/08/e18480e185b3e18485e185b5e186b72.png?w=1400)

이 경우도 위 실험과 거의 비슷한 결과를 관찰할 수 있습니다. 다만 BN을 사용할 경우 batch size가 너무 작으면 (< 8) batch statistics가 부정확해져서 약간의 성능저하가 생김을 관찰할 수 있습니다. 또한 SGD의 batch size와 BN의 batch size를 분리하여 (multi-GPU를 사용하는 일반적인 상황) 학습한 실험 결과는 아래와 같으며, SGD의 batch size와 무관하게 BN의 batch size가 8 정도 일 때 최적의 성능이 얻어짐을 보여줍니다.

![스크린샷 2018-08-02 오후 6.05.58](https://bloglunit.files.wordpress.com/2018/08/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2018-08-02-e1848be185a9e18492e185ae-6-05-58-e1533293773837.png?w=465&h=381)

### Summary

이 논문은 small batch training의 장점을 다양한 실험을 통해 입증했습니다. 일반적으로 알려진 바와 같이 small batch가 generalization 측면에서 유리하며, 안정적인 학습을 가능하게 함으로써 보다 넓은 범위의 learning rate를 사용할 수 있음을 보였습니다. 뿐만 아니라, BN을 위한 최적의 batch size는 SGD batch size보다 일반적으로 작으며, SGD batch size와 무관한 성향을 보이기도 함을 발견하였습니다. 한 가지 아쉬운 점은, 이러한 결과를 발생시킨 원인에 대한 이론적인 분석이 다소 부족하다는 것입니다. 아래에서 소개드릴 논문은 이와 관련된 조금 더 이론적인 분석을 제공합니다.

 

### **On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima (ICLR 2017)**

두 번째 논문은 SGD에서 batch size의 영향을 조금 더 이론적인 측면에서 접근한 논문입니다. 논문의 주제를 먼저 간단히 요약하면 “**Large batch를 사용할수록 training function의 sharp minima로 수렴할 가능성이 높아지고, 이는 generalization 성능을 저하시킨다.**” 입니다. 아래 그림과같은 loss function을 생각 해 볼때, sharp minima는 loss function의 작은 변화에도 민감하게 반응하기 때문에 flat minima에 비해 generalization 측면에서 훨씬 불리하다고 볼 수 있습니다.

![loss](https://bloglunit.files.wordpress.com/2018/08/loss.png?w=591&h=252)

### Sharpness of Minima

Small Batch (SB)로 얻어진 solution을 ![x_s^*](https://s0.wp.com/latex.php?latex=x_s%5E%2A&bg=ffffff&fg=000000&s=0), Large Batch (LB)로 얻어진 solution을 ![x_l^*](https://s0.wp.com/latex.php?latex=x_l%5E%2A&bg=ffffff&fg=000000&s=0) 라고 할 때, 두 solution을 잇는 line segment에 대한 loss ![f(x)](https://s0.wp.com/latex.php?latex=f%28x%29&bg=ffffff&fg=000000&s=0) 값 및 CNN에서 이를 직접 구하여 plotting한 결과는 아래와 같습니다.

![f(\alpha x_l^* + (1-\alpha) x_s^*), \alpha \in [-1, 2]](https://s0.wp.com/latex.php?latex=f%28%5Calpha+x_l%5E%2A+%2B+%281-%5Calpha%29+x_s%5E%2A%29%2C+%5Calpha+%5Cin+%5B-1%2C+2%5D&bg=ffffff&fg=000000&s=2)

![스크린샷 2018-08-03 오후 5.32.26](https://bloglunit.files.wordpress.com/2018/08/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2018-08-03-e1848be185a9e18492e185ae-5-32-26.png?w=1400)

이 때 ![\alpha=0](https://s0.wp.com/latex.php?latex=%5Calpha%3D0&bg=ffffff&fg=000000&s=0)은 SB solution에, ![\alpha=1](https://s0.wp.com/latex.php?latex=%5Calpha%3D1&bg=ffffff&fg=000000&s=0)은 LB solution에 해당합니다. 그래프에서 보이는 바와 같이, SB solution 근처에서는 loss 값이 천천히 변화하는 반면, LB solution 근처에서는 급격하게 변화합니다. 이는 SB와 LB가 각각 flat minima와 sharp minima로의 수렴을 유도함을 간접적으로 나타내는 결과라고 볼 수 있습니다.

다음으로 논문은 minima의 sharpness에 대한 좀더 엄밀한 분석을 시도합니다. Loss function ![f(x)](https://s0.wp.com/latex.php?latex=f%28x%29&bg=ffffff&fg=000000&s=0)에 대한 sharpness는 Hessian matrix ![\nabla^2 f(x)](https://s0.wp.com/latex.php?latex=%5Cnabla%5E2+f%28x%29&bg=ffffff&fg=000000&s=0)에 대한 eigenvalue들의 magnitude로 표현됩니다. 그러나 deep neural network에서 이를 직접 계산하는 것이 거의 불가능하므로, 다음과 같은 approximation을 도입합니다. 우선 특정 solution ![x](https://s0.wp.com/latex.php?latex=x&bg=ffffff&fg=000000&s=0)에 대한 neighborhood를 다음과 같이 정의합니다.

![eq](https://bloglunit.files.wordpress.com/2018/08/eq.png?w=1400)

여기서 ![\epsilon](https://s0.wp.com/latex.php?latex=%5Cepsilon&bg=ffffff&fg=000000&s=0)는 neighborhood box의 크기, ![A](https://s0.wp.com/latex.php?latex=A&bg=ffffff&fg=000000&s=0)는 random projection matrix 입니다. 이렇게 정의된 ![\mathcal{C}_\epsilon](https://s0.wp.com/latex.php?latex=%5Cmathcal%7BC%7D_%5Cepsilon&bg=ffffff&fg=000000&s=0)을 이용하여, sharpness에 대한 아래와 같은 measure를 정의합니다.

![mt](https://bloglunit.files.wordpress.com/2018/08/mt.png?w=1400)

이는 특정 solution ![x](https://s0.wp.com/latex.php?latex=x&bg=ffffff&fg=000000&s=0) 에서의 loss 값 대비 그 주변에서 얻어지는 loss의 최대값의 비율로 해석되며, 이 값이 클수록 sharp minima, 작을수록 flat minima라고 볼 수 있습니다.

### Results

아래 표는 다양한 network에 대해 SB solution과 LB solution의 sharpness를 비교한 결과이며, 모든 network에 대해 LB solution이 SB solution보다 1-2 order-of-magnitude 더 큰 sharpness를 가지게 됨을 보여줍니다.

![스크린샷 2018-08-03 오후 6.55.16.png](https://bloglunit.files.wordpress.com/2018/08/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2018-08-03-e1848be185a9e18492e185ae-6-55-16.png?w=1400)

아래 그림은 batch size에 따른 test accuracy 와 sharpness를 그래프로 보여준 결과입니다. batch size가 커짐에 따라 sharpness가 증가하고 test accuracy가 감소함을 확인할 수 있습니다.

![스크린샷 2018-08-03 오후 7.00.13.png](https://bloglunit.files.wordpress.com/2018/08/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2018-08-03-e1848be185a9e18492e185ae-7-00-13.png?w=1400)

아래 그림은 SB training 과 LB training 과정에서, cross-entropy 감소 (학습 진행)에 따른 sharpness의 변화를 비교한 것입니다. SB training의 경우 학습이 진행될수록 sharpness가 감소하는 반면, LB training의 경우 오히려 처음 상태보다 더 sharpness가 커지게 됩니다.

![스크린샷 2018-08-03 오후 7.02.35.png](https://bloglunit.files.wordpress.com/2018/08/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2018-08-03-e1848be185a9e18492e185ae-7-02-35.png?w=1400)

### Summary

이 논문은 Small batch와 large batch의 generalization 성능 차이를 sharpness of minima의 관점에서 설명하고, 실험적으로 그러한 주장을 뒷받침하였습니다. 또한 이러한 현상의 원인에 대해, “small batch를 사용할 경우 gradient의 noise가 커지기 때문에 sharp minimizer에서 쉽게 벗어날 수 있고 noise에 둔감한 flat minimizer로 수렴하게 된다.”는 직관적인 해석을 덧붙였습니다. 그러나 이 논문의 경우도 왜 small batch training이 flat minimizer로 수렴하는가? flat minimizer가 왜 generalization 에 더 좋은가? 등에 대한 엄밀한 증명은 하지 못하고 제한된 상황에서 실험 결과로만 보여주었다는 한계점이 있습니다.

### 

### **Conclusion**

이 포스트는 딥러닝에서 SGD에 batch size가 끼치는 영향에 관해 설명한 두 논문을 살펴보았습니다. 두 논문이 서로 다른 방식으로 접근하긴 했지만, 공통적으로 주장하는 바는 small batch를 사용하는 것이 generalization 측면에서 더 좋은 영향을 끼친다는 것입니다. 그러나 포스트의 서론에서 명시하였듯이, 아직까지 딥러닝에서 batch size의 영향에 관해 뚜렷하게 밝혀진 바는 없습니다.  실제로 최적의 성능을 얻기 위한 batch size는 모델과 task의 특성에 따라 크게 달라지며, 학습 시간을 단축하기 위한 측면에서는 batch size를 최대한 크게 키우면서 성능을 향상시키는 것이 훨씬 좋은 접근법이라고 볼 수 있습니다 [1, 2]. 그럼에도 불구하고 이 두 논문은 딥러닝 모델의 optimization에 대한 보다 깊은 이해를 제공하며, 실제 model의 hyper-parameter를 설정함에 있어서 좋은 직관을 제공해준다는 것에 의의를 둘 수 있습니다.

 

#### Reference

[1] Priya Goyal et al., Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour, Data@Scale, 2017

[2] Xianyan Jia, Highly Scalable Deep Learning Training System with Mixed-Precision: Training ImageNet in Four Minutes, arXiv, 2017