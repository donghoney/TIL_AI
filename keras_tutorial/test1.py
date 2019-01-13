import numpy as np
from keras.models import Model
from keras.datasets import mnist
from keras.models import load_model
from sklearn.metrics import label_ranking_average_precision_score
import os
cur_path = str(os.path.dirname(os.path.abspath(__file__)))
print('current path :',cur_path)
(x_train, y_train),(x_test,y_test) = mnist.load_data()

print(x_train.shape)
print(y_train[0])
for i in range(0,10):
    print(y_train[i])