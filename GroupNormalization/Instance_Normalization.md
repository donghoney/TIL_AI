[PAPER REVIEW](https://blog.lunit.io/category/paper-review/)[2018년 APRIL 12일](https://blog.lunit.io/2018/04/12/group-normalization/)

# Group Normalization

이번 포스트에서는 최근 많이 회자되고있는 Yuxin Wu와 Kaiming He가 2018년 3월에 공개한 논문 Group Normalization에 대해 살펴보도록 하겠습니다. 이 논문에서는 batch의 크기가 극도로 작은 상황에서 batch normalization 대신 사용하면 좋은 normalization 기술을 소개했는데, Faster RCNN과 같이 학습시에 batch 크기가 극도로 작을수 밖에 없는 모델에 적용하면 유용한 기술인듯 합니다. ![스크린샷 2018-04-11 오후 2.42.02.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-2-42-02.png?w=1400)

### 1. Introduction

![스크린샷 2018-04-11 오후 2.42.25.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-2-42-25.png?w=522&h=387)

Batch normalization (BN) 은 현재 대부분의 딥러닝 모델에 사용 되는 기술입니다. 간략히 BN에 대해 설명을 하면 네트워크에서 만들어지는 feature의 평균과 분산값을 batch 단위로 계산해서 normalize 시켜주는 기술입니다. 이때 계산되는 평균값은 비록 batch 내에서만 계산되지만  batch의 크기가 충분히 크면, 구해진 평균과 분산이 데이터셋 전체의 평균과 분산을 대표할수 있다는 가정을 가지고 있습니다. BN을 이용하면 상당히 깊은 네트워크도 더 빠르고 안정적으로 학습시킬수 있고 네트워크의 generalization 성능도 좋아진다고 알려져 있습니다. 하지만 아무때나 BN을 사용한다고해서 성능이 보장되는것은 아닙니다. 위 그래프에서 보여지는바와 같이 BN은 batch의 크기가 작으면 batch에서 구하는 값이 데이터셋 전체를 대표한다고 보기 어려워지고, 구해지는 평균과 분산도 매 iteration마다 들죽날죽하게 됩니다. 때문에 batch 크기가 작을때 BN을 사용하게 되면 batch가 클때에 비해 상당히 떨어지는 성능을 보여주게 됩니다. 이를 극복하기 위해 소개된 것이 group normalization (GN) 입니다.

### 2. Group normalization

![스크린샷 2018-04-11 오후 3.07.41.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-3-07-41.png?w=1400)
일단 저자는 batch 단위로 계산하는 것은 batch 크기에 영향을 받기 때문에 각각의 batch 단위로 normalize 시키는 부분을 없애고자 했습니다. 그와 관련해서 이전에도 비슷한 기술들이 있었는데, Layer normalization (LN) 과 Instance normalization(IN) 와 같은 기술들 입니다. 일단 위 그림을 보면 BN, LN, IN, GN이 어떤 기술들인지 한눈에 볼 수 있는데, 그림에서 표시된바와 같이 LN 은 각 채널과 영상전체를 모두 normalize 시켜주는 기술이고 IN의 경우에는 각 채널 단위로 normalize 시켜주는 기술입니다. LN과 IN은 batch의 크기에 독립적으로 동작할 수 있고, 특정 모델들에 대해서는 상당히 잘 동작하는 기술이지만 visual recognition 분야에서는  좋은 성능을 보장하지 못했고, 실험 결과를 통해 보면 GN인 BN에 비해  상당히 뒤쳐지는 성능을 보여줍니다. GN의 경우에는 LN과 IN의 절충된 형태로 볼 수 있는데, 각 채널을 N개의 group으로 나누어 normalize 시켜주는 기술입니다. 이러한 접근을 하게된 이유는 기존의 영상처리 기법들에서 영감을 얻었다고 하는데, 기존의 HOG나 SIFT와 같은 기술들의 경우 영상의 특징들을 몇 가지 그룹으로 나누어서 처리하는 방식을 취하고 있습니다. 이것에 착안해 각각의 채널들도 몇 개의 그룹으로 묶어서 처리하면 좀 더 기존의 영상처리 기법과 유사한 방식으로 네트워크가 동작하도록 강제할 수 있지 않을까 하여 이러한 방식을 고안했다고 합니다. 수식으로는 어떻게 표현 하였는지 살펴보도록 하겠습니다. 워낙 간단한 방법이라서 만약 위 설명 만으로도 이해가 충분히 되셨다면 수식은 살펴보지 않아도 무방할것 같습니다.
![스크린샷 2018-04-11 오후 3.45.04.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-3-45-04.png?w=452&h=171)
BN, LN, IN, GN 모두 마찬가지로 normalize 되어있는 결과에 학습가능한 scale, shift 파라미터를 적용합니다. 수식으로 표현하면 위와 같습니다. GN 이 그룹을 어떻게 나누는지의 수식은 아래와 같습니다.
![스크린샷 2018-04-11 오후 3.49.03.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-3-49-03.png?w=452&h=344)
이때 G=1이면 LN과 동일하게 되고 G=C 이면 IN과 동일해집니다. 이제 바로 결과를 살펴보도록 하겠습니다.

### 3. Experiments

##### 3.1 Imagenet Classification

일단 Imagenet에 적용한 결과를 살펴보겠습니다. 사용된 모델은 ResNet-50 입니다.![스크린샷 2018-04-11 오후 3.54.43.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-3-54-431.png?w=1400)일단 BN, LN, IN, GN을 비교했는데, batch 크기가 32일때 BN 보다는 못하지만 GN이 IN이나 LN보다 뛰어난 성능을 보여줌을 확인할 수 있습니다.
![스크린샷 2018-04-11 오후 3.59.26.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-3-59-26.png?w=1400)batch 크기에 따른 BN과 GN의 결과도 비교했는데, BN의 경우 batch 크기가 줄어듦에 따라 성능하락이 두드러졌지만 GN은 영향을 받지 않는것을 확인할 수 있습니다.

그렇다면 그룹은 몇 개의 그룹으로 나누는것이 좋을까요.
![스크린샷 2018-04-11 오후 7.36.58.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-7-36-58.png?w=365&h=241)당연하겠지만 어떤 수로 나누는 것이 가장 좋을지는 매번 실험해 봐야만 알 수 있을것 같습니다. 하지만 대강 적정한 그룹 수를 찾아서 사용하기만 해도 LN이나 IN보다 뛰어난 성능을 보여줌을 위 실험 결과를 통해서 확인 할 수 있습니다.

##### 3.2 Object Detection and Segmentation in COCO

이제 COCO 데이터셋을 이용해서 Object detection을 수행한 결과를 살펴보도록 하겠습니다. 여기서는 Mask R-CNN을 이용해서 실험했습니다. Mask R-CNN의 경우 워낙에 큰 네트워크를 사용하기도 하고 학습시키는 영상의 크기가 큰 경우가 많아 GPU 1장당 영상을 1장만 올릴 수 있는 경우들이 많습니다. 즉 BN에서 활용할수 있는 batch의 크기가 1이라는 뜻입니다. 이 때문에 Mask R-CNN을 학습시킬때는 대부분 BN의 ![\mu](https://s0.wp.com/latex.php?latex=%5Cmu&bg=ffffff&fg=000000&s=0) 와 ![\sigma](https://s0.wp.com/latex.php?latex=%5Csigma&bg=ffffff&fg=000000&s=0) 를 업데이트 시키지 않습니다. 대신 Imagenet으로 pretrained 되어있는 네트워크를 불러올때 이미 학습되어있는 ![\mu](https://s0.wp.com/latex.php?latex=%5Cmu&bg=ffffff&fg=000000&s=0) 와 ![\sigma](https://s0.wp.com/latex.php?latex=%5Csigma&bg=ffffff&fg=000000&s=0) 값을 고정시켜둔체 학습 시킵니다.  어쩔수 없이 이러한 방식으로 학습시키기는 하지만 찝찝함이 남을 수 밖에 없습니다. 분명히 Imagenet dataset과 COCO dataset을 서로 다른 특성을 가진 데이터셋일 것이기 때문입니다. 더 나아가 생각해보면, 영상 중에 X-ray나 안저영상과 같은 것들에 Mask R-CNN을 적용한다 하면, 이들 영상은 COCO 보다도 훨씬 더 다른 영상 특성을 갖기 때문에 그 찝찝함은 더 커집니다. 하지만 GN을 활용하면 이러한 찝찝함을 없앨 수 있을 것 같습니다. GN은 batch크기에 상관없이 동일하게 동작하므로 ![\gamma](https://s0.wp.com/latex.php?latex=%5Cgamma&bg=ffffff&fg=000000&s=0) 와 ![\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=000000&s=0) 를 고정시킬 필요가 없기 때문입니다.![스크린샷 2018-04-11 오후 8.01.28.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-8-01-28.png?w=473)위 결과를 보면 BN을 고정시켜둔 결과와 GN을 BN 대신에 사용한 결과를 볼 수 있는데, 모든 경우에 GN을 사용한 경우에 더 좋은 성능을 보여주는 것을 확인 할 수 있습니다.

##### 3.3 Video Classification in Kinetics

Kinetics dataset에서 비디오 분류를 수행한 결과도 확인할 수 있습니다. 일반적으로 비디오 데이터는 2D에 시간축을 더해 3D 영상의 형태를 갖는데, 2D 문제에 비해 훨씬더 많은 메로리를 사용하기 때문에, 더 작은 batch로 학습 시키게 됩니다. 결과를 보면 이 경우에도 GN이 도움이 되는 것을 확인 할 수 있습니다. 실험에는 이전에 Non-local neural network 관련 포스트에서 소개된 적 있었던 I3D 모델을 사용했습니다.![스크린샷 2018-04-11 오후 8.06.26.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-8-06-26.png?w=1400)![스크린샷 2018-04-11 오후 8.06.33.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-8-06-33.png?w=508&h=177)

### 4. Discussion

이전에 Batch renormalization (BR) 이라는 논문에 소개된적이 있었습니다. Batch normalization의 약점을 극복하고 batch의 크기가 작은 상황에서도 효과적으로 동작하는 BN을 제안한 것이었습니다. 이는 GN이 추구하는바와 같기 때문에 BR을 알고 있는 사람이라면 자연스레 GN과 BR 중에 어느 것이 더 뛰어난지 알고 싶을 것입니다. 이번 논문에서도 아주 상세히 다루지는 않았지만 GN과 BR의 성능을 비교했습니다. 그 결과를 보면 아래와 같이 기술되어 있습니다. ![스크린샷 2018-04-11 오후 8.18.29.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-8-18-292.png?w=422&h=124)![스크린샷 2018-04-11 오후 8.18.34.png](https://bloglunit.files.wordpress.com/2018/04/ec8aa4ed81aceba6b0ec83b7-2018-04-11-ec98a4ed9b84-8-18-341.png?w=422&h=61)여기서는 GN이 BR보다 더 뛰어난 성능을 보여줌을 확인 할 수 있습니다. 하지만 GN이나 BR 모두  조정해야 파라미터가 다양하기 때문에 상황에 따라서 어느 쪽이 더 좋을지는 그때그때 차이가 크지 않을까 생각해봅니다.

이번 논문에서는 GN를 영상인식 분야에만 적용하여 실험해 보았지만, 이전에 LN이나 IN이 recurrent network (RNN/LSTM)이나 GAN과 같은 분야에서 좋은 성능을 보여주었기 때문에 GN을 이러한 곳에도 적용했을때도 좋은 성능을 보여주지 않을까 기대됩니다. 논문의 저자는 후에 GN을 다른 분야에도 적용해서 실험해 볼 계획이라니 후속 연구가 기대됩니다.

### 5. Conclusion

Batch의 크기가 작은 상황에서 기존의 BN 보다 더 좋은 성능을 보여주는 GN을 소개드렸습니다. 실제로 딥러닝을 이용하여 제품을 개발하다 보면 영상도 크고 네트워크도 커서 batch의 크기가 작을 수 밖에 없는 상황이 종종 있는데, 이러한 상황에서 성능도 보장해 줄수 있고 심지어 구현도 정말 간편한 GN이 앞으로 많이 사용되지 않을까 예측해봅니다. 논문에는 이 포스트에 담지 못한 좀더 세세한 사항들이 있으니 관심있으신 분들은 한 번 읽어보시는것을 추천 드립니다. 논문 내용이 간단한 편이라서 포스트를 보신 후에는 한 번 슥 훑어만 보셔도 도움이 많이 되실 것 같습니다 (참고로 Tensorflow 에서의 구현 코드도 논문에 있습니다). 이상으로 이번 포스트를 마치도록 하겠습니다.