## [[Review\] 3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation](http://cdm98.tistory.com/35)

2018.11.16 00:03

![img](https://t1.daumcdn.net/cfile/tistory/9952F04B5BED89B806)



2016.06.21에 발표된 **3D U-Net**에 대해서 정리하도록 하겠습니다.



3D U-Net은 기존의 **2D U-Net**에 착안하여 만든 모델입니다.

Input, Convolution, Pooling, Upsampling 과정이 모두 2D였던 기존의 U-Net을

3D로 대체할 뿐만 아니라 Batch Normalization과 같은 기법을 이용해 더욱 성능을 향상시켰습니다.







**Abstract**



\- 이 논문에서는 띄엄띄엄 레이블링된 입체 이미지(sparsely annotated volumetric images)로부터 학습하는 3D segmentation 모델을 제시합니다. 여기서 띄엄띄엄 레이블링된 입체 이미지가 강조된 것은 segmentation task의 ground truth는 매우 만들기 어렵고 원하는 데이터를 얻기 어려우므로 비교적 적은 수의 데이터만 가지고 학습할 수 있기 때문입니다.



\- 이전에 제시된 u-net에서 2D 연산을 3D로 확장시킨 네트워크입니다.



\- 학습 과정에서 효율적인 data augmentation을 위해 elastic deformation을 가합니다.



\- End-to-end로 학습될 뿐만 아니라 pre-trained network이 요구되지 않습니다.





**1. Introduction**



\- 의학 데이터 분석에서 3D 데이터(volumetric data)는 많이 존재합니다. 하지만 이러한 데이터를 annotate하는 것은 매우 어려운 일입니다. 왜냐하면 컴퓨터 화면에서는 오직 2D 단면만 시각화할 수 있기 때문입니다.

  또한 이웃하는 단면들은 서로 거의 동일한 정보를 갖고 있기 때문에 이를 하나하나 annotation하는 것은 매우 비효율적입니다. 즉, 3D 데이터의 전체 단면에 대해서 annotate하는 것은 매우 효율적인 방법이 아니며 크고 질 좋은 데이터셋을 만드는 것이 어렵습니다.



\- 이 논문에서는 3D 데이터의 전체 단면이 아닌 일부 단면에 대해서만 annotate된 데이터를 필요로 하는 네트워크를 제시합니다. 3D U-Net은 아래의 그림과 같은 두 가지 방법으로 사용될 수 있습니다.



![img](https://t1.daumcdn.net/cfile/tistory/99215A4A5BEDAE0901)

  (a) Semi-automated segmentation : 사용자가 segment될 각각의 volume의 몇 개의 단면만 annotate합니다. 그리고 네트워크는 dense segmentation을 예측합니다. 즉, sparsely annotated slices로 부터 dense annotated slices를 예측하도록 학습합니다.



  (b) Fully-automated segmentation : 네트워크는 representative training set의 annotated 단면으로 학습을 하고 non-annotated volumes을 예측할 수 있습니다. 이는 흔히 이루어지는 segmentation task라고 생각하시면 될 것 같습니다. [Fully-annotated volumes로 학습한 후, non-annotated volumes을 예측]





\- 3D U-Net은 3D volumes을 인풋으로 받으며 3D convolutions, 3D max pooling, 그리고 3D up-convolutional layers와 같은 3D 연산을 합니다. 또한 Max pooling 이전에 channel의 수를 2배로 늘려줌으로써 bottlenecks을 해결했으며 batch normalization을 사용했습니다.



\- 가중 손실 함수 (weighted loss function)과 특별한 방법의 data augmentation을 통해 작은 수의 annotated 단면만으로도 모델을 학습할 수 있도록 합니다.



\- **Xenopus kidney** 데이터셋에 대해 좋은 성능을 보입니다. 









**2. Network Architecture**



![img](https://t1.daumcdn.net/cfile/tistory/99C09C4E5BEDB0B402)

\- 기존의 U-Net과 큰 차이는 없기 때문에 간단하게 중요한 점만 정리하고 넘어가도록 하겠습니다.

  1) Max pooling 전에 channel의 수를 2배로 늘려 bottleneck를 해결했습니다.

  2) **Batch normalization**("BN")을 사용했습니다.

  3) Sparse annotation에 대해서도 학습할 수 있도록 가중 소프트맥스 손실 함수(**weighted softmax loss function**)을 사용합니다. [Weighted loss function에 관한 자세한 내용은 **이 글**을 참고하시길 바랍니다.]



\- Input image의 shape은 3 channels의 132 x 132 x 116이고 output의 shape은 44 x 44 x 28입니다. 그리고 voxel size는 1.76 x 1.76 x 2.04 μm3입니다.

  Input image가 3D Scan image의 크기보다 작은 이유는 이미지를 한번에 모델에 넣어주는 것이 아니라 patch 단위로 넣어주기 때문입니다.





**3. Implementation Details**

 \- Data augmentation에 회전(rotation), scaling, 그리고 gray value augmentation 뿐만 아니라 smooth dense deformation도 추가하였습니다.

 \- Weighted cross-entropy loss에서 background에 대한 가중치(weights)는 상대적으로 줄이고 segment하고자 하는 대상에 대한 가중치는 높여서 class imbalance를 해결했습니다.

   [논문에는 기술되어 있지 않지만 주로 positive patch와 negative patch의 비율을 1:3으로 구성하여 학습합니다.]

 \- Optimizer로는 Stochastic Gradient Descent (SGD)를 사용했습니다.

 \- NVIDIA TitanX GPU를 통한 70000 training iterations에 3일이 소요되었습니다.









**4. Experiments**





![img](https://t1.daumcdn.net/cfile/tistory/99F67E4D5BEDB27503)

**Table 1:** 2D보다 3D를 사용하는 것이, 그리고 Batch Normalization을 사용하는 것이 더욱 좋은 결과를 보입니다.

**Table 2:** Semi-automated 학습에 사용되는 단면(slices)의 개수가 많을수록 더 좋은 성능을 보입니다.





![img](https://t1.daumcdn.net/cfile/tistory/99EF9D4D5BEDB27504)

**Table 3**: Fully-automated segmentation에서도 2D보다는 3D를 사용하는 것이, 그리고 BN을 사용하는 것이 더 좋은 성능을 보입니다.





\5. Conclusion

 

\- 3D U-Net은 2D input을 받고 2D 연산을 하였던 기존의 U-Net을 확장시켜 3D 데이터를 다룰 수 있을 뿐만 아니라 이를 통해 성능을 향상시켰습니다. 이 논문을 이후로 의료 데이터에서는 주로 2D 단면을 통해 학습하기보다는 3D patch를 통해 학습합니다.





\6. Implementation with Keras





```python
from keras.layers import Input, Conv3D, MaxPooling3D, concatenate, Conv3DTranspose, Dropout, ReLU,
                         Cropping3D, Dropout
from keras.models import Model
from keras.optimizers import Adam
from keras import regularizers 
from keras.layers.normalization import BatchNormalization as bn
from keras.utils.training_utils import multi_gpu_model


def conv_3d(input_tensor, n_filters, kernel_size = (3, 3, 3), strides = (1, 1, 1),
            activation = "relu", padding = "valid", batch_norm = True, dropout = True):
  '''
  Convolution Block with Batch Normalization, ReLU, and Dropout
  '''
  conv = Conv3D(n_filters, kernel_size, padding = padding, strides = strides)(input_tensor)
  
  if batch_norm:
    conv = bn()(conv)
    
  if activation.lower() == "relu":
    conv = ReLU()(conv)
  
  if dropout:
    conv = Dropout(0.3)(conv)
    
  return conv




def upconv_and_concat(tensor_to_upconv, tensor_to_concat, upconv_n_filters, 
                      kernel_size = (2, 2, 2), strides = (2, 2, 2), padding = "valid"):
  '''
  Upsampling, cropping and concatenation given two tensor.
  '''
  
  upconv = Conv3DTranspose(upconv_n_filters, kernel_size, strides = strides,
                           padding = padding)(tensor_to_upconv)
  
  crop_size = (int(tensor_to_concat.shape[1]) - int(tensor_to_upconv.shape[1])*2) // 2
  cropped = Cropping3D((crop_size, crop_size, crop_size))(tensor_to_concat)
  concat = concatenate([upconv, cropped], axis = 4)
  
  return concat




def unet_3d(input_shape, n_classes, loss, metrics, n_gpus = 1, optimizer = "adam", 
            lr = 0.0001, batch_norm = True, activation = "relu", pool_size = (2, 2, 2)):
  
  # Encoder
  input = Input(input_shape)
  conv1_1 = conv_3d(input, 32, batch_norm = batch_norm, activation = activation)
  conv1_2 = conv_3d(conv1_1, 32, batch_norm = batch_norm, activation = activation)
  pool_1 = MaxPooling3D(pool_size)(conv1_2)
  


  conv2_1 = conv_3d(pool_1, 64, batch_norm = batch_norm, activation = activation)
  conv2_2 = conv_3d(conv2_1, 64, batch_norm = batch_norm, activation = activation)
  pool_2 = MaxPooling3D(pool_size)(conv2_2)
  
  conv3_1 = conv_3d(pool_2, 128, batch_norm = batch_norm, activation = activation)
  conv3_2 = conv_3d(conv3_1, 128, batch_norm = batch_norm, activation = activation)
  pool_3 = MaxPooling3D(pool_size)(conv3_2)
  
  conv4_1 = conv_3d(pool_3, 256, batch_norm = batch_norm, activation = activation)
  conv4_2 = conv_3d(conv4_1, 128, batch_norm = batch_norm, activation = activation)
  
  
  # Decoder
  upconv_5 = upconv_and_concat(conv4_2, conv3_2, 128)
  conv5_1 = conv_3d(upconv_5, 128, batch_norm = batch_norm, activation = activation)
  conv5_2 = conv_3d(conv5_1, 64, batch_norm = batch_norm, activation = activation)
  
  upconv_6 = upconv_and_concat(conv5_2, conv2_2, 64)
  conv6_1 = conv_3d(upconv_6, 64, batch_norm = batch_norm, activation = activation)
  conv6_2 = conv_3d(conv6_1, 32, batch_norm = batch_norm, activation = activation)
  
  upconv_7 = upconv_and_concat(conv6_2, conv1_2, 32)
  conv7_1 = conv_3d(upconv_7, 32, batch_norm = batch_norm, activation = activation)
  conv7_2 = conv_3d(conv7_1, 32, batch_norm = batch_norm, activation = activation)
  
  final_conv = Conv3D(n_classes, kernel_size = (1, 1, 1), padding = "same")(conv7_2)
  
  
  model = Model(input, final_conv)
  
  
  # Multi GPU
  if n_gpus > 1:
    model = multi_gpu_model(model, gpus = n_gpus)
    
  # Compile  
  if optimizer == "adam":
    adam = Adam(lr = lr)
    
    model.compile(optimizer = adam, loss = loss, metrics = metrics)
  
  else:
    model.compile(optimizer = optimizer, loss = loss, metrics = metrics)
  
  return model
```