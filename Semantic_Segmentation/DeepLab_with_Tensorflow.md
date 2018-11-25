

## [Semantic Image Segmentation with DeepLab in TensorFlow](http://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html)

원본 링크 : https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html

Monday, March 12, 2018

Posted by Liang-Chieh Chen and Yukun Zhu, Software Engineers, Google Research

Semantic image segmentation, the task of assigning a semantic label, such as “road”, “sky”, “person”, “dog”, to every pixel in an image enables numerous new applications, such as the synthetic shallow depth-of-field effect shipped in the portrait mode of the Pixel 2 and Pixel 2 XL smartphones and mobile real-time video segmentation. Assigning these semantic labels requires pinpointing the outline of objects, and thus imposes much stricter localization accuracy requirements than other visual entity recognition tasks such as image-level classification or bounding box-level detection.

[![img](https://2.bp.blogspot.com/-meO7Y3kMxSg/WqMOKHbslrI/AAAAAAAACd8/ETeZFnYylbYylXwhCtivPTsZ9vaWYikSwCLcBGAs/s640/image1.png)](https://2.bp.blogspot.com/-meO7Y3kMxSg/WqMOKHbslrI/AAAAAAAACd8/ETeZFnYylbYylXwhCtivPTsZ9vaWYikSwCLcBGAs/s1600/image1.png)

Today, we are excited to announce the open source release of our latest and best performing semantic image segmentation model,DeepLab-v3+[1]*, implemented in TensorFlow. This release includes DeepLab-v3+ models built on top of a powerful convolutional neural network (CNN) backbone architecture [2, 3] for the most accurate results, intended for server-side deployment. As part of this release, we are additionally sharing our TensorFlow model training and evaluation code, as well as models already pre-trained on the Pascal VOC 2012 and Cityscapes benchmark semantic segmentation tasks. Since the first incarnation of our DeepLab model [4] three years ago, improved CNN feature extractors, better object scale modeling, careful assimilation of contextual information, improved training procedures, and increasingly powerful hardware and software have led to improvements with DeepLab-v2 [5] and DeepLab-v3 [6]. With DeepLab-v3+, we extend DeepLab-v3 by adding a simple yet effective decoder module to refine the segmentation results especially along object boundaries. We further apply the depthwise separable convolution to both atrous spatial pyramid pooling [5, 6] and decoder modules, resulting in a faster and stronger encoder-decoder network for semantic segmentation.

[![img](https://2.bp.blogspot.com/-gxnbZ9w2Dro/WqMOQTJ_zzI/AAAAAAAACeA/dyLgkY5TnFEf2j6jyXDXIDWj_wrbHhteQCLcBGAs/s640/image2.png)](https://2.bp.blogspot.com/-gxnbZ9w2Dro/WqMOQTJ_zzI/AAAAAAAACeA/dyLgkY5TnFEf2j6jyXDXIDWj_wrbHhteQCLcBGAs/s1600/image2.png)

Modern semantic image segmentation systems built on top of convolutional neural networks (CNNs) have reached accuracy levels that were hard to imagine even five years ago, thanks to advances in methods, hardware, and datasets. We hope that publicly sharing our system with the community will make it easier for other groups in academia and industry to reproduce and further improve upon state-of-art systems, train models on new datasets, and envision new applications for this technology.

Acknowledgements

We would like to thank the support and valuable discussions with Iasonas Kokkinos, Kevin Murphy, Alan L. Yuille (co-authors of DeepLab-v1 and -v2), as well as Mark Sandler, Andrew Howard, Menglong Zhu, Chen Sun, Derek Chow, Andre Araujo, Haozhi Qi, Jifeng Dai, and the Google Mobile Vision team. 

References

1. [Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1802.02611), *Liang-Chieh Chen, Yukun Zhu, George Papandreou, Florian Schroff, and Hartwig Adam, arXiv: 1802.02611, 2018.*
2. [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357), *François Chollet, Proc. of CVPR, 2017.*
3. [Deformable Convolutional Networks — COCO Detection and Segmentation Challenge 2017 Entry](http://presentations.cocodataset.org/COCO17-Detect-MSRA.pdf), *Haozhi Qi, Zheng Zhang, Bin Xiao, Han Hu, Bowen Cheng, Yichen Wei, and Jifeng Dai, ICCV COCO Challenge Workshop, 2017.*
4. [Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs](https://arxiv.org/abs/1412.7062), *Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, and Alan L. Yuille, Proc. of ICLR, 2015.*
5. [Deeplab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs](https://arxiv.org/abs/1606.00915), *Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, and Alan L. Yuille, TPAMI, 2017.*
6. [Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587), *Liang-Chieh Chen, George Papandreou, Florian Schroff, and Hartwig Adam, arXiv:1706.05587, 2017.*

------


***** DeepLab-v3+ is not used to power Pixel 2's portrait mode or real time video segmentation. These are mentioned in the post as examples of features this type of technology can enable.[↩](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html#top1)

