from keras.datasets import boston_housing

(train_data, train_targets),(test_data, test_targets) = boston_housing.load_data()

#print(train_data.shape)
#print(test_data.shape)

#print(train_targets)

train_data_copy = train_data.copy()

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std
print(mean)
print(std)

mean = train_data_copy.mean(axis=0)
std = train_data_copy.std(axis=0)
train_data_copy -= mean
train_data_copy /= std

print(mean)
print(std)

test_data -= mean
test_data -= std