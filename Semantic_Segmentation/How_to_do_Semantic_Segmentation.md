## How to do Semantic Segmentation using Deep Learning 

출처 : https://medium.com/nanonets/how-to-do-image-segmentation-using-deep-learning-c673cc5862ef

### Sementic Segmentation이란?

Semantic segmentation은 거친 추세에서 좋은 추론으로 진행하는 자연스러운 단계이다.

1. 첫 단계는 전체 input에서 예측을 하는 분류로 지정될 수 있다.
2. 다음 단계는 localization / detection 인데, 클래스들 뿐만 아니라, 클래스 각각의 위치에 기반해서 추가적인 정보를 제공한다.
3. 마지막으로, semantic segmentation은 모든 픽셀에 대한 레이블을 추정하여 밀도가 높은 예측을함으로써 세밀한 추론을 달성하므로 각 픽셀은 그 객체를 둘러싸는 객체 영역의 클래스로 레이블링 된다.

![img](https://cdn-images-1.medium.com/max/2000/1*MQCvfEbbA44fiZk5GoDvhA.png)

컴퓨터 비전 분야에서 충분한 기여를 했던, deep network를 리뷰할만한 가치가 있다는 것을 보여주고,

그 networks들은 Semantic segmentation 시스템의 기반이 된다.

아래와 같다.

* AlexNet : 2012 ImageNet Competition에서 84.6%의 정확도로 우승했던 CNN 모델이다. 5개의 convolutional layers와 max-pooling 1개, ReLU로 non-linearities를 표현했고, 3개의 fully-convolutional layer를 가지고 있고, dropout을 사용했다.
* VGG-16 : 이건 옥스포드에서 만든건데, 2013년 ImageNet Competition에서 92.7%의 정확도로 우승했다. 이건 첫번째 레이어에 큰 수용 field들을 가진 적은 레이어대신에, 작은 수용하는 field들을 가진 convolution layer stack을 사용한다. 
* GoogLeNet : 구글 네트워크, 2014년 ImageNet Competition에서 93.3%의 정확도로 우승했던 모델이고, 22개의 레이어를 갖고 있고, 새롭게 inception module을 도입했다. 
* ResNet : 이것은 마이크로 소프트 에서 만들었고, 2016년도 ImageNet Competition에서 96.4%의 정확도로 우승했다. 152개의 layer로 잘 알려져 있고, residual block을 도입했다. Residual blocks는 엄청 깊은 구조에서 학습이 잘 안되는 문제를 레이어들을 다음 레이어의 input으로 붙여넣는 skip connection으로 해결하는 구조이다.

![img](https://cdn-images-1.medium.com/max/1600/1*7UXzOt97gQAmCCOL58hgAw.png)



### 기존 Semantic Segmentation 접근 방법은 뭘까?

일반적인 semantic segmentation 아키텍처는 광범위하게 encoder와 decoder로 이루어진 network로 생각될 수 있다.

* encoder는 보통 VGG/ResNet 같은 pre-trained된 classification 네트워크들이고 decoder가 뒤따른다.
* decoder의 임무는 의미있는 분류를 얻기 위해 encoder에 의해 학습 된 차별적인 특징 (낮은 해상도)을 픽셀 공간 (더 높은 해상도)에 의미적으로 투사하는 것이다.



### 1 - Region-Based Semantic Segmentation

Region-Based method들은 일반적으로 인식을 사용한 segmentation pipline을 따른다. 이 파이프라인은 이미지에서 자유 형식 영역을 추출하고 설명 한 다음 영역 기반 분류를 수행한다.

테스트할 때, 그 영역 기반의 예측은 픽셀 예측으로 변형된다, 가장 높은 스코어를 가진 지역에 포함된 픽셀에 labeling하는 방식이다.

#### R-CNN(Regions with CNN feature)

![img](https://cdn-images-1.medium.com/max/1200/1*ccdPdFdcSqkxRg-7902Uuw.jpeg)

R-CNN은 지역 기반의 가장 대표적인 방법중 하나이다. 이것은 semantic segmentation을 object detection 결과에 기반하여 수행한다. 구체화 하기위해, R-CNN은 처음에 많은 양의 객체 제안을 추출하기 위해 선택적 search를 하고 그로부터 나온 CNN feature들을 계산한다.

마지막으로, 클래스 특정의 선형 SVM을 사용해 각각의 영역을 분류한다. 이미지 분류를 위해 하던 전통적인 CNN구조와 비교했을 때, R-CNN은 object detection과 image segmentation과 같은 더 복잡한 task를 할 수 있다 . 그리고 이것은 두 분야의 중요한 토대가됩니다. 또한 R-CNN은 AlexNet, VGG, GoogLeNet 및 ResNet과 같은 CNN 벤치 마크 구조 위에 구축 될 수 있다.



Image segmentation task를 위해 , R-CNN은 2가지 타입의 특징을 각각의 영역에서 추출하는데,

전역 특징과 전경 특징, 이 두가지가 영역 특징과 함께 결합되면, 더 좋은 성능을 보여준다는 것을 확인했다.

R-CNN은 높은 구분적인 CNN 특징들을 사용해 퍼포먼스 개선을 보여줬다. 그러나, 이것은 segmentation에서 몇가지 단점이 있다.

1. The feature는 segmentation과 호환되지 않는다.
2. The feature는 정확한 테두리 생성을 위한 충분한 공간 정보를 포함하지 않는다.
3. sement 기반의 제안서를 생성하는 것은 시간이 걸리고, 최종 성능에 큰 영향을 준다.

이런 병목 현상들 때문에,이 문제를 해결하기 위한  최근 연구들(SDS, Hypercolumns, Mask R-CNN)이 제안되었다.



### 2  - 	Fully Convolutional Network-Based Semantic Segmentation

![img](https://cdn-images-1.medium.com/max/1200/1*Aa2fKFN2PEKmMQoy8ps-lw.png)

오리지널 Fully Convolutional Network(FCN)은 픽셀에서 픽셀로 mapping하는 것을 학습시킨다. FCN Network 파이프라인은 기본 CNN을 확장시킨다. 주요한 개념은 클래식한 CNN을 만드는 것이고, 그 CNN은 임의의 사이즈를 가진 이미지를 input으로 받는다. 특정한 사이즈의 인풋에 대한 label만 받아들이는 CNN의 한계점은 고정된 fully-connectec layer로부터 비롯된다. 이와 반대로, FCN은 오직 Convolutional layer와 Pooling Layer만을 가지고 있기 때문에, 임의의 크기의 입력에 대한 예측을 만들어낼 수 있다. 이 FCN의 한가지 문제점은 여러가지 Convolutional 과 Pooling Layer를 번갈아 전파함으로써 출력 feature 맵 해상도가 다운 샘플링된다는 점이다.

따라서, FCN의 직접적인 예측은 일반적으로 해상도가 낮아 상대적으로 퍼지는 object boundary들을 결과로 낸다. SegNet, DeepLab-CRF, Dilated Convolution을 포함한 다양한 고급 FCN 기반의 접근법들이 제안되었다.



### 3 - Weakly Supervised Semantic Segmentation

Semantic segmentation에서 대부분의 방법들은 픽셀 단위 segmentation mask를 사용하는 많은 수의 이미지에 의존한다. 그러나 수동적으로 이 mask들에 주석을 다는 것은 꽤 오랜 시간이 소모되고, 실망스럽고 경제적으로 비싸다. 그러므로 몇몇 약한 supervised 방법들이 제안되었는데, 이것은 주석된 바운딩 박스를 이용하여 semantic segmentation을 충족시키는 데 전념한다.

![img](https://cdn-images-1.medium.com/max/1200/1*Zti4CyayplzrKnIJIQfb_Q.jpeg)



예를 들어, Boxsup은 네트워크를 교육하고 semantic segmentation을 위해 추정된 mask를 반복적으로 개선하기 위해 바운딩 박스 주석을 supervision으로 사용했다. 약한 supervision 제한을 입력 label 잡음의 문제로 취급하고 재귀적인 training을 탐구했다. 픽셀 수준 labeling은 다중 인스턴스 학습 프레임워크 내에서 segmentation 작업을 해석하고 이미지 수준 분류를 위해 중요한 픽셀에 더 많은 가중치를 할당하도록 모델을 제한하는 추가 레이어를 추가했다.



### Doing Semantic Segmentation with Fully-Convolutional Network

이 섹션에서는, 한 단계씩 Semantic Segmentation을 위해 가장 많이 사용되는 아키텍처인 FCN(Fully-Convolutional Network)를 구현해 볼 것이다. Numpy나 Scipy와 같은 다른 의존성과 함께 Python3의 Tensorflow 라이브러리를 사용하여 구현할 것이다.

실제로 우리는 FCN을 이용해서 도로 이미지의 픽셀을 label할 것이다. 우리는 Kitti ROad Dataset을 Road/Lane 검출에 사용할 것이다. Udacity의 자율주행 차량 Nano Degree 프로그램에 대한 간단한 excercise이다. GitHub Repo를 참조하면 더 많이 알 수 있다. 
GIthub링크 : https://github.com/udacity/CarND-Semantic-Segmentation/

![img](https://cdn-images-1.medium.com/max/2000/1*OJJyC_CBCM8V1uwLOv2RMA.png)

Kitti ROad Dataset Training Sample : http://www.cvlibs.net/datasets/kitti/eval_road_detail.php?result=3748e213cf8e0100b7a26198114b3cdc7caa3aff

FCN 아키텍처의 중요한 feature들은 다음과 같다.

* FCN은 VGG16 네트워크로부터 semantic Segmentation을 위해 지식을 전이한다.
* VGG16 네트워크의 Fully Connected Layer들은 Fully Convolutional Layer들로 대체된다. 여기에 1x1 Convolution이 사용된다. 이 과정은 낮은 해상도로 클래스 존재 열지도를 생성한다.
* 이 저해상도 semantic Feature map들을 Upsampling 한 것은 Convolution ( Bilinear Interpolation Filter로 초기화됨 )을 사용하여 수행된다.
* 각각의 단계에서, Upsampling 과정은 VGG16의 하위 레이어에서 더 거칠지만 더 높은 해상도의 feature map에서 feature를 추가하여 더욱 정교해진다.
* Skip Connection은 각각의 convolution block뒤에 도입되는데, 이것은 후속 bloack이 더 많은 추상적인 클래스- 현저한 feature들을 이전 pooling된 feature로 부터 추출할 수 있도록 하기 위함이다.

FCN(FCN-32, FCN-16, FCN-8)의 3가지 버전이 있다. 

우리는 FCN-8을 해볼거고, 자세한 단계는 다음과 같다 :

* Encoder : 미리 학습된 VGG16이 인코더로 사용된다. 디코더는 VGG16 네트워크의 Layer 7로부터 시작한다.
* FCN Layer-8 : VGG16의 마지막 Fully Connected Layer는 1x1 Convolution을 대체된다.
* FCN Layer-9 : FCN Layer-8은 매개변수(kernel=(4,4) , stride=(2,2), padding='same')을 사용하여 전치된 convolution을 사용하여 VGG16의 Layer 4와 demension을 맞추기 위해 2회 upsampling을 실시한다. 그 뒤, Skip Connection은 VGG16의 Layer 4 와 FCN Layer 9 사이에 더해진다.
* FCN Layer-10 : FCN Layer-9는 매개변수(kernel=(4,4), stride=(2,2), padding='same' )을 사용하여 전치된 convolution을 VGG16의 Layer 3과 dimension을 맞추기 위해서 2회 upsampling된다. 그 뒤, Skip Connection은 VGG16의 Layer 3과 FCN Layer-10사이에 더해진다.
* FCN Layer-11 : FCN Layer-10은 input image 크기(size)와 차원(dimension)을 맞추기위해 4회 upsampling된다. 그래서 우리는 매개변수(kernel=(16,16), stride(8,8), padding='same')을 전치된 convolution을 사용하여 실제 이미지를 다시 얻고 깊이는 클래스 수와 같습니다.

![img](https://cdn-images-1.medium.com/max/1600/1*e08wr6of8F1J-6v4iiG2HQ.png)

​	FCN-8의 아키텍처 (Source: <https://www.researchgate.net/figure/Illustration-of-the-FCN-8s-network-architecture-as-proposed-in-20-In-our-method-the_fig1_305770331>)



### Step 1

우선, 미리 학습된 VGG-16 모델을 Tensorflow에서 로드한다. Tensorflow 세션을 열고, VGG Folder로 가는 경로를 지정한다. 다운로드 참고 : http://www.cs.toronto.edu/~frossard/post/vgg16/

그리고 image input, keep_prob(dropout rate 제어하기 위함), layer3, layer4, layer 7을 포함하여 vgg 모델에서 튜플을 반환한다.

```python
def load_vgg(sess, vgg_path):
    
    #load the model and weights
    model = tf.saved_model.loader.load(sess,['vgg16'],vgg_path)
    
    #Get Tensors to be returned from graph
    graph = tf.get_default_graph()
    image_input = graph.get_tensor_by_name('image_input:0')
    keep_prob = graph.get_tensor_by_name('keep_prob:0')
    layer3 = graph.get_tensor_by_name('layer3_out:0')
    layer4 = graph.get_tensor_by_name('layer4_out:0')
    layer7 = graph.get_tensor_by_name('layer7_out:0')
    
    return image_input, keep_prob, layer3, layer4, layer7
```



### Step2

지금 우리는VGG 모델로부터 tensor들을 사용해서  FCN에 대한 layer를 만드는데 초점을 둔다. VGG Layer 출력에 대한 tensor 및 클래스 분류 수를 감안했을 때, 해당 출력의 마지막 Layer에 대한 tensor를 반환한다. 특히, Encoder 계층에 1x1 Convolution을 적용한 다음 Skip Connection 및 Upsampling을 통해 Decoder 계층을 네트워크에 추가한다.

```python
def layers(vgg_layer3_out, vgg_layer4_out, vgg_layer7_out, num_classes):
    
    #Use a shorter variable name for simplicity
    layer3, layer4, layer7 = vgg_layer3_out, vgg_layer4_out, vgg_layer7_out
    
    # Apply 1x1 convolution in place of fully connected layer
    fcn8 = tf.layers.conv2d(layer7, filters=num_classes,kernel_size=1,name="fcn8")
    
    #Upsampling FCN-8 with size depth=(4096?) to match size of layer 4 so that we can add skip connection with 4th layer
    fcn9 = tf.layers.conv2d_transpose(fcn8, filters=layer4.get_shape().as_list()[-1], kernel_size=4, strides=(2,2), padding='same', name="fcn9")
    
    #Add a skip connection between current final layer fcn8 and 4th layer
    fcn9_skip_connected = tf.add(fcn9, layer4, name="fcn9_plus_vgg_layer4")
    
    #Upsample again
    fcn10 = tf.layers.conv2d_transpose(fcn9_skip_connected, filters=layer3.get_shape().as_list()[-1], kernel_size=4, strides=(2,2), padding='same', name="fcn10_conv2d")
    
    #Add skip connection
    fcn10_skip_connected = tf.add(fcn10, layer3, name="fcn10_plus_vgg_layer3")
    
    #Upsample again
    fcn11 = tf.layers.conv2d_transpose(fcn10_skip_connected, filters=num_classes, kernel_size=16, strides=(8,8), padding='same', name="fcn11")
    
    return fcn11
```



### Step 3

다음 단계는 우리의 Neural Network를 최적화 하는 단계이다. 일명 Tensorflow Loss Function과 Optimizer operation이다. 여기서 우리는 Cross Entropy를 loss function으로 사용하고, Adam을 Optimizer로 사용한다.

```python
def optimize(nn_last_layer, correct_label, learning_rate, num_classes):
    
    #Reshape 4D tensors to 2D, each row represents a pixel, each column a class
    logits = tf.reshape(nn_last_layer, (-1, num_classes),name="fcn_logits")
    correct_label_reshaped = tf.reshape(correct_label,(-1,num_classes))
    
    #Calculate distance from actual labels using cross entropy
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=correct_label_reshaped[:])
    #Take mean for total loss
    loss_op = tf.reduce_mean(cross_entropy, name="fcn_loss")
    
    #The Model implements this operation to find the weights/parameters that would yeild correct pixel labels
    train_op = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(loss_op,name="fcn_train_op")
    
    return logits, train_op, loss_op
```



### Step 4

여기서 우리는 train_nn function을 정의한다 그리고 그 train_nn은 epoch의 수, batch size, loss function, optimizer operation, input이미지에 대한 placeholder, label, learning rate을 포함한 중요한 parameter를 정의한다.

그리고 keep_probabilityfmf 0.5로 세팅하고 learning_rate를 0.001로 설정한다. 과정을 트래킹하기위해, 또한 training동안 loss를 프린트 한다.

```python
def train_nn(sess, epochs, batch_size, get_batches_fn, train_op, cross_entropy_loss, input_image, correct_label, keep_prob, learning_rate):
    keep_prob_value = 0.5
    learning_rate_value = 0.001
    for epoch in range(epochs):
        #Create function to get batches
        total_loss = 0
        for X_batch,gt_batch in get_batches_fn(batch_size):
            
            loss, _ = sess.run([cross_entropy_loss,train_op],
                              feed_dict={input_image: X_batch, correct_label:gt_batch,
                                        keep_prob: keep_prob_value, learning_rate : learning_rate_value})
            total_loss += loss;
        print("EPOCH {} ".format(epoch+1))
        print("Loss = {:.3f}".format(total_loss))
        print()
```



### Step 5

마지막으로, 우리의 네트워크를 학습할 시간이다! 이 function에서, 우리는 load_vgg, layers, and optimize function을 사용해서 우리의 네트워크를 빌드한다. 그러고 나서 train_nn 함수를 사용해서 네트워크를 train 한다. 그리고 기록을 위해 inference data를 저장한다

```python
def run():
    
    #Download pretrained vgg model
    helper.maybe_download_pretrained_vgg(data_dir)
    
    # A function to get batches
    get_batches_fn = helper.gen_batch_function(training_dir,image_shape)
    
    with tf.Session() as session:
        
        #Returns the three layers, keep probability and input layer from the vgg architecture
        image_input , keep_prob, layer3, layer4, layer7 = load_vgg(session,vgg_path)
        #The resulting network architecture from adding a decoder on top of the given vgg model
        model_output = layers(layer3, layer4, layer7, num_classes)
        
        #Returns the ouput logits, training operation and cost operation to be used
        # - logits : each row represents a pixel , each column a class
        # - train_op : function used to get the right parameters to the model to correctly label the pixels
        # - cross_entropy_loss : function outputting the cost which we are minimizing, lower cost should yield higher accuracy
        logits, train_op, cross_entropy_loss = optimize(model_output, correct_label, learning_rate, num_classes)
        
        # Initialize all variables
        session.run(tf.global_variables_initializer())
        session.run(tf.local_variables_initializer())
        
        print("Model build successful, starting training")
        
        # Train the neural network
        train_nn(session, EPOCHES, BATCH_SIZE, get_batches_fn, train_op, cross_entropy_loss,image_input,correct_label, keep_prob, learning_rate)
        
        # Run the model with the test images and save each painted output image(roads painted green)
        helper.save_inference_samples(runs_dir,data_dir,session, image_shape, logits,keep_prob, image_input)
        
        print("All Done!")
        
```



파라미터에 대해서, epochs =40 , batch_size = 16, num_classes = 2, image_shape(160,576)

Dropout = 0.5 and Dropout = 0.75 로 2가지로 시도해본 후 , 0.75가 더 좋은 결과를 보였다(더 나은 average losses)

![img](https://cdn-images-1.medium.com/max/2000/1*mjUI2EeA5DIKXwDBnIx-cg.png)