## Bag Of Words in Computer Vision

* **G. Csurka, C. Dance, L.X. Fan, J. Willamowski, and C. Bray. "Visual categorization with bags of keypoints“, ECCV 2004. (기본적인 BoW 방법)**
  * **단계별 방법**
    1. Interesting Point Detection
    2. Key Patch Extraction
    3. Assignment of Feature Descriptors
    4. Contruction of Bag of Keypoints
    5. Multi-class Classifier : SVM , Naive Bayes

![img](https://miro.medium.com/max/1250/1*QgI1t-7yJApi4vQigFgsLQ.jpeg)

![img](https://t1.daumcdn.net/cfile/tistory/13056C4D4F683EF130)



**Image Representation**

1. Feature representation : **Refular grid** or **Interest Point detector**로 특징 검출 -> 패치 뜯고 정규화 ->  **SIFT descriptor**
2. Codebook generation : **k-means clustering** -> **codewords** dictionary
   * K-means 클러스터링이 아닌 Mean-shift등의 다른 클러스터링 방법을 사용해도 무방함.

**Training and Recognition**

1. Generative models-> Naive Bayes, Hierarchical Bayesian models
2. Discriminative models -> Pyramid match kernel

**최근 발전과 한계**

개선된 방법으로 SVM을 추가할 수 있다.

단점 : object component들의 기하학적인 정보가 없다. viewpoint 불변, scale 불변에 대한 test가 광범위하게 되지 않았다. segmentation과 localization이 불분명하다.



> 출처 )
>
>  https://mokga.tistory.com/35
>
>  https://en.wikipedia.org/wiki/Bag-of-words_model_in_computer_vision
>
> https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb