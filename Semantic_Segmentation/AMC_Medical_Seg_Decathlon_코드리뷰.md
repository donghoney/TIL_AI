### 2018 MSD(Medical Segmentation Decathlon) 2위 Segmentation Keras 코드 



### 코드의 큰 틀

1. train.py
2. model.py
3. preprocess.py



## 1. train.py

1. Path선언 : Data 디렉토리 접근
2. Train_&_Validation Path list 선언
3. Preprocess 클래스에서 영역별(심장,간,폐 등등) HU 조절을 위한 Task작업과 rotation, zoom, width_shift, height_shift, depth_shift, horizontal_flip, fill_constant의 작업을 거쳐 Generate된 Image를 객체로 저장한다.
4. (None,None,None,data.num_channels)로 input_shape를 지정한다.
5. Model을 Load한다. 
6. Model을 compile한다. -> optimizer : Adam(lr = 1e-4) , loss : average_dice_coef, metrics : average_dice_coef
7. Train_file_path를 가진 train_cases(경로리스트)를 DataLoader의 매개변수로 file_path와 is_shuffle 변수를 가진 객체를 생성하고, 그 객체를 tensorpack.dataflow.common의 MapDataComponent 함수를 통해 GPU multiCore로 데이터 preprocess Task를 빠르게 실행하여 ds_train 프로세스 생성
8. gen() 함수를 사용하여**gen이란 함수안에서 return이 아닌 yield로 반환값을 지속적으로 함수 밖으로 내보내는 것을 의미한다.  

```python
from tensorpack.dataflow.common import MapDataComponent
from tensorpack.dataflow import PrefetchData

class DataLoader(RNGDataFlow):
    def __init__(self, file_paths, is_shuffle=True):
        self.file_paths = file_paths
        self.is_shuffle = is_shuffle

    def get_data(self):
        if self.is_shuffle == True:
            random.shuffle(self.file_paths)
        for file_path in self.file_paths:
            image_dummy = sitk.ReadImage(file_path)
            image = sitk.GetArrayFromImage(image_dummy).astype('float32')
            resize_factor = image_dummy.GetSpacing()[::-1]
            image = ndimage.zoom(image, resize_factor, order=0, mode='constant', cval=0.0)

            label_dummy = sitk.ReadImage(file_path.replace('imagesTr', 'labelsTr'))
            label = sitk.GetArrayFromImage(label_dummy).astype('float32')
            resize_factor = label_dummy.GetSpacing()[::-1]
            label = ndimage.zoom(label, resize_factor, order=0, mode='constant', cval=0.0)
            yield [image, label]

            
def gen_data(ds):
    while True:
        for d in ds.get_data():
            yield d
            
ds_train = DataLoader(train_cases, is_shuffle=True)
ds_train = MapDataComponent(ds_train, config_task.preprocess_img, index=0)
ds_train = PrefetchData(ds_train, 2, 1)
gen_train = gen_data(ds_train)
```

9. list에 checkpoint의 이름을 저장하고, CSVLogger를 저장한다.
10. model.fit_generator에 generator=gen_train(데이터 flow), step_per_epoch=len(train_cases:데이터길이), epochs=1000, validation=data=gen_valid,validation_steps=len(valid_cases),max_queue_size=1, workers=1, use_multiprocessing=False,callbacks=cbs(checkpoint와 CSVLogger가 담긴 리스트) 의 매개변수를 담아 학습한다.

*** 이 코드에는 patch_whole이라는 parameter가 있는데, 여기의 네트워크 모델 구조는 learn to learn 구조로 2 step Network를 이해하고 넘어가면 쉽다.

동일한 구조이지만, 앞의 네트워크는 roi model이 되며, 학습할 때, binary channel로 어디에 seg할 객체가 존재하는지를 학습한다. 뒤의 네트워크는 seg model이 되며, 최종 output을 내는 네트워크다.

whole은 전체에서 binary channel로 객체의 위치를 seg하기 위해, 데이터를 학습할 때, mask를 0~객체 개수의 채널을 np.sum(mask, axis=-1) -> np.expand_dims(mask, axis=-1)의 과정을 거쳐 0,1의 채널로 mask data를 만들고, 180x180x180보다 큰 사이즈의 데이터일 경우, image,mask를 resize하는 과정을 거쳐 데이터셋을 만든다. (최대사이즈 180x180x180)



반대로, patch의 경우에는 seg model이 되는 과정으로 데이터셋을 준비한다.

roi model이 제대로 roi를 한다는 가정하에, mask가 존재하는 부분만을 학습하도록 한다.

image와 mask 데이터는  객체가 존재하는 영역을 roi로 3차원 crop하고, 최소 사이즈는 28x28x28로 하며, 이미지외곽에서 객체 크기의 20%정도의 마진을 준다. (최소사이즈 28x28x28)

만약 3차원 patch image,mask가 24보다 작은 dimension이 존재할 경우, 24의 크기이상이 나올수 있도록 resize_patch 작업을 거친다(ndimage.zoom()) 이후 180보다 클 경우엔, resize_patch 작업을 거친다. 





## 2. model.py

모델은 코드를 첨부한다.

```python
#input_img의 shape는 (None,None,None,num_channels)
input_img = Input(shape=input_shape)
	#GaussianNoise를 입힌다.
    d0 = GaussianNoise(noise)(input_img)
    #일반 keras 내장함수 Conv3D를 사용하고 base filter=32 
    d1 = Conv3D(base_filter, (3, 3, 3), use_bias=False, padding='same')(d0)
    # keras_contrib.layer의 내장함수 InstanceNormalization을 이용해 값을 모아준다
    d1 = InstanceNormalization(axis=axis)(d1)
    # LeakyReLU 사용
    d1 = LeakyReLU(alpha=0.3)(d1)
    # 2배로 커지고
    d2 = conv3d(d1, base_filter*2, se_res_block=se_res_block)
    # 2배 커지고
    d3 = conv3d(d2, base_filter*4, se_res_block=se_res_block)
    
    d4 = conv3d(d3, base_filter*8, se_res_block=se_res_block)
    
    if depth_size == 4:
        d5 = conv3d(d4, base_filter*16, se_res_block=se_res_block)
        u4 = deconv3d(d5, d4, base_filter*8, se_res_block=se_res_block)
        u3 = deconv3d(u4, d3, base_filter*4, se_res_block=se_res_block)
    elif depth_size == 3:
        u3 = deconv3d(d4, d3, base_filter*4, se_res_block=se_res_block)
    else:
        raise Exception('depth size must be 3 or 4. you put ', depth_size)
    
    u2 = deconv3d(u3, d2, base_filter*2, se_res_block=se_res_block)
    u1 = ZeroPadding3D(((0, 1), (0, 1), (0, 1)))(u2)
    u1 = Conv3DTranspose(base_filter, (2, 2, 2), strides=(2, 2, 2), use_bias=False, padding='same')(u1)
    u1 = InstanceNormalization(axis=axis)(u1)
    u1 = LeakyReLU(alpha=0.3)(u1)
    u1 = CropToConcat3D()([u1, d1])
    u1 = Conv3D(base_filter, (3, 3, 3), use_bias=False, padding='same')(u1)
    u1 = InstanceNormalization(axis = axis)(u1)
    u1 = LeakyReLU(alpha=0.3)(u1)
    output_img = Conv3D(num_labels, kernel_size=1, strides=1, padding='same', activation='sigmoid')(u1)
    if last_relu == True:
        output_img = ThresholdedReLU(theta=0.5)(output_img)
    if roi_model == True:
        output_roi = Conv3D(1, kernel_size=1, strides=1, padding='same', activation='sigmoid')(d4)
        output_roi = ThresholdedReLU(theta=0.5)(output_roi)
        model_roi = Model(inputs=input_img, outputs=output_roi)
        model_seg = Model(inputs=input_img, outputs=output_img)
        return model_roi, model_seg
    else:
        model = Model(inputs=input_img, outputs=output_img)
        return model
```

