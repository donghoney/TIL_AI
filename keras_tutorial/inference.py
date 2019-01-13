import numpy as np
from keras.models import Model
from keras.datasets import mnist
from keras.models import load_model
from sklearn.metrics import label_ranking_average_precision_score
import os
cur_path = str(os.path.dirname(os.path.abspath(__file__)))
print('current path :',cur_path)
(x_train, y_train),(x_test,y_test) = mnist.load_data()

autoencoder = load_model('autoencoder.h5')

encoder = Model(inputs =autoencoder.input, outputs = autoencoder.get_layer('encoder').output)

scores = []

n_test_samples = 1000

n_train_samples = [10, 50, 100, 200, 300, 400, 500, 750, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
                   20000, 30000, 40000, 50000, 60000]


def compute_average_precision_score(test_codes, test_labels, learned_codes, y_train, n_samples):
    # For each n_samples (=number of retrieved images to assess) we store the corresponding labels and distances
    out_labels = []
    out_distances = []

    # For each query image feature we compute the closest images from training dataset
    for i in range(len(test_codes)):
        print('{}번째, 거리 계산'.format(i+1))
        distances = []
        # Compute the euclidian distance for each feature from training dataset
        for code in learned_codes:
            distance = np.linalg.norm(code - test_codes[i])
            distances.append(distance)

        # Store the computed distances and corresponding labels from training dataset
        distances = np.array(distances)

        # Scoring function needs to replace similar labels by 1 and different ones by 0
        labels = np.copy(y_train).astype('float32')
        labels[labels != test_labels[i]] = -1
        labels[labels == test_labels[i]] = 1
        labels[labels == -1] = 0
        distance_with_labels = np.stack((distances, labels), axis=-1)
        sorted_distance_with_labels = distance_with_labels[distance_with_labels[:, 0].argsort()]

        # The distances are between 0 and 28. The lesser the distance the bigger the relevance score should be
        sorted_distances = 28 - sorted_distance_with_labels[:, 0]
        sorted_labels = sorted_distance_with_labels[:, 1]

        # We keep only n_samples closest elements from the images retrieved
        out_distances.append(sorted_distances[:n_samples])
        out_labels.append(sorted_labels[:n_samples])

    out_labels = np.array(out_labels)
    out_labels_file_name = '{}/computed_data/out_labels_{}'.format(cur_path,n_samples)
    np.save(out_labels_file_name, out_labels)

    out_distances_file_name = '{}/computed_data/out_distances_{}'.format(cur_path,n_samples)
    out_distances = np.array(out_distances)
    np.save(out_distances_file_name, out_distances)

    # Score the model based on n_samples first images retrieved
    score = label_ranking_average_precision_score(out_labels, out_distances)
    scores.append(score)
    return score

def test_model(n_test_samples, n_train_samples):
    print(x_train.shape)
    learned_codes = encoder.predict(x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1))
    learned_codes = learned_codes.reshape(learned_codes.shape[0],
                                          learned_codes.shape[1] * learned_codes.shape[2] * learned_codes.shape[3])
    print(learned_codes.shape)
    # Compute features for query images
    test_codes = encoder.predict(x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1))
    test_codes = test_codes.reshape(test_codes.shape[0],
                                    test_codes.shape[1] * test_codes.shape[2] * test_codes.shape[3])
    print(test_codes.shape)
    indexes = np.arange(len(y_test))
    np.random.shuffle(indexes)
    indexes = indexes[:n_test_samples]
    print(indexes)
    score = compute_average_precision_score(test_codes[indexes], y_test[indexes], learned_codes, y_train,
                                            n_train_samples)
    print(score)

for n_train_sample in n_train_samples:
    test_model(n_test_samples,n_train_sample)

np.save('{}/computed_data/scores'.format(cur_path),np.array(scores))