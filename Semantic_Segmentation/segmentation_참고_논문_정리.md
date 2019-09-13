## segmentation, classification 참고 논문 정리글

출처 : [**sogangori**님의 네이버 블로그](http://blog.naver.com/PostView.nhn?blogId=sogangori&logNo=221092445500&parentCategoryNo=&categoryNo=6&viewDate=&isShowPopularPosts=false&from=postView)



본 글의 출처는 sogangori님의 네이버 블로그입니다.

도로면의 균열 검출에 2019.9월 기준 sota인 FPHBN의 backbone 네트워크인 Holistically-Nested Edge Detection(HED) 논문을 보던 중 자료를 접하게 되어 개인적으로 출처를 남기고 공유하는 글입니다.

>2017.11.24  Efficient and Invariant Convolutional Neural Networks for Dense Prediction
>
>2017.11.24  Pixel Deconvolutional Networks
>
>2017.09.05  Squeeze-and-Excitation Networks
>
>2017.09.01  Single Shot Text Detector with Regional Attention
>
>2017.08.22  Learning Efficient Convolutional Networks through Network Slimming
>
>2017.07.20  IDK Cascades: Fast Deep Learning by Learning not to Overthink
>
>2017.05.27  CASENet: Deep Category-Aware Semantic Edge Detection 
>
>2017.04.23  Residual Attention Network for Image Classification
>
>2017.04.19  Learning Video Object Segmentation with Visual Memory   
>
>2017.04.13  One-Shot Video Object Segmentation
>
>2017.04.11  FastMask: Segment Multi-scale Object Candidates in One Shot
>
>2017.04.09  Deeply Supervised Salient Object Detection with Short Connections
>
>2017.04.05  Not All Pixels Are Equal: Difficulty-aware Semantic Segmentation via Deep Layer Cascade
>
>2017.03.10  Deep Image Matting Adobe
>
>2017.01.23  DSSD: Deconvolutional Single Shot Detector 
>
>2016.12.05  Classification with an edge: improving semantic image segmentation with boundary detection
>
>2016.12.04  Pyramid Scene Parsing Network  
>
>2016.11.25  Semantic Segmentation using Adversarial Networks
>
>2016.11.05  LAYER RECURRENT NEURAL NETWORKS
>
>2016.07.15  DSD: Dense-Sparase-Dense Training For Deep Neural Networks 
>
>2016.03.31  Object Boundary Guided Semantic Segmentation
>
>2016.03.19  Brain tumor segmentation with Deep Neural Networks
>
>2015.10.04  Holistically-Nested Edge Detection
>
>2015.03.18  U-Net: Convolutional Networks for Biomedical Image Segmentation 
>
>2015         Recurrent Convolutional Neural Network for Object Recognition
>
>

2017.11.24  **Efficient and Invariant Convolutional Neural Networks for Dense Prediction** Washington State Unv
세그멘테이션에서 회전된 대상에 대해 같은 특징을 얻기 위해서 3x3 컨볼루션 커널을 45씩 회전시켜서 max-out 으로 통합하는 실험을 했다.커널 회전, flip 를 이용하는 것이 입력데이터를 회전, flip 하는 것보다 효율적

![img](http://postfiles4.naver.net/MjAxNzEyMjFfMTA0/MDAxNTEzODE1Mjc1Mzc5.jaHtoBzDhBgGpMLbHGIsSDwU6gBcxbp19tiXi00kuw8g.Uv_IDE5xABtbVVJ39nWBvNQKWj4ZfvTz5kWpGo4F_A0g.PNG.sogangori/1.PNG?type=w1)

1) 커널 회전시키기

![img](http://postfiles8.naver.net/MjAxNzEyMjFfMTEw/MDAxNTEzODE1Mjc1NDk5.ehc4zeVYCSNcGfSrZhpvDl2ETZmIvHYUdKlw2mEQa0Ug.EwxDnrJl_Q0qbpqOHKyqC-L51sDc15_3dDkp_rdOR3Ig.PNG.sogangori/2.PNG?type=w1)

2) 커널 flip

![img](http://postfiles13.naver.net/MjAxNzEyMjFfMjky/MDAxNTEzODE1Mjc1NjA0.ejlMsQCL34ZlpJIREE5xVg0IrZfrIWF82erNwsj5dhwg.3s1tYWpq7ReCiEyU-h_2Hj85w6HDZqttSpPaC9fB7gkg.PNG.sogangori/3.PNG?type=w1)![img](http://postfiles8.naver.net/MjAxNzEyMjFfMTkx/MDAxNTEzODE1Mjc1Nzc5.PziT9k6TKeH2PRaXBkWeD8-oZlLyGzjhUgay3Kr02PYg.zxq3SCGeKstXWYbaSIHx0q3QlbHVf7CuoqlddO73Mdkg.PNG.sogangori/5.PNG?type=w1)

3) 컨볼루션 커널을 회전시켜서 얻은 특징들을 엘리먼트별로 Maxout을 구해서 통합한다. 

4) 입력 데이터와 가까운 레이어에서 Flip 과 Rotation 의 Maxout 을 1번 수행한다.![img](http://postfiles5.naver.net/MjAxNzEyMjFfMTc1/MDAxNTEzODE1Mjc1ODc5.NAfRMjBKJu_aXoPDfDtWEtf_Bl5ut1AIJzUqPvxR_MYg.OPmU_ILcCbBK8pe7B_8YZlXjh4JH0hssycgn0eNyYWEg.PNG.sogangori/t1.PNG?type=w1) 

5) 기본 성능, 입력데이터의 회전, flip을 모두 구해 통합했을때의 성능과 제안한 모델의 성능



2017.11.24  **Pixel Deconvolutional Networks** Washington State Unv
일반 Deconvolution 레이어에서 체크보드 현상이 발생하는 원인을 분석.그 결점을 보완하는 성능이 더 좋은 Dense 한 Deconvolution 방법을 제안. 그 대가로 속도는 더 느리지만 세그멘테이션 성능은 약간 상승.Conv 에서만 Dense를 사용하기 쉬운데 Deconv에서도 Dense 기법이 효율적임을 상기시킨다.![img](http://postfiles16.naver.net/MjAxNzExMjhfNzUg/MDAxNTExODU4NTUwNDg5.vBPZwyifZoY5oL7axCwaUIt8LTtAiRx-VjkbyQb67HIg.OLhUQrHX-Z6KxdrVgWJfZ15TGVFJujUzHydNoSoVVkEg.PNG.sogangori/f2.PNG?type=w1)

그림) 1D 데이터의 1x4 deconv는 1x2 deconv + 1x2 deconv 로 분리할 수 있다.
![img](http://postfiles11.naver.net/MjAxNzExMjhfNyAg/MDAxNTExODU4NTUwNzQx.z8eK8F4Rtyvkec6VPVv2L_VSJlGqxdNQaukj32kXou8g.9Oxpa7lohN5XonjWsV2v0LsiC0Tv3Ob6bN6Qgi7wM_Mg.PNG.sogangori/f3.PNG?type=w1)

그림) 2D 데이터의 4x4 deconv 는 4개의 deconv 로 분리할 수 있다.
![img](http://postfiles14.naver.net/MjAxNzExMjhfMTk0/MDAxNTExODU4NTQ5OTQ0.ZWcVpDLWR1wo6uzpV4pjVjgLHmceAMwXjQ6pI2xvs5Yg.9YCFT_9ff0COcYZ_2RF7nA6niWnxFsmw_-_5qX89rIsg.PNG.sogangori/e1.PNG?type=w1)

식) 2D의 deconv 분리 식을 나타낸다.
![img](http://postfiles9.naver.net/MjAxNzExMjhfMjQz/MDAxNTExODU4NTUwODk5.SH63GdzdfRpeNELUb5gm622hAymOiSa2Bx8G_ijDKUgg.bQdEMDLV-ANz6pNq8ZYhA6k2CSslNr7LYzFQFqA6_1sg.PNG.sogangori/f5.PNG?type=w1)

그림) 제안하는 dense한 deconvolution
![img](http://postfiles9.naver.net/MjAxNzExMjhfMTEy/MDAxNTExODU4NTUwMTc2.uuwc4XorGHH2JM9jM8Oza_C6YkiWNjcHMVTXh7RfB7kg.VLZen_c3CG6kFUNlGT0Z4G1FFh3MVvEj0L-TK2TBfVAg.PNG.sogangori/e2.PNG?type=w1)

그림) 제안 deconv의 식
![img](http://postfiles6.naver.net/MjAxNzExMjhfOTQg/MDAxNTExODU4NTUxMDg3.-WFHPFZVbCwQ_RIFtsz-Z7YQyFr2FJRdOGIaqOSL_88g.xq0UmWm9PujNJSUWlB-5OewxrYdZJBHv9WDmBaBCuHEg.PNG.sogangori/f6.PNG?type=w1)

그림) 제안하는 효율적인 deconvolution
![img](http://postfiles4.naver.net/MjAxNzExMjhfMTUx/MDAxNTExODU4NTUwMzQ0.WmM7pgK3Dry20r2UgmYHW7XWzI7EOAzs-GRFe_w4Luwg.xAfb-xMzNfm4d54_g_qzE7PZpdG75ilbDlmPOCXk9D8g.PNG.sogangori/e3.PNG?type=w1)
그림) 효율적인 deconv 식![img](http://postfiles6.naver.net/MjAxNzExMjhfMTMy/MDAxNTExODU4NzM4NjUy.THVnKi9N2GjQYMx23R8PpVEnlr9NdDwNXq1yAWzqvlcg.YhrOSlCgGNeu_7dP1OAbNHNx9kp_TkCy9AFAL4lm12gg.PNG.sogangori/t1.PNG?type=w1) 

표) 성능향상은 크지않으나 시도해볼 가치가 있다.



2017.09.05 **Squeeze-and-Excitation Networks**  Momenta, Oxford

ILSVRC 2017 Object Localization 부분에서 classification 1등컨볼루션 연산은 입력특징맵의 모든 채널을 필터와 곱한 후 다 더할때 중요한 채널과 그렇지 않은 채널이 모두 얽혀므로 데이터의 sensitivity 가 나빠진다.이 문제를 해결 하기 위해서 특징맵을 채널 별로 중요도에 따라 scale 해주는 간단한 Squeeze-and-Excitation Module (짜내기와 자극)을 제안한다.간단하고 연산량이 적어 오버헤드가 적음에도 불구하고 성능 향상 효과를 볼 수 있다.![img](http://postfiles16.naver.net/MjAxNzA5MTBfMTU1/MDAxNTA1MDQyMzM4NTQ4.NjzG4YFTbzbbdadqK5CuXbTiaSGBQ1LP4Mnt7AysXEcg.sAC2aYAW71UEv-Fr-dF5Skgs-VPRilb1tOC8yT2ZUk4g.PNG.sogangori/f1.PNG?type=w1)

그림) Squeeze-and-Exciting block(SE) ![img](http://postfiles1.naver.net/MjAxNzA5MTBfMjU4/MDAxNTA1MDQyMzM3ODcz.yvEot-zR0QVf0A4GENl_WBRk51yTraYD5pkhdhM7uLkg.eCccEHX3TvkTBuJvBTG_SjSTTBS4ZVkTbtbNRDsluWMg.PNG.sogangori/e2.PNG?type=w1)

식) squeeze : global avg pooling 이다. 채널 별 평균을 구한다. 입력 u(H x W x C) 는 z (1 x 1 x C) 가 된다.
![img](http://postfiles8.naver.net/MjAxNzA5MTBfOTAg/MDAxNTA1MDQyMzM4MDA1.Cqdv6gxURV6Qw5_UxDEAgl3mo72CX_qAYvQvSW6C3Jsg._L2mUvL7wSQ2sCQrpEZHWIRitPFPm8fSzmyIR0GuVRsg.PNG.sogangori/e3.PNG?type=w1)

식) exciting : W1과 z 를 Fully Connection(FC), 델타는 Relu 함수, 결과를 W2와 FC, 시그모이드 함수를 취한다.W1, W2 는 2차원 파라미터로 다음과 같은 shape 을 갖는다. ![img](http://postfiles13.naver.net/MjAxNzA5MTBfMTMw/MDAxNTA1MDQyMzM4Mjcx.K3PbSabnPo2FMAbaPQrak0BEo8rcKmykU03d5StKhcsg.2cbUQcrujwg092mji19T6JfFy1wz2f3yzuy3zCbkm6Yg.PNG.sogangori/w1.PNG?type=w1) ![img](http://postfiles13.naver.net/MjAxNzA5MTBfMjM2/MDAxNTA1MDQyMzM4Mzk1.iWbFjCZdr88XeTfoUf3MrdxGSVXrnF0IKTKaA-WpDDMg.oMabR_lzgq9IdGIj-YTCZYBdqA6psEDVIj_cuTNhmdEg.PNG.sogangori/w2.PNG?type=w1)  W1 과 z를 fc 하게 되면 1 x 1 x  C/r  의 output 을 얻는다. r = 16 으로 차원을 줄이는 역활을 한다. W2와의 FC를 통해 C 개의 채널로 복원된다.
![img](http://postfiles12.naver.net/MjAxNzA5MTBfODcg/MDAxNTA1MDQyMzM4MTI4.wOHWr9Dcf01N2V-c00bmrgX4wfu_Jeo10jGITse6crgg.FhSWKZh38mId00UZkgaOKOuBZM4AQjkaIfI8_9e960Ag.PNG.sogangori/e4.PNG?type=w1)

식) squeeze-and-excitation module 의 output 으로 입력(u) 를 scale 하기. s 의 shape은 1x1x c 이므로 단순한 채널별 곱셈이다. 
![img](http://postfiles11.naver.net/MjAxNzA5MTBfMTc3/MDAxNTA1MDQyMzM4Njg1.X-WO5APCUNEJXc7HDdGnrjSTycBYh3lxxKFX5kdBPd0g.wFdKcXmLwyY4PcJ8u5Rp2du5oRpwxN-pH8i7WGMKa68g.PNG.sogangori/f3.PNG?type=w1) ![img](http://postfiles15.naver.net/MjAxNzA5MTBfMjYx/MDAxNTA1MDQyMzM4ODE0.qS9IbuDMAd6hnpUIPcGPJ6mLvOaOERCUmcyqDbBwRA4g.NF7HLkE-GWjrEHdommIZHy8Tzsk5HMiubB8neP0dk8Eg.PNG.sogangori/t3.PNG?type=w1)그림 (좌) 

ResNet에서 SE 모듈 사용하기 (우) Single-crop 에서 SOTA 와 분류 성능 비교
참고 [저자 PPT](http://image-net.org/challenges/talks_2017/SENet.pdf) [저자 GitHub CAFFE](https://github.com/hujie-frank/SENet)



2017.09.01 **Single Shot Text Detector with Regional Attention** 
영상에 나타난 문장들의 경계박스를 찾는다. SSD 를 Backbone 으로 사용하며, 추가적으로 Text Mask 를 학습에 사용한다.Text Mask 는 영상에서 글자 부분에만 Attention 하여 특징맵에서 글자 부분의 값을 키운다.처음에는 Text Mask 학습 데이터가 필요하지만 보조 loss 를 사용해 학습된 이후에는 네트워크 스스로 생성한다.
![img](http://postfiles11.naver.net/MjAxNzA5MTFfMjE1/MDAxNTA1MTAxNTAyODUw.lT8UeLnssraKv4RsUs4SFhsxkgUvM3fu7yxbW9as8fkg.XWhIaWPLhrNYLswm1y9SVFQ7jhaoCaO_eYR6wetwfD0g.PNG.sogangori/f2.PNG?type=w1)

그림) single-shot text detector 의 구조. 상단의 convolutional part, 중단의 text-specific part, 하단의 Word Box Predictor part 로 구성된다.TAM(Text Attention Module) 과 HIM(Hierarchical Inception Module) 을 사용해서 성능을 더 올렸다. 
![img](http://postfiles16.naver.net/MjAxNzA5MTFfNTIg/MDAxNTA1MTAxNTAzMDAz.LytIYX1n-DTAJnNaLAMXtyiSoMmWvY1LWng2LQDoBJYg.iefNsTllPv-Nt7Hpz3tac0ePigPs_rYE3xM7z_HcRXQg.PNG.sogangori/f3.PNG?type=w1) ![img](http://postfiles1.naver.net/MjAxNzA5MTFfNjAg/MDAxNTA1MTAzMjE1MzAy.Fxq5yrw6r0oRfdgZ2mNtp4uAUhtmK02owLUxn08wLXQg.oS_Q5U4YZlPJLyW8I3WD9-oDU9LTZJrcAGLt65QLrBMg.PNG.sogangori/t2.PNG?type=w1)

그림) AIF (Aggregated Inception Features)  우측의 Attention map(Softmax 결과로 2개 채널 중 1번째 채널)은 글자 부분에서 값이 크다.Attention map 과 AIF 를 pixel-wise dot production 이다. 연산 결과 글자 부분을 제외한 특징맵의 값이 작아졌다.표) Ablation 성능 측정. SSD 를 Text 검출에 맞게 수정 + Inception Module 을 적용.
![img](http://postfiles10.naver.net/MjAxNzA5MTFfMTg2/MDAxNTA1MTAxNTAzNTQ5.0MKY6g66eFec1nhbLHuov26c6xmvv0MEYwosNmsUc6Qg.E-1YJ_mBA-I20z-YvWwu_qysEaLi71JBN14B2p-zmLkg.PNG.sogangori/f4.PNG?type=w1) 

그림) TAM(Text Attention Module) 을 사용하지 않은 위쪽과 사용한 아래쪽의 성능 비교2017.08.22  



**Learning Efficient Convolutional Networks through Network Slimming** Tsinghua,Intel,Fudan,Cornell  ICCV 2017

특징맵의 여러 채널 중에서 중요하지 않은 채널을 잘라버리는 방법으로 네트워크를 slim 하게 만든다.CIFAR-10,100 분류 문제에서 VGGNet,ResNet,DenseNet 에서 slimming 을 사용하면 40%,60% Prune 했음에도 오히려 성능이 올라감을 보여준다.
![img](http://postfiles2.naver.net/MjAxNzA5MTFfMjUg/MDAxNTA1MDg3Njg4MTE4.WNnaZU6EkhuTO-tTjuP1-aPzfn-sfQyH7EHxJnwp-40g.OzYS5Yj9vRlffKYiPyfCCR73Gfae8HndGPNy19FMvNAg.PNG.sogangori/f0.PNG?type=w1)



그림) channel scaling factors 는 batch normalize 의 파라미터를 재사용한다. 여기에 regularization 을 사용하기 때문에 chanel scaling factor 들의 일부는 작아진다.scaling factor 가 작은 좌측의 주황색 채널들은 prune 되어 오른쪽처럼 파란색 채널들만 남는다. 우측의 compact 넷은 initial 넷 이상의 성능을 낸다.
![img](http://postfiles1.naver.net/MjAxNzA5MTFfMTA4/MDAxNTA1MDg3Njg4Mjky.k6TDwzIiPzagOIWiO8cC1C26NqPff_QYUikxuduDRPkg.ODF8ofI303eHJHW3OpOnJeqYwZ-IKPRGMSp43RnBC1Ig.PNG.sogangori/f2.PNG?type=w1)



그림) netowrk slimming procedure의 플로우 차트. 점선은 multi-pass/반복이다. 
![img](http://postfiles3.naver.net/MjAxNzA5MTFfNjAg/MDAxNTA1MDg4MDcyNDIz.uW3ix4bLfBsgQcN8SroNl60-vAnFaINcGbk7rP-TE9Ag.JsMbd75evoNYUNmTmYthxLPk5BD0XWnOX6YsDUIwm8sg.PNG.sogangori/e1.PNG?type=w1)

식) 플로우 차트의 2번째 학습 단계에서는 Sparsity Regularization Loss 를 추가하여 prune 할 channel 을 찾는다.
![img](http://postfiles13.naver.net/MjAxNzA5MTFfNzAg/MDAxNTA1MDg3Njg4NDQy.tizplb0olQBZhKiMnZ7yjAKOfaUMmt-Hyo7Mhb-y428g.WdaOcdBB8ylaAP6wjNNVAkL_WgFCWZ0HLTWS9dvcjRkg.PNG.sogangori/f5.PNG?type=w1)

 그림 ) CIFAR-10 ,DenseNet-40 모델에서 channel pruning 정도에 따른 성능 변화. Sparsity Regularizaton Loss 를 추가하는 것만으로도 큰 효과가 있다.



2017.7.20 **IDK Cascades: Fast Deep Learning by Learning not to Overthink** UC Berkeley
예측하기 쉬운 데이터는 빠른 모델이 해결하고 어려운 데이터는 느리지만 정확한 모델이 처리하는 cascade 방식의 framework를 제안한다.장점은 빠른 속도다. joint 학습을 위한 loss 함수를 디자인했다.
![img](http://postfiles8.naver.net/MjAxNzA5MTRfMjkg/MDAxNTA1Mzc1NTE1MDM1.6PwsjXnYxBw2_u8xNDlPV1gXRcIwE57b-VFUs_mKaFkg.amzhEDYR_N4xn-jHizhKbpI23Of4_xb11n4ZUANqvPIg.JPEG.sogangori/f1.PNG?type=w1) 

그림) 입력데이터를 간단한 분류기부터 분류할 수 있으면 분류(Pred) 하고 모르겠으면(IDK: I don't know ) 다음 분류기에게 Input을 넘긴다.
![img](http://postfiles16.naver.net/MjAxNzA5MTRfMTkx/MDAxNTA1Mzc0NzQ5Mjcy.Q-LBk8-ib3r_9KyOv7IIg-l5xCqDxhJ8TRwCikPUzGsg.95qeWlWArKyGqCu7G0t81zvEfXi8OBWK4nPGRflhUdEg.PNG.sogangori/e1.PNG?type=w1)

식) 빠른 모델이 x를 모르겠다고 하면 정확한 모델이 예측한다.
![img](http://postfiles5.naver.net/MjAxNzA5MTRfMTUg/MDAxNTA1Mzc0NzQ5NDY0.ZpSnjWQs_w6lat2BvvOtIgY1UTuxzj2IAVI_Z1md8Bog.yuZKmaTvk3XTzoY1WqMIEoU-bFlEG2GsQG2XyhjgHuog.PNG.sogangori/e2.PNG?type=w1)

빠른 모델에서 x에 대한 entropy 가 a 이상이면 모른다고 판단한다.![img](http://postfiles14.naver.net/MjAxNzA5MTRfMTcz/MDAxNTA1Mzc1MzE1Mzg5.SS26nmyAG3qJfbLyRIJySvq7dB1V4jrgyWLn8KEISHkg.sf1vBye0vcr_c2vOa4C02YmDoGjytf42kjIWc44xOZkg.PNG.sogangori/e3.PNG?type=w1)

좌측의 L 은 원래의 예측 로스이고 우측의 C는 모델을 호출(더 정확하고 느린 모델들) 하는 비용이다.![img](http://postfiles10.naver.net/MjAxNzA5MTRfMTQy/MDAxNTA1Mzc1MzE1NTY2._tPn8-sFPAL-B38rZWIxlIIb8ylnCDbKsTv-d5mFMR4g.rRT5Z01aGotXXuL6xEbKEmxjGw_-tm_xZEougzmzDhYg.PNG.sogangori/e4.PNG?type=w1) 

acc 한 모델을 미리 학습시켜 놓은 후 원래의 GT인 y 을 acc 모델의 예측으로 대체한다.
![img](http://postfiles16.naver.net/MjAxNzA5MTRfNiAg/MDAxNTA1Mzc0OTg0MTg5.on7yKSq2ox9mt8R9eI_qk1GEGV6oPeXpr6SfHKw6GUAg.vkkTqEhCnP0T88lXTVJFjbp9_Pc0I2C-z8i_n393h6og.PNG.sogangori/e5.PNG?type=w1) 

원래는 y가 k 까지 밖에 없으모로 IDK 클래스를 예측할 수 있도록 빠른 모델의 마지막에 채널을 하나 늘려주는 레이어를 추가(Extend)한다.![img](http://postfiles3.naver.net/MjAxNzA5MTRfOTUg/MDAxNTA1Mzc0OTU2NDU4.NthLI_qvKFsFRfFvmLHC-jcIVzYP2nTHRpljYiM4obYg.KZv_nKavWmRNkoCTAIHtHUU6vf8vqbClfOz5iAEY-hEg.PNG.sogangori/e6.PNG?type=w1)

 c=1, x에 대해 IDK 라고 예측할 수록 Lce(Cross Entropy) 가 커지지만 반면 좌측의 항은 작아진다.IDK 라고 예측하는 경우가 적으면서 원래 클래스들에 대한 예측오류가 적을때 전체 로스가 작아진다.

2017.05.27 **CASENet: Deep Category-Aware Semantic Edge Detection** CVPR 2017 spotlight paper Carnegie Mellon, Mitsubishi
멀티 클래스가 아닌 멀티 카테고리 윤곽선 검출기를 개발했다.
![img](http://postfiles15.naver.net/MjAxNzA5MTVfMjY0/MDAxNTA1NDQ4MTA0OTAx.WKcf6zCPr9XeyU3grGQT6JY6SgxGy-oM17_mTtcy3lUg.M_Yrl_HCGuW1RkiDI_-3YRrjvvZ5TO9QTB0xDVQS2V8g.JPEG.sogangori/f1.PNG?type=w1)

그림) 카테고리 종류![img](http://postfiles8.naver.net/MjAxNzA5MTVfMzQg/MDAxNTA1NDQ4MTE2NTAy.50EUFHbNaWOPtk9swCl8aEmyFCf-Ua2SUV9H6eCh1YUg.W2bofvF_Yv9Jj4sXAQJJvgx82BgXq9B3LLnHhmoXJPog.JPEG.sogangori/f1.PNG?type=w1)

그림) (좌) 입력이미지 (우) 라벨
윤곽선 라벨은 segmentation 라벨로부터 생성하는데 2픽셀 거리 안에서 segmentation 라벨이 달라지면 edge 로 분류한다.
![img](http://postfiles3.naver.net/MjAxNzA5MTRfMTUz/MDAxNTA1MzQ1MjQxMTM3.lXa5ITJZ0W7XRzPMwBY9UYIZpUdBw7sOBBAvLjEOhqMg.C5m2YDevK1eJET5ZJsH4iuxJjmQsdk5YTzvf8o5LJBYg.PNG.sogangori/f3.PNG?type=w1) 

그림) 기존의 CNN Edge Detector 는 (b) 로 여러개의 superviser 를 갖는 binary edge detector 였다. 이를 multi class edge detector인 (c) CASENet으로 발전시켰다.
![img](http://postfiles3.naver.net/MjAxNzA5MTRfMTY3/MDAxNTA1MzQ1MjM5OTQ1.3aQTZj-s7hSoGbSPPDUupbuM_Ece6Dn3Gvhp3tkE_QAg.lVfltq6nBIPrFFnPa3Aj2XhtQuuwBopKOw9Fxu8Ya1sg.PNG.sogangori/e11.PNG?type=w1) 

그림 (b) 의 5개의 side classification activation maps 각각을 A(1), A(2),...,A(5) 라고 하자. ![img](http://postfiles14.naver.net/MjAxNzA5MTRfMjc1/MDAxNTA1MzQ1MjM5NDkz.3fAETim_9LZd2sBED9r7ly424H0ehBVj5tNkqtu-c_Ig.jJFDPILWah_yaOQW0j_OSMMqHKyEy5GXa1A4yO3gJjUg.PNG.sogangori/e2.PNG?type=w1)

그림 (g) 의 Sliced Concatenation은 같은 클래스를 의미하는 컬러의 레이어리 그룹별로 모은다.
![img](http://postfiles7.naver.net/MjAxNzA5MTRfMTY1/MDAxNTA1MzQ1MjM5NjU3.G8xIE0hnURTDOIAbUZiJQcYfXyozbe9bc4fh3n2qw30g.pvicuBubRcjCU5hKlNuMNoN2FV0GybtP6zEmb4XhdBgg.PNG.sogangori/e3.PNG?type=w1)

그림 (f) 는 글룹별로 모인 특징맵을 그룹별로 컨볼루션한다.
![img](http://postfiles11.naver.net/MjAxNzA5MTRfMzAg/MDAxNTA1MzQ1MjM5ODEw.EQ7MRMV-K4DH8iuUqSErwwIwg2M5b_-8LBeAjVD48x4g.3tyGgRLnpg44tifgXemMPh6v9YS_gEmEObUcBcSjEZAg.PNG.sogangori/e4.PNG?type=w1)

그림 (h)는 그림 (c) 에서 얻은 3개의 side feature extraction 과 1개의 side 5 classification 을 합칠때 3개의 side featuer extration을 k번 shared 해서 합친다.

2017.4.23 **Residual Attention Network for Image Classification** CVPR 2017
ImageNet 2017 classification 1위, localization 3위 
집중할 feature 의 값은 커지고 그렇지 않은 것은 작아지는 Attention Mudule 을 구현했다. 모델이 좋은 feature 에 집중할 수 있기 때문에 높은 성능을 얻을 수 있다.Attention Module 이 Residual 하게 더해지므로 깊은 네트워크에서도 문제가 없으며 모듈을 추가할 수록 성능이 높아진다.![img](http://postfiles9.naver.net/MjAxNzA5MTVfMTg2/MDAxNTA1NDQ2OTgxMTU3.4NlPE42OxLhNssRAP0APXspAKTYl4He8ydT9QHvO2qYg.nYkk1Va3uzPuStGauhB19mueJ6o0p7cde9y8wyKhpxgg.PNG.sogangori/f1.PNG?type=w1)

그림 (좌) 좌측이 Attention Map으로 우측에서 필요없는 위쪽의 feature 들이 사라지고 중요한 부분은 강조되었다.

그림 (우) 여러개의 attention mask 를 거치면서 필요한 feature 에 집중하며 최종예측에 필요하지 않은 feature 들의 값은 상대적으로 작아진다. ![img](http://postfiles6.naver.net/MjAxNzA5MTVfNDAg/MDAxNTA1NDQ2OTgxNTA4.WrvtA3WHg8eFqJVw3MHfVzvi1HL3QUTk_SBTlgTZIg4g.FE97jrKSWKPIf37g1PrtK1HvU-R5Wox3dh4cza1fcgog.PNG.sogangori/f2.PNG?type=w1)

그림) 모델의 구조. 3개의 Attention Module 이 있고 모듈의 위쪽은 Trunk Branch, 아래쪽은 Mask Branch 이다.
![img](http://postfiles2.naver.net/MjAxNzA5MTVfMjI2/MDAxNTA1NDQ3MDAyMDE1.JaEKsyJ-eDve7zpIGqVg1WFm7UDsTkmnYAK6HpON8_gg.H7CAj1bZcnSp_2UbCof6gcKfqAOiagaSDK8ichhF7VMg.PNG.sogangori/e3.PNG?type=w1) 

식) Trunk Branch(F) 와 Mask Branch(M) 의 결합 공식이다.Mask Branch 의 output은 sigmoid 로 인해 [0,1] 사이의 값이므로 결국 중요한 feature 는 최대 2배 커질 수 있다.



2017.04.19 **Learning Video Object Segmentation with Visual Memory**  CVPR 2017
Video 에서 핵심 오브젝트의 segmentation 이 목표일반적인 CNN을 이용한 Appearance network 과 Optical flow 를 계산하는 Motion network 를 이용해 특징을 추출Conv GRU 를 이용해 Visual Memory 를 구성했다.![img](http://postfiles4.naver.net/MjAxNzA5MjVfMTg3/MDAxNTA2MzE0NzczNTY5.FtEIIhG4_ovR1RAWNQuB3DrZpC6grljm9tb_KEqtrgIg.MLzgCTjxM8mmXROl13oX75bq10ByCJYfhN4pRtTz05kg.PNG.sogangori/fig2.PNG?type=w1) 

그림) 모델 구조
 ![img](http://postfiles5.naver.net/MjAxNzA5MjVfMjc0/MDAxNTA2MzE0NzczNzU5.sZ1_-xd9RO5A5jcmfKk48fiMhby87E-GAgOzElRmOVYg.fom6aRSFolFfoVyyFc0tWtu0Bea0nYqAWNFiighS2z0g.PNG.sogangori/fig3.PNG?type=w1)![img](http://postfiles9.naver.net/MjAxNzA5MjVfMTc0/MDAxNTA2MzE0NzczOTQ5.beKPMr_HRNUrialoP7-CbzEWWmZgqrSs78fHupIxFjQg.A-_U95gHdmudma3UgHgg4CcIes86mtkXTHpH6gOQSLkg.PNG.sogangori/fig4.PNG?type=w1)

그림) Conv GRU 모듈과 2개의 Bidirection Conv GRU 



2017.04.13 **One-Shot Video Object Segmentation**  ETH Zurich, TU Munchen  CVPR 2017
DAVID Dataset의 Video Segmentation 에서 타겟 오브젝트를 잘 추적하는 방법을 제안한다.타겟을 한 번 보면(one-shot) 이후 타겟의 이동이나 움직임에 의한 변형이 발생해도 강인하게 추적할 수 있다.![img](http://postfiles14.naver.net/MjAxNzA5MjZfNTIg/MDAxNTA2Mzg1NTM0NTc2.DoPwrCQ-qnubjrbFaW8oL3_699cygGr9gAapWF_E7XIg.qDMkcUz7GOKUz2RkXtm3fgHdoPUuxKy1jEa4Kv5caoQg.PNG.sogangori/f1.PNG?type=w1)

그림) 1번째 빨간색 마스크로 Fine-tune 학습을 시키고 나면 이후의 비디오 시퀀스에서 해당 타겟(녹색:학습하지 않음)을 정확히 segmentation 할 수있다.
![img](http://postfiles2.naver.net/MjAxNzA5MjZfMiAg/MDAxNTA2Mzg1NTM0OTY0.ksTRr4tDJ6EpMtzrzpAKL5j0KPCzUC62lRvjWSMfVWUg.OgJbQ_LXSUeODM19agiKZlE75vpYVsF4MffId_2p95og.PNG.sogangori/f2.PNG?type=w1)

그림) static image 로 Pre-train, video로 re-train, video의 타겟으로 fine-tune 3단계 학습한다.Pre-train 만 하면 전혀 segmentation을 하지 못한다. re-train 까지만 하는 경우에는 배경의 object까지 segmentation 한다. 테스트 단계에서 타겟 오브젝트 마스크를 한번 더 Fine-tune 하면 이후 프레임에서도 타겟 오브젝트를 정확하게 segmentation 할 수 있다.Test 과정에서 mask 를 학습하는 것이 의아할 수 있는데, DAVID Dataset는 다음과 같이 Test 데이터로 비디오의 첫 프레임의 segmentation Label 을 제공한다.
![img](http://postfiles5.naver.net/MjAxNzA5MjZfMjIw/MDAxNTA2MzkxOTY0MzQ0.TIcYHkKNp5rJXjsenMI_qTvc_hBxO4IHxCA_7Za8ZgAg.CeoRcR6uFyn2pns3Oh3oP4Y67qmjYM4rdRv2Nhf8WWcg.PNG.sogangori/davidDataset.PNG?type=w1) 



그림) [David Dataset](http://davischallenge.org/code.html)
![img](http://postfiles2.naver.net/MjAxNzA5MjZfMTkz/MDAxNTA2Mzg1NTM1MTAz.L5BeDug7oU16Ua-hsu_li5yHwrs6A7G5DrwG7TE80FAg.twCnaTFCPFQOtf6B0lGRGFutfOYwLpo_mD5kxHKGhecg.PNG.sogangori/f4.PNG?type=w1)

그림) 모델 구조.  Foreground 를 예측하는 Foreground Branch, 윤곽을 예측하는 Contour Branch 의 Two-stream FCN 이다.Ultrametric Contour Map(UMC) 으로 예측된 Contour 와 매칭되는 superpixel 을 계산한다. UMC 는 미분이 가능하므로 네트워크 학습에 방해가 되지 않는다.하나의 superpixel 에서 (1)에서 예측한 Foreground 픽셀이 50% 이상 존재하면 해당 superpixel을 Foreground 로 판정한다.superpixel의 contour(boundary)를 자른다(snappig).

![img](http://postfiles10.naver.net/MjAxNzA5MjZfNzIg/MDAxNTA2Mzg3NjQ2MDU2.SYCncfov9s-nK63jtrDAA8DpESwrM8q4rF8rO_43UhQg.mpZcMdjjV3_wG06Xwp7zljC7PmdIU9BaGoOFJkt-7PEg.JPEG.sogangori/UMC1.PNG?type=w1)  ![img](http://postfiles9.naver.net/MjAxNzA5MjZfMTQ1/MDAxNTA2Mzg3NjU2MTA4.yszieKTL9YX_q1O_vDyuY5QIJ_dmDOU7BbNWbUCqHHIg.OrGLoh0-hZuRkurDFHgmYa3wj9cw8FXzlomXGEsz-l4g.JPEG.sogangori/UMC1.PNG?type=w1)

 

 ![img](http://postfiles2.naver.net/MjAxNzA5MjZfMTA1/MDAxNTA2Mzg1ODc3NjA2.OjdjDKQtA4C09peTWozHeNq70xhpa52T9cZ4VTj7PwMg.Ou24v0yJxe832At-YVbrRJEOQZ964fHOSUOqvklPjPMg.JPEG.sogangori/superpixel.jpg?type=w1)

그림) Ultrametric Contour Map(UMC) 와 SuperPixelUltrametric Definition : D(x,y) <= max{ D(x,z), D(z,y)} ![img](http://postfiles14.naver.net/MjAxNzA5MjZfNyAg/MDAxNTA2Mzg1NTM1MjYw.yM6NjJbvbAMCYcL0SjhflUgtNQ22SdtLYZWGzDcxHY0g.7auB04hIo-D22rPbuu4IsJLmCCC3Uc89t9YFy9GfcvAg.PNG.sogangori/f5.PNG?type=w1)

그림) BS(Boundary Snapping) 을 사용하면 타겟 오브젝트에서 먼곳에서 발생하는 False-Positive 에러를 크게 줄일 수 있다.



2017.04.11 **FastMask: Segment Multi-scale Object Candidates in One Shot**  CVPR 2017
Bbox-based proposal 이 아닌 Segment-based proposal 방식으로 기존 STOA 이상의 성능으로 5~20 배 빠르게 오브젝트 위치 proposal, segmentation 을 수행한다.다양한 scale에 대응하기 위해서는 dense한 이미지 피라미드 샘플링이 필수이다. 때문에 Input Image를 여러 크기로 resize해서 Forward 하는 방법을 사용했었다.이 과정에서 bottleneck 이 발생하므로 이것을 해결하는 간단한 One-shot Segment 를 통해 속도향상을 이뤘다.가중치를 공유하기 때문에 임의로 추가하거나 줄일 수 있는 간단한 neck 모듈을 이용해 이미지 피라미드를 구성한다.또한 Attention Map 을 이용해서 정확한 segmentation 결과를 얻을 수 있다.오브젝트의 카테고리 분류는 하지 않는다.
![img](http://postfiles15.naver.net/MjAxNzA5MjVfMTA5/MDAxNTA2MzE0NDczNTIz.lGOkBBflEDzO0PR6qfbAnHdectb6EH0mV156r3P7VQAg.EdExv31JXxtIQel2s7aORDf_cGV0IxSm3Td5hrYbRYcg.PNG.sogangori/f2_m.PNG?type=w1)

그림) 모델 구조. Neck 부분에 [실제 코드](https://github.com/voidrank/FastMask/blob/master/models/fm-res39.train.prototxt) 구현 과 다른 부분이 있어서 표시해 두었다. BodyNet은 특징 추출기로 Res39 사용, Neck은 이미지 피라미드 인코딩을 수행하며 Head가 예측한다.BodyNet 이후에는 Overhead 가 걸리는 연산이 없다. 몇개의 fc 와 up-sampling 에서의 Deconv 1개가 다이며 conv 는 없다.1x1 컨볼루션으로 Dimensionality Reduction 를 수행하여 이미지 피라미드 특징맵을 구성한다.이미지 피라미드맵의 각각의 해상도의 맵을 개별적으로 슬라이딩 윈도우 방식으로 특징맵을 잘라낸 패치들을 모은다.(Concat dim:0)BN을 수행한 후 Head 모듈을 이용해 각각의 패치로부터 confidence(Objectness probability) 와 segmention map을 얻는다. ![img](http://postfiles5.naver.net/MjAxNzA5MjVfMjAx/MDAxNTA2MzE0NDczMDIz.NBWlahC36Qg5-AWKTmQGhtcxJn27HqSId1G2xUHqQjAg.8bG_KbPahfpEj6CKnYUGsM5XKB_h9Ra3jYJmscgHtAQg.PNG.sogangori/e1_1.PNG?type=w1) ![img](http://postfiles13.naver.net/MjAxNzA5MjVfMTEy/MDAxNTA2MzE0NDczMjE3.YPGb8cJj-CtIuky496JHfINRM6cP-BVdwhbCblGxM9Ag.PwgC09_RaHkodmg6H8ieeuG_kv7FZikl_RLeAasiTPwg.PNG.sogangori/e1_2.PNG?type=w1)

식) Loss 함수. confidence(Objectness) , seg(segmentation), att(attention) 3개의 합. 1(ck)는 Object가 있는 것에 한정. 3개다 Binary Cross Entropy 를 사용한다. ![img](http://postfiles10.naver.net/MjAxNzA5MjVfMTgg/MDAxNTA2MzE0NDczODU3.E__0nao-rCCPURJGq-rX-cfoVf4G3wS9STR_wZ8HLuMg.oZdqHSWyXKUtXI0BtuU4yfG20BLra_vEdLug4B5ABSEg.PNG.sogangori/f4.PNG?type=w1)![img](http://postfiles15.naver.net/MjAxNzA5MjVfMjAw/MDAxNTA2MzE0NTA2OTA4.P8DlFidDcId4Xb7SIbbD67SsVLF8v-fONN8l-W7RbNYg.oDeX9SgpKguOJk7ADYrS3H21kHeDwnzXAM8YHRQUeeAg.PNG.sogangori/f3b_modify.PNG?type=w1)

그림) (좌) Neck 모듈. 이미지 피라미드를 구성하기 위해 AVG Pooling 을 통해 해상도를 낮춘다(Zoom-out). (우) 실제 구현과 다른 부분을 표시했다.
![img](http://postfiles16.naver.net/MjAxNzA5MjVfMTMx/MDAxNTA2MzE0NDc0MTc4.8ssQ2rvfQg9PsiRNhXIbPs54ilu-XPlSLmkOdYupchUg.daQLMBI02BTtYJ0iuHy1F_f5OOj_5FTA-e_Lbw4AYhsg.PNG.sogangori/f5.PNG?type=w1)

그림) Head 모듈. 이미지 피라미드맵의 10x10 패치로부터 Confidence Score(Objectness) 와 Attention Map(오브젝트를 둘러싸는 경계박스), Mask를 구한다.Attention Map은 Feature Map과 요소별로 곱해져서 타겟 오브젝트의 특징값을 키우며, 10x10 크기의 특징맵은 Deconv 를 통해서 40x40 의 마스크 맵이 된다.전체적인 구조는 SSD: Single Shot MultiBox Detector 와 비슷한 것 같다.



2017.04.09  **Deeply Supervised Salient Object Detection with Short Connections**  CVPR 2017
Multy Supervised 학습과 fusion, Short Connection(Concatenate)를 이용해 segmentation 에서 더 높은 성능을 얻을 수 있음을 보여준다.
![img](http://postfiles5.naver.net/MjAxNzA5MjVfNDIg/MDAxNTA2MzE0ODU3NzU1.egxALW9_7iq_F0C4thk8lA6Lu4oFjn_kVKXYFaWcv4Eg.NC9uRkkYC9gAOX10icatRDys2IhkFzWmWqtVi53tx98g.PNG.sogangori/f2.PNG?type=w1) 그림) 다양한 아키텍쳐 (a) Hpyercolumn (b) HED (c,d) 제안하는 아키텍쳐로 Hidden Layer간의 Short Connection(concat)과 그것으로 부터의 loss Layer, fusion 이 보인다.
![img](http://postfiles14.naver.net/MjAxNzA5MjVfMTA3/MDAxNTA2MzE0ODU3OTIx.tkcqno1xDzI6sYmuyXzldsYxkZNp1EN3lnAj773cCfIg.JjwWz30EyTOWZq0UZDjjXX3_gi0C3uZRrFEY0Bn39_0g.PNG.sogangori/f3.PNG?type=w1)![img](http://postfiles15.naver.net/MjAxNzA5MjVfMTUg/MDAxNTA2MzE0ODU4MTEw.iNF9bB2CSqkuTvA3brR2Lxf9zULXPF50BdAs7BeYDIAg.OTOp4Jzx51p3QvSBeMOXrBuHDDkhTVJt2mAjLB-xXggg.PNG.sogangori/f4.PNG?type=w1)그림) 제안하는 구조. 성능 비교를 위해 VGGNet 을 선택했다. 6가지 서로 다른 크기의 Hidden Layer 가 skip을 통해 concat 된다.각 해상도의 예측맵을 bilnear inerpolation 하여 GT와의 CE loss 를 구하고 6개의 예측을 합쳐서 Fusion loss 를 구한다.
![img](http://postfiles10.naver.net/MjAxNzA5MjVfMTMy/MDAxNTA2MzE0ODU4Mjc1.NyNhbv33skLOD7NKlGUb3ew8uKAX6PomDOpgu2Q3AUwg.spYppxAgR8CqtdqjZaPMaXB0q_Ac6o7wvfHrBg2X3MUg.PNG.sogangori/e12.PNG?type=w1) 로스 함수는 fuse 로스와 각각의 side loss의 합이다. ![img](http://postfiles16.naver.net/MjAxNzA5MjVfMTY2/MDAxNTA2MzE0ODU4NDg2.djocsfGoDST4K_59KD-L7PD-QSDOLYdSHnE0U1QRjcsg.OlkzTPE6fiNlKCBS8qlXRnS5ODqOPi5jxUg0SW09Lmog.PNG.sogangori/f1b.PNG?type=w1)

그림) s-out 1~6으로 갈수록 해상도가 작아지면서 선명도가 떨어진다. short connection(skip) 이 없는 HED 보다 성능이 더 좋다. 최종 예측은 fuse와 s-out 2~4 의 평균이다.



2017.04.05  **Not All Pixels Are Equal: Difficulty-aware Semantic Segmentation via Deep Layer Cascade**  CVPR 2017 spotlight paper
Single Network 에서 쉬움-보통-어려움의 난이도를 Cascade 방식으로 처리하여 성능이 높으면서 빠르다.성능면에서 최고는 아니지만 segmentation 이 어려운 char, table, sofa 등의 클래스에 대해서는 높은 IoU를 보인다.그리고 분류 결과의 지표상 성능은 약간 떨어질지 몰라도 사람의 눈으로 봤을 때는 더 자연스러운 것도 자랑이다.![img](http://postfiles12.naver.net/MjAxNzA5MTJfNDUg/MDAxNTA1MjAxNjM4NDgw.FAWuijgFCebkVCbqJiOk2hxFszyWvi19BJSZajXf5a4g.3iSs2t-tHfTlp-o9LUq9v8hBaGhTER959XCJYBCPXtIg.PNG.sogangori/f1.PNG?type=w1)

그림 (위) Segmentation 이 어려운 부분은 대부분 오브젝트의 경계부분이다. (아래) 각 클래스의 난이도 픽셀 비율. (아래 오른쪽)픽셀 경계가 대부분 분류하기 어렵다.
![img](http://postfiles7.naver.net/MjAxNzA5MTJfMTIw/MDAxNTA1MjAyNzI5MDc1.2jnZK907zdR1yYV8ZaTgR2z6vjqV13KkzCve9bng360g.2x50yIREhobMUS2JNQZilDMyxl1gaMCxo_9HQs_uqsEg.JPEG.sogangori/f2a.PNG?type=w1)

그림) 모델 구조. IRNet(Inception-ResNet-v2). 3단계 stage로 구성되어 쉬움-보통-어려움 순서대로 분류해나간다. 각 stage마다 loss를 얻는다.stage-1,2 에서 확률이 0.95 이상으로 분류된 특징은 Region Convolution을 통해 다음 stage로 전달된다.
![img](http://postfiles2.naver.net/MjAxNzA5MTJfMTAz/MDAxNTA1MjAxNjM5MjEw.jrzlSVA9KHvj25Cpdyb84ZDYImpRHJY7C8vCA8chdXcg.KUuyU_oUI_ODSlSGQmhQi5oI5okTa5R9Yxr357FAEqUg.PNG.sogangori/f3a.PNG?type=w1)![img](http://postfiles12.naver.net/MjAxNzA5MTJfMjYg/MDAxNTA1MjAxNjM5MzY5.hH5eWdY11RJREUjb3XCDI6fV4gxxwxWLAElLBcPedQUg.bwsA_DHOpVYe0XJwiH6KWPaIjLexnzKabGNJPIS9d_Mg.PNG.sogangori/f3b.PNG?type=w1)![img](http://postfiles4.naver.net/MjAxNzA5MTJfMjMz/MDAxNTA1MjAxNjM5NTI1.AblsacYQQTq72dKUwQElDmCEfLiRX816qISvRFBMZUUg.Qkh8YArt3TiHnqyGH-30Dy0o3aqF5cBE8nh3w3DtM0sg.PNG.sogangori/f3c.PNG?type=w1)그림) Layer Cascae 

모듈의 구조. (a)는 일반적인 컨볼루션 (b) 관심 영역인 M 에서만 Convolution 하고 바깥쪽은 zero 셋팅한다. (c) 입력 특징 I 와 (b)의 결과를 더한다.2017.03.10 **Deep Image Matting** Adobe
Matting은 Trimap에서 background 와 foreground 를 제외한 unknown 부분에서만 loss 를 구한다.![img](http://postfiles3.naver.net/MjAxNzA5MDhfMTk3/MDAxNTA0ODU4MjQzNTQ2.aTWn9PYOz_Uwta-YELBH0Wkapfna48Vi3DdsieV2fvwg.se_SGVwEDuo1a36ZbnWXrsqan1HeysgfwwRTpFrL-ccg.PNG.sogangori/e1.PNG?type=w1) , ![img](http://postfiles5.naver.net/MjAxNzA5MDhfNjMg/MDAxNTA0ODU4MjQzNDEz.FzJ7jKFQ71yfXo71M1NdMxMdSgDb2P9zA2E3jY8FN1sg.VemAF7fR1i7HOULWAcPcb0KlS8K756szl_-p76ZQU9Ig.PNG.sogangori/e2.PNG?type=w1)식) Alpha-loss , Color-lossAlpha-로스 : GT Matte 와 예측 Matte 의 MSE  Color-로스 : 예측 Matte를 GT의 전경(여자 사진) 에 alpha 채널로 적용 + GT의 배경(야구장 사진) 을 합성(Composition)한것과 입력 영상과의 MSE.2개의 Loss 를 사용해 학습을 안정시키고, cascade 방식으로 서브네트워크를 사용해 예측을 Refinement 한다.
![img](http://postfiles13.naver.net/MjAxNzA5MDhfMjM4/MDAxNTA0ODU4MDc0NjEz.JcLV3cAwfRVnQ1-930UihgELLZpZC1hoKb_xr5MktZAg.NsW3HCOGVyQk1FFBu2grc3WpHEb6ahWuYCZTpN7mkiEg.JPEG.sogangori/Reading_Note_20170316_Matting_0.jpg?type=w1) 



2016.12.05 **Classification with an edge: improving semantic image segmentation with boundary detection** 
boundary 를 이용해서 segmentation 을 할때 더 좋은 결과를 얻을 수 있다.Holistically-Nested Edge Detection 을 regression loss를 사용해서 boundary detector 를 학습시킨다.검출된 boundary는 Input 에 concate 시켜 segmentation network 로 들어간다.boundary 는 다이아몬드 구조체를 사용해서 두껍게 만든다.
![img](http://postfiles8.naver.net/MjAxNzA5MTVfMjY3/MDAxNTA1NDUzMjg3NTky.6DaB-y5wIvHz6uZNYoib9akplcTkbm4DO5xA_8l8a8Yg.bh3SavzMwj0dSjKlSGGSQW-ORzlSTq9KXUo1Dt53x2Mg.PNG.sogangori/f4.PNG?type=w1)그림) 모델 구조 CB:Class Bounday, DEM(Digital elevation model 수치표고모델)CB 는 미리 학습키키고 segmentation 모델을 붙인 이후 fine-tuning 된다.
![img](http://postfiles15.naver.net/MjAxNzA5MTVfMTg0/MDAxNTA1NDUzMjg3NzQz.wbbKKw1wo9o1rEswsLnr_QSjsqQOH5htvflvyDMWhywg.sVY6eRB_mt77pZlmMw0bNayH03xP958G1fi0dJ-Z_CUg.PNG.sogangori/t3.PNG?type=w1)

표) sc1 : scale 1
![img](http://postfiles10.naver.net/MjAxNzA5MTVfNzgg/MDAxNTA1NDUzMjg3OTEz.3i3DFgOZwepIITSV-_fgqXZvUA9zAS5r6hu2CcMN1rMg.OAoiMH0jZfTmERySpKLXP6iAQUgRs-rLt9_Mb0YY524g.PNG.sogangori/t7.PNG?type=w1) 

그림) CB(Class Boundary) 사용시 경계면이 더 선명해진다.2016.12.04 **Pyramid Scene Parsing Network**  CVPR 2017
PSPNet은 cityscapes dataset의 labeling 에서 오랜 기간 Top 순위를 지키고 있다.ResNet 의 최종 출력 Feature Map 에 피라미드 풀링 모듈을 추가하여 좋은 성능을 냈다.
![img](http://postfiles3.naver.net/MjAxNzA5MjVfMjI5/MDAxNTA2MzE1MTk2NzM5.ZEf3ZkjAwojdDwJ7QB_C80fAUJ-n6YQVnNXzVZd_NIIg.dSLkgfYCL595NWa_MNWZTZTLPjAQNjLd_NnnKfOjUYcg.PNG.sogangori/3-Figure3-1.png?type=w1)

그림) ResNet101 backbone 으로 dilated, Pyramid Pooling Module 을 사용한다PPM에서 concatenate ( 지역 특징 (50%) + 전체전역특징(12.5%) + L 전역특징(12.5%) + M 전역특징(12.5%) + S 전역특징(12.5%) )
![img](http://postfiles12.naver.net/MjAxNzA5MjVfODgg/MDAxNTA2MzE1MTk3Mjky.q9WlcbehHfjqGHmh6dEfR35shcwZcy9KtPsAlfVjbzMg.1xrxg5WEwMm23XKNRFhoLEZi-LxFQQ4N-p18f6NjD-Ug.PNG.sogangori/resnet.PNG?type=w1)

그림) 50~269 레이어에서 깊이와 성능이 비례한다.



2016.11.05 **LAYER RECURRENT NEURAL NETWORKS** Weidi Xie, Alison Noble & Andrew Zisserman Department of Engineering Science, University of Oxford, UK 
CNN과 RNN 의 결합. RNN 을 모듈화 해서 간편하게 사용하여 Segmentation 성능을 높일 수 있음을 보인다.![img](http://postfiles2.naver.net/MjAxNzEwMjdfMTg2/MDAxNTA5MDgzNzExMjM5.-Lx-BnIQReEpj9wk6fgAEYRDO67NIlsraVSo6j0KulIg.3FI4F-IXdAksSOeyNR_AqYIWB9mEVoVg8WcZJBHNf1og.PNG.sogangori/f1.PNG?type=w1)![img](http://postfiles5.naver.net/MjAxNzEwMjdfMzMg/MDAxNTA5MDgzNzExNDEx.U2YjcoZQRFwI6OnQQtzbTXSpcvmAIQqeoKf5bMCjXmAg.2Tl3yBmA7o4mx_HZz8WBHhZ9_rL4x0EV9fL3yjPwhVUg.PNG.sogangori/f2a.PNG?type=w1)![img](http://postfiles15.naver.net/MjAxNzEwMjdfMTA3/MDAxNTA5MDgzNzExNTg3.BIrVno4IP7z5Vm3WARKkRcsW4C-jO0q8JNu4gA3skLwg.JuvG0_hzmbwDJM5JQZh4I62yz__E9PfmlE9JQs5ZjCIg.PNG.sogangori/f2b.PNG?type=w1)

그림 왼쪽. 기본 구조. (B)는 모든 픽셀에서 채널 데이터를 이용해 양방향 수평 RNN을 수행한다. 양방향 결과값 2개는 Concat하거나 더한다. 아래쪽 그림에서 주황색 가로 선은 가운데 검은 점의 receptive field이다. 양방향이 아니고 -> 방향만 했다면 검은 점의 receptive field는 좌측뿐이었을 것이다.(B)의 결과물을 양방향 수직 RNN을 수행하게 되면 가운데 검은 점의 receptive field는 영상 전체가 된다.

 그림 오른쪽. L-RNN 모듈 구조. CNN Residual 모듈과 비슷한 방식으로 사용한다. 
![img](http://postfiles5.naver.net/MjAxNzEwMjdfMjEx/MDAxNTA5MDgzNzExNzQ4.90JtUrdCexND8sICJ80oy1oJI9SM__Z7mpYYL7pSi84g.edNcbP9fIZj7W2_1Iv-YnxAK8-b7idOJUqEYKIPOfX0g.PNG.sogangori/t1.PNG?type=w1)

표1. CIFAR-10 을 위한 네트워크 설계 실험
![img](http://postfiles4.naver.net/MjAxNzEwMjdfMjkw/MDAxNTA5MDgzNzExOTc1.4CwhR_plyrpeS7nmpDPcXY6UvkES2k5WGdSy4sXeTf0g.okIRE0-7RjsBbcQDm_UloN0v2l-iqn7SUkyQmLz5Sasg.PNG.sogangori/t2.PNG?type=w1) 

표2. CIFAR-10 성능 결과. 좋은 성능이지만 ResNet-164와 Dense Net 보다는 낮다.
참고 - [라온피플 머신러닝 아카데미](http://laonple.blog.me/221045380560) 



2016.7.15 **DSD: Dense-Sparase-Dense Training For Deep Neural Networks** ICLR 2017
정칙화(regularize) 와 성능에 도움을 주는 학습 방법으로 CNN/RNN/LSTM 에서 성능 향상이 일어나는 것을 확인했다.0에 가까운 파라미터를 일시적으로 제외시키는 Spare 학습방법과 모든 파라미터를 이용해 학습시키는 일반적인 Dense 학습 방법을 반복한다.파라미터의 히스토그램에서 0을 기준으로 나타나는 대칭성을 깨트려서 더 좋은 분포로 학습될 수 있게 한다.
![img](http://postfiles12.naver.net/MjAxNzA5MTFfMjI4/MDAxNTA1MDk2MjY0NTM1.js11iY4mqvk0H5gohzUwyZQrJd3nahtjTVHDi8dvHbYg.-JouxRIKfKpy9BKx8z6aqCdirEbyayUPC03aWrdCeQEg.PNG.sogangori/fig1.PNG?type=w1)

그림) Dense -> Sparse -> Dense 학습 방법. 0에 가까운 parameters 을 Pruning 한다.
![img](http://postfiles9.naver.net/MjAxNzA5MTFfMTc4/MDAxNTA1MDk2MjY0ODI5.JNgz05FgqhlXbDKtlycbMBM5heZWg-gXw5u_brEGQ_Yg.X6g635CABHs4TZ8vvetS1rS434gLbt_HPo4dWYcvMA0g.PNG.sogangori/fig2.PNG?type=w1) 

그림) 특정 레이어의 가중치 히스토그램. 0에 가까운 파라미터들이 Pruning되어 학습이 진행된 후 제거되었던 파라미터들을 0으로 복원시키고 Dense 학습을 시켰다.



2016.03.31  **Object Boundary Guided Semantic Segmentation** 
segmentation 에서 오브젝트 Boundary를 가이드로 사용하면 더 좋은 성능을 얻을 수 있음을 보인다.segmentation label 로부터 배경, 경계, 오브젝트 내부의 3가지 Boundary 라벨을 생성한다.
![img](http://postfiles9.naver.net/MjAxNzA5MTVfMTc2/MDAxNTA1NDUwODMxNzI3.bMB5Hdv1pmqQSjMh_OkANww8Q7uo-_4zyONxzL8bUSEg.ZnbMstbN_BHHTdrfnyaCjS7FsJfKxmblwznsrMoiyUIg.PNG.sogangori/f1.PNG?type=w1)

그림) 3개의 네트워크로 구성된다. Stage-1의 FCN, Stage-2의 OBP(Object Boundary Proposal) FCN, stage-3의 OBG_Masking.1,2 따로 학습시킨 후, 모두 연결해서 3을 학습한다. softmax loss function을 사용한다.
![img](http://postfiles3.naver.net/MjAxNzA5MTVfMTYw/MDAxNTA1NDUwODMyMzQz.6mW5WU3uGyf7RS3qaHXJfPk3Yv77K8lVueWfpFLx-uQg.7bzcbZ1zx8U26T1iYG1mmqAsxldcpinsw0_dguiob5Ig.PNG.sogangori/t2.PNG?type=w1) 

표) 성능 비교. boundary width 2의 Object Boundary Guide 모델의 성능이 가장 좋다.



2016.03.19 **Brain tumor segmentation with Deep Neural Networks**  
MRI 영상에서 악성 종양을 찾아낸다. 다양한 방식의 cascade 네트워크를 구성해서 실험했다.![img](http://postfiles5.naver.net/MjAxNzA5MDhfMjA2/MDAxNTA0ODU5OTEzODkx.ZPyFxESzaSUkYsyF7bK3S57hEmog76J2HqFbCHtwtJEg.A3gEsyGZTSkh38l7tU8vBURLvnwsZUxYfwfpgyH8Q_og.PNG.sogangori/5-Figure2-1.png?type=w1)

그림) Two-pathway CNN architecture



2016.11.25 **Semantic Segmentation using Adversarial Networks** FAIR
Segmentation 을 위해 Adversarial Network를 정칙화로 사용해서 더 높은 성능을 얻을 수 있음을 보여준다.![img](http://postfiles7.naver.net/MjAxNzA5MThfMjA3/MDAxNTA1NzE2NjkwMjQ0.OZJP8S1epaO4MK4LIgQJiDOPtTSW5C3CGPwcAAUuQDYg.lrXofcKQEvjQ0m89HYDY3kEuJWg2F4mXi0mA069spFUg.PNG.sogangori/f1.PNG?type=w1)

그림1) 전체 구조. Segmentor 는 class 확률맵을 예측한다. Adversarial network 는 Input과 확률맵/GT를 받아 1/0 을 예측한다.![img](http://postfiles16.naver.net/MjAxNzA5MThfMTEy/MDAxNTA1NzE2NjkwNDI0.i4olDQVImmU_lwpJ4yxvCYGkWpQHtCJ6GYaeiL2SMO4g.ETvuTxnhw1E63Ykf87ld6apn2EJfDbN3ak8WER6gyiQg.PNG.sogangori/f2.PNG?type=w1)

그림2) GT를 그냥 넣어서는 성능 향상 효과가 없어서, Input RGB와 GT(혹은 확률맵)을 곱해서 Adversarial 에게 feed 한다.Input RGB 3채널 과 GT의 C개 채널이 각각 곱해져서 C 개의 특징맵이 된다.
![img](http://postfiles6.naver.net/MjAxNzA5MThfNzgg/MDAxNTA1NzE2NjkwNTcw.xrbsucG20CsYPaO-1KbsiGOQPYvUbkwU53n85W3uWsog.oNzou-UlKvFgEmlkwcy-vzL9mi1SuIphR8mtigUXAzAg.PNG.sogangori/f3.PNG?type=w1)

그림3) 1번째 행은 adversarial 없이 학습한 예측맵이다. 2번째 행은 adversarial과 같이 학습된 예측맵이다.
![img](http://postfiles14.naver.net/MjAxNzA5MThfMzAw/MDAxNTA1NzE2NjkwNzQ4.1MYSqmcZxYEjYzWPo16PD6S3RgZbSZAjqPluL1_27Ycg.17s603lHvSb9ynLekf-e-cIWpTj94HaW2qim0-FLqlQg.PNG.sogangori/f4.PNG?type=w1) 

그림4) adversarial 사용 유무 성능 비교



2015.10.04  **Holistically-Nested Edge Detection**  University of California
Deep Supervise Net을 이용(auxiliary loss)하여 해상도별 엣지를 예측하고 fusion 해서 최종 엣지를 예측한다.![img](http://postfiles11.naver.net/MjAxNzA5MjJfMjE0/MDAxNTA2MDU1Mzk1Mzc0._G76O0rFlAf60EgtgjuIYVVPlUQXfHIVNol_OtLPKyMg.-iGRFMKq4CO1wuIWdxIaQnWm6arf4bYuWLEazKafTxEg.PNG.sogangori/hed%60.PNG?type=w1)

그림) (a) multi-stream (b) skip-layer (c) multi-scale inputs (d) multi network (e) 제안모델 multiple side output

![img](http://postfiles12.naver.net/MjAxNzA5MjJfMjE4/MDAxNTA2MDU1Mzk1MjMy.d_NrcVFvteez2PNMFIcadKN_tTNe-CMCo1nEPlOzowYg.zy2x7gn20XEnnj4rwiaNfcPxdLQkkDUVTkfegvHPQDwg.PNG.sogangori/f3.PNG?type=w1)

그림) 네트워크 구조. 다양한 해상도에서 각각 엣지를 예측하고 인터폴레이션해서 gt 와 비교한다. side-output1~5는 concat 으로 fuse 하여 gt 와 비교. 최종적으로 모든 예측의 평균을 구한다.
![img](http://postfiles4.naver.net/MjAxNzA5MjJfMjc5/MDAxNTA2MDU1Mzk1MDIw.dw-CFlbkqPd9jmRchT-8OFcC-dnzdQ0hhHfI8CquykIg._8Rsi77K4JTzbIE-zxPw7tAUP4hv-pd7AXZHR-XcIVMg.PNG.sogangori/e6.PNG?type=w1) 



2015.3.18 **U-Net: Convolutional Networks for Biomedical Image Segmentation** 
ISBI cell tracking challenge 2015 Winnerskip layer, up-conv 를 사용한 심플한 네트워크를 디자인, 세포막 분리 작업에서 높은 정확도를 얻을 수 있었다.
![img](http://postfiles5.naver.net/MjAxNzA5MDhfMzYg/MDAxNTA0ODU5NDkwMzc1.-h07TIaj0WreJnsk5q-HdqhepfVoIVL_R2jggUQRJTAg.i37428rdxYHIFlY6IEyQ0wEIVj0POz-9e3b0R3uk1NEg.JPEG.sogangori/u-net-architecture.png?type=w1)

그림) Valid Convolution을 사용한다
![img](http://postfiles3.naver.net/MjAxNzA5MDhfMTky/MDAxNTA0ODU5Mjg5MTE4._Y031GCXM1n_Vx_SsY3U4eKB17m4oqvDKbwwMbQ9mhYg.KXxQlE4Dk8TNwdAir0ypXjA5OWN7YoxbNCNABrkoX5Eg.PNG.sogangori/augment.PNG?type=w1)그림) Deformation 으로 Augment 해서 다양한 형태의 변형에 대응했다.



2015 **Recurrent Convolutional Neural Network for Object Recognition** CVPR2015
Recurrent CNN 을 제안한 의미있는 논문. 일반적인 RNN 이 아니다.정적 이미지를 대상으로 Recurrent 한 방식으로 Convolution 연산을 한다.
![img](http://postfiles13.naver.net/MjAxNzEwMzFfNzEg/MDAxNTA5NDM4NzM1Mjc4.zF-2-gmD4pW7fysBZsx6NBLk0SQ28JYFcfeBeLpn6FMg.P4mpcipB_pOWxOY3JDcvtTQcQTCBVkpilePgnz__mNsg.PNG.sogangori/f3.PNG?type=w1) ![img](http://postfiles2.naver.net/MjAxNzEwMzFfMTQ2/MDAxNTA5NDM4NzM1MTI2.rpiveBzBL0RblUsxrVqTxjX1F7tvZ1L435VEx9-VhdQg.e6Mrqa9nRPs8OIgHiJ47eFTjQr6YqsGOZvkRFwB7e5gg.PNG.sogangori/e1.PNG?type=w1)

그림) 좌측의 u 는 원래의 input 이고, 우측의 x 는 원래의 input인 u를 convolution 한 recurrent input 이다.이제 와서 보면 Residual 과 형태가 비슷하다고 볼 수 있는것 같다.