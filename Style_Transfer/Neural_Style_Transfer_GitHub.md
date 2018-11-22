## Neural-Style-Transfer-Paper

뉴럴 네트워크 기반 style transfer 논문 리스트

https://github.com/ycjing/Neural-Style-Transfer-Papers

Selected papers, corresponding codes and pre-trained models in our review paper "**Neural Style Transfer: A Review**"

*If I missed your paper in this review, please email me or just pull a request here. I am more than happy to add it. Thanks!*

## *News!*

- [July, 2018] Our paper *Stroke Controllable Fast Style Transfer with Adaptive Receptive Fields* has been accepted by ECCV 2018. Our review will be updated correspondingly.
- [June, 2018] Upload a new version of our paper on arXiv which adds several missing papers (e.g., the work of Wang et al. *ZM-Net: Real-time Zero-shot Image Manipulation Network*).
- [Apr, 2018] We have released a new version of the paper with significant changes at: <https://arxiv.org/pdf/1705.04058.pdf> 
  Appreciate the feedback!
- [Feb, 2018] Update the *Images* *(Images_neuralStyleTransferReview_v2)* in the *Materials*. Add the results of Li et al.'s NIPS 2017 paper.
- [Jan, 2018] *Pre-trained models* and all the *content images*, the *style images*, and the *stylized results* in the paper have been released.


[![img](https://github.com/ycjing/Neural-Style-Transfer-Papers/raw/master/framework_n4.png)](https://github.com/ycjing/Neural-Style-Transfer-Papers/blob/master/framework_n4.png)

## Citation

If you find this repository useful for your research, please cite

```
@article{jing2017neural,
  title={Neural Style Transfer: A Review},
  author={Jing, Yongcheng and Yang, Yezhou and Feng, Zunlei and Ye, Jingwen and Yu, Yizhou and Song, Mingli},
  journal={arXiv preprint arXiv:1705.04058},
  year={2017}
}
```

## Materials corresponding to Our Paper

✅ [**Supplementary Materials**](http://yongchengjing.com/pdf/review_supp.pdf)

✅ [**Pre-trained Models**](https://www.dropbox.com/s/37lje23pb75ecob/Models_neuralStyleTransferReview.zip?dl=0)

✅ [**Images (v2)**](https://www.dropbox.com/s/dkp45oc4mvqt4m8/Images_neuralStyleTransferReview_v2.zip?dl=0)

## A Taxonomy of Current Methods

### 1. "Slow" Neural Methods Based On Online Image Optimization

### 1.1. Parametric "Slow" Neural Methods with Summary Statistics

✅ [**A Neural Algorithm of Artistic Style**] [[Paper\]](https://arxiv.org/pdf/1508.06576.pdf) *(First Neural Style Transfer Paper)*

❇️ **Code:**

- [Torch-based](https://github.com/jcjohnson/neural-style)
- [TensorFlow-based](https://github.com/anishathalye/neural-style)
- [TensorFlow-based with L-BFGS optimizer support](https://github.com/cysmith/neural-style-tf)
- [Caffe-based](https://github.com/fzliu/style-transfer)
- [Keras-based](https://github.com/titu1994/Neural-Style-Transfer)
- [MXNet-based](https://github.com/pavelgonchar/neural-art-mini)
- [MatConvNet-based](https://github.com/aravindhm/neural-style-matconvnet)

✅ [**Image Style Transfer Using Convolutional Neural Networks**] [[Paper\]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf) *(CVPR 2016)*

✅ [**Incorporating Long-range Consistency in CNN-based Texture Generation**] [[Paper\]](https://arxiv.org/pdf/1606.01286.pdf) *(ICLR 2017)*

❇️ **Code:**

-   [Theano-based](https://github.com/guillaumebrg/texture_generation)

✅ [**Laplacian-Steered Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1707.01253.pdf) *(ACM MM 2017)*

❇️ **Code:**

- [Torch-based & TensorFlow-based](https://github.com/askerlee/lapstyle)

✅ [**Demystifying Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1701.01036.pdf) *(Theoretical Explanation)* *(IJCAI 2017)*

❇️ **Code:**

-   [MXNet-based](https://github.com/lyttonhao/Neural-Style-MMD)

✅ [**Stable and Controllable Neural Texture Synthesis and Style Transfer Using Histogram Losses**] [[Paper\]](https://arxiv.org/pdf/1701.08893.pdf)

### 1.2. Non-parametric "Slow" Neural Methods with MRFs

✅ [**Combining Markov Random Fields and Convolutional Neural Networks for Image Synthesis**] [[Paper\]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Li_Combining_Markov_Random_CVPR_2016_paper.pdf) *(CVPR 2016)*

❇️ **Code:**

- [Torch-based](https://github.com/chuanli11/CNNMRF)

✅ [**Arbitrary Style Transfer with Deep Feature Reshuffle**] [[Paper\]](https://arxiv.org/pdf/1805.04103.pdf) *(CVPR 2018)*

### 2. "Fast" Neural Methods Based On Offline Model Optimization

### 2.1. Per-Style-Per-Model "Fast" Neural Methods

✅ [**Perceptual Losses for Real-Time Style Transfer and Super-Resolution**] [[Paper\]](https://arxiv.org/pdf/1603.08155.pdf) *(ECCV 2016)*

❇️ **Code:**

- [Torch-based](https://github.com/jcjohnson/fast-neural-style)
- [TensorFlow-based](https://github.com/lengstrom/fast-style-transfer)
- [Chainer-based](https://github.com/yusuketomoto/chainer-fast-neuralstyle)

❇️ **Pre-trained Models:**

- [Torch-models](https://github.com/ProGamerGov/Torch-Models)
- [Chainer-models](https://github.com/gafr/chainer-fast-neuralstyle-models)

✅ [**Texture Networks: Feed-forward Synthesis of Textures and Stylized Images**] [[Paper\]](http://www.jmlr.org/proceedings/papers/v48/ulyanov16.pdf) *(ICML 2016)*

❇️ **Code:**

- [Torch-based](https://github.com/DmitryUlyanov/texture_nets)
- [TensorFlow-based](https://github.com/tgyg-jegli/tf_texture_net)

✅ [**Precomputed Real-Time Texture Synthesis with Markovian Generative Adversarial Networks**] [[Paper\]](https://arxiv.org/pdf/1604.04382.pdf) *(ECCV 2016)*

❇️ **Code:**

- [Torch-based](https://github.com/chuanli11/MGANs)

### 2.2. Multiple-Style-Per-Model "Fast" Neural Methods

✅ [**A Learned Representation for Artistic Style**] [[Paper\]](https://arxiv.org/pdf/1610.07629.pdf) *(ICLR 2017)*

❇️ **Code:**

- [TensorFlow-based](https://github.com/tensorflow/magenta/tree/master/magenta/models/image_stylization)

✅ [**Multi-style Generative Network for Real-time Transfer**] [[Paper\]](https://arxiv.org/pdf/1703.06953.pdf)  **\*（arXiv, 03/2017）***

❇️ **Code:**

- [PyTorch-based](https://github.com/zhanghang1989/PyTorch-Style-Transfer)
- [Torch-based](https://github.com/zhanghang1989/MSG-Net)

✅ [**Diversified Texture Synthesis With Feed-Forward Networks**] [[Paper\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Li_Diversified_Texture_Synthesis_CVPR_2017_paper.pdf) *(CVPR 2017)*

❇️ **Code:**

-   [Torch-based](https://github.com/Yijunmaverick/MultiTextureSynthesis)

✅ [**StyleBank: An Explicit Representation for Neural Image Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1703.09210.pdf) *(CVPR 2017)*

### 2.3. Arbitrary-Style-Per-Model "Fast" Neural Methods

✅ [**Fast Patch-based Style Transfer of Arbitrary Style**] [[Paper\]](https://arxiv.org/pdf/1612.04337.pdf)

❇️ **Code:**

- [Torch-based](https://github.com/rtqichen/style-swap)

✅ [**Exploring the Structure of a Real-time, Arbitrary Neural Artistic Stylization Network**] [[Paper\]](https://arxiv.org/pdf/1705.06830.pdf) *(BMVC 2017)*

❇️ **Code:**

- [TensorFlow-based](https://github.com/tensorflow/magenta/tree/master/magenta/models/arbitrary_image_stylization)

✅ [**Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization**] [[Paper\]](https://arxiv.org/pdf/1703.06868.pdf) *(ICCV 2017)*

❇️ **Code:**

- [Torch-based](https://github.com/xunhuang1995/AdaIN-style)
- [TensorFlow-based with Keras](https://github.com/eridgd/AdaIN-TF)
- [TensorFlow-based without Keras](https://github.com/elleryqueenhomels/arbitrary_style_transfer)

✅ [**Universal Style Transfer via Feature Transforms**] [[Paper\]](https://arxiv.org/pdf/1705.08086.pdf) *(NIPS 2017)*

❇️ **Code:**

- [Torch-based](https://github.com/Yijunmaverick/UniversalStyleTransfer)
- [TensorFlow-based](https://github.com/eridgd/WCT-TF)
- [PyTorch-based #1](https://github.com/sunshineatnoon/PytorchWCT)
- [PyTorch-based #2](https://github.com/pietrocarbo/deep-transfer)

✅ [**Meta Networks for Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1709.04111.pdf) *(CVPR 2018)*

❇️ **Code:**

- [Caffe-based](https://github.com/FalongShen/styletransfer)

✅ [**ZM-Net: Real-time Zero-shot Image Manipulation Network**] [[Paper\]](https://arxiv.org/pdf/1703.07255.pdf)

✅ [**Avatar-Net: Multi-Scale Zero-Shot Style Transfer by Feature Decoration**] [[Paper\]](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/0137.pdf) *(CVPR 2018)*

❇️ **Code:**

- [TensorFlow-based](https://github.com/LucasSheng/avatar-net)

## Improvements and Extensions

✅ [**Preserving Color in Neural Artistic Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1606.05897.pdf)

✅ [**Controlling Perceptual Factors in Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1611.07865.pdf) *(CVPR 2017)*

❇️ **Code:**

- [Torch-based](https://github.com/leongatys/NeuralImageSynthesis)

✅ [**Content-Aware Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1601.04568.pdf)

✅ [**Towards Deep Style Transfer: A Content-Aware Perspective**] [[Paper\]](http://www.bmva.org/bmvc/2016/papers/paper008/paper008.pdf) *(BMVC 2016)*

✅ [**Neural Doodle_Semantic Style Transfer and Turning Two-Bit Doodles into Fine Artwork**] [[Paper\]](https://arxiv.org/pdf/1603.01768.pdf)

✅ [**Semantic Style Transfer and Turning Two-Bit Doodles into Fine Artwork**] [[Paper\]](https://arxiv.org/pdf/1603.01768.pdf)

❇️ **Code:**

- [Torch-based](https://github.com/alexjc/neural-doodle)

✅ [**The Contextual Loss for Image Transformation with Non-Aligned Data**] [[Paper\]](https://arxiv.org/pdf/1803.02077) *(ECCV 2018)*

❇️ **Code:**

- [TensorFlow-based](https://github.com/roimehrez/contextualLoss)

✅ [**Improved Texture Networks: Maximizing Quality and Diversity in Feed-forward Stylization and Texture Synthesis**] [[Paper\]](https://arxiv.org/pdf/1701.02096.pdf) *(CVPR 2017)*

❇️ **Code:**

- [Torch-based](https://github.com/DmitryUlyanov/texture_nets)

✅ [**Instance Normalization：The Missing Ingredient for Fast Stylization**] [[Paper\]](https://arxiv.org/pdf/1607.08022.pdf)

❇️ **Code:**

- [Torch-based](https://github.com/DmitryUlyanov/texture_nets)

✅ [**A Style-Aware Content Loss for Real-time HD Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1807.10201) *(ECCV 2018)*

✅ [**Multimodal Transfer: A Hierarchical Deep Convolutional Neural Network for Fast Artistic Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1612.01895.pdf) *(CVPR 2017)*

❇️ **Code:**

- [TensorFlow-based](https://github.com/fullfanta/multimodal_transfer)

✅ [**Stroke Controllable Fast Style Transfer with Adaptive Receptive Fields**] [[Paper\]](https://arxiv.org/pdf/1802.07101.pdf) *(ECCV 2018)*

❇️ **Code:**

- [TensorFlow-based](https://github.com/LouieYang/stroke-controllable-fast-style-transfer)

✅ [**Depth-Preserving Style Transfer**] [[Paper\]](https://github.com/xiumingzhang/depth-preserving-neural-style-transfer/blob/master/report/egpaper_final.pdf)

❇️ **Code:**

- [Torch-based](https://github.com/xiumingzhang/depth-preserving-neural-style-transfer)

✅ [**Depth-Aware Neural Style Transfer**] [[Paper\]](https://dl.acm.org/citation.cfm?id=3092924) *(NPAR 2017)*

✅ [**Neural Style Transfer: A Paradigm Shift for Image-based Artistic Rendering?**] [[Paper\]](https://tobias.isenberg.cc/personal/papers/Semmo_2017_NST.pdf) *(NPAR 2017)*

✅ [**Pictory: Combining Neural Style Transfer and Image Filtering**] [[Paper\]](https://www.researchgate.net/publication/320035123_Demo_Pictory_-_Neural_Style_Transfer_and_Editing_with_CoreML) *(ACM SIGGRAPH 2017 Appy Hour)*

✅ [**Painting Style Transfer for Head Portraits Using Convolutional Neural Networks**] [[Paper\]](http://dl.acm.org/citation.cfm?id=2925968) *(SIGGRAPH 2016)*

✅ [**Son of Zorn's Lemma Targeted Style Transfer Using Instance-aware Semantic Segmentation**] [[Paper\]](https://arxiv.org/pdf/1701.02357.pdf) *(ICASSP 2017)*

✅ [**Style Transfer for Anime Sketches with Enhanced Residual U-net and Auxiliary Classifier GAN**] [[Paper\]](https://arxiv.org/pdf/1706.03319.pdf) *(ACPR 2017)*

✅ [**Artistic Style Transfer for Videos**] [[Paper\]](https://arxiv.org/pdf/1604.08610.pdf) *(GCPR 2016)*

❇️ **Code:**

- [Torch-based](https://github.com/manuelruder/artistic-videos)

✅ [**DeepMovie: Using Optical Flow and Deep Neural Networks to Stylize Movies**] [[Paper\]](https://arxiv.org/pdf/1605.08153.pdf)

✅ [**Characterizing and Improving Stability in Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1705.02092.pdf)) *(ICCV 2017)*

✅ [**Coherent Online Video Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1703.09211.pdf) *(ICCV 2017)*

✅ [**Real-Time Neural Style Transfer for Videos**] [[Paper\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Huang_Real-Time_Neural_Style_CVPR_2017_paper.pdf) *(CVPR 2017)*

✅ [**A Common Framework for Interactive Texture Transfer**] [[Paper\]](http://www.icst.pku.edu.cn/F/zLian/papers/CVPR18-Men.pdf) *(CVPR 2018)*

✅ [**Deep Photo Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1703.07511.pdf) *(CVPR 2017)*

❇️ **Code:**

- [Torch-based](https://github.com/luanfujun/deep-photo-styletransfer)
- [TensorFlow-based](https://github.com/LouieYang/deep-photo-styletransfer-tf)

✅ [**A Closed-form Solution to Photorealistic Image Stylization**] [[Paper\]](https://arxiv.org/pdf/1802.06474.pdf) *(ECCV 2018)*

❇️ **Code:**

- [PyTorch-based](https://github.com/NVIDIA/FastPhotoStyle)

✅ [**Decoder Network Over Lightweight Reconstructed Feature for Fast Semantic Style Transfer**] [[Paper\]](http://feng-xu.com/papers/iccv2017_style.pdf) *(ICCV 2017)*

✅ [**Stereoscopic Neural Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1802.10591.pdf) *(CVPR 2018)*

✅ [**Awesome Typography: Statistics-based Text Effects Transfer**] [[Paper\]](https://arxiv.org/abs/1611.09026) *(CVPR 2017)*

❇️ **Code:**

- [Matlab-based](https://github.com/williamyang1991/Text-Effects-Transfer)

✅ [**Neural Font Style Transfer**] [[Paper\]](http://ieeexplore.ieee.org/document/8270274/) *(ICDAR 2017)*

✅ [**Rewrite: Neural Style Transfer For Chinese Fonts**] [[Project\]](https://github.com/kaonashi-tyc/Rewrite)

✅ [**Separating Style and Content for Generalized Style Transfer**] [[Paper\]](https://arxiv.org/pdf/1711.06454.pdf) *(CVPR 2018)*

✅ [**Visual Attribute Transfer through Deep Image Analogy**] [[Paper\]](https://arxiv.org/pdf/1705.01088.pdf) *(SIGGRAPH 2017)*

❇️ **Code:**

- [Caffe-based](https://github.com/msracver/Deep-Image-Analogy)

✅ [**Fashion Style Generator**] [[Paper\]](https://www.ijcai.org/proceedings/2017/0520.pdf) *(IJCAI 2017)*

✅ [**Deep Painterly Harmonization**] [[Paper\]](https://arxiv.org/abs/1804.03189)

❇️ **Code:**

- [Torch-based](https://github.com/luanfujun/deep-painterly-harmonization)

✅ [**Fast Face-Swap Using Convolutional Neural Networks**] [[Paper\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Korshunova_Fast_Face-Swap_Using_ICCV_2017_paper.pdf) *(ICCV 2017)*

✅ [**Learning Selfie-Friendly Abstraction from Artistic Style Images**] [[Paper\]](https://github.com/ycjing/Neural-Style-Transfer-Papers/blob/master) *(ACML 2018)*

## Application

✅ [**Prisma**](https://prisma-ai.com/)

✅ [**Ostagram**](https://ostagram.ru/)

❇️ **Code:**

- [Website code](https://github.com/SergeyMorugin/ostagram)

✅ [**Deep Forger**](https://deepforger.com/)

✅ [**NeuralStyler**](http://neuralstyler.com/)

✅ [**Style2Paints**](http://paintstransfer.com/)

❇️ **Code:**

- [Website code](https://github.com/lllyasviel/style2paints)

## Application Papers

✅ [**Bringing Impressionism to Life with Neural Style Transfer in Come Swim**] [[Paper\]](https://arxiv.org/pdf/1701.04928.pdf)

✅ [**Imaging Novecento. A Mobile App for Automatic Recognition of Artworks and Transfer of Artistic Styles**] [[Paper\]](https://www.micc.unifi.it/wp-content/uploads/2017/01/imaging900.pdf)

✅ [**ProsumerFX: Mobile Design of Image Stylization Components**] [[Paper\]](https://www.researchgate.net/publication/319631844_ProsumerFX_Mobile_Design_of_Image_Stylization_Components)

✅ [**Pictory - Neural Style Transfer and Editing with coreML**] [[Paper\]](https://www.researchgate.net/publication/320035123_Demo_Pictory_-_Neural_Style_Transfer_and_Editing_with_CoreML)

✅ [**Tiny Transform Net for Mobile Image Stylization**] [[Paper\]](https://dl.acm.org/citation.cfm?id=3079034) *(ICMR 2017)*

## Blogs

✅ [**Caffe2Go**][<https://code.facebook.com/posts/196146247499076/delivering-real-time-ai-in-the-palm-of-your-hand/>]

✅ [**Supercharging Style Transfer**][<https://research.googleblog.com/2016/10/supercharging-style-transfer.html>]

✅ [**Issue of Layer Chosen Strategy**][<http://yongchengjing.com/pdf/Issue_layerChosenStrategy_neuralStyleTransfer.pdf>]

✅ [**Picking an optimizer for Style Transfer**][<https://blog.slavv.com/picking-an-optimizer-for-style-transfer-86e7b8cba84b>]

## To be classified

✅ [**Conditional Fast Style Transfer Network**] [[Paper\]](http://img.cs.uec.ac.jp/pub/conf17/170612yanai_0.pdf)

✅ [**Unseen Style Transfer Based on a Conditional Fast Style Transfer Network**] [[Paper\]](https://openreview.net/forum?id=H1Y7-1HYg&noteId=H1Y7-1HYg)

✅ [**DeepStyleCam: A Real-time Style Transfer App on iOS**][[Paper\]](http://img.cs.uec.ac.jp/pub/conf16/170103tanno_0.pdf)