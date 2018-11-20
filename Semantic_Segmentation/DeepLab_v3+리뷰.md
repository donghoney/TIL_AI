# DeepLab V3+: Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation

## Semantic Segmentation

![semantic_segmentation_ex](https://bloglunit.files.wordpress.com/2018/07/semantic_segmentation_ex1.png?w=646&h=263)입력 영상으로부터 semantic segmentation을 수행한 예시. [출처](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/)

이미지 분석 task 중 semantic segmentation은 중요한 방법 중 하나입니다. Semantic segmentation은 입력 영상에 주어진 각각의 픽셀에 대해서 class label을 할당하는 것을 목표로 합니다. 주로 의료영상 분석, 자율주행 등 다양한 분야에 활용될 수 있습니다.

![voc2012.png](https://bloglunit.files.wordpress.com/2018/07/voc2012.png?w=650&h=237)Pascal VOC 2012 leaderboard 결과. [출처](http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?challengeid=11&compid=6)

Semantic segmentation을 해결 하기 위한 방법론은 여러가지가 존재합니다. 이러한 여러 알고리즘들을 정해진 데이터와 지표를 기준으로 성능을 비교해 볼 수 있는데, 여러 벤치마크 중 PASCAL VOC 2012 데이터셋이 대표적으로 자주 활용되고 있습니다. 위 leaderboard 결과를 보면 DeepLab 이라 불리우는 알고리즘들이 상위권에 많이 포진해 있음을 볼 수 있습니다. 본 포스트에서는 그중에서도 *가장 높은 성능*을 보이고 있는 **DeepLab V3+**에 대해 살펴보려고 합니다.

## DeepLab

DeepLab 이라 불리는 semantic segmentation 방법은 version 1부터 시작하여 지금까지 총 4번의 개정본(1, 2, 3, 3+)이 출판되었습니다.

- DeepLab V1
  Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs. ICLR 2015.
- DeepLab V2
  DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs. TPAMI 2017.
- DeepLab V3
  Rethinking Atrous Convolution for Semantic Image Segmentation. arXiv 2017.
- DeepLab V3+
  Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation. arXiv 2018.

전체적으로 DeepLab은 semantic segmentaion을 잘 해결하기 위한 방법으로 atrous convolution을 적극적으로 활용할 것을 제안하고 있습니다. V1에서는 atrous convolution을 적용해 보았고, V2에서는 multi-scale context를 적용하기 위한 Atrous Spatial Pyramid Pooling (ASPP) 기법을 제안하고, V3에서는 기존 [ResNet](https://arxiv.org/abs/1512.03385) 구조에 atrous convolution을 활용해 좀 더 dense한 feature map을 얻는 방법을 제안하였습니다. 그리고 최근 발표된 V3+에서는 separable convolution과 atrous convolution을 결합한 atrous separable convolution의 활용을 제안하고 있습니다. 각각에 대해서는 아래에서 좀 더 자세하게 설명드리겠습니다.

 

## Related Work

### Atrous Convolution

![atrous.png](https://bloglunit.files.wordpress.com/2018/07/atrous.png?w=644&h=308)Atrous convolution 예시. [출처](http://www.mdpi.com/2072-4292/9/5/498/htm)

Atrous convolution은 기존 convolution과 다르게, 필터 내부에 빈 공간을 둔 채로 작동하게 됩니다. 위 예시에서, 얼마나 빈 공간을 둘 지 결정하는 파라미터인 rate *r*=1일 경우, 기존 convolution과 동일하고, *r*이 커질 수록, 빈 공간이 넓어지게 됩니다.

Atrous convolution을 활용함으로써 얻을 수 있는 이점은, 기존 convolution과 동일한 양의 파라미터와 계산량을 유지하면서도, field of view (한 픽셀이 볼 수 있는 영역) 를 크게 가져갈 수 있게 됩니다. 보통 semantic segmentation에서 높은 성능을 내기 위해서는 convolutional neural network의 마지막에 존재하는 한 픽셀이 입력값에서 어느 크기의 영역을 커버할 수 있는지를 결정하는 receptive field 크기가 중요하게 작용합니다. Atrous convolution을 활용하면 파라미터 수를 늘리지 않으면서도 receptive field를 크게 키울 수 있기 때문에 DeepLab series에서는 이를 적극적으로 활용하려 노력합니다.

### Spatial Pyramid Pooling

 

![aspp](https://bloglunit.files.wordpress.com/2018/07/aspp1.png?w=1400)Atrous spatial pyramid pooling (ASPP)

Semantic segmentaion의 성능을 높이기 위한 방법 중 하나로, spatial pyramid pooling 기법이 자주 활용되고 있는 추세입니다. DeepLab V2에서는 feature map으로부터 여러 개의 rate가 다른 atrous convolution을 병렬로 적용한 뒤, 이를 다시 합쳐주는 atrous spatial pyramid pooling (ASPP) 기법을 활용할 것을 제안하고 있습니다. 최근 발표된 [PSPNet](https://arxiv.org/abs/1612.01105)에서도 atrous convolution을 활용하진 않지만 이와 유사한 pyramid pooling 기법을 적극 활용하고 있습니다. 이러한 방법들은 multi-scale context를 모델 구조로 구현하여 보다 정확한 semantic segmentation을 수행할 수 있도록 돕게 됩니다. DeepLab 에서는 ASPP를 기본 모듈로 사용하고 있습니다.

### Encoder-Decoder

![Image result for u-net](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/u-net-architecture.png)U-Net 구조

Encoder-decoder 구조 또한 semantic segmentation을 위한 CNN 구조로 자주 활용되고 있습니다. 특히, [U-Net](https://arxiv.org/abs/1505.04597)이라 불리는 encoder-decoder 구조는  정교한 픽셀 단위의 segmentation이 요구되는 biomedical image segmentation task의 핵심 요소로 자리잡고 있습니다. 왼쪽의 encoder 부분에서는 점진적으로 spatial dimension을 줄여가면서 고차원의 semantic 정보를 convolution filter가 추출해낼 수 있게 됩니다. 이후 오른쪽의 decoder 부분에서는 encoder에서 spatial dimension 축소로 인해 손실된 spatial 정보를 점진적으로 복원하여 보다 정교한 boundary segmentation을 완성하게 됩니다.

U-Net이 여타 encoder-decoder 구조와 다른 점은, 위 그림에서 가운데 놓인 회색 선입니다. Spatial 정보를 복원하는 과정에서 이전 encoder feature map 중 동일한 크기를 지닌 feature map을 가져 와 prior로 활용함으로써 더 정확한 boundary segmentation이 가능하게 만듭니다.

이번에 발표된 DeepLab V3+에서는 U-Net과 유사하게 intermediate connection을 가지는 encoder-decoder 구조를 적용하여 보다 정교한 object boundary를 예측할 수 있게 됩니다.

### Depthwise Separable Convolution

![conv](https://bloglunit.files.wordpress.com/2018/07/conv.png?w=200&h=360)Convolution. [출처](https://eli.thegreenplace.net/2018/depthwise-separable-convolutions-for-machine-learning/)

입력 이미지가 8×8×3 (*H*×*W*×*C*) 이고, convolution filter 크기가 3×3 (*F*×*F*) 이라고 했을 때, filter 한 개가 가지는 파라미터 수는 3×3×3 (*F*×*F*×*C*) = 27 이 됩니다. 만약 filter가 4개 존재한다면, 해당 convolution의 총 파라미터 수는 3×3×3×4 (*F*×*F*×*C×N)* 만큼 지니게 됩니다.

![depth_conv](https://bloglunit.files.wordpress.com/2018/07/depth_conv.png?w=300&h=299)Depthwise convolution. [출처](https://eli.thegreenplace.net/2018/depthwise-separable-convolutions-for-machine-learning/)

Convolution 연산에서 channel 축을 filter가 한 번에 연산하는 대신에, 위 그림과 같이 입력 영상의 channel 축을 모두 분리시킨 뒤, channel 축 길이를 항상 1로 가지는 여러 개의 convolution 필터로 대체시킨 연산을 depthwise convolution이라고 합니다.

![depthwise_separable_conv](https://bloglunit.files.wordpress.com/2018/07/depthwise_separable_conv.png?w=300&h=435)Depthwise separable convolution. [출처](https://eli.thegreenplace.net/2018/depthwise-separable-convolutions-for-machine-learning/)

이제, 위의 depthwise convolution으로 나온 결과에 대해, 1×1×*C* 크기의 convolution filter를 적용한 것을 depthwise separable convolution 이라 합니다. 이처럼 복잡한 연산을 수행하는 이유는 기존 convolution과 유사한 성능을 보이면서도 사용되는 파라미터 수와 연산량을 획기적으로 줄일 수 있기 때문입니다.

예를 들어, 입력값이 8×8×3 이고 16개의 3×3 convolution 필터를 적용할 때 사용되는 파라미터의 개수는

- Convolution: 3×3×3×16 = 432
- Depthwise separable convolution: 3×3×3 + 3×16 = 27 + 48 = 75

임을 확인할 수 있습니다.

Depthwise separable convolution은 기존 convolution filter가 spatial dimension과 channel dimension을 동시에 처리하던 것을 따로 분리시켜 각각 처리한다고 볼 수 있습니다. 이 과정에서, 여러 개의 필터가 spatial dimension 처리에 필요한 파라미터를 하나로 공유함으로써 파라미터의 수를 더 줄일 수 있게 됩니다. 두 축을 분리시켜 연산을 수행하더라도 최종 결과값은 결국 두 가지 축 모두를 처리한 결과값을 얻을 수 있으므로, 기존 convolution filter가 수행하던 역할을 충분히 대체할 수 있게 됩니다.

픽셀 각각에 대해서 label을 예측해야 하는 semantic segmentation은 난이도가 높은 편에 속하기 때문에 CNN 구조가 깊어지고 receptive field를 넓히기 위해 더 많은 파라미터들을 사용하게 되는 상황에서, separable convolution을 잘 활용할 경우 모델에 필요한 parameter 수를 대폭 줄일 수 있게 되므로 보다 깊은 구조로 확장하여 성능 향상을 꾀하거나, 기존 대비 메모리 사용량 감소와 속도 향상을 기대할 수 있습니다.

### DeepLab V3

![deeplabv3.png](https://bloglunit.files.wordpress.com/2018/07/deeplabv3.png?w=1400)DeepLab V3 구조

DeepLab V3+ 바로 이전 논문인 DeepLab V3의 경우,

- Encoder: ResNet with atrous convolution
- ASPP
- Decoder: Bilinear upsampling

으로 이루어져 있습니다.

## DeepLab V3+

![deeplabv3plus](https://bloglunit.files.wordpress.com/2018/07/deeplabv3plus.png?w=1400)DeepLab V3+ 구조

이번에 소개드릴 DeepLab V3+는 제목에서도 알 수 있듯이 V3에 비해서 약간의 변화만이 존재합니다.

- Encoder: ResNet with atrous convolution → [Xception](https://arxiv.org/abs/1610.02357) (Inception with separable convolution)
- ASPP → ASSPP (Atrous Separable Spatial Pyramid Pooling)
- Decoder: Bilinear upsampling → Simplified U-Net style decoder

우선, ResNet을 사용하던 encoder가 앞서 소개드린 separable convolution을 적극 활용한 구조인 Xception으로 대체됩니다. Multi-scale context를 얻기 위해 활용되던 ASPP에는 separable convolution과 atrous convolution을 결합한 atrous separable convolution이 적용된 ASSPP로 대체되었습니다. 또한, 기존에 단순하게 bilinear upsampling으로 해결했던 decoder 부분이 U-Net과 유사한 형태의 decoder로 대체됩니다. Encoder와 ASPP, 그리고 decoder 모두 separable convolution을 적극 활용함으로써 파라미터 사용량 대비 성능 효율을 극대화시키려는 노력이 보이는 구조입니다.

![deeplabv3plus_detail.png](https://bloglunit.files.wordpress.com/2018/07/deeplabv3plus_detail.png?w=649&h=333)DeepLab V3+ 구조 디테일

 

## Experiment

![exp_table3.png](https://bloglunit.files.wordpress.com/2018/07/exp_table3.png?w=652&h=326)

다양한 파라미터와 세팅에 대해서 실험을 진행하였는데, 우선 ResNet-101 구조를 encoder로 사용하였을 때 성능을 측정하였습니다. Decoder 부분을 bilinear upsampling 대신, 단순화된 U-Net 구조로 변경할 경우 기존 대비 mIOU 1.64% 향상이 있음을 확인할 수 있습니다.

![exp_table5.png](https://bloglunit.files.wordpress.com/2018/07/exp_table5.png?w=1400)

이후 encoder을 Xception으로 교체하여 실험을 진행하였습니다. ResNet-101과 대비해 Xception 구조가 약 2% 가량의 성능 향상을 가져옴을 일단 확인할 수 있습니다. ASPP 부분과 decoder 부분에 사용되는 convolution 들을 모두 separable convolution으로 대체할 경우 (위 표의 SC 부분), 성능은 기존 convolution을 사용할 때와 거의 비슷하게 유지되는 반면, 모델이 사용하는 연산량(Multiply-Adds)이 획기적으로 줄어듦을 확인할 수 있습니다.

![result_vis.png](https://bloglunit.files.wordpress.com/2018/07/result_vis.png?w=649&h=488)Pascal VOC 2012 validation set에서의 visualization 결과

위 Visualization 결과를 보면 상당히 안정적이고 정확하게 각각의 픽셀에 대해 클래스를 예측하고 있음을 확인할 수 있습니다. Xception 기반의 encoder로 양질의 high level semantic 정보를 가지는 feature를 추출할 수 있고, ASPP 모듈을 통해 각 픽셀이 여러 스케일의 context 정보를 취해 보다 정확한 추론이 가능하며, U-Net 구조의 decoder를 통해 각 물체에 해당하는 정교한 boundary를 그려낼 수 있기에 위와 같은 visualization 결과를 얻어낼 수 있다고 해석해 볼 수 있습니다.

## Conclusion

DeepLab V3+ 논문의 경우 뛰어난 novelty가 존재하는 것은 아니지만, DeepLab V1부터 시작해 꾸준히 semantic segmentation 성능을 향상시키기 위한 방법론을 연구하는 단계의 최신선상에 놓인 논문이며, encoder, ASPP, decoder 각 모듈이 수행하는 역할이 명확하고 모듈화 되어 있어 모델의 확장성 또한 좋아 보입니다. 더욱이, 저자가 google에 속해 있어 tensorflow에서 공식적으로 제공하는 대표적인 semantic segmentation 방법으로 [소개](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html)되고 있으며, 그 코드 또한 깔끔하게 공식적으로 [공개](https://github.com/tensorflow/models/tree/master/research/deeplab)되어 있습니다. 다양한 데이터셋과 여러 encoder 구조로 학습해 둔 pre-trained model 또한 [공개](https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/model_zoo.md)되어 있으므로 semantic segmentation 모델을 구축하고 싶지만 어떤 방법론을 택해야 할지 고민되신다면 DeepLab V3+는 더할나위 없이 좋은 시발점이 될 것이라고 생각합니다.