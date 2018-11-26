# Tencent ML-Images

GitHub 링크 : https://github.com/Tencent/tencent-ml-images



This repository introduces the open-source project dubbed **Tencent ML-Images**, which publishes

- **ML-Images**: the largest open-source multi-label image database, including 17,609,752 training and 88,739 validation image URLs, which are annotated with up to 11,166 categories
- **Resnet-101 model**: it is pre-trained on ML-Images, and achieves the top-1 accuracy 80.73% on ImageNet via transfer learning

## Updates

- **NOTE**: A clear demonstration about how to download the original images using URLs has been added into the subsection `How to handle the invalid URLs during downloading?`
- A demo for single-label image classification has been added to `Single-Label Image Classification`. One can use the provided checkpoint to predict the label of any custom image.

# Contents

- [Dependencies](https://github.com/Tencent/tencent-ml-images#dependencies)
- [Data](https://github.com/Tencent/tencent-ml-images#data)
  - [Download](https://github.com/Tencent/tencent-ml-images#download)
  - [Image Source](https://github.com/Tencent/tencent-ml-images#source)
  - [Semantic Hierarchy](https://github.com/Tencent/tencent-ml-images#hierarchy)
  - [Annotations](https://github.com/Tencent/tencent-ml-images#annotation)
  - [Statistics](https://github.com/Tencent/tencent-ml-images#statistics)
- [Train](https://github.com/Tencent/tencent-ml-images#train)
  - Download Images using URLs
    - [How to handle the invalid URLs during downloading?](https://github.com/Tencent/tencent-ml-images#invalid-URLs)
  - [Prepare the TFRecord File](https://github.com/Tencent/tencent-ml-images#prepare-tfrecord)
  - [Pretrain on ML-Images](https://github.com/Tencent/tencent-ml-images#pretrain)
  - [Finetune on ImageNet](https://github.com/Tencent/tencent-ml-images#finetune)
  - [Checkpoints](https://github.com/Tencent/tencent-ml-images#checkpoint)
  - [Single-Label Image Classification](https://github.com/Tencent/tencent-ml-images#classification)
  - [Feature Extraction](https://github.com/Tencent/tencent-ml-images#feature-extraction)
- [Results](https://github.com/Tencent/tencent-ml-images#result)
- [Copyright](https://github.com/Tencent/tencent-ml-images#copyright)
- [Citation](https://github.com/Tencent/tencent-ml-images#citation)

# [Dependencies](https://github.com/Tencent/tencent-ml-images#dependencies)

- Linux
- [Python 2.7](https://www.python.org/)
- [Tensorflow >= 1.6.0](https://www.tensorflow.org/install/)

# [Data](https://github.com/Tencent/tencent-ml-images#data)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

### [Download](https://github.com/Tencent/tencent-ml-images#download)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

- train_urls.txt ([link1](https://drive.google.com/open?id=1ExY0GpRWxGzDHAI-p44m-B0AB76NeLy7), [link2](https://pan.baidu.com/s/1cx6n6CYNqegKVq1O2YVCJg))
- val_urls.txt ([link1](https://drive.google.com/open?id=13SSar872e73UcshIW7IGbmvUGcFjHyxg), [link2](https://pan.baidu.com/s/1BfipStD2PY7MAMRoZa9ecg))

The image URLs and the corresponding annotations can be downloaded above.

The format of `train_urls.txt` is as follows

```
...
https://c4.staticflickr.com/8/7239/6997334729_e5fb3938b1_o.jpg  3:1  5193:0.9  5851:0.9 9413:1 9416:1
https://c2.staticflickr.com/4/3035/3033882900_a9a4263c55_o.jpg  1053:0.8  1193:0.8  1379:0.8
...
```

As shown above, one image corresponds to one row. The first term is the image URL. The followed terms separated by space are the annotations. For example, "5193:0.9" indicates class 5193 and its confidence 0.9. Note that the class index starts from 0, and you can find the class name from the file [data/dictionary_and_semantic_hierarchy.txt](https://github.com/Tencent/tencent-ml-images/blob/master/data/dictionary_and_semantic_hierarchy.txt).

### [Image Source](https://github.com/Tencent/tencent-ml-images#source)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

The image URLs of ML-Images are collected from [ImageNet](http://www.image-net.org/) and [Open Images](https://github.com/openimages/dataset). Specifically,

- Part 1: From the whole database of ImageNet, we adopt 10,706,941 training and 50,000 validation image URLs, covering 10,032 categories.
- Part 2: From Open Images, we adopt 6,902,811 training and 38,739 validation image URLs, covering 1,134 unique categories (note that some other categories are merged with their synonymous categories from ImageNet).

Finally, ML-Images includes 17,609,752 training and 88,739 validation image URLs, covering 11,166 categories.

### [Semantic Hierarchy](https://github.com/Tencent/tencent-ml-images#hierarchy)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

We build the semantic hiearchy of 11,166 categories, according to [WordNet](https://wordnet.princeton.edu/). The direct parent categories of each class can be found from the file [data/dictionary_and_semantic_hierarchy.txt](https://github.com/Tencent/tencent-ml-images/blob/master/data/dictionary_and_semantic_hierarchy.txt). The whole semantic hierarchy includes 4 independent trees, of which the root nodes are `thing`, `matter`, `object, physical object` and `atmospheric phenomenon`, respectively. The length of the longest semantic path from root to leaf nodes is 16, and the average length is 7.47.

### [Annotations](https://github.com/Tencent/tencent-ml-images#annotation)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

Since the image URLs of ML-Images are collected from ImageNet and Open Images, the annotations of ML-Images are constructed based on the original annotations from ImageNet and Open Images. Note that the original annotations from Open Images are licensed by Google Inc. under [CC BY-4.0](https://creativecommons.org/licenses/by/4.0/). Specifically, we conduct the following steps to construct the new annotations of ML-Images.

- For the 6,902,811 training URLs from Open Images, we remove the annotated tags that are out of the remained 1,134 categories.
- According to the constructed [semantic hierarchy](https://github.com/Tencent/tencent-ml-images/blob/master/data/dictionary_and_semantic_hierarchy.txt) of 11,166 categories, we augment the annotations of all URLs of ML-Images following the cateria that if one URL is annotated with category i, then all ancestor categories will also be annotated to this URL.
- We train a ResNet-101 model based on the 6,902,811 training URLs from Open Images, with 1,134 outputs. Using this ResNet-101 model, we predict the tags from 1,134 categories for the 10,756,941 single-annotated image URLs from ImageNet. Consequently, we obtain a normalized co-occurrence matrix between 10,032 categories from ImageNet and 1,134 categories from Open Images. We can determine the strongly co-occurrenced pairs of categories. For example, category i and j are strongly co-occurrenced; then, if one image is annotated with category i, then category j should also be annotated.

The annotations of all URLs in ML-Images are stored in `train_urls.txt` and `val_urls.txt`.

### [Statistics](https://github.com/Tencent/tencent-ml-images#statistics)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

The main statistics of ML-Images are summarized in ML-Images.

| # Train images | # Validation images | # Classes | # Trainable Classes | # Avg tags per image | # Avg images per class |
| -------------- | ------------------- | --------- | ------------------- | -------------------- | ---------------------- |
| 17,609,752     | 88,739              | 11,166    | 10,505              | 8                    | 1447.2                 |

Note: *Trainable class* indicates the class that has over 100 train images.

The number of images per class and the histogram of the number of annotations in training set are shown in the following figures.

[![GitHub](https://github.com/Tencent/tencent-ml-images/raw/master/git_images/num_images_per_class.png)](https://github.com/Tencent/tencent-ml-images/blob/master/git_images/num_images_per_class.png) [![GitHub](https://github.com/Tencent/tencent-ml-images/raw/master/git_images/hist_num_annotations.png)](https://github.com/Tencent/tencent-ml-images/blob/master/git_images/hist_num_annotations.png)

# [Train](https://github.com/Tencent/tencent-ml-images#train)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

### [Download Images using URLs](https://github.com/Tencent/tencent-ml-images#download-image)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

The full `train_urls.txt` is very large. Here we provide a tiny file [train_urls_tiny.txt](https://github.com/Tencent/tencent-ml-images/blob/master/data/train_urls_tiny.txt) to demonstrate the downloading procedure.

```
cd data
./download_urls_multithreading.sh
```

A sub-folder `data/images` will be generated to save the downloaded jpeg images, as well as a file `train_im_list_tiny.txt` to save the image list and the corresponding annotations.

#### [How to handle the invalid URLs during downloading?](https://github.com/Tencent/tencent-ml-images#invalid-URLs)

##### For URLs from ImageNet

The first 10,706,941 rows of `train_urls.txt` and the first 50,000 rows of `val_urls.txt` are URLs from ImageNet. A large proportion of these URLs have expired. However, the ImageNet website could provide the original images (see <http://image-net.org/download>), as well as the corresponse between each image ID and its original URL. Thus, we provide two novel files, that tell the image ID of each URL used in our database, including `train_urls_and_index_from_imagenet.txt` and `val_urls_and_index_from_imagenet.txt`.

- train_urls_and_index_from_imagenet.txt ([link1](https://drive.google.com/open?id=1iK5j1zJ7SkitQ3ZIblYbUalAr5nFlngj), [link2](https://pan.baidu.com/s/145sGwH8Tv3RVwXZ95DuN4w))
- val_urls_and_index_from_imagenet.txt ([link1](https://drive.google.com/open?id=1ojVU0TIA3n9ytOW8p94IWbGD8QfXAfNj), [link2](https://pan.baidu.com/s/1p5sQrMUbfxiG94OjHj9-mQ))

The format is as follows

```
...
n03874293_7679  http://image24.webshots.com/24/5/62/52/2807562520031003846EfpYGc_fs.jpg 2964:1  2944:1  2913:1  2896:1  2577:1  1833:1  1054:1  1041:1  865:1   2:1
n03580845_3376  http://i02.c.aliimg.com/img/offer/22/85/63/27/9/228563279   3618:1  3604:1  1835:1  1054:1  1041:1  865:1   2:1
...
```

In each row, the first term is the image ID in ImageNet, while other terms are the corresponding URL and annotations. Then, two steps should be done to obtain the images used in ML-Images:

- Download the original images of the whole database of ImageNet from (<http://image-net.org/download>), and the corresponding URL file is `List of all image URLs of Fall 2011 Release` (see <http://image-net.org/download-imageurls>)
- Pick out the images used in ML-Images, accoording to `train_urls_and_index_from_imagenet.txt` and `val_urls_and_index_from_imagenet.txt`.

##### For URLs from Open Images

The last 6,902,811 rows of `train_urls.txt` and the last 38,739 rows of `val_urls.txt` are URLs from Open Images. Most of these URLs are valid, and you can directly download the images using the provided `download_urls_multithreading.sh`.

### [Prepare the TFRecord File](https://github.com/Tencent/tencent-ml-images#prepare-tfrecord)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

Here we generate the tfrecords using the multithreading module. One should firstly split the file `train_im_list_tiny.txt`into multiple smaller files, and save them into the sub-folder `data/image_lists/`.

```
cd data
./tfrecord.sh
```

Multiple tfrecords (named like `x.tfrecords`) will saved to `data/tfrecords/`.

### [Pretrain on ML-Images](https://github.com/Tencent/tencent-ml-images#pretrain)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

Before training, one should move the train and validation tfrecords to `data/ml-images/train` and `data/ml-images/val`, respectively. Then,

```
./example/train.sh
```

**Note**: Here we only provide the training code in the single node single GPU framework, while our actual training on ML-Images is based on an internal distributed training framework (not released yet). One could modify the training code to the distributed framework following [distributed tensorFlow](https://www.tensorflow.org/deploy/distributed).

### [Finetune on ImageNet](https://github.com/Tencent/tencent-ml-images#finetune)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

One should firstly download the ImageNet (ILSVRC2012) database, then prepare the tfrecord file using [tfrecord.sh](https://github.com/Tencent/tencent-ml-images/blob/master/example/tfrecord.sh). Then, you can finetune the ResNet-101 model on ImageNet as follows, with the checkpoint pre-trained on ML-Images.

```
./example/finetune.sh
```

### [Checkpoints](https://github.com/Tencent/tencent-ml-images#checkpoint)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

- ckpt-resnet101-mlimages ([link1](https://drive.google.com/open?id=1FKkw2HD0jrCJKOM_kpyOvZ_m_YPA9tdV), [link2](https://pan.baidu.com/s/1166673BNWuIeWxD7lf6RNA)): pretrained on ML-Images
- ckpt-resnet101-mlimages-imagenet ([link1](https://drive.google.com/open?id=1wIhRemoPxTw7uDz-TlwfYJsOR2usb2kg), [link2](https://pan.baidu.com/s/1UE7gavcVznYVA5NZ-GFAvg)): pretrained on ML-Images and finetuned on ImageNet (ILSVRC2012)

Please download above two checkpoints and move them into the folder `checkpoints/`, if you want to extract features using them.

### [Single-Label Image Classification](https://github.com/Tencent/tencent-ml-images#classification)

Here we provide a demo for single-label image-classification, using the checkpoint `ckpt-resnet101-mlimages-imagenet`downloaded above.

```
./example/image_classification.sh
```

The prediction will be saved to `label_pred.txt`. If one wants to recognize other images, `data/im_list_for_classification.txt` should be modified to include the path of these images.

### [Feature Extraction](https://github.com/Tencent/tencent-ml-images#feature-extraction)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

```
./example/extract_feature.sh
```

# [Results](https://github.com/Tencent/tencent-ml-images#result)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

The retults of different ResNet-101 checkpoints on the validation set of ImageNet (ILSVRC2012) are summarized in the following table.

| Checkpoints                                                  | Train and finetune setting                             | Top-1 acc on Val 224 | Top-5 acc on Val 224 | Top-1 acc on Val 299 | Top-5 accuracy on Val 299 |
| ------------------------------------------------------------ | ------------------------------------------------------ | -------------------- | -------------------- | -------------------- | ------------------------- |
| [MSRA ResNet-101](https://github.com/KaimingHe/deep-residual-networks) | train on ImageNet                                      | 76.4                 | 92.9                 | --                   | --                        |
| [Google ResNet-101 ckpt1](https://arxiv.org/abs/1707.02968)  | train on ImageNet, 299 x 299                           | --                   | --                   | 77.5                 | 93.9                      |
| Our ResNet-101 ckpt1                                         | train on ImageNet                                      | 77.8                 | 93.9                 | 79.0                 | 94.5                      |
| [Google ResNet-101 ckpt2](https://arxiv.org/abs/1707.02968)  | Pretrain on JFT-300M, finetune on ImageNet, 299 x 299  | --                   | --                   | 79.2                 | 94.7                      |
| Our ResNet-101 ckpt2                                         | Pretrain on ML-Images, finetune on ImageNet            | **78.8**             | **94.5**             | 79.5                 | 94.9                      |
| Our ResNet-101 ckpt3                                         | Pretrain on ML-Images, finetune on ImageNet 224 to 299 | 78.3                 | 94.2                 | **80.73**            | **95.5**                  |
| Our ResNet-101 ckpt4                                         | Pretrain on ML-Images, finetune on ImageNet 299 x 299  | 75.8                 | 92.7                 | 79.6                 | 94.6                      |

Note:

- if not specified, the image size in training/finetuning is 224 x 224.
- *finetune on ImageNet from 224 to 299* means that the image size in early epochs of finetuning is 224 x 224, then 299 x 299 in late epochs.
- *Top-1 acc on Val 224* indicates the top-1 accuracy on 224 x 224 validation images.

# [Copyright](https://github.com/Tencent/tencent-ml-images#copyright)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

The annotations of images are licensed by Tencent under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. The contents of this repository, including the codes, documents and checkpoints, are released under an [BSD 3-Clause](https://opensource.org/licenses/BSD-3-Clause) license. Please refer to [LICENSE](https://github.com/Tencent/tencent-ml-images/blob/master/LICENSE.txt) for more details.

If there is any concern about the copyright of any image used in this project, please [email us](mailto:wubaoyuan1987@gmail.com).

# [Citation](https://github.com/Tencent/tencent-ml-images#citation)

[[back to top](https://github.com/Tencent/tencent-ml-images#)]

The arxiv paper describling the details of this project will be available soon!