import keras
import numpy as np

path = keras.utils.get_file(
    'nietzsche.txt',
    origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt'
)
text = open(path,encoding="utf-8").read().lower()
print('말뭉치 크기:',len(text))

maxlen = 60
step = 3

sentences = []

next_chars= []

for i in range(0, len(text)-maxlen, step):
    sentences.append(text[i:i+maxlen])
    next_chars.append(text[i+maxlen])
print('시퀀스 갯수:',len(sentences))

chars = sorted(list(set(text)))
print('고유한 글자:',len(chars))
char_indices = dict((char, chars.index(char)) for char in chars)

print('벡터화...')
x = np.zeros((len(sentences), maxlen, len(chars)),dtype=np.bool)
y = np.zeros((len(sentences),len(chars)),dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        #print(i,t,char_indices[char])
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

from keras import layers

model = keras.models.Sequential()
model.add(layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(layers.Dense(len(chars), activation='softmax'))
optimizer= keras.optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy',optimizer=optimizer)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds)
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

import random
import sys

random.seed(42)
start_index = random.randint(0, len(text) - maxlen - 1)