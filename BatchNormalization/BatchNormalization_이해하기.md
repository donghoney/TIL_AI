# Understanding Batch Normalization with Examples in Numpy and Tensorflow with Interactive Code

[![Go to the profile of Jae Duk Seo](https://cdn-images-1.medium.com/fit/c/100/100/0*LxeFHiTjRmxNK5vQ.jpg)](https://towardsdatascience.com/@SeoJaeDuk?source=post_header_lockup)

![img](https://cdn-images-1.medium.com/max/1600/1*XDDcoYNNTTvVJqnb-YrnnQ.gif)

Gif from [here](https://imgur.com/gallery/j6JLpVA)

So for today, I am going to explore batch normalization ([*Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*](https://arxiv.org/abs/1502.03167) *by* [*Sergey Ioffe*](https://arxiv.org/find/cs/1/au:+Ioffe_S/0/1/0/all/0/1)*, and* [*Christian Szegedy*](https://arxiv.org/find/cs/1/au:+Szegedy_C/0/1/0/all/0/1)). However, to strengthen my understanding for data preprocessing, I will cover 3 cases,

**Case 1** — [Normalization](http://www.dataminingblog.com/standardization-vs-normalization/): Whole Data (Numpy)
**Case 2** — [Standardization](http://www.dataminingblog.com/standardization-vs-normalization/): Whole Data (Numpy)
**Case 3** — [Batch Normalization](https://arxiv.org/abs/1502.03167): Mini Batch (Numpy / Tensorflow)

***\* NOTE **** I won’t cover back propagation in this post!

------

**Experiment Set Up**



![img](https://cdn-images-1.medium.com/max/1200/1*v9Qdu7kEM7ZrbC-rFnvzIg.png)



![img](https://cdn-images-1.medium.com/max/1200/1*t6hXXvoqeJe4hhh8wH5dfQ.png)

The set up for this experiment is extremely simple. To simulate real world use case, lets create an 32*32 image from random normal distrubition and add some noise to it. Above is how our image looks like.



![img](https://cdn-images-1.medium.com/max/800/1*4TK0h4_AINYymXWbFGP2Fw.png)



![img](https://cdn-images-1.medium.com/max/1600/1*fJiU3WouiU_3mGstSs0Zyg.png)

**Red Box** → (# of Images, Width of Image, Height of Image, # of channels) for now we will be working with 32*32 gray scale images. 
**Left Graph** → Histogram of our Image data

As you can see above, our images have mean of 26 and Variance of 306. And on the left we can see the histogram of our image data.

------

**Case 1: Normalization — Whole Data**



![img](https://cdn-images-1.medium.com/max/1200/1*FxUb57f-MnTsXKe3hK_cbg.png)



![img](https://cdn-images-1.medium.com/max/1200/1*AnoNwYUac9Xk0-Kj8_1Xmg.png)

For our first case lets perform normalization on the whole data set. Visually there is no difference we can observe.



![img](https://cdn-images-1.medium.com/max/800/1*Hnzh1LSq-wS41d7fKfyuaw.png)



![img](https://cdn-images-1.medium.com/max/1600/1*awI18jG3_emJ98Tz5mztuw.png)

However, once we plot the histogram or view the mean and the standard deviation, we can clearly see that our data is in the range of 0 and 1.

------

**Case 2: Standardization — Whole Data**



![img](https://cdn-images-1.medium.com/max/1200/1*Rh9FAXH_EtaJwaKqVh4oEA.png)



![img](https://cdn-images-1.medium.com/max/1200/1*p1RDofSFrSZcpa8Y6z1Y8A.png)

Again, visually I can’t see anything too difference from one another.



![img](https://cdn-images-1.medium.com/max/800/1*JevHVRMixsivWcEulq5VPQ.png)



![img](https://cdn-images-1.medium.com/max/1600/1*huExjJIhG1mq6zRPK6d5xQ.png)

However, when we see the axis of the histogram, we can clearly see that the mean of the our data have shifted to 0 (almost) and variance is 1.

------

**Equations for Normalization / Standardization**









Image from this [website](http://www.dataminingblog.com/standardization-vs-normalization/)

**Left →** Equation for Normalization 
**Right** → Equation for Standardization

Just in case, if anyone is wondering, lets review the equation for both cases normalization as well as standardization. Please note **μ** is the mean and **σ** is the standard deviation.

------

**Equation for Batch Normalization**



![img](https://cdn-images-1.medium.com/max/1600/1*Wh5KvzofrPoaod0RpkQgQA.png)

**Red Box →** Equation for Standardization
**Blue Line →** Parameters that are going to be learned

Now we have covered both normalization and standardization we can see that the equation for batch normalization is exactly the same process for standardization. The only difference is the gamma and beta term, underlined in blue. We can think of these terms exactly like weights, we are going to calculate the error from the ground truth data and using back propagation learn these parameters.

*But there is one thing I wish to note! If we set the gamma (thank you* [*Luoyang Fang*](https://medium.com/@clementlfang?source=post_info_responses---------1----------------) *for correcting me*) *as 1 and beta as 0 the whole process is just standardization. And for Tensorflow’s implementation we are going to abuse this property.*

------

**Case 3: Batch Normalization — Pure Implementation**



![img](https://cdn-images-1.medium.com/max/1600/1*SQJUUQ6dKVAh14CFubRiLg.png)

**Red Line** → Mini Batch, the first 10 images from our image data
**Blue Box** → Standardization of data



![img](https://cdn-images-1.medium.com/max/1200/1*6GsJ5Q-fRfgK_bJDxuMU6w.png)



![img](https://cdn-images-1.medium.com/max/1200/1*LtUxg28mT8tLDD45hFnYuQ.png)

There is one thing to note here, for batch normalization we are going to take the first 10 images from our test data and apply batch normalization.



![img](https://cdn-images-1.medium.com/max/800/1*xyHd9VFFyirGRD5Ez3Hleg.png)



![img](https://cdn-images-1.medium.com/max/1600/1*xEKh6m4Q76BaMk41mQoMgA.png)

Again, we can see that the mean is around 0 and variance is 1. Now lets take a look at the tensorflow’s implementation.

------

**Case 3: Batch Normalization — Tensorflow**



![img](https://cdn-images-1.medium.com/max/1600/1*-VF0YXVZXleNJjBFobtf5w.png)

**Red Line** → Mini Batch, the first 10 images from our image data
**Blue Line →** Offset (Beta) as 0, and Scale (Gamma) as 1



![img](https://cdn-images-1.medium.com/max/1200/1*LtUxg28mT8tLDD45hFnYuQ.png)



![img](https://cdn-images-1.medium.com/max/1200/1*6GsJ5Q-fRfgK_bJDxuMU6w.png)

Again, visually, we can’t see any difference.



![img](https://cdn-images-1.medium.com/max/800/1*xyHd9VFFyirGRD5Ez3Hleg.png)



![img](https://cdn-images-1.medium.com/max/1600/1*Mpme6YXMp7s3jxSNOol6QA.png)

However, if we take a look at the mean and Variance of the data we can see that it is *exactly* the same as applying standardization.

------

**Interactive Code (Google Collab/ Replit/ Microsoft Azure Notebook)**



![img](https://cdn-images-1.medium.com/max/800/1*dTM2zq8YLPvceF9rVApSfQ.png)



![img](https://cdn-images-1.medium.com/max/800/1*nWQt9z2EHbQiaiYa-75KdQ.png)



![img](https://cdn-images-1.medium.com/max/800/1*9-LZ1C0y_DJM8Ufi_ME4Bw.png)

*For Google Colab, you would need a google account to view the codes, also you can’t run read only scripts in Google Colab so make a copy on your play ground. Finally, I will never ask for permission to access your files on Google Drive, just FYI. Happy Coding!*

To access the code on Google Colab, [please click here](https://colab.research.google.com/drive/19ECWYHC72rSBuF9fQCGCuu6OAgZ1HBWu). 
To access the code on Repl it, [please click here](https://repl.it/@Jae_DukDuk/33-Batch-Norm). 
To access the code on Microsoft Azure Notebook, [please click here](https://selfcar-jaedukseo.notebooks.azure.com/nb/notebooks/33%20Batch%20Norm.ipynb).

------

**Final Words**

Recently Face book AI research group released group normalization. ([*Group Normalizatio*](https://arxiv.org/pdf/1803.08494.pdf)*n by* [*Yuxin Wu*](https://arxiv.org/find/cs/1/au:+Wu_Y/0/1/0/all/0/1)*, and* [*Kaiming He*](https://arxiv.org/find/cs/1/au:+He_K/0/1/0/all/0/1)) I’ll try to cover that.

If any errors are found, please email me at jae.duk.seo@gmail.com, if you wish to see the list of all of my writing please [view my website here](https://jaedukseo.me/).

Meanwhile follow me on my twitter [here](https://twitter.com/JaeDukSeo), and visit [my website](https://jaedukseo.me/), or my [Youtube channel](https://www.youtube.com/c/JaeDukSeo) for more content. I also did comparison of Decoupled Neural Network [here if you](https://becominghuman.ai/only-numpy-implementing-and-comparing-combination-of-google-brains-decoupled-neural-interfaces-6712e758c1af) are interested.

------

**Reference**

1. CS231n Winter 2016: Lecture 5: Neural Networks Part 2. (2018). YouTube. Retrieved 19 March 2018, from <https://www.youtube.com/watch?v=gYpoJMlgyXA&feature=youtu.be&list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC&t=3078>
2. thorey, C. (2016). What does the gradient flowing through batch normalization looks like ?. Cthorey.github.io. Retrieved 19 March 2018, from <http://cthorey.github.io/backpropagation/>
3. Deriving Batch-Norm Backprop Equations | Chris Yeh. (2018). Chrisyeh96.github.io. Retrieved 19 March 2018, from <https://chrisyeh96.github.io/2017/08/28/deriving-batchnorm-backprop.html>
4. Deriving the Gradient for the Backward Pass of Batch Normalization. (2018). Kevinzakka.github.io. Retrieved 19 March 2018, from <https://kevinzakka.github.io/2016/09/14/batch_normalization/>
5. Kratzert, F. (2018). Understanding the backward pass through Batch Normalization Layer. Kratzert.github.io. Retrieved 19 March 2018, from <https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html>
6. (2018). Arxiv.org. Retrieved 19 March 2018, from <https://arxiv.org/pdf/1502.03167.pdf>
7. numpy.histogram — NumPy v1.13 Manual. (2018). Docs.scipy.org. Retrieved 19 March 2018, from <https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.histogram.html>
8. numpy.random.weibull — NumPy v1.13 Manual. (2018). Docs.scipy.org. Retrieved 19 March 2018, from <https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.weibull.html#numpy.random.weibull>
9. numpy.var — NumPy v1.14 Manual. (2018). Docs.scipy.org. Retrieved 26 March 2018, from <https://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html>
10. data?, H. (2018). How to plot a histogram using Matplotlib in Python with a list of data?. Stackoverflow.com. Retrieved 26 March 2018, from <https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data>
11. numpy.random.randn — NumPy v1.14 Manual. (2018). Docs.scipy.org. Retrieved 27 March 2018, from <https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html>
12. Wu, Y., & He, K. (2018). Group Normalization. Arxiv.org. Retrieved 27 March 2018, from <https://arxiv.org/abs/1803.08494>
13. Standardization vs. normalization | Data Mining Blog — [www.dataminingblog.com](http://www.dataminingblog.com/). (2007). Dataminingblog.com. Retrieved 27 March 2018, from <http://www.dataminingblog.com/standardization-vs-normalization/>
14. Ioffe, S., & Szegedy, C. (2015). Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. Arxiv.org. Retrieved 27 March 2018, from <https://arxiv.org/abs/1502.03167>
15. Normal Distribution. (2018). Mathsisfun.com. Retrieved 27 March 2018, from <https://www.mathsisfun.com/data/standard-normal-distribution.html>
