# Keras Tutorial: Content Based Image Retrieval Using a Convolutional Denoising Autoencoder

**Content based image retrieval** (CBIR) systems enable to find similar images to a query image among an image dataset. The most famous CBIR system is the search per image feature of Google search. This article uses the [**keras**](https://keras.io/)**deep learning framework to perform image retrieval on the** [**MNIST dataset**](http://yann.lecun.com/exdb/mnist/).

Our CBIR system will be based on a **convolutional denoising autoencoder**. It is a class of **unsupervised deep learning** algorithms.

### Content based image retrieval

To explain what content based image retrieval (CBIR) is, I am going to quote this [research paper](http://www.baskent.edu.tr/~hogul/RA1.pdf).

> *There are two [image retrieval] frameworks: text-based and content-based. The text-based approach can be tracked back to 1970s. In such systems, the images are manually annotated by text descriptors, which are then used by a database management system to perform image retrieval. There are two disadvantages with this approach. The first is that a considerable level of human labour is required for manual annotation. The second is the annotation inaccuracy due to the subjectivity of human perception. To overcome the above disadvantages in text-based retrieval system, content-based image retrieval (CBIR) was introduced in the early 1980s.* **In CBIR, images are indexed by their visual content, such as color, texture, shapes.**

Basically we first **extract features** from an image database and store it. Then we compute the features associated with a **query image.** Finally we **retrieve images with the closest features**.



![img](https://cdn-images-1.medium.com/max/2000/1*A8XGoiRfGusTxdfmglrKww.png)

### Feature extraction for content based image retrieval

The **key point** about content based image retrieval is the **feature extraction**. The features correspond to the way we represent an image on a high level. How to describe the colours on an image? Its texture? The shapes on it? The features we extract should also allow an efficient retrieval of the images. This is especially true if we have a big image database.

There are many ways to extract these features.

One way is to use what we call **hand crafted features**. Examples are: [**histogram of colours**](https://en.wikipedia.org/wiki/Color_histogram) to define colours, [**histogram of oriented gradients**](https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients) to define shapes.

Other descriptors like [**SIFT**](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) and [**SURF**](https://en.wikipedia.org/wiki/Speeded_up_robust_features) have proven to be robust for image retrieval applications.

Another possibility is to use deep learning algorithms. In this [research paper](https://arxiv.org/pdf/1404.1777.pdf)the authors demonstrate that [**convolutional neural networks**](http://cs231n.github.io/convolutional-networks/) (CNN) trained for classification purposes can be used to extract a ‘neural code’ for images. These neural codes are the features used to describe images. It also demonstrates that it performs as well as state of the art approaches on many datasets. The problem about this approach is that we first need labelled data to train the neural network. **The labelling task can be costly and time consuming**. Another way to generate these ‘neural codes’ for our image retrieval task is to use an unsupervised deep learning algorithm. This is where the **denoising autoencoder** comes.

### Denoising autoencoder

A **denoising autoencoder** is a **feed forward neural network that learns to denoise images**. By doing so the neural network learns interesting features on the images used to train it. Then **it can be used to extract features** from similar images to the training set.



![img](https://cdn-images-1.medium.com/max/1600/1*G0V4dz4RKTKGpebeoSWB0A.png)

If you are not familiar with autoencoders, I highly recommend to first browse these three sources:

- [Deep learning book](http://www.deeplearningbook.org/)
- Course [videos](https://www.youtube.com/watch?v=FzS3tMl4Nsc) by Hugo Larochelle
- [Autoencoder keras tutorial](https://blog.keras.io/building-autoencoders-in-keras.html)

### Denoising autoencoder for content based image retrieval

We use the convolutional denoising autoencoder algorithm provided on [keras](https://blog.keras.io/building-autoencoders-in-keras.html)tutorial.

#### Training the model



<iframe width="700" height="250" data-src="/media/0a37bef5b15c9782a6548bd5c7b163a4?postId=dc91450cc511" data-media-id="0a37bef5b15c9782a6548bd5c7b163a4" data-thumbnail="https://i.embed.ly/1/image?url=https%3A%2F%2Favatars1.githubusercontent.com%2Fu%2F20651903%3Fv%3D4%26s%3D400&amp;key=a19fcc184b9711e1b4764040d3dc5c07" class="progressiveMedia-iframe js-progressiveMedia-iframe" allowfullscreen="" frameborder="0" src="https://blog.sicara.com/media/0a37bef5b15c9782a6548bd5c7b163a4?postId=dc91450cc511" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 1208.98px;"></iframe>

For the general explanations on the above lines of code please refer to [keras tutorial](https://blog.keras.io/building-autoencoders-in-keras.html).

Notice that there are small differences compared to the tutorial. The first difference is this line:

```
encoded = MaxPooling2D((2, 2), padding='same', name='encoder')(x)
```

We set a name to the encoder layer in order to be able to access it.

We also saved the learned model by adding:

```
autoencoder.save('autoencoder.h5')
```

This will enable us to load it later in order to test it.

Finally, we reduced the number of epochs from 100 to 20 in order to save time :).

#### Denoising an image

Let’s try our learned model to denoise an input test image.

First we regenerate the noisy data and load the previously trained autoencoder.



<iframe width="700" height="250" data-src="/media/a405206214b7b0ccc8a77a35f370b9c6?postId=dc91450cc511" data-media-id="a405206214b7b0ccc8a77a35f370b9c6" data-thumbnail="https://i.embed.ly/1/image?url=https%3A%2F%2Favatars1.githubusercontent.com%2Fu%2F20651903%3Fv%3D4%26s%3D400&amp;key=a19fcc184b9711e1b4764040d3dc5c07" class="progressiveMedia-iframe js-progressiveMedia-iframe" allowfullscreen="" frameborder="0" src="https://blog.sicara.com/media/a405206214b7b0ccc8a77a35f370b9c6?postId=dc91450cc511" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 724.984px;"></iframe>

Then we call the following function that denoises the first noisy test image and plot it:



<iframe width="700" height="250" data-src="/media/da9d96537af02246aac6dc83b291a7d5?postId=dc91450cc511" data-media-id="da9d96537af02246aac6dc83b291a7d5" data-thumbnail="https://i.embed.ly/1/image?url=https%3A%2F%2Favatars1.githubusercontent.com%2Fu%2F20651903%3Fv%3D4%26s%3D400&amp;key=a19fcc184b9711e1b4764040d3dc5c07" class="progressiveMedia-iframe js-progressiveMedia-iframe" allowfullscreen="" frameborder="0" src="https://blog.sicara.com/media/da9d96537af02246aac6dc83b291a7d5?postId=dc91450cc511" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 262.984px;"></iframe>

The result is



![img](https://cdn-images-1.medium.com/max/1600/1*Ontq0fsdqOmNLzznPYg75A.jpeg)

Noisy image



![img](https://cdn-images-1.medium.com/max/1600/1*GDXkINmL31jHWcCKK75Rqw.jpeg)

Denoised image

#### Computing the features of the training dataset

Our image database is the MNIST training dataset.

Our goal is to **provide a query image and find the closest MNIST images**.

First, **we compute the features of the training dataset and the query images**:



<iframe width="700" height="250" data-src="/media/b32468d2c385fc1369948632a30b3286?postId=dc91450cc511" data-media-id="b32468d2c385fc1369948632a30b3286" data-thumbnail="https://i.embed.ly/1/image?url=https%3A%2F%2Favatars1.githubusercontent.com%2Fu%2F20651903%3Fv%3D4%26s%3D400&amp;key=a19fcc184b9711e1b4764040d3dc5c07" class="progressiveMedia-iframe js-progressiveMedia-iframe" allowfullscreen="" frameborder="0" src="https://blog.sicara.com/media/b32468d2c385fc1369948632a30b3286?postId=dc91450cc511" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 1099px;"></iframe>

#### Scoring function

Before scoring our model we need to understand the scoring function we will use.

To assess the model, we use the [scikit learn](http://scikit-learn.org/stable/) **function:**[**label_ranking_average_precision_score**](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html). This function takes two arrays as input. First an array of zeros and ones. Second an array of relevance scores.

In our case, we compute the relevance score from the computed distance between the feature of the query image and the images of the database. The lower the distance the higher the relevance score should be.

We construct the first array following this rule: for each image on database, if the image has the same label as the query image, we append a ‘1’ to the array. Otherwise we append a ‘0’.

This scoring function **returns a maximum score of 1 if the closest images have the same label as the query image**. If there are images with a different label that are closer to the query image, the score decreases.

To get a feel of what it does let’s compute the value of this scoring function on some examples.

Suppose we have a query image with label ‘7’ and that we have four images in our database with following labels : ‘7’, ‘7’, ‘1’, ‘0’. The first two images of the database are relevant regarding the query image, and the two last ones are not. The first array that we pass to the scoring function should be [1, 1, 0, 0]. For each image on our image database we will compute a relevance score:



<iframe width="700" height="250" data-src="/media/5c61772e0d45f843f1f61e4aa9c20e11?postId=dc91450cc511" data-media-id="5c61772e0d45f843f1f61e4aa9c20e11" data-thumbnail="https://i.embed.ly/1/image?url=https%3A%2F%2Favatars1.githubusercontent.com%2Fu%2F20651903%3Fv%3D4%26s%3D400&amp;key=a19fcc184b9711e1b4764040d3dc5c07" class="progressiveMedia-iframe js-progressiveMedia-iframe" allowfullscreen="" frameborder="0" src="https://blog.sicara.com/media/5c61772e0d45f843f1f61e4aa9c20e11?postId=dc91450cc511" style="display: block; position: absolute; margin: auto; max-width: 100%; box-sizing: border-box; transform: translateZ(0px); top: 0px; left: 0px; width: 700px; height: 681px;"></iframe>

#### Scoring the model

**For each query image feature, we compute the Euclidian distance to the training dataset images features**. The closer the distance the higher the relevance score should be. Then we apply the scoring function label_ranking_average_precision_score to our results.