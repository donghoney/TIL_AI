의료 AI Segmentation 자료

U-net : [https://arxiv.org/abs/1505.04597](https://arxiv.org/abs/1505.04597?fbclid=IwAR1dMlEhC9k1OheWee0w3sa6ydyscc1qhoLS1ZtBhDZmqbN_Lzem6iVaUh8)
3D U-net : [https://arxiv.org/abs/1606.06650](https://arxiv.org/abs/1606.06650?fbclid=IwAR39bbdnIFey7PLowIQyOW4B5bj6c3Pv8EmYPvO96O8xWtUxqnZHyEXxjrM)
3D U-Net 정리 사이트 : http://cdm98.tistory.com/35?fbclid=IwAR3JygSmQiK-Kzk6_cq0xICZxleyGPoSRvukgaPUJsOTxZ0_eLt_QcmVoiM

사실 어떤 모델이 가장 적절할지는 데이터에 따라 다르다고 들어서 확정을 내리는건 힘듬
biomedical 쪽에서 주로 쓰이는 모델은 대부분 U-net 계열의 Encoder-encoder 형태



Mask R-CNN이나 DeepLab과 같은 모델도 좋은 성능을 보이기도 함



의료 분야에서 segmentation은 다른 분야와 달리 모델보다는 전처리와 학습 방법이 큰 영향을 미침



장기나 종양을 예측하는 것이 task라고 했을때, 전체 pixel 중에서 target이 차지하는 pixel은 매우 극소수이기 때문에 (종양의 경우에는 더더욱) 우선 class imbalance 문제가 가장 큰 문제

이를 해결해기 위해서 patch를 만들어 학습하는 것 (positive patch와 negative patch 비율 조정), weighted loss function을 사용하는것 등등의 방법으로 해결하기도 함.

논문마다 방법도 다름

의료 분야에서는 필연적으로 발생할 수 밖에 없는 class imbalance 문제

애초에 병변이 CT에서 차지하는 비율이 적어서.. 장기라면 조금 덜함

밑바닥부터 시작하는 의료 AI 관련 영상

[https://youtu.be/EM1uBl5T09c](https://youtu.be/EM1uBl5T09c?fbclid=IwAR2vXKV249HacfRuyacT3EnuhM8I0oEuViAeL2leatoJJEUtmDUbn2Ns4YQ)
**질문사항:

- Patch samling 과정에서 center cropping 대신에 resize를 쓰는 이유는 무엇인가요? Resize대신 cropping을 쓰면 정보의 왜곡을 방지할 수 있을 것 같아서 궁금증이 들었습니다!

Full Preprocessing Tutorial | Kaggle 

[https://www.kaggle.com/gzuidhof/full-preprocessing-tutorial](https://www.kaggle.com/gzuidhof/full-preprocessing-tutorial?fbclid=IwAR1dMlEhC9k1OheWee0w3sa6ydyscc1qhoLS1ZtBhDZmqbN_Lzem6iVaUh8)





