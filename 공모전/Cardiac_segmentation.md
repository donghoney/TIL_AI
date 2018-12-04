## [HeLP Challenge 2018](https://www.synapse.org/#!Synapse:syn15569329)

### 서울아산병원이 주최하는 의료인공지능 개발콘테스트

* **주관** : 서울아산병원/보건복지부

* **후원** :  kakaobrain/ 정보통신산업진흥원(NIPA)/ 창업선도대학/ 대한의료인공지능학회

#### HeLP Challenge 2018 링크 : 

https://www.synapse.org/#!Synapse:syn15569329/wiki/582412

### TIMELINE

### ![schedule](/Users/donghoon/GitHub/TIL_AI/공모전/image/schedule.jpg)

### REGISTER

### [Challenge Register](http://www.amc.seoul.kr/asan/academy/event/eventDetail.do?eventId=947#menu2)

### CHALLENGE ORGANIZERS

![20181031_172725](/Users/donghoon/GitHub/TIL_AI/공모전/image/20181031_172725.png)



### DATA CONTRIBUTORS & ENGINEERING ADVISORS

![20181101_110807](/Users/donghoon/GitHub/TIL_AI/공모전/image/20181101_110807.png)

### FUNDERS

![f](/Users/donghoon/GitHub/TIL_AI/공모전/image/f.png)





### CLOUD COMPUTING SPONSORS

![kakao](/Users/donghoon/GitHub/TIL_AI/공모전/image/kakao.png)



### SPONSORS



![s3](/Users/donghoon/GitHub/TIL_AI/공모전/image/s3.png)





## Contest 1-2. Cardiac segmentation



## Background and Task

- 심장 구조의 Segmentation은 심장 CT의 정량 분석을 위한 가장 필수적인 기술입니다.
- 두 가지 Segmentation 작업
  **Task 1:** 우심실(RV) , 좌심실(LV), 좌심실 질량(LVM)의 Segmentation - segmentation of right ventricle (RV), left ventricle (LV), left ventricular mass (LVM).
  **Task 2:** 좌심실 질량(LVM), 앞 유두근(APM) 및 후 유두근(PPM)의 Segmentation - segmentation of left ventricular mass (LVM), anterior papillary muscle (APM) and posterior papillary muscle (PPM)

## Data description

- 아산 메디컬 센터의 명암 강화 심전도 심장 판막 CT - Contrast enhanced, electrocardiography-gated cardiac CT (dual source CT, Siemens FLASH) from Asan Medical Center.

- 심장 CT 이미지는 메타 이미지 형식으로 제공됩니다 - The cardiac CT images are provided in meta image format (.mha).

- **Task 1을 위한 선천성 심장병(120건)** RV(파란색), LV(녹색) 및 LVM(빨간색) - **Congenital heart disease for the Task 1 (120 cases)**
  RV (blue), LV (green), and LVM (red)

- **Task 2를 위한 비대증 성 심근 병증 (88건)과 정상 대조군 (22건)** LVM(빨간색), APM(녹색), PPM(파란색) - Hypertrophic cardiomyopathy (88 cases) and normal control (22 cases) for the Task 2

  LVM (red), APM (green), PPM (blue)

  ![Test](/Users/donghoon/GitHub/TIL_AI/공모전/image/Test.PNG)

  **사진 설명** : (위) 선천성 심장병 환자의 심장 CT에 대한 심장의 주석 , (아래) 비대증 성 심근 병증 환자에서 심장 CT의 심장에 대한 주석

  **참고** : diastole - 이완기, systole - 수축기, LVM - 좌심실 질량, APM - 앞 유두근, PPM - 후 유두근

## Difference from other public datasets

- 이 Contest의 독특한 도전 과제는 '변형된' 또는 '비정형적인' 심장 구조가 있는 많은 사례가 있다는 것입니다. - A unique challenge in this contest is we have many cases with 'deformed' or 'atypical' cardiac structures.

  ![atypical cardiac](/Users/donghoon/GitHub/TIL_AI/공모전/image/atypical cardiac.png)

  **사진 설명** : 심장 구조의 비순환 형태학

  (좌) : 변형된 심실

  (우) : 악세서리 유두근(유두근 비대와 관련)

## Evaluation matrix

- 다이스 유사 계수 (DSC)는 테스트 데이터 세트의 모든 성능 측정에 사용됩니다. - The dice similarity coefficient (DSC) is used for all performance measures in test dataset.

- 전반적인 성능 점수 , - Overall performance score,

  ![score1](/Users/donghoon/GitHub/TIL_AI/공모전/image/score1.png)



## 1-2.1. Scientific overview



**정량적 CT 영상 분석 및 그 중요성**

심장 컴퓨터 단층 촬영 (CT)은 다양한 심장 질환을 진단하는 데 널리 사용되는 방법입니다. 초기에는 심장 CT가 주로 관상 동맥 질환을 진단하는 데 사용되었습니다. 최근 심혈관계 질환(예 : 판막 질환, 선천성 심장병 및 심근 병증 ) 진단을 위한 심장 CT의 사용이 증가하고 있습니다. 심장 CT를 진단하는 가장 기본적인 단계는 심한 이상이 있는지 여부를 결정하는 것입니다. 예를 들어, 좌심실의 크기가 더 커 보이거나 작아 보입니다. 그러나 이 안구 추정은 부정확하고 넓은 관찰자 변동성의 위험이 있습니다. 심장 구조의 정량 분석, 예를 들어, 좌심실의 볼륨은 100ML, 안구 추정보다 정확한 정보를 제공할 수 있습니다. 심장 CT의 이러한 정량 분석은 이제 임상 실습 및 연구에 널리 사용됩니다. 정량 분석을 위한 필수 기술 중 하나는 각각의 심장 구조 (예를 들어, 우심실 또는 좌심실, 심실 근육 및 유두근)의 Segmentation입니다.

**Quantitative CT image analysis and its importance**

Cardiac computed tomography (CT) is a widely used method for the diagnosis of various heart diseases. In the early days, cardiac CT was mainly used to diagnose coronary artery disease. Recently use of cardiac CT for diagnosing structural heart disease (e.g., valvular disease, congenital heart disease, and cardiomyopathy) is increasing. The most basic step in diagnosing cardiac CT is to determine whether there is a gross abnormality. For example, the size of the left ventricle seems larger or looks smaller. However, this eyeball estimation has the risk of being inaccurate and the wide interobserver variability. Quantitative analysis of heart structures, for example, the volume of the left ventricle is 100 ml, can provide more accurate information than the eyeball estimation. This quantitative analysis of cardiac CT is now widely used in clinical practice and research. One of the essential techniques for the quantitative analysis is the segmentation of each cardiac structure (e.g., right or left ventricular chamber, ventricular muscle, and papillary muscle).


![ventricle volume](/Users/donghoon/GitHub/TIL_AI/공모전/image/ventricle volume.PNG)

**사진 설명** : 심실의 volume은 큰 예후적 의미를 갖는다.

* 만성 폐동맥 판막 역류 환자에서 RV 이완기 volume 지수가 163ml/m2를 초과하거나 RV 수축기 volume 지수가 80ml/m2를 초과하기 전에 폐동맥 판막 치환술을 고려해야 합니다.



**다른 Segmentation Contest와 차이가 있습니다**

최근 CT 또는 MRI에서 심장 세분화 문제와 관련하여 인공 지능 기법을 사용하는 일부 연구가 발표되었습니다. 이 연구 및 데이터 세트는 심장 크기와 모양이 비교적 건강한 사람들의 이미지를 기반으로 합니다. 우리는 이 대회에서 두 가지 임상적으로 중요한 시나리오를 기반으로 심장 CT를 사용하여 Segmentation 작업을 설정했습니다. 선천성 심장병과 비대증성 심근 병증과 같은 두 가지 심장 질환에서 CT 데이터 세트를 준비했습니다. 우리는 이 데이터 세트가 심장 CT의 보다 실질적인 Segmentation 기술을 개발하는데 도움이 될 것으로 믿습니다.



**There is a difference from other segmentation contests**

Recently, some studies using artificial intelligence techniques regarding cardiac segmentation issues in CT or MRI have been published. These studies and data sets are based on images of people whose heart size and shape are relatively healthy. We set up a segmentation task using cardiac CT based on two clinically significant scenarios in this contest. We prepared CT dataset in two different types of cardiac disease: congenital heart disease and hypertrophic cardiomyopathy. We believe this dataset will help develop the more practical segmentation technology of cardiac CT.



## 1-2.2. Challenge questions

참가자들은 두 종류의 cardaic CT 데이터 세트(**Task1**)에 대한 Segmentation 작업을 수행합니다.

* 첫 번째는 선천성 심장병 (CHD) CT 데이터세트입니다. CHD 데이터 세트에서 우심실(RV), 좌심실(LV) 및 좌심실 심근(LVM)을 분류해야합니다.
* 두 번째는 비대성 심근 병증 CT 데이터 세트입니다. 이 데이터 세트에는 몇 가지 일반 컨트롤이 포함되어있습니다. HCMP 데이터 세트에서 좌심실 심근(LVM), 전방 유두근(APM) 및 후 유두근(PPM)이 분절되어야합니다(**Task2**)

Participants will perform segmentation tasks on two types of cardaic CT data sets (**Task 1**).

- The first is the congenital heart disease (CHD) CT data set. In the CHD data set, right ventricular chamber (RV), left ventricular chamber (LV), and left ventricular myocardium (LVM) should be segmented.
- The second is hypertrophic cardiomyopathy CT dataset. This dataset also contains some normal controls. In the HCMP dataset, the left ventricular myocardium (LVM), anterior papillary muscle (APM), and posterior papillary muscle (PPM) should be segmented (**Task 2**).

![Test](/Users/donghoon/GitHub/TIL_AI/공모전/image/Test.PNG)





## 1-2.3. Data description

### 선천성 심장병 (CHD) CT 데이터 세트

CHD CT 데이터에는 선천성 심장 지로한을 앓고 있으며 아산 메디컬 센터에서 심장 CT 체적 연구를 받은 연속적인 환자가 포함됩니다. 심전도 동기화 된 심장 CT는 2세대 이중 소스 CT(Somatom Definition FLASH, Siemens)를 사용하여 수행되었습니다. 환자 연령의 범위는 7일에서 64세 사이에 광범위 합니다. 이 연구 집단에 포함된 CHD는 Fallot 증후군(TOF), 두 배의 출구 우심실, 심실 중격 결손이 있는 폐동맥 폐쇄증 및 다른 것들이었습니다. 수술 후 TOF는 심장 CT 체적 측정의 가장 일반적인 징후였습니다. 이완기와 수축기 모두를 얻고 분석하였습니다.



* 우심실(RV)과 좌심실(LV)의 주석은 상업용 워크스테이션(Advantage Windows 4.6, GE Healthcare)에서 3D 임계 값 기반 및 region-growing segmentation을 통해 수행되었습니다.
* 좌심실 심근(LVM)의 주석은 연구용 버전의 소프트웨어(Cardiac A-view, Asan Medical Center)를 사용하여 수동으로 수행되었습니다.
* 심장 CT 이미지는 메타 이미지 형식(.mha)으로 제공됩니다. 레이블 파일의 이름은 'image file name_M.mha'입니다. 이미지의 평면 크기는 512x512입니다. 그러나 모든 심장 영역을 포괄하기 위해 조각 수는 200에서 500까지 다양합니다. 해상도는 약 0.35mm x 0.35mm x 0.4mm입니다.

### Congenital heart disease (CHD) CT dataset

The CHD CT data includes consecutive patients with congenital heart disease who underwent the heart CT volumetry study at Asan Medical Center. The electrocardiography-synchronized cardiac CT was performed using the second generation dual-source CT (Somatom Definition FLASH, Siemens). The range of patient age is vast from 7 days to 64 years. The CHDs included in this study population were tetralogy of Fallot (TOF), double outlet right ventricle, pulmonary atresia with the ventricular septal defect, and others. Postoperative TOF was the most common indication of the heart CT volumetry. Both end-diastolic and end-systolic phases were obtained and analyzed.

- Annotation of the right ventricular chamber (RV) and the left ventricular chamber (LV) was performed in a commercially available workstation (Advantage Windows 4.6, GE Healthcare) with 3D threshold-based and region-growing segmentation.
- Annotation of the left ventricular myocardium (LVM) was performed manually using a research version of the software (Cardiac A-view, Asan Medical Center).
- The cardiac CT images are provided in meta image format (.mha). The label files are named as ‘image file name_M.mha.’ The in-plane dimension of the image is 512 x 512. However, the number of slices varies from 200 to 500 for covering all cardiac region. The resolution is around 0.35mm x 0.35mm x 0.4mm.



### 비대증 성 심근 병증(HCM) CT 데이터세트

CHD CT 데이터에는 HCM(n=102)과 정상 대조군(n=22)을 가진 연속적인 환자들이 아산 메디컬 센터에서 심장 CT를 받았습니다. CT검사는 2세대 이중 소스 CT(Somatom Definition FLASH, Siemens)를 사용하여 수행되었습니다. 회고적 심전도 스캔이 수행되었습니다. CT 영상의 최종 이완기 단계를 얻고 분석하였습니다. 

* 좌심실 심근(LVM), 앞 유두근 (APM) 및 후 유두근(PPM)의 주석을 연구용 소프트웨어(Cardiac A-view, Asan Medical Center)를 사용하여 수동으로 수행했습니다.
* 심장 CT 이미지는 메타 이미지형식(.mha)으로 제공됩니다. 레이블 파일의 이름은 'image file name_M.mha'입니다. 이미지의 평면 치수는 512 x 512 입니다. 그러나 모든 심장 영역을 포괄하기 위해 조각 수는 200에서 500까지 다양합니다. 해상도는 약 0.35mm x 0.35mm x 0.4mm입니다.

### Hypertrophic cardiomyopathy (HCM) CT dataset

The CHD CT data includes consecutive patients with HCM (n=102) and normal control (n=22) who underwent cardiac CT at Asan Medical Center. CT examinations were performed using a second-generation dual-source CT (Somatom Definition FLASH, Siemens). Retrospective electrocardiography scanning was performed. The end-diastolic phase of CT image was obtained and analyzed.

- Annotation of the left ventricular myocardium (LVM), anterior papillary muscle (APM), and posterior papillary muscle (PPM) was performed manually using a research version of the software (Cardiac A-view, Asan Medical Center).
- The cardiac CT images are provided in meta image format (.mha). The label files are named as ‘image file name_M.mha.’ The in-plane dimension of the image is 512 x 512. However, the number of slices varies from 200 to 500 for covering all cardiac region. The resolution is around 0.35mm x 0.35mm x 0.4mm.



## 1-2.4. Evaluation matrix

이 방법의 성능은 각 라벨 기준으로 먼저 평가되고 이후에 각 테스트(CHD 및 HCMP)에 대해 집계됩니다. 마지막으로 최종 점수는 두 점수의 가중치 합계로 계산됩니다. 다이스 유사 계수(DSC)는 테스트 데이터 세트의 모든 성능 측정에 사용됩니다.

The performance of the methods will be evaluated first for each label basis and aggregated for each test (CHD and HCMP) afterward. Finally, the final performance score will be calculated from the weighted summation of these two scores.
The Dice similarity coefficient (DSC) is used for all performance measures in the test dataset.

#### Scoring

![score](/Users/donghoon/GitHub/TIL_AI/공모전/image/score.PNG)