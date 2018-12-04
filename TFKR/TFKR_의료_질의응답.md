## Tensorflow KR U-Net 관련 질문과 답변

### 질문 1.

질문자 : 이도일


안녕하세요.

현재 U-net Network를 사용해서 폐에 있는 작은 Nodule을 segment하는 작업을 진행하고 있습니다.

영상은 512x512 size의 Lung CT 영상이고,
제가 segment 하고자 하는 노듈은 보통 20x20 pixel 보다 작다고 보시면 됩니다.

segment 하고자 하는 Target이 전체 영상 사이즈에 비해 너무 작다 보니 class imabalance 문제가 있는 듯 합니다.

한 장 가지고만 Train해보면 Loss는 줄어들다가 어느 값에 수렴은 하는데 결과 값은 segment되지 않고 까만 영상만 나옵니다.
Lung이 아닌 입자가 큰 팬텀 영상은 segmentation이 잘 됩니다.

어떻게 해야 작은 target을 segmentation 할 수 있을지 조언 부탁드립니다.

Network 구조
Layer : 4 
feature map : 32
optimizer : adam(1e-4)

현재 512x512 영상을 64x64 패치로 쪼개서 32 stride로 windowing하며 영상을 학습합니다. 512x512 1 슬라이스 경우 64x64 225장이 나오게 되는거죠.

이해를 돕기 위해 이미지도 함께 넣겠습니다.
Label 영상과 Input 영상입니다.

조언 부탁드립니다.

답변자 1 : 김남국

Size invariant 에 강한 네트워, curriculum learning, 충분한 데이터, 일관된 데이터 등을 써서 해 보시죠. Detection으로 가면 어려운 문제 입니다. 지금 Lidc 가지고 만든 3d nodule cad가 96 sen / 1 fp입니다

답변자 2 : 이주현

1. Lung Mask를 추출한 뒤, Lung Mask 포함 비율(Threshold)을 일정 이상이 되는 패치만 Valid Patch로 사용한다. 
   -> Normal Patch의 개수 감소

2. Data Extraction을 windowing 형식이 아닌 Random Extraction형식으로 노듈마스크와 lung마스크를 이용히여 사용자가 임의로 값을 준 만큼 뽑을 수 있도록 한다. 
   -> 대략적인 Normal과 노듈의 비율을 맞춰 Data Imbalance 방지

3. U-Net도data-science-bowl-2018 1위팀이 사용했을 정도로 좋은 모델이지만 SOTA 중 하나 인 Deep Lab V3 등의 모델도 고려해볼 만하다고 생각합니다.