### Text classification using CNN written in tensorflow.

원문 링크 : http://manishankert.blogspot.com/2017/04/text-classification-using-cnn-writte-in.html

**Problem statement :**

You are supposed to build a model which automatically classifies an article under Finance, Law, Fashion and Lifestyle. Use the data from leading magazines for training the model.

**Solution**:
  

Github Repo : https://github.com/manishanker/cnn_text_classification

In past, I had used NLTK and python to solve the above problem, but neural networks have proven to be more accurate when it comes to NLP. I had researched on text classification libraries and different approaches to solve this problem and decided to use CNN.

I have used Denny Britz code for implementing the CNN(https://en.wikipedia.org/wiki/Convolutional_neural_network). 

Blog posting : http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/



I would describe the files and the procedure I followed to get the data, train the model, test the model and the results.

First, I went to the leading newspaper

TheGuardian(https://www.theguardian.com/international)

and looked for the labels i.e Finance, Law, Fashion, Lifestyle. Scraping the data from the same source would be help in keeping the homogeneity in the articles.

I have used

Goose(https://github.com/grangier/python-goose)

and 

BeautifulSoup(https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 

to scrape the articles. Code for the same is uploaded in the

Github(https://github.com/manishanker/cnn_text_classification/tree/master/raw_data). The folder structure and the data files description is as follows:

raw_data/  ​                            Contains files related to train and test

├──

collect_url_data.py               Python script that scrapes articles       

├──  data        ​                                 Training data folder

│   ├──  fashion_7000.txt ​      7000 training data for class fashion

│   ├──  finance_7000.txt       7000 training data for class finance

│   ├──  law_7000.txt   ​           7000 training data for class law

│   └── lifestyle_7000.txt       7000 training data for class lifestyle

├──  fashion                                 From original scraped data and cleaned one

│   ├──  fashion_7000.txt         7000 training data for class fashion

│   ├──  fashion_original.txt       Original scraped data

│   ├──  log                                 Log output of python

│   ├──  test_fashion.txt  ​         test data for python 1001 samples

│   ├── urls.txt                           urls which were scraped

│   └──urltext.txt                    raw text from urls

├──  finance                            From original scraped data and cleaned one

│   ├──  finance.txt                  raw text from urls

│   ├──  finance_7000.txt          7000 training data for class finance

│   ├──  finance_urls.txt             urls scraped for finance

│   ├──  log_financ                     log output

│   ├──  original_finance.txt      Original scraped file

│   └── test_finance.txt           test sample for finance

├── law                                     Data folder for law

│   ├── law.txt                         scraped data for law

│   ├── law_7000.txt              7000 training samples for law

│   ├── law_urls.txt                urls scraped for law

│   ├── log_law                       log output

│   ├── original_law.txt         original scraped data for law

│   └── test_law.txt                test data for law

└── lifestyle                            Data folder for lifestyle

​    ├── lifestyle.txt                  cleaned data for lifestyle

​    ├── lifestyle_7000.txt        7000 training samples for lifestyle

​    ├── lifestyle_urls.txt         urls collected for scraping

​    ├── log_lifestyle                 log output of the script

​    ├── original_lifestyle.txt   original scraped data

​    └── test_lifestyle.txt          test data for lifestyle

Using the python script (https://github.com/manishanker/cnn_text_classification/blob/master/raw_data/collect_url_data.py)

I have scraped the above categories. Each folder has the respective raw data and the cleaned data. I have cleaned the unnecessary lines using sed.

Once the data was ready, I went through the basics of neural networks and made appropriate changes in the tensorflow code to solve the problem. Changes include changing the source files and increasing the array size on  lines 16-20 and 52 in this

script(https://github.com/manishanker/cnn_text_classification/blob/master/train.py#L20)

Once the script was ready and the required python libraries were installed, I was able to successfully run the code and tensorflow created a new folder called runs, which holds the final results.

Here is a screenshot of the results.

[![img](https://1.bp.blogspot.com/-e1LfEma0EjE/WPkVmV9622I/AAAAAAAAJJg/mSBLicMLglANn_IFvWgoauLr7t_nFMAcwCLcB/s640/Accuracy.PNG)](https://1.bp.blogspot.com/-e1LfEma0EjE/WPkVmV9622I/AAAAAAAAJJg/mSBLicMLglANn_IFvWgoauLr7t_nFMAcwCLcB/s1600/Accuracy.PNG)





Picture(https://drive.google.com/file/d/0B_5QsuonCZarV0hzcEJCZlNvMjQ/view)

Results:

I was able to get 94 % accuracy using the second checkpoint in the runs folder.

Here is the google sheet(https://docs.google.com/spreadsheets/d/1CKeoGyhmYdAAJ42BEQ7p3IM9uSCVoMftyXNu4j4ER5s/edit)

Unfortunately there were few empty lines since I had split the article in the training data, CNN predicted the label for that anyway. I could have avoided this mistake.

If you have more questions, feel free to reach out to me at shanker.mani0@gmail.com.

Happy hacking !