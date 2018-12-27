# [nnU-Net: Self-adapting Framework for U-Net-Based Medical Image Segmentation](http://openresearch.ai/t/nnu-net-self-adapting-framework-for-u-net-based-medical-image-segmentation/408)



# Essence

- [https://arxiv.org/abs/1809.10486 5](https://arxiv.org/abs/1809.10486)
- Fabian Isensee @ DKFZ(Division of Medical Image Computing, German Cancer Research Center)
- Medical Decathlon 2018 1st Place : [http://medicaldecathlon.com 2](http://medicaldecathlon.com/)

# Contribution

- UNet 기반으로 네트워크에 큰 변화는 주지 않았지만, 새로운 데이터에 대해서도 좋은 성능을 보여줄 수 있도록 Pipeline 설계를 잘 했음.
- 메디컬 이미지에 대한 경험을 바탕이 잘 녹아있는 Practical한 내용.

# Key Ideas

[Medical Decathlon 2](http://medicaldecathlon.com/)에 UNet을 적용한 방식을 소개합니다. Medical Decathlon은 서로 다른 10개의 Medical 3D Segmentation 문제를 하나의 트레이닝 파이프라인으로 풀도록 요구하는 Task입니다.

논문에서 제시한 모델이 UNet에서 변경된 것은 ReLU->Leaky ReLU 와 Batch Normalization -> Instance Normalization 가 주된 변화이며, **주로 트레이닝 파이프라인 설계가 핵심이라고 합니다.**

### Models

3가지 종류의 모델을 트레이닝, 서로 조합한 앙상블 결과까지 본 후 가장 Validation 성능이 좋은 것을 사용합니다.

#### (1) 2D U-Net

3D Image의 Slice 들에 대해서 2D Segmentation UNet을 각각 적용해 합친다는 건데요. anisotropic*한 데이터셋에 대해서는 2D Segmentation이 더 좋은 결과가 있다고 합니다.

asisotropic* : 3D 이미지에서 한 축으로는 이미지가 continuous하지만, 다른 축에서는 그렇지 않은 경우를 말하는 것 같습니다. 3D 이미지 취득 시 2D 이미지 데이터를 듬성듬성 취득해 결합한 경우 등에서 그럴 것 같습니다. (자세히 아시는 분 있으면 댓글로…)

#### (2) 3D U-Net

알려진 3D U-Net을 Patch-based로 적용하였습니다. 다만 이미지가 너무 큰 경우에는 Patch가 Global Context(주변 이미지 정보)를 많이 잃어버리게 되므로, (3)의 Cascaded 3D Unet을 적용했다고 합니다. 대략 데이터셋의 Median Size가 네트워크의 Input보다 4배 이상 크면 Cascaded 버전을 고려했다고 합니다.

#### (3) Cascaded 3D U-Net



![image](http://openresearch.ai/uploads/default/original/1X/a06cb102f736265d4ed2f52c2da48f46bce86eba.png)

언급된 것처럼 Large Image에 대해 적용합니다.

- Stage 1 : Downsample된 3D 이미지에 대해 적용됩니다. 마찬가지로 Patch-based입니다.
- Stage 2 : Stage1 에서 얻은 Output Label(one-hot encoded)을 3D 이미지에 Concat한 후, 기존의 Patch-based 3D Unet을 적용합니다.

### Preprocessing

이미지 사이즈가 모두 다르므로, GPU 메모리에 맞게 리사이즈 조절하는 휴리스틱 과정이 있습니다.

- GPU 메모리 수준을 미리 알고 있는 상태
- 2D의 경우 256x256 Image, 42 Batch에서 가장 높은 레이어에서 30개 Feature Map을 갖는 네트워크일 때 문제 없는 수준
- 3D의 경우 128x128x128 Voxel, 2 Batch에서 3D Unet에서 가장 높은 레이어에서 30개 Feature Map을 갖는 네트워크 일 때 문제 없는 수준
- 위 수준을 고려해서 데이터셋의 Median Size에 맞추도록 하되, 3D의 경우 1283 크기는 넘지 않는 Input을 갖도록 했다고 함
- Network는 Axis별로 Pooling을 진행하며, 각 축이 8보다 작아질 때까지 Pooling을 진행. 최대 5번의 Pooling.



![image](http://openresearch.ai/uploads/default/optimized/1X/cce943f09f086a486318b2b5dd3b97dc884dacc4_1_610x500.png)

**Cropping** : Non-zero 영역만 사용한다고 합니다.
**Resampling** : 메타데이터에 Voxel Spacing 정보가 있습니다. 이미지 pixel 간의 간격이 실제로 physical space에서 어느정도의 거리인지를 나타내주는 정보입니다. 이를 이용하면 모든 데이터의 voxel space를 homogenous하게 만들 수 있습니다. 이미지는 Spline Interpolation을 사용하고, Segmentation Label 은 Nearest Neighbor Interpolation을 사용했다고 합니다.
**Normalization** : 기본적으로 z score normalization을 합니다. 다만 메타데이터에 **CT라고 명시된 경우**에는 0.05-0.95 percetile의 데이터는 clipping을 해버린 후, z score normalization을 한다고 합니다.

### Loss



![image](http://openresearch.ai/uploads/default/original/1X/14b25a59dd36fc203bc1faa5d4e143937641ba28.jpg)



Dice 와 Cross Entropy를 조합해서 사용했다고 합니다.



![image](http://openresearch.ai/uploads/default/original/1X/ba303db56af304f1ee89a3a8f874638d6edd080e.jpg)



참고로 Dice Loss는 위와 같이 Dice Score의 변종입니다.

### Augmentation

Random Rotation, Random Scaling, Random Elastic Deformations, Gamma Correction, Mirroring 등을 사용했다고 합니다. Anisotropic 한 데이터에 대해서는 2D Image Augmentation을 적용했다고 합니다.

2nd Stage UNet에는 이전 Stage에서 넘어온 레이블 데이터에 의해 Co-adaption(레이블만 보는 경향이 짙어지는) 현상을 줄이기 위해서 random morphological operation을 추가하고, 세그먼테이션 결과를 일부 지우는 등의 처리를 했다고 합니다.

### Training & Inference

Cross-validation을 통해 5개의 네트워크를 학습한 것을 앙상블했다고 합니다. Test time augmentation을 통해 최대 64개의 prediction을 조합했다고 합니다. 패치를 결합할 때에는 패치의 중심에 더 많은 weight가 가도록 설계했다고 합니다.

### Postprocessing

주어진 데이터셋의 Label이 항상 연결된 상태인지는 체크해보고, 그렇다고 하면, 테스트했을 때 가장 큰 Label만 남기는 형태로 처리했다고 합니다.

# Results

![image](http://openresearch.ai/uploads/default/original/1X/1d0e25271b330ad8f4aab5d1574d89946b399fc4.png)