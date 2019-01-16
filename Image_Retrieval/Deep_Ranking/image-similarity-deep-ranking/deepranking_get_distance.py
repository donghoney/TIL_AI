# coding: utf-8

import argparse
import os
import pickle
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
    help="Path to the deep ranking model")


args = vars(ap.parse_args())

if not os.path.exists(args['model']):
    print("The model path doesn't exist!")
    exit()

args = vars(ap.parse_args())

import numpy as np
from keras.applications.vgg16 import VGG16
from keras.layers import *
from keras.models import Model
from keras.preprocessing.image import load_img, img_to_array
from skimage import transform
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Embedding
import cv2

def preprocess(queries, db):
    query_img = []
    reference_img = []
    img_size=(224,224)
    for img_path in queries:
        img = cv2.imread(img_path, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, img_size)
        img = np.asarray(img).astype('float64')
        img *= 1. / 255
        img = np.expand_dims(img, axis=0)
        print(img.shape)
        query_img.append(img)

    for img_path in db:
        img = cv2.imread(img_path, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, img_size)
        img = np.asarray(img).astype('float64')
        img *= 1. / 255
        img = np.expand_dims(img, axis=0)
        print(img.shape)
        reference_img.append(img)

    return queries, query_img, db, reference_img

def convnet_model_():
    vgg_model = VGG16(weights=None, include_top=False)
    x = vgg_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(4096, activation='relu')(x)
    x = Dropout(0.6)(x)
    x = Dense(4096, activation='relu')(x)
    x = Dropout(0.6)(x)
    x = Lambda(lambda  x_: K.l2_normalize(x,axis=1))(x)
    convnet_model = Model(inputs=vgg_model.input, outputs=x)
    return convnet_model

def deep_rank_model():
 
    convnet_model = convnet_model_()
    first_input = Input(shape=(224,224,3))
    first_conv = Conv2D(96, kernel_size=(8, 8),strides=(16,16), padding='same')(first_input)
    first_max = MaxPool2D(pool_size=(3,3),strides = (4,4),padding='same')(first_conv)
    first_max = Flatten()(first_max)
    first_max = Lambda(lambda  x: K.l2_normalize(x,axis=1))(first_max)

    second_input = Input(shape=(224,224,3))
    second_conv = Conv2D(96, kernel_size=(8, 8),strides=(32,32), padding='same')(second_input)
    second_max = MaxPool2D(pool_size=(7,7),strides = (2,2),padding='same')(second_conv)
    second_max = Flatten()(second_max)
    second_max = Lambda(lambda  x: K.l2_normalize(x,axis=1))(second_max)

    merge_one = concatenate([first_max, second_max])

    merge_two = concatenate([merge_one, convnet_model.output])
    emb = Dense(4096)(merge_two)
    l2_norm_final = Lambda(lambda  x: K.l2_normalize(x,axis=1))(emb)

    final_model = Model(inputs=[first_input, second_input, convnet_model.input], outputs=l2_norm_final)

    return final_model


model = deep_rank_model()

# for layer in model.layers:
#     print (layer.name, layer.output_shape)

model.load_weights(args['model'])

start_path = os.getcwd()

queries = os.listdir(os.path.join(start_path,'test/query'))
queries = [start_path+'/test/query/'+v for v in queries]
db = os.listdir(os.path.join(start_path,'test/reference'))
db = [start_path+'/test/reference/'+v for v in db]

print(queries,db)

queries, query_img, db, reference_img = preprocess(queries,db)
print('query list len : {0}, query_img len : {1}, reference len : {2} , reference img len : {3}'.format(len(queries),len(query_img),len(db),len(reference_img)))
print(query_img[0].shape)


result={}
for i in range(len(query_img)):
    embedding1 = model.predict([query_img[i], query_img[i], query_img[i]])[0]
    query = queries[i].split('/')[-1].split('.')[0]
    dist_list = []
    refer_list = []
    sorted_refer_list = []
    for j in range(len(reference_img)):
        embedding2 = model.predict([reference_img[j],reference_img[j],reference_img[j]])[0]
        distance = sum([(embedding1[idx] - embedding2[idx])**2 for idx in range(len(embedding1))])**(0.5)
        refer = db[j].split('/')[-1].split('.')[0]
        refer_list.append(refer)
        dist_list.append(distance)
    dummy = zip(refer_list,dist_list)
    sorted_dist_list = sorted(dummy,key=lambda x : x[1], reverse=False)
    for k in range(len(sorted_dist_list)):
        sorted_refer_list.append(sorted_dist_list[k][0])
    result[query]=sorted_refer_list
    print('ranked list length : ', len(sorted_refer_list))
    print('ranked list : ', sorted_refer_list)
print(list(zip(range(len(result)),result.items())))
#print(result.items())





# caching db output, db inference
# db_output = './db_infer.pkl'
# if os.path.exists(db_output):
#     with open(db_output, 'rb') as f:
#         reference_vecs = pickle.load(f)
# else:
#     reference_vecs = get_feature_layer([reference_img, 0])[0]
#     with open(db_output, 'wb') as f:
#         pickle.dump(reference_vecs, f)
#
# retrieval_results = {}
#
# for (i, query) in enumerate(queries):
#     query = query.split('/')[-1].split('.')[0]
#     sim_list = zip(references, sim_matrix[i].tolist())
#     sorted_sim_list = sorted(sim_list, key=lambda x: x[1], reverse=True)
#
#     ranked_list = [k.split('/')[-1].split('.')[0] for (k, v) in sorted_sim_list]  # ranked list
#     print('ranked list length : ', len(ranked_list))
#     print('ranked list : ', ranked_list)
#     retrieval_results[query] = ranked_list
# print('done')
#
# list(zip(range(len(retrieval_results)), retrieval_results.items()))





