[TUTORIAL](https://blog.lunit.io/category/tutorial/)[2017년 APRIL 27일](https://blog.lunit.io/2017/04/27/style-transfer/)

# Style Transfer

본문 링크 : https://blog.lunit.io/2017/04/27/style-transfer/

## Introduction

![스크린샷 2017-05-16 오후 1.56.54.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-1-56-54.png?w=520&h=392)Results from **“Image Style Transfer Using Convolutional Neural Networks”**

Style transfer란, 두 영상(content image & style image)이 주어졌을 때 그 이미지의 주된 형태는 content image와 유사하게 유지하면서 스타일만 우리가 원하는 style image와 유사하게 바꾸는 것을 말합니다. 위 그림에서는 주택사진을 content image로 주고 다른 화가의 작품들을 style image로 주었는데, 주택의 형태와 배치는 유지되면서 화풍만 각 작품과 유사하게 바뀐 것을 볼 수 있습니다.

Neural network를 이용한 Style transfer의 연구는 아래와 같이 두 분류로 나눌 수 있습니다.

- Image-net 등의 데이터로 미리 학습된(pre-trained) 네트워크를 이용한 방법
  - Content image와 style image를 네트워크에 통과시킬 때 나온 각각의 feature map을 저장하고, 새롭게 합성될 영상의 feature map이 content image와 style image로부터 나온 feature map과 비슷한 특성을 가지도록 영상을 최적화합니다.
  - 장점: 이미지 2장(content image & style image)으로 style transfer가 가능하다.
  - 단점: 매번 이미지를 새롭게 최적화 해야 하므로 시간이 오래걸린다.

- Style transfer network를 학습시키는 방법
  - 서로 다른 두 도메인(예를 들면, 풍경 사진들과 모네의 그림들)의 영상들이 주어졌을 때 한 도메인에서 다른 도메인으로 바꿔주도록 학습 시킵니다.
  - 장점: 네트워크를 한 번 학습시킨 후에 새로운 이미지에 적용할 때는 feed forward만 해주면 된다.
  - 단점: 새로운 네트워크를 학습해야 하므로 각 도메인 별로 다수의 영상이 필요하며, 학습에 시간이 소요된다.

이번 포스트의 1-3장에서는 첫번째 방법에 대한 소개와 분석을, 4장에서는 GAN을 이용한 Style transfer network학습 방법을 소개합니다.

------

## Contents

소개드릴 논문은 5개이며, 아래와 같이 5개의 장으로 나누어 작성하였습니다.

1. Image Style Transfer Using Convolutional Neural Networks ![{}^{[1]}](https://s0.wp.com/latex.php?latex=%7B%7D%5E%7B%5B1%5D%7D&bg=ffffff&fg=000000&s=0)

   - Pre-trained network의 feature map을 이용한 style transfer 방법론을 제시

2. Extensions

   - 

     의 단점을 보완하고 목적함수를 확장

     - Stable and Controllable Neural Texture Synthesis and Style Transfer Using Histogram Losses ![{}^{[2]}](https://s0.wp.com/latex.php?latex=%7B%7D%5E%7B%5B2%5D%7D&bg=ffffff&fg=000000&s=0)
     - Deep Photo Style Transfer ![{}^{[3]}](https://s0.wp.com/latex.php?latex=%7B%7D%5E%7B%5B3%5D%7D&bg=ffffff&fg=000000&s=0)

3. Demystifying Neural Style Transfer

    



   - Style transfer가 feature vector의 분포(distribution)를 맞춰주는 것과 동일함을 보이고, domain adaptation과의 유사성을 발견

4. Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks ![{}^{[5]}](https://s0.wp.com/latex.php?latex=%7B%7D%5E%7B%5B5%5D%7D&bg=ffffff&fg=000000&s=0)

   - GAN을 이용한 style transfer

5. Conclusion

[1] Image Style Transfer Using Convolutional Neural Networks, Gatys et al.
[2] Stable and Controllable Neural Texture Synthesis and Style Transfer Using Histogram Losses, Risser et al.
[3] Deep Photo Style Transfer, Luan et al.
[4] Demystifying Neural Style Transfer, Li et al.
[5] Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks, Zhu et al.

------

## 1. Image Style Transfer Using Convolutional Neural Networks

![스크린샷 2017-05-16 오후 1.50.07.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-1-50-07.png?w=1400)Image Style Transfer Using Convolutional Neural Networks

[1]에서 제시한 방법은 내용(Content)을 담고있는 ![I_{content}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)와 스타일을 담고있는  ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)를 입력으로 받습니다. 그리고 이 두 영상으로 부터 각각의 특성을 담고있는 새로운 영상 ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0) 을 만들어 내는 것이 목적입니다.

이를 위하여 Image-net 등으로 미리 학습된(pre-trained) 네트워크에서![I_{content}, I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D%2C+I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)각각의 feature map을 추출합니다. 그리고![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)의 feature map이![I_{content}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)의 feature map과는 content가 비슷해지도록,  ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)과는 style이 비슷해지도록  ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)의 픽셀들을 optimize함으로써 우리가 원하는 영상을 얻을 수 있습니다 (모든 과정에서 네트워크의 변수에 대한 학습은 일어나지 않습니다).

![S_l](https://s0.wp.com/latex.php?latex=S_l&bg=ffffff&fg=000000&s=0): ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)의 ![l](https://s0.wp.com/latex.php?latex=l&bg=ffffff&fg=000000&s=0)번째 layer의 feature map
![P_l](https://s0.wp.com/latex.php?latex=P_l&bg=ffffff&fg=000000&s=0): ![I_{content}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)의 ![l](https://s0.wp.com/latex.php?latex=l&bg=ffffff&fg=000000&s=0)번째 layer의 feature map
![F_l](https://s0.wp.com/latex.php?latex=F_l&bg=ffffff&fg=000000&s=0): ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)의 ![l](https://s0.wp.com/latex.php?latex=l&bg=ffffff&fg=000000&s=0)번째 layer의 feature map

이미지 사이의 content간의 차이는 content loss, ![L_{content}](https://s0.wp.com/latex.php?latex=L_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)로 측정하는데, 주로 정보의 추상화가 많이 이루어진 high level layer의 feature map으로 비교하게 됩니다. ![l](https://s0.wp.com/latex.php?latex=l&bg=ffffff&fg=000000&s=0)번째 layer에서 content loss는 다음과 같이 feature map 간 차의 [Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)의 제곱으로 정의됩니다.

![L_{content} = \sum (F_l - P_l)^2](https://s0.wp.com/latex.php?latex=L_%7Bcontent%7D+%3D+%5Csum+%28F_l+-+P_l%29%5E2&bg=ffffff&fg=000000&s=0)

Feature map을 직접 비교하는 content loss와는 달리 style loss, ![L_{style}](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)은 각 feature map에 대해 [Gram matrix](https://en.wikipedia.org/wiki/Gramian_matrix)를 구하고, Gram matrix 간 차의 Frobenius norm의 제곱으로 정의됩니다. Style loss는 low layer부터 high layer까지 다양한 수준에서 loss를 계산하고 weighted sum하여 ![L_{style}](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)로 정의합니다.

![F_l](https://s0.wp.com/latex.php?latex=F_l&bg=ffffff&fg=000000&s=0)이 ![[c_l\times w_l\times h_l]](https://s0.wp.com/latex.php?latex=%5Bc_l%5Ctimes+w_l%5Ctimes+h_l%5D&bg=ffffff&fg=000000&s=0) 행렬일 때(![c_l = number\ of\ channels](https://s0.wp.com/latex.php?latex=c_l+%3D+number%5C+of%5C+channels&bg=ffffff&fg=000000&s=0)),  Gram matrix의 크기는 ![[c_l\times c_l]](https://s0.wp.com/latex.php?latex=%5Bc_l%5Ctimes+c_l%5D&bg=ffffff&fg=000000&s=0)로, feature map의 channel간 activation의 correlation 정보를 담고 있습니다.

![L_{style}^l = \sum (Gram(F_l) - Gram(S_l))^2](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D%5El+%3D+%5Csum+%28Gram%28F_l%29+-+Gram%28S_l%29%29%5E2&bg=ffffff&fg=000000&s=0)

![L_{style} = \sum w_lL_{style}^l](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D+%3D+%5Csum+w_lL_%7Bstyle%7D%5El&bg=ffffff&fg=000000&s=0)

최종 목적함수는 다음과 같이 정의됩니다.

![\min\limits_{I_{output}} L_{total}=\min\limits_{I_{output}}(\alpha L_{content}+\beta L_{style})](https://s0.wp.com/latex.php?latex=%5Cmin%5Climits_%7BI_%7Boutput%7D%7D+L_%7Btotal%7D%3D%5Cmin%5Climits_%7BI_%7Boutput%7D%7D%28%5Calpha+L_%7Bcontent%7D%2B%5Cbeta+L_%7Bstyle%7D%29&bg=ffffff&fg=000000&s=0)

여기서 ![\alpha](https://s0.wp.com/latex.php?latex=%5Calpha&bg=ffffff&fg=000000&s=0)와 ![\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=000000&s=0)의 비율에 따라서 ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)의 특징이 달라지는데, 아래 그림과 같이 ![\beta](https://s0.wp.com/latex.php?latex=%5Cbeta&bg=ffffff&fg=000000&s=0)가 상대적으로 더 클수록 ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)는 ![I_{content}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)의 형태를 유지하지 못하고 뭉개지며 ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)과 비슷한 texture를 보여줍니다.

![스크린샷 2017-05-16 오후 3.44.01.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-3-44-01.png?w=395)Results from different loss ratio ![r](https://s0.wp.com/latex.php?latex=r&bg=ffffff&fg=000000&s=0). ![(r = \beta/\alpha)](https://s0.wp.com/latex.php?latex=%28r+%3D+%5Cbeta%2F%5Calpha%29&bg=ffffff&fg=000000&s=0)

또한, 각각의 loss에 사용되는 layer의 위치와 조합을 바꾸면 어떻게 되는지, ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)의 initialization에 따라 어떻게 달라지는지도 논문에서 다루고 있습니다.

------

## 2. Extensions

### [2] Stable and Controllable Neural Texture Synthesis and Style Transfer Using Histogram Losses

[1]의 style transfer를 이용한 텍스쳐 합성을 할 때 생기는 불안정성(instability)을 보완해줄 수 있는 error term을 추가한 연구입니다.

Style transfer에서 ![I_{content}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)를 주지 않고 ![L_{style}](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)만 이용하여 같은 패턴을 가진 더 큰 이미지를 합성할 수 있는데, 이 때 [1]에서 제시된 Loss를 사용하면 아래 그림의 가운데 열과 같이 많은 부분이 뿌옇고 흐리게 나옵니다.

![스크린샷 2017-05-16 오후 4.12.40.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-4-12-40.png?w=433)Instabilities in texture synthesis of Gatys et al.

[2]에서는 이러한 불안정성의 원인을 Gram matrix에서 찾습니다. 아래 그림과 같이 평균, 분산이 매우 다른 feature map이 같은 gram matrix를 가질 수 있다는 것이 그 이유입니다.

**![스크린샷 2017-05-16 오후 4.29.25.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-4-29-25.png?w=370)**

따라서 이 연구에서는 gram matrix를 이용한 loss에 더하여 [histogram matching](https://en.wikipedia.org/wiki/Histogram_matching)으로 feature map의 분포를 맞춰주는 histogram loss, ![L_{hist}](https://s0.wp.com/latex.php?latex=L_%7Bhist%7D&bg=ffffff&fg=000000&s=0)를 추가해 주었습니다(Histogram matching에 대해서는 링크를 참조해 주시기 바랍니다). 우선, ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)으로부터 계산된 feature map ![F_l](https://s0.wp.com/latex.php?latex=F_l&bg=ffffff&fg=000000&s=0)과 ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)의 feature map ![S_l](https://s0.wp.com/latex.php?latex=S_l&bg=ffffff&fg=000000&s=0)이 있을 때, ![F_l](https://s0.wp.com/latex.php?latex=F_l&bg=ffffff&fg=000000&s=0)을 ![S_l](https://s0.wp.com/latex.php?latex=S_l&bg=ffffff&fg=000000&s=0)에 histogram matching 한 ![R(F_l)](https://s0.wp.com/latex.php?latex=R%28F_l%29&bg=ffffff&fg=000000&s=0)을 구합니다. 그리고 ![L_{hist}](https://s0.wp.com/latex.php?latex=L_%7Bhist%7D&bg=ffffff&fg=000000&s=0)를 다음과 같이 정의합니다.

![L_{hist}^l=\sum (F_l - R(F_l))^2](https://s0.wp.com/latex.php?latex=L_%7Bhist%7D%5El%3D%5Csum+%28F_l+-+R%28F_l%29%29%5E2&bg=ffffff&fg=000000&s=0)

![Histogram_matching.png](https://bloglunit.files.wordpress.com/2017/04/histogram_matching.png?w=297&h=203)An example of histogram matching

Histogram loss를 적용한 결과, 안정적인 texture synthesis 결과를 얻었다고 합니다. 논문에서는 Histogram loss 외에 그림의 영역을 나누어서 style transfer 하는 localized style transfer도 다루고 있습니다.

### **[3] Deep Photo Style Transfer**

[1]을 이용하여 실제 사진을 style transfer 할 때, 작은 detail 들에 왜곡이 일어나게 되는데, 이를 막아주는 loss term을 추가한 연구입니다. Style transfer 결과를 확대한 아래 그림을 보면, [1]을 이용한 경우 창문이나 건문의 형태가 조금씩 왜곡되어 실제 detail과는 많이 달라진 것을 관찰할 수 있습니다.

![스크린샷 2017-05-16 오후 5.01.12.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-5-01-12.png?w=560&h=214)



![스크린샷 2017-05-16 오후 5.01.57.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-5-01-57.png?w=289&h=316)Results using [1] (Middle column) shows distortions, while [3] (Right column) preserves the photorealism of the output.



의 세부적인 모양과 특징을 보존하기 위해 이 연구에서는 Style transformation이 locally affine transform이 되도록 하는 loss term을 추가하였습니다.



이를 살펴보기에 앞서, Affine transformation이 어떤 것인지 알아보도록 하겠습니다. 어떤 영상 ![X](https://s0.wp.com/latex.php?latex=X&bg=ffffff&fg=000000&s=0)에 transform ![f](https://s0.wp.com/latex.php?latex=f&bg=ffffff&fg=000000&s=0)를 적용하여 ![Y](https://s0.wp.com/latex.php?latex=Y&bg=ffffff&fg=000000&s=0)를 얻는데 이때 ![f](https://s0.wp.com/latex.php?latex=f&bg=ffffff&fg=000000&s=0)가 [Affine transformation](https://en.wikipedia.org/wiki/Affine_transformation)이라면, ![f:X\rightarrow Y](https://s0.wp.com/latex.php?latex=f%3AX%5Crightarrow+Y&bg=ffffff&fg=000000&s=0)는 ![y_i=\textbf{M}x_i+\textbf{b}](https://s0.wp.com/latex.php?latex=y_i%3D%5Ctextbf%7BM%7Dx_i%2B%5Ctextbf%7Bb%7D&bg=ffffff&fg=000000&s=0)의 형태인 것을 말합니다.

![(x_i=[r_i, g_i, b_i],\ rgb\ value\ of\ i\ th\ pixel\ of\ image\ X,\ \textbf{M}\ is\ a\ linear\ transformation,\ \textbf{b}\ is\ a\ rgb\ vector)](https://s0.wp.com/latex.php?latex=%28x_i%3D%5Br_i%2C+g_i%2C+b_i%5D%2C%5C+rgb%5C+value%5C+of%5C+i%5C+th%5C+pixel%5C+of%5C+image%5C+X%2C%5C+%5Ctextbf%7BM%7D%5C+is%5C+a%5C+linear%5C+transformation%2C%5C+%5Ctextbf%7Bb%7D%5C+is%5C+a%5C+rgb%5C+vector%29&bg=ffffff&fg=000000&s=0)

Affine transformation의 예로는 color image를 grayscale image로 바꿔주는 transform이 있고(eg. ![y_i=0.2989r_i + 0.5870g_i + 0.1140b_i](https://s0.wp.com/latex.php?latex=y_i%3D0.2989r_i+%2B+0.5870g_i+%2B+0.1140b_i&bg=ffffff&fg=000000&s=0), 출처: [MATLAB](https://www.mathworks.com/help/matlab/ref/rgb2gray.html)), 사진을 sephia tone으로 바꿔주거나 rgb 중 특정 채널값을 linear하게 증가/감소시키는 것도 모두 affine transform에 속합니다. Affine transformation은 전체 픽셀에 대하여 동일한 transformation을 수행하기 때문에, 적절한 style transform function이 될 수는 없습니다(하늘이든 바다든 같은 색이기만 하면 output에서도 동일한 색으로 mapping됩니다).

하지만 전체 이미지에서 작은 영역을 떼어서 해당 부분의 style transformation을 생각해 보면, affine transformation으로 근사할 수 있을 것이라는 것이 이 연구의 아이디어입니다. 예를 들면, 아래 사진에서 창문부분의 style transformation은 검은색을 하얀색으로, 하얀색을 검은색으로 바꿔주는 affine transformation으로 근사할 수 있을 것입니다.

![스크린샷 2017-05-16 오후 6.05.52.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-6-05-52.png?w=1400)![스크린샷 2017-05-16 오후 6.06.06.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-6-06-06.png?w=165&h=174)

이를 위해 기존 연구(A closed-form solution to natural image matting, *Levin et al.*)의 loss function을 이용하였고, ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)으로의 transformation을 locally affine transformation에 가깝게 만들어 ![I_{content}](https://s0.wp.com/latex.php?latex=I_%7Bcontent%7D&bg=ffffff&fg=000000&s=0)의 세부적인 모양도 유지하면서 style을 성공적으로 바꿀 수 있음을 보였습니다.

이 논문을 다룬 짧은 영상도 함께 공유합니다.



------

## 3. Demystifying Neural Style Transfer

[4]에서는 [1]에서 제시한 방법론과 domain adaptation의 연결고리를 찾아 연결한 논문입니다. Gram matrix에 대한 ![L_{style}](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)을 최소화하는 것과, ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)과 ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)에서 나온 feature map의 분포(distribution) 간 거리를 최소화 하는 것이 같음을 보였습니다.

우선 feature map의 분포를 정의하고 난 뒤에, 분포 사이의 거리를 측정하는 방법들에 대해 알아보겠습니다.

Feature map의 분포라는 것은, ![[c_l\times w_l\times h_l]](https://s0.wp.com/latex.php?latex=%5Bc_l%5Ctimes+w_l%5Ctimes+h_l%5D&bg=ffffff&fg=000000&s=0) feature map을  ![w_l\times h_l](https://s0.wp.com/latex.php?latex=w_l%5Ctimes+h_l&bg=ffffff&fg=000000&s=0)개의 multivariate random sample ![\textbf{v} \in \mathbb{R}^{c_l},\ where\ \textbf{v} \sim \mathbb{P}_X](https://s0.wp.com/latex.php?latex=%5Ctextbf%7Bv%7D+%5Cin+%5Cmathbb%7BR%7D%5E%7Bc_l%7D%2C%5C+where%5C+%5Ctextbf%7Bv%7D+%5Csim+%5Cmathbb%7BP%7D_X&bg=ffffff&fg=000000&s=0) 로 봤을 때 ![\mathbb{P}_X](https://s0.wp.com/latex.php?latex=%5Cmathbb%7BP%7D_X&bg=ffffff&fg=000000&s=0)를 의미합니다. Style transfer에서, ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)로부터 계산된 ![l](https://s0.wp.com/latex.php?latex=l&bg=ffffff&fg=000000&s=0)번째 layer의 feature map은 크기가 ![[c_l\times w_l^s\times h_l^s]](https://s0.wp.com/latex.php?latex=%5Bc_l%5Ctimes+w_l%5Es%5Ctimes+h_l%5Es%5D&bg=ffffff&fg=000000&s=0)입니다. 따라서 ![\mathbb{P}_l^s](https://s0.wp.com/latex.php?latex=%5Cmathbb%7BP%7D_l%5Es&bg=ffffff&fg=000000&s=0)를 따르는 ![w_l^s\times h_l^s](https://s0.wp.com/latex.php?latex=w_l%5Es%5Ctimes+h_l%5Es&bg=ffffff&fg=000000&s=0)개의 sample이 있고, 마찬가지로 ![I_{output}](https://s0.wp.com/latex.php?latex=I_%7Boutput%7D&bg=ffffff&fg=000000&s=0)로부터 나온 ![l](https://s0.wp.com/latex.php?latex=l&bg=ffffff&fg=000000&s=0)번째feature map에는 ![\mathbb{P}_l^o](https://s0.wp.com/latex.php?latex=%5Cmathbb%7BP%7D_l%5Eo&bg=ffffff&fg=000000&s=0)를 따르는 ![w_l^o\times h_l^o](https://s0.wp.com/latex.php?latex=w_l%5Eo%5Ctimes+h_l%5Eo&bg=ffffff&fg=000000&s=0)개의 sample이 있습니다.

이렇게 [두 분포가 주어졌을 때, 둘 사이의 거리(Statistical distance)를 측정하는 방법](https://en.wikipedia.org/wiki/Statistical_distance)에는 아래와 같은 여러 정의들이 많이 쓰입니다.

- Kullback–Leibler divergence
- Total variation distance (sometimes just called “the” statistical distance)
- Rényi’s divergence
- Jensen–Shannon divergence
  - GAN의 목적함수가 real data의 distribution과 (generated) fake data의 distribution 사이의 JS divergence를 minimize 합니다
- Wasserstein metric: also known as the Kantorovich metric, or earth mover’s distance
  - Wasserstein GAN의 목적함수가 real data의 distribution과 (generated) fake data의 distribution 사이의Wasserstein metric을 minimize 합니다
- The maximum mean discrepancy which is defined in terms of the kernel embedding of distributions

우리가 주목할 것은 가장 마지막에 있는 MMD(Maximum Mean Discrepancy)입니다. (MMD에 대한 자세한 설명은 다음 링크 참고: [Summary and Discussion of: “A Kernel Two-Sample Test”](http://www.stat.cmu.edu/~ryantibs/journalclub/mmd.pdf))

![M\!M\!D(P, Q)=\sup\limits_{\|f\|_\mathcal{H} \leq 1}(\mathbb{E}_X[f(X)] - \mathbb{E}_Y[f(Y)])](https://s0.wp.com/latex.php?latex=M%5C%21M%5C%21D%28P%2C+Q%29%3D%5Csup%5Climits_%7B%5C%7Cf%5C%7C_%5Cmathcal%7BH%7D+%5Cleq+1%7D%28%5Cmathbb%7BE%7D_X%5Bf%28X%29%5D+-+%5Cmathbb%7BE%7D_Y%5Bf%28Y%29%5D%29&bg=ffffff&fg=000000&s=0)

![\widehat{M\!M\!D}(P,Q)=\|\frac{1}{n}\sum\limits_{i=1}^{n}\phi(x_i)-\frac{1}{m}\sum\limits_{i=1}^{m}\phi(y_i)\|=\frac{1}{nm}\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{m}[k(x_i,x_j) + k(y_i,y_j) - 2k(x_i,y_j)]](https://s0.wp.com/latex.php?latex=%5Cwidehat%7BM%5C%21M%5C%21D%7D%28P%2CQ%29%3D%5C%7C%5Cfrac%7B1%7D%7Bn%7D%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bn%7D%5Cphi%28x_i%29-%5Cfrac%7B1%7D%7Bm%7D%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bm%7D%5Cphi%28y_i%29%5C%7C%3D%5Cfrac%7B1%7D%7Bnm%7D%5Csum%5Climits_%7Bi%3D1%7D%5E%7Bn%7D%5Csum%5Climits_%7Bj%3D1%7D%5E%7Bm%7D%5Bk%28x_i%2Cx_j%29+%2B+k%28y_i%2Cy_j%29+-+2k%28x_i%2Cy_j%29%5D&bg=ffffff&fg=000000&s=0)

어떤 kernel function ![k(\cdot,\cdot)](https://s0.wp.com/latex.php?latex=k%28%5Ccdot%2C%5Ccdot%29&bg=ffffff&fg=000000&s=0)가 주어졌을 때, 각 분포의 sample ![x, y](https://s0.wp.com/latex.php?latex=x%2C+y&bg=ffffff&fg=000000&s=0)들로부터 MMD에 대한 추정량을 위와 같이 계산할 수 있습니다. 이 연구에서는 ![k(x,y)=(x^Ty)^2](https://s0.wp.com/latex.php?latex=k%28x%2Cy%29%3D%28x%5ETy%29%5E2&bg=ffffff&fg=000000&s=0) 일 때![M\!M\!D(\mathbb{P}_l^s, \mathbb{P}_l^o)](https://s0.wp.com/latex.php?latex=M%5C%21M%5C%21D%28%5Cmathbb%7BP%7D_l%5Es%2C+%5Cmathbb%7BP%7D_l%5Eo%29&bg=ffffff&fg=000000&s=0)의 추정량을 최소화 하는 목적함수와, Gram matrix 간 차의 제곱합을 최소화하는 [1]의 ![L_{style}](https://s0.wp.com/latex.php?latex=L_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)이 같음을 증명하였습니다.

이로부터, style transfer가 feature map의 분포를 ![I_{style}](https://s0.wp.com/latex.php?latex=I_%7Bstyle%7D&bg=ffffff&fg=000000&s=0)의 feature map의 분포와 유사하게 만드는 방법이라는 직관을 얻을 수 있습니다. 저자는 다른 kernel function을 이용했을 때에도 성공적으로 style transfer된 이미지를 얻을 수 있었고, 단순히 distribution의 first, second moment를 맞춰주는 방법으로도 좋은 결과를 얻을 수 있음을 보였습니다.

![스크린샷 2017-05-16 오후 9.34.09.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-9-34-09.png?w=1400)Visual results of style transfer using different kernels. (BN: moment matching)

------

## 4. Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks

![스크린샷 2017-05-16 오후 9.39.16.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-16-e1848be185a9e18492e185ae-9-39-16.png?w=1400)Given any two unordered image collections X and Y, algorithm learns to automatically “translate” an image from one into the other and vice versa

이 연구에서는 GAN 구조를 응용하여 두 도메인 X, Y의 영상이 주여졌을 때, X에 속하는 영상을 Y에 속하는 영상으로 바꿔주는 네트워크 ![G: X\mapsto Y](https://s0.wp.com/latex.php?latex=G%3A+X%5Cmapsto+Y&bg=ffffff&fg=000000&s=0), 그리고 그 반대로 바꿔주는 네트워크 ![F: Y\mapsto X](https://s0.wp.com/latex.php?latex=F%3A+Y%5Cmapsto+X&bg=ffffff&fg=000000&s=0)를 동시에 학습하는 방법을 제시하고 있습니다. (X는 풍경사진 도메인, Y는 모네의 그림 도메인이라고 하면, G는 풍경사진을 모네의 그림처럼 바꿔주는 함수가 될 것이고, F는 모네의 그림을 사진처럼 바꿔주는 함수가 됩니다.)

![스크린샷 2017-05-17 오후 5.40.33.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-5-40-33.png?w=1400)Cycle-consistent adversarial network

이런 세팅에서 기존 GAN의 목적함수를이용하여 학습시킨다면 어떻게 될까요? 다른 도메인으로 transfer가 될 수는 있어도, 기존의 content를 그대로 유지하도록 하는 제약조건이 없기 때문에 완전히 다른 content를 담고있는 결과가 나올 수도 있습니다. 따라서 여기서는 domain transfer 후에도 같은 content를 유지하도록 cycle-consistency loss를 추가합니다. Cycle consistency loss란, ![x\in X](https://s0.wp.com/latex.php?latex=x%5Cin+X&bg=ffffff&fg=000000&s=0)에 대해, ![x\approx F(G(x))](https://s0.wp.com/latex.php?latex=x%5Capprox+F%28G%28x%29%29&bg=ffffff&fg=000000&s=0)가 되도록 하는 loss입니다. 사진과 모네 그림의 예에서는, 사진을 그림으로 바꿨다가 다시 사진으로 바꿨을 때 원래 사진과 유사해야 한다는 뜻입니다.

![스크린샷 2017-05-17 오후 7.32.20.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-7-32-20.png?w=403&h=457)Inputs, generated images and reconstructed images from different domain pairs

이렇게 양쪽의 generator와 discriminator를 동시에 학습시키며 ![F](https://s0.wp.com/latex.php?latex=F&bg=ffffff&fg=000000&s=0)와 ![G](https://s0.wp.com/latex.php?latex=G&bg=ffffff&fg=000000&s=0)가 서로의 역함수가 되도록 유도하였고, 아래와 같이 성공적으로 style transfer 및 domain transfer 네트워크를 학습한 결과를 볼 수 있습니다. 더 많은 결과는 저자의 [github page](https://junyanz.github.io/CycleGAN/)에서 볼 수 있습니다.

![스크린샷 2017-05-17 오후 7.27.48.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-7-27-481.png?w=1400)Left: real Monet, Right: generated photo

![스크린샷 2017-05-17 오후 7.23.55.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-7-23-55.png?w=1400)

![스크린샷 2017-05-17 오후 7.23.38.png](https://bloglunit.files.wordpress.com/2017/04/e18489e185b3e1848fe185b3e18485e185b5e186abe18489e185a3e186ba-2017-05-17-e1848be185a9e18492e185ae-7-23-38.png?w=1400)

------

## 5. Conclusion

이상 Neural network를 이용한 style transfer 연구들을 몇가지 알아보았습니다. 최근에 나온 review paper, [Neural Style Transfer: A Review](https://arxiv.org/abs/1705.04058v1)에 포스트에서 다루지 못한 여러 확장 연구들이 자세히 정리되어 있으니 관심있으신 분들은 참고하셔도 좋을 것 같습니다. 감사합니다!