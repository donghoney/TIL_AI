## Pavement Crack Segmentation

Created by glee1228@naver.com

Please leave your questions at donghoon.rhie@gmail.com I'll spend as much time as I can to give you a friendly answer.



## Table of Contents

* **Datasets**
* **Dataset Evaluation**
* **Additional Dataset (GAPsV2)**
* **How to Download GAPsV2 Dataset**
* **GAPsV2 Data Description**
* **GAPsV2 Dataset Evaluation**

* **Edge Detection Git Repos**

* **Experiments and Evaluation**



## Datasets

**Feature Pyramid and Hierarchical Boosting Network for Pavement Crack Detection** 의 구현 Git Repo 참조

https://drive.google.com/drive/folders/1y9SxmmFVh0xdQR-wdchUmnScuWMJ5_O-

* **GAPs384**
  * Source Image 1920 x 1080(384kb, jpg)
  * Cropped Image **540 x 640** and **540 x 440** (width , height)
  * Dataset Size : 404 Source Images  / 509 Cropped Images
* **cracktree200**
  * Format : 800 x 600(228kb, jpg)
  * Dataset Size : 206 Images
* **CRACK500**
  * Format :**640 x 360**(60kb, jpeg)
  * Dataset Size : Total 3368 Images - Train(1896 Images), Val(348 Images), Test(1124 Images)
* **CFD**
  * Format : 480 x 320 (27kb, jpg)
  * Dataset Size : Total 118 Images
* **AEL**
  * Format : MINSIZE : 700 x 462
    * AIGLE_RN : 991 x 462 (170KB, jpg), 331 x 462 (60KB, jpg)
    * ESAR : 768x 512 (140KB,jpg)
    * LCMS : 700x 1000 (100KB,jpg)
  * Dataset Size : Total 58 Images
    * AIGLE_RN : 38 Images
    * ESAR : 15 Images
    * LCMS : 5 Images



## Dataset Evaluation

> 균열의 촬영 방법마다 시각적으로 이미지가 가지는 특성이 두드러짐.
>
> 가장 사용할 데이터에 적합하다고 판단되는 데이터셋은 GAPs384로 가장 우리 데이터와 흡사한 형태를 갖고 있음.
>
> Domain attributes are prominent for each dataset.
> GAPs384 Data has been determined to be the most suitable data for road crack operations





## Additional Dataset

**Neuroinformatics and Cognitive Robotics Lab** - **GAPsV2**

https://www.tu-ilmenau.de/en/neurob/data-sets-code/gaps/ 





## How to Download GAPsV2 Dataset

Detail : https://www.tu-ilmenau.de/neurob/data-sets-code/gaps/

>GAPs V1,V2 데이터 셋은 각각 별도의 로그인 계정
>
>(요청 후 발급받은 계정)을 통해 다운로드 가능
>
>Each GAPs V1,V2 data set is a separate login account.
>
>Downloadable via accounts issued after request



1. Install gaps-dataset 

```
 pip install gaps-dataset
```

2. Download using Python

<img src="image/GAPsV2_1.png" alt="GAPsV2_2" style="zoom:50%;" />



##GAPsV2 Data Description

**German Aspalt Pavement Distress Dataset**

---

Total 2468 Gray Images(8bit)

1920 x 1080 pixel Size

1.2mm x 1.2mm Per Pixel

---

1417 training Images

51 validation Images

500 validation-test Images

442 test Images

---

여러 패치 크기(160,224,256 etc..) 제공

50k 서브셋(500Mb) 단위로 쪼개서 제공

Provides multiple patch sizes (160,224,256 etc..)

Offered in 50k subset (500Mb)

---

<img src="image/GAPsV2_2.png" alt="GAPsV2_2" style="zoom:50%;" />



## GAPsV2 Dataset Evaluation

1. Segmentation에 사용할 수 있는 데이터 셋은 test 디렉토리의 442장 이미지 중에서 crack이 포함된 296장의 이미지 활용 가능

   The set of data available for Segmentation is available from Chapter 442 images in the test directory to 296 images with crack

2. Classification에는 Data Aug + ResNet 이 좋은 성능

   Data Aug + ResNet showed good performance in the Classification.

3. Binary Classification(Crack or Not) 문제에서는 F1-Score 0.9 이상

   The Binary Classification (Crack or Not) issue showed F1-Score 0.9 or higher performance.

4. Patch Size는 클수록 좋음

   The larger the patch size, the better

5. ZEB_50k, NORMvsDISTRESS

   50k : Binary Annotation 

   Segmentation (Train, Valid, Valid-test) : Annotation in fraction

   Segmentation(Test) : Segemantion Annotation





## Edge Detection Git Repos

- **Feature Pyramid and Hierarchical Boosting Network for Pavement Crack Detection(FPHBN)** (2019, IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS)  Caffe 코드

  https://github.com/fyangneil/pavement-crack-detection



- **Holistically Nested Edge Detection(HED)** (2015, ICCV) pytorch 코드

  https://github.com/buntyke/pytorch-hed



- **Richer Convolutional Features for Edge Detection(RCF)** (2019, IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE / 2017, CVPR ) pytorch 코드

  https://github.com/meteorshowers/RCF-pytorch



- **CASENet: Deep Category-Aware Semantic Edge Detection** (2017, CVPR) 

  https://github.com/milongo/CASENet



## Experiments and Evaluation

* ##GAPs384 (HED)

  | **ODS   (fixed contour threshold)** | **GAPs(original size)** | **GAPs(256x256)** |
  | :---------------------------------: | :---------------------: | :---------------: |
  |               **130**               |          0.707          |       0.676       |
  |               **150**               |          0.713          |       0.628       |
  |               **170**               |          0.710          |       0.749       |
  |               **190**               |          0.698          |       0.628       |
  |               **210**               |          0.669          |       0.668       |
  |               **230**               |          0.602          |       0.733       |

  **Example)**

  **f1-score by fixed threshold**

  <img src="Image/Experiment_1.png" alt="Experiment_1" style="zoom:50%;" />

  

  <img src="Image/Experiment_2.png" alt="Experiment_1" style="zoom:50%;" />

  

  <img src="Image/Experiment_3.png" alt="Experiment_1" style="zoom:50%;" />

