## U-Net Review

링크 : https://m.blog.naver.com/worb1605/221333597235

U-net이란 Network 형태가 알파벳 U 와 형태가 비슷하게 생겼다고 해서 지어진 이름이다.

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMjkg/MDAxNTMzNTUxOTUxOTU0.YzYd-ho-1jFLlBmDWRTlnxRjjKlA2XX0wmutkUXARrcg.r_RiV19V9ocbF_9jM_D9kze0TdFf5oWKY7rnZHQYLIUg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

형태를 보면 정말 U 의 형태와 같다.
이제 Network가 수록된 

U-Net: Convolutional Networks for Biomedical Image Segmentation
논문에 대해 알아보도록 하겠다.


먼저 이 논문에서 자주 나오는 표현에 대해 알 필요가 있다. 이걸 알아야 이해가 쉽다.
\1. Patch -> 쉽게 이해하자면 이미지 인식 단위라고 생각하면 된다.

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMTI2/MDAxNTMzNTUyMTYyNDI3.6H687QqX_fwkUOeN0d2bikIjF5pCRkScJKgjCVr3qfIg.VquY3LzAnbFSnEJEQosZ3oNQ-VFRfCv2wPcF5_FbQgMg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

이 논문에선 Sliding window처럼 이미지를 잘라 인식하는 단위를 만들었는데, 그게 바로 patch이다.

\2. Contracting Path, Expanding Path

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfOSAg/MDAxNTMzNTUyMzUxMjI0.BGLNzpU6JtmP8Jy43qpgLaSzAUWTCdtOiBSkFERltxcg.JZPXg332u0zTZLCv_OM0WYtdrgJQ7QzAba-zcrN1K14g.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

이미지를 점점 줄여 나가는 부분이 Contracting path, 이미지를 키워나가는 부분이 Expanding path이다.

\3. Context - 이웃한 픽섹들 관의 관계 정도로 표현할 수 있다. 글을 읽고 문맥(Context)를 파악하듯 이미지 일부를 보고 이미지의 문맥을 파악하는 것을 생각하면 된다.


이제 논문에 대한 이해를 해보도록 하겠다.



##### 1. Introduction

우선 이 Network는 의약쪽에서 탁월한 효과를 보이는 Segmenation network이다.
기존의 CNN들은 단순 classification에서 주로 쓰였다면, U-Net은 Classification + Localization 에서 주로 쓰인다.

***\*기존 논문의 문제점 해결**
또한, 이 Network는 기존의 Segmentation network들의 문제점을 해결할 수 있다는 강점을 가진다.
우선 첫번째로, U-net은 기존 network들의 단점인 느린 속도를 개선시킬 수 있다.
속도의 향상이 가능한 이유는 overlap 의 비율이 적기 때문이다.
sliding window 방식을 사용하면 내가 이미 사용한 patch 구역을 다음 sliding window에서 다시 검증한다. 이 과정은 이미 검증이 끝난 부분을 다시 검증하는것이기 때문에 똑같은 일을 반복하는 것이라 할 수 있다.
이에 반해 U-net은 검증이 끝난 곳을 다시 검증하는 Sliding window방식보단 이미 검증이 끝난 부분은 아예 건너뛰고 다음 patch부분부터 검증을 하기 때문에 속도면에서 우위를 가질 수 있다.

![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMTQy/MDAxNTMzNTUyODM2OTgx.hUUEJ7JW9z-6_9xTJpGjVJ9DSG4a0DlNMdwcuyAvmwgg.NY6cNj1PQzBor2gdWBjMLDo3YKhGW4QAxmT3yt11X-kg.PNG.worb1605/image.png?type=w800)

기존 방식의 sliding window



![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfNzAg/MDAxNTMzNTUyODUxMjUz.5psyOt9C-k4qc3dZ6HFeySjrZep8EuHYqK2lsBBcPSAg.3YydwqUN0rnWDcTPG11NJHwFcbw_DsD3sV1-osE_DJIg.PNG.worb1605/image.png?type=w800)

U-net의 patch 탐색 방식

두번째로는, Trade off의 늪에 빠지지 않는다
만약 Patch size가 커진다면 더 넓은 범위의 이미지를 한번에 인식하다보니까 context 인식에는 탁월한 효과가 있다. 하지만 Localization에서 패널티를 가지게 된다. 너무 넓은 범위를 한번에 인식하다보니 localization에서 약한 모습을 보이게 된다.
Patch size가 작아진다면 반대 효과를 가지게 된다.
U-Net은 이 논문의 reference 4, 11번에 있는 논문에서 확인가능하듯 여러 layer의 output을 동시에 검증하면서 localization과 context 인식 두가지 토끼를 다 잡을 수가 있게 된다.



***\* Network 구조**

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMjkg/MDAxNTMzNTUxOTUxOTU0.YzYd-ho-1jFLlBmDWRTlnxRjjKlA2XX0wmutkUXARrcg.r_RiV19V9ocbF_9jM_D9kze0TdFf5oWKY7rnZHQYLIUg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

U-net은 논문에서 나와있듯 Fully Connected Layer가 없다. FCN 가 없다보니 속도측면에선 빠를 수 밖에 없다.

***\* Mirroring the input image**

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMTU0/MDAxNTMzNTUzODg3ODE2.DKWcQtz4CnZOm2Nw0cU6kvC9DDSM3ebyu3RDzUh2G78g.ARzCg73VyOgWGlkVR7yTukdQHN9Ybx978TNyv0UIUcYg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

위 이미지는 input image를 U-net에 통과시켜 나오는 output과 사이즈 측면에서 비교한 것이다.
위 논문에선 input image 사이즈가 572x572 인 반면 output image 사이즈는 388x388이다.
이는 contracting path에서 padding이 없었기 때문에 점점 이미지 외곽 부분이 없어진 결과이다.
그렇다보니 이미지가 단순 작아진것이 아니라 외곽 부분이 잘려나간것과 같게 되었다.
이를 해결하기 위해 이 논문에선 mirroring이라는 것을 택했다.
mirroring 을 제대로 이해하기 위해 image를 좀 더 확대해보겠다.

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMTk4/MDAxNTMzNTU0MzU2MDQx.qpLw2IrxBmA4cet6gP0YIj2CMJO5KRHSlqSgzbmSwQ8g.RcwcpV96vzLZp2B2OQuXDeN1wYHT-vF8SuUqmXbc6yAg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

위 이미지를 보면 맨 바깥쪽 없어지는 부분이 안쪽 이미지와 형태는 같고, 거울에 반사된 형태를 가지고 있다. 이처럼 사라지는 부분은 zero-padding이 아닌 mirror padding 의 형태로 채워서 없어진 것에 대한 보상을 해준다.

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMjMw/MDAxNTMzNTU0MzExMDUz.w0Gft09tqkBaZVDuvZSKXhLhKT7_RFsd-c8K1Mt5RYsg.hmoW1ZV_oP3PV5gDe1JEizIaGalWvhuLeeZCekLo1gwg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)



##### 2. Network Architecture

network 구조는 각 Convolution에선 3x3 convolution이 사용되었고, 활성화 함수로는 relu가 사용되었다. 각 pooling 계층에선 2x2 max pooling이 사용되어 매 계층이 내려갈때마다 1/2 down sampling이 되게 된다. 또한, 각 계층을 내려갈땐 채널 갯수를 2배씩 늘려간다.
expanding path에선 2x2 up convolution이 사용되고, 같은 계층 안에선 contracting path와 같이 3x3 convolutuion이 사용되었다.

한가지 특이점이라 한다면 U-net을 가로지르는 회색의 선이다.

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA4MDZfMjkg/MDAxNTMzNTUxOTUxOTU0.YzYd-ho-1jFLlBmDWRTlnxRjjKlA2XX0wmutkUXARrcg.r_RiV19V9ocbF_9jM_D9kze0TdFf5oWKY7rnZHQYLIUg.PNG.worb1605/image.png?type=w800)](https://m.blog.naver.com/worb1605/221333597235#)

이 선은 input이 output에 영향을 끼치도록 만든 선인데, mirror padding을 진행할때 손실되는 path를 살리기 위해서 contracting path의 데이터를 적당한 크기로 crop(잘라냄)한 후  concat하는 방식으로 이미지 보상처리를 해주게 된다.



##### 3. Training

Training 같은 경우엔 GPU 메모리를 최대한으로 사용하기 위해 batch 사이즈를 줄이고, patch 사이즈를 최대화 하였다고 하는데, 이러한 행위가 어떻게 GPU 사용량을 최대한으로 늘리는지에 대한 이해는 아직 부족하다.
아무튼 이러한 방식을 사용하되 momentum을 0.99로 주어 input 의 영향력을 최대한으로 키우는 방향으로 optimize를 진행하게 된다.



##### 3.1 Data Augmentation

Data Augmentation이란 데이터가 한정되어 있을때 데이터를 회전, 반전과 같은 여러 효과를 주어 데이터의 크기를 키우는 방식이다. training 데이터가 한정되어있을때 사용하는 방식이긴 한데, 별로 좋은 방식은 아니라고 들었으나, U-net이 세포 segmentation에서 강점을 보이는 network이고, 세포 데이터에선 Data Augmentation의 적용이 나쁘지 않은 효과를 가져오기 때문에, 이 논문에선 큰 무리 없이 사용된 것 같다.
아무튼 Data Augmentation을 통해 적은 데이터셋으로 큰 데이터셋의 효과를 낸것에 관한 내용이 3.1에 수록되어있다.

여기까지가 U-net에 대한 논문 review이다.