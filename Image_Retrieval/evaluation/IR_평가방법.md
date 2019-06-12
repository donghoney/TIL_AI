## Image Retrieval Project

By glee1228@naver.com



5k Dataset Download Link : [http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/](http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/)

1. 데이터셋 구성(train)

루트 디렉토리 이름 : oxbuild_images

* train
  * AllSouls_Oxford(133 pics)
  * Balliol_Oxford(155 pics)
  * ChristChurch_Oxford(544 pics)
  * Hertford_Oxford(68 pics)
  * Jesus_Oxford(162 pics)
  * Keble_Oxford(122 pics)
  * Magdalen_Oxford(686 pics)
  * New_Oxford(459 pics)
  * Oriel_Oxford(96 pics)
  * Trinity_Oxford(218 pics)
  * RadcliffeCamera_Oxford(283 pics)
  * Cornmarket_Oxford(60 pics)
  * Bodleian_Oxford(215 pics)
  * PittRivers_Oxford(109 pics)
  * Ashmolean_Oxford(196 pics)
  * Worcester_Oxford(71 pics)

* 레이블 없는1503 pics



## 성능 평가 방법

* Precision@K (P@K)
* Mean Average Precision (MAP)



### Precision@K

1. Set a rank threshold K

2. Compute % relevant in top K

3. Ignores documents ranked lower than K

   ![example](/Users/donghoon/GitHub/TIL_AI/Image_Retrieval/evaluation/example.png)

   ### Ex: True, False, True, False, True
   #### $Prec@3  \ of \  2/3$
   #### $Prec@4 \  of \  2/4$
   #### $Prec@5 \ of \ 3/5$

   



### Mean Average Precision

1. Consider rank position of each relevant doc

2. Compute Precision@K for each$$K_1, K_2,…, K_R$$

3. Average precision = average of P@K

   ![example](/Users/donghoon/GitHub/TIL_AI/Image_Retrieval/evaluation/example.png)

   ### Ex: True, False, True, False, True

   ### 이 결과의 $MAP =  \frac{1}{3}*(\frac{1}{1}+\frac{2}{3}+\frac{3}{5}) \approx 0.76$

4. MAP is Average Precision across multiple
   queries/rankings



### Average Precision example

![AP_example](/Users/donghoon/GitHub/TIL_AI/Image_Retrieval/evaluation/AP_example.png)



### MAP example



![MAP_example](/Users/donghoon/GitHub/TIL_AI/Image_Retrieval/evaluation/MAP_example.png)



