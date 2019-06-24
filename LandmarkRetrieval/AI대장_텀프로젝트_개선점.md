## 인공지능 텀프로젝트 개선점

1. CNN으로 추출된 global feature를 SIFT와 같은 피쳐추출을 활용해 vlad를 통과하는 방식으로 개선할 수 있는 여지가 있었던 것 같다.
2. 만약, DB에 존재하지 않는 클래스 또는 관련 이미지가 들어왔을 때 어떻게 할 수 있는가?
3. CNN network단에 ImageNet이 아닌 Tokyo TM 데이터셋으로 pretrain할 경우 성능이 많게는 Building Challenge에서는 20%이상 향상한다는 점을 netvlad 논문에서 참고할 수 있었다.

