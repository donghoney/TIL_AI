# # tensorflow라는 라이브러리를 tf 라는 이름으로 사용하기 위해 아래와 같이 import
# import tensorflow as tf
#
# # 1 이라는 원소를 가진 텐서를 만들어 a에 대입하여라
# # 텐서는 다차원 배열과 같다.
# a = tf.constant(1)
#
# # 2 라는 원소를 가진 텐서를 만들어 b에 대입하여라
# b = tf.constant(2)
#
# # a와 b를 더하여 c라는 텐서에 대입하여라
# c = tf.add(a,b)
#
# '''
# =================================
# [중요]
# 텐서플로우 연산은 세션을 통해 "연산을 수행"시켜야 결과를 볼 수 있습니다!!!!
# =================================
# '''
# # 먼저 세션을 열고
# sess = tf.Session()
#
# # 세션을 수행합니다.
# print(sess.run(c))

#
# import tensorflow as tf
#
# # 5 라는 값의 텐서 변수를 a 에 담고
# a = tf.Variable(5)
#
# # 3 라는 값의 텐서 변수를 b 에 담고
# b = tf.Variable(3)
#
# # 텐서 a와 텐서 b의 곱을 c에 담는 연산자를 설정하고
# c = tf.multiply(a,b)
#
# # ===============
# # [중요]상수와 변수의 차이!!변수는 이부분이 핵심!!
# # ===============
# init = tf.global_variables_initializer()
#
# sess = tf.Session()
# sess.run(init)
# v = sess.run(c)
# print(v)
#
#
#
# # 변수 a 는 변경하능하다. 15로 변경해보자.
# a = tf.Variable(15)
#
# # 변수값이 변경되었으면, C도 다시 초기화 해줘야 한다.
# c = tf.multiply(a,b)
#
# # 변수값이 바뀌었으니, init도 초기화해줘야 한다.
# init = tf.global_variables_initializer()
#
# sess.run(init)
# v = sess.run(c)
# print(v)

# 플레이스홀더 예제 1
import tensorflow as tf

input = [1, 2, 3, 4, 5]
x = tf.placeholder(dtype=tf.float32)
k = tf.placeholder(dtype=tf.float32)
y = x + 5
z = y + 5 + k

sess = tf.Session()
print(sess.run(tf.shape(z),feed_dict={x: input,k:input}))

#
# # 플레이스홀더 예제2
# import tensorflow as tf
#
# mathScore = [85, 99, 84, 97, 92]
# englishScore = [59, 80, 84, 68, 77]
#
# a = tf.placeholder(dtype=tf.float32)
# b = tf.placeholder(dtype=tf.float32)
# y = (a+b)/2
#
# sess = tf.Session()
# print(sess.run(y,feed_dict={a: mathScore, b: englishScore}))

# import tensorflow as tf
#
# #
# a = tf.constant(17)
# b = tf.constant(5)
#
# '''
# 주요 함수 사용하기
# '''
# sess = tf.Session()
# c = tf.add(a,b)
# v1 = sess.run(c)
#
# c = tf.subtract(a,b)
# v2 = sess.run(c)
#
# c = tf.multiply(a,b)
# v3 = sess.run(c)
#
# c = tf.truediv(a,b)
# v4 = sess.run(c)
#
# c = tf.mod(a,b)
# v5 = sess.run(c)
#
# c = -a
# v6 = sess.run(c)
#
# print(v1, v2, v3, v4, v5, v6)
#
# import tensorflow as tf
#
#
# a = tf.constant(17.5)
# b = tf.constant(5.0)
#
# c = tf.negative(a)
# v1 = sess.run(c)
#
# c = tf.sign(a)
# v2 = sess.run(c)
#
#
# c = tf.square(a)
# v3 = sess.run(c)
#
# c = tf.pow(a,2)
# v4 = sess.run(c)
#
#
# c = tf.maximum(a,b)
# v5 = sess.run(c)
#
# c = tf.minimum(a,b)
# v6 = sess.run(c)
#
# c = tf.exp(b)
# v7 = sess.run(c)
#
# c = tf.log(b)
# v8 = sess.run(c)
#
# c = tf.sin(b)
# v9 = sess.run(c)
#
# c = tf.cos(b)
# v10 = sess.run(c)
#
# print(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
#
# import tensorflow as tf
#
# a = tf.constant(17.5)
# b = tf.constant(5.0)
# c = tf.add(a,b)
#
# # 값이 아니라, 텐서를 출력했다.
# print(c)
#
# # 즉, 위와 같은 명령어는 실제로 연산을 수행한 것이 아니라
# # 그래프를 정의한 것이다.
# # 연산을 수행하기 위해서는,
# # a와 b에 데이터를 넣어서 흐름(flow)가 이루어지도록 만들어야 합니다.
#
# # 이렇게! 흐름을 실행해야 한다.
#
# sess = tf.Session()
# sess.run(c)
#
# # 즉, 세션은 실제로 값을 대입한 그래프가 동작하도록 하는 역할을 수행하는 것이다.!!!!
#
#
# 랜덤 변수 생성 테스트
# import tensorflow as tf
#
# #
# tf.set_random_seed(777)
#
# # X and Y 설정
# x_train = [1, 2, 3]
# y_train = [1, 2, 3]
#
# # 텐서 크기 1짜리 랜덤 값을 텐서변수 W에 대입하고, 이름을 weight라고 지정
# W = tf.Variable(tf.random_normal([3,2,4]), name="weight")
#
# # 텐서 크기 1짜리 랜덤 값을 텐서변수 b에 대입하고, 이름을 bias라고 지정
# b = tf.Variable(tf.random_normal([1]), name="bias")
#
#
# # 세션열고, 실행하여
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# print(sess.run(W))

import tensorflow as tf
#
# import tensorflow as tf
#
# tf.set_random_seed(777)  # for reproducibility
#
# x1_data = [73., 93., 89., 96., 73.]
# x2_data = [80., 88., 91., 98., 66.]
# x3_data = [75., 93., 90., 100., 70.]
#
# y_data = [152., 185., 180., 196., 142.]
#
# # placeholders for a tensor that will be always fed.
# x1 = tf.placeholder(tf.float32)
# x2 = tf.placeholder(tf.float32)
# x3 = tf.placeholder(tf.float32)
#
# Y = tf.placeholder(tf.float32)
#
# w1 = tf.Variable(tf.random_normal([1]), name='weight1')
# w2 = tf.Variable(tf.random_normal([1]), name='weight2')
# w3 = tf.Variable(tf.random_normal([1]), name='weight3')
# b = tf.Variable(tf.random_normal([1]), name='bias')
#
#
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# print(sess.run([w1,w2,w3,b]))
#
# for i in range(101):
#     print(sess.run([w1,w2,w3,b]))

# import tensorflow as tf
#
# #
# tf.set_random_seed(777)
#
# # X and Y 설정
# x_train = [1, 2, 3]
# y_train = [1, 2, 3]
#
# # 텐서 크기 1짜리 랜덤 값을 텐서변수 W에 대입하고, 이름을 weight라고 지정
# W = tf.Variable(tf.random_normal([2]), name="weight")
#
# # 텐서 크기 1짜리 랜덤 값을 텐서변수 b에 대입하고, 이름을 bias라고 지정
# b = tf.Variable(tf.random_normal([1]), name="bias")
#
#
# # 가설 설정 그래프 생성
# hypothesis = x_train * W + b
#
# # 로스 함수/비용 함수 그래프 생성
# # 선형 회귀 함수 방정식에 맞게 비용 함수 아래와 같이 작성
# cost = tf.reduce_mean(tf.square(hypothesis - y_train))
#
# # 최소값을 찾기 위해 아래와 같이 "경사하강최적화방법"을 설정
# train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
#
# # 세션열고, 실행하여
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# print(sess.run(W))
# for step in range(10001):
#   _, cost_val, W_val, b_val = sess.run([train, cost, W, b])
#
#   if step % 1000 == 0:
#       print(step, cost_val, W_val, b_val)
#
# import tensorflow as tf
#
# tf.set_random_seed(777)  # for reproducibility
#
# # X and Y data
# x_train = [1, 2, 3]
# y_train = [1, 2, 3]
#
# # Try to find values for W and b to compute y_data = x_data * W + b
# # We know that W should be 1 and b should be 0
# # But let TensorFlow figure it out
#
# W = tf.Variable(tf.random_normal([1]), name="weight")
# b = tf.Variable(tf.random_normal([1]), name="bias")
#
# init_op = tf.global_variables_initializer()
#
# '''
# sess = tf.Session()
# sess.run(init_op)
# v1, v2 = sess.run([W,b])
# print(v1,v2)
# '''
#
# # '''
# with tf.Session() as sess:
#     sess.run(init_op)
#     v1, v2 = sess.run([W, b])
#
# print(v1, v2)
#
# sess.close()
# # '''
#
#
# #==========================================
# # https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-03-1-minimizing_cost_show_graph.py
# #==========================================
# # Lab 3 Minimizing Cost
# import tensorflow as tf
# import matplotlib.pyplot as plt
#
# X = [1, 2, 3]
# Y = [1, 2, 3]
#
# W = tf.placeholder(tf.float32)
#
# # Our hypothesis for linear model X * W
# hypothesis = X * W
#
# # cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Variables for plotting cost function
# W_history = []
# cost_history = []
#
# # Launch the graph in a session.
# with tf.Session() as sess:
#     for i in range(-30, 50):
#         curr_W = i * 0.1
#         curr_cost = sess.run(cost, feed_dict={W: curr_W})
#
#         W_history.append(curr_W)
#         cost_history.append(curr_cost)
#
# # Show the cost function
# plt.plot(W_history, cost_history)
# plt.show()
#
#
# # https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-03-2-minimizing_cost_gradient_update.py
#
# # Lab 3 Minimizing Cost
# import tensorflow as tf
#
# tf.set_random_seed(777)  # for reproducibility
#
# x_data = [1, 2, 3]
# y_data = [1, 2, 3]
#
# # Try to find values for W and b to compute y_data = W * x_data
# # We know that W should be 1
# # But let's use TensorFlow to figure it out
# W = tf.Variable(tf.random_normal([1]), name="weight")
#
# X = tf.placeholder(tf.float32)
# Y = tf.placeholder(tf.float32)
#
# # Our hypothesis for linear model X * W
# hypothesis = X * W
#
# # cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Minimize: Gradient Descent using derivative: W -= learning_rate * derivative
# learning_rate = 0.1
# gradient = tf.reduce_mean((W * X - Y) * X)
# descent = W - learning_rate * gradient
# update = W.assign(descent)
#
#
# # https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-03-X-minimizing_cost_tf_gradient.py
# # Lab 3 Minimizing Cost
# # This is optional
# import tensorflow as tf
#
# # tf Graph Input
# X = [1, 2, 3]
# Y = [1, 2, 3]
#
# # Set wrong model weights
# W = tf.Variable(5.)
#
# # Linear model
# hypothesis = X * W
#
# # Manual gradient
# gradient = tf.reduce_mean((W * X - Y) * X) * 2
#
# # cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Minimize: Gradient Descent Optimizer
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
#
# # Get gradients
# gvs = optimizer.compute_gradients(cost)
#
# # Optional: modify gradient if necessary
# # gvs = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gvs]
#
# # Apply gradients
# apply_gradients = optimizer.apply_gradients(gvs)
#
# # Launch the graph in a session.
# with tf.Session() as sess:
#     # Initializes global variables in the graph.
#     sess.run(tf.global_variables_initializer())
#
#     for step in range(101):
#         gradient_val, gvs_val, _ = sess.run([gradient, gvs, apply_gradients])
#         print(step, gradient_val, gvs_val)
#
# '''
# 0 37.333332 [(37.333336, 5.0)]
# 1 33.84889 [(33.84889, 4.6266665)]
# 2 30.689657 [(30.689657, 4.2881775)]
# 3 27.825289 [(27.825289, 3.981281)]
# ...
# 97 0.0027837753 [(0.0027837753, 1.0002983)]
# 98 0.0025234222 [(0.0025234222, 1.0002704)]
# 99 0.0022875469 [(0.0022875469, 1.0002451)]
# 100 0.0020739238 [(0.0020739238, 1.0002222)]
# '''
#
# # Launch the graph in a session.
# with tf.Session() as sess:
#     # Initializes global variables in the graph.
#     sess.run(tf.global_variables_initializer())
#
#     for step in range(21):
#         _, cost_val, W_val = sess.run(
#             [update, cost, W], feed_dict={X: x_data, Y: y_data}
#         )
#         print(step, cost_val, W_val)
#
# """
# 0 1.93919 [ 1.64462376]
# 1 0.551591 [ 1.34379935]
# 2 0.156897 [ 1.18335962]
# 3 0.0446285 [ 1.09779179]
# 4 0.0126943 [ 1.05215561]
# 5 0.00361082 [ 1.0278163]
# 6 0.00102708 [ 1.01483536]
# 7 0.000292144 [ 1.00791216]
# 8 8.30968e-05 [ 1.00421977]
# 9 2.36361e-05 [ 1.00225055]
# 10 6.72385e-06 [ 1.00120032]
# 11 1.91239e-06 [ 1.00064015]
# 12 5.43968e-07 [ 1.00034142]
# 13 1.54591e-07 [ 1.00018203]
# 14 4.39416e-08 [ 1.00009704]
# 15 1.24913e-08 [ 1.00005174]
# 16 3.5322e-09 [ 1.00002754]
# 17 9.99824e-10 [ 1.00001466]
# 18 2.88878e-10 [ 1.00000787]
# 19 8.02487e-11 [ 1.00000417]
# 20 2.34053e-11 [ 1.00000226]
# """
#
#
#
# # https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-04-1-multi_variable_linear_regression.py
# # Lab 4 Multi-variable linear regression
# import tensorflow as tf
# tf.set_random_seed(777)  # for reproducibility
#
# x1_data = [73., 93., 89., 96., 73.]
# x2_data = [80., 88., 91., 98., 66.]
# x3_data = [75., 93., 90., 100., 70.]
#
# y_data = [152., 185., 180., 196., 142.]
#
# # placeholders for a tensor that will be always fed.
# x1 = tf.placeholder(tf.float32)
# x2 = tf.placeholder(tf.float32)
# x3 = tf.placeholder(tf.float32)
#
# Y = tf.placeholder(tf.float32)
#
# w1 = tf.Variable(tf.random_normal([1]), name='weight1')
# w2 = tf.Variable(tf.random_normal([1]), name='weight2')
# w3 = tf.Variable(tf.random_normal([1]), name='weight3')
# b = tf.Variable(tf.random_normal([1]), name='bias')
#
# hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
#
# # cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Minimize. Need a very small learning rate for this data set
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
# train = optimizer.minimize(cost)
#
# # Launch the graph in a session.
# sess = tf.Session()
# # Initializes global variables in the graph.
# sess.run(tf.global_variables_initializer())
#
# for step in range(2001):
#     cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
#                                    feed_dict={x1: x1_data, x2: x2_data, x3: x3_data, Y: y_data})
#     if step % 10 == 0:
#         print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
#
# '''
# 0 Cost:  19614.8
# Prediction:
#  [ 21.69748688  39.10213089  31.82624626  35.14236832  32.55316544]
# 10 Cost:  14.0682
# Prediction:
#  [ 145.56100464  187.94958496  178.50236511  194.86721802  146.08096313]
#  ...
# 1990 Cost:  4.9197
# Prediction:
#  [ 148.15084839  186.88632202  179.6293335   195.81796265  144.46044922]
# 2000 Cost:  4.89449
# Prediction:
#  [ 148.15931702  186.8805542   179.63194275  195.81971741  144.45298767]
# '''
#
#
# # https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-04-2-multi_variable_matmul_linear_regression.py
# # Lab 4 Multi-variable linear regression
# import tensorflow as tf
# tf.set_random_seed(777)  # for reproducibility
#
# x_data = [[73., 80., 75.],
#           [93., 88., 93.],
#           [89., 91., 90.],
#           [96., 98., 100.],
#           [73., 66., 70.]]
# y_data = [[152.],
#           [185.],
#           [180.],
#           [196.],
#           [142.]]
#
#
# # placeholders for a tensor that will be always fed.
# X = tf.placeholder(tf.float32, shape=[None, 3])
# Y = tf.placeholder(tf.float32, shape=[None, 1])
#
# W = tf.Variable(tf.random_normal([3, 1]), name='weight')
# b = tf.Variable(tf.random_normal([1]), name='bias')
#
# # Hypothesis
# hypothesis = tf.matmul(X, W) + b
#
# # Simplified cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Minimize
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
# train = optimizer.minimize(cost)
#
# # Launch the graph in a session.
# sess = tf.Session()
# # Initializes global variables in the graph.
# sess.run(tf.global_variables_initializer())
#
# for step in range(2001):
#     cost_val, hy_val, _ = sess.run(
#         [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
#     if step % 10 == 0:
#         print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
#
# '''
# 0 Cost:  7105.46
# Prediction:
#  [[ 80.82241058]
#  [ 92.26364136]
#  [ 93.70250702]
#  [ 98.09217834]
#  [ 72.51759338]]
# 10 Cost:  5.89726
# Prediction:
#  [[ 155.35159302]
#  [ 181.85691833]
#  [ 181.97254944]
#  [ 194.21760559]
#  [ 140.85707092]]
# ...
# 1990 Cost:  3.18588
# Prediction:
#  [[ 154.36352539]
#  [ 182.94833374]
#  [ 181.85189819]
#  [ 194.35585022]
#  [ 142.03240967]]
# 2000 Cost:  3.1781
# Prediction:
#  [[ 154.35881042]
#  [ 182.95147705]
#  [ 181.85035706]
#  [ 194.35533142]
#  [ 142.036026  ]]
# '''
#
# #
#
# # Lab 4 Multi-variable linear regression
#
# import tensorflow as tf
# import numpy as np
# tf.set_random_seed(777)  # for reproducibility
#
# xy = np.loadtxt('data-01-test-score.csv', delimiter=',', dtype=np.float32)
# x_data = xy[:, 0:-1]
# y_data = xy[:, [-1]]
#
# # Make sure the shape and data are OK
# print(x_data, "\nx_data shape:", x_data.shape)
# print(y_data, "\ny_data shape:", y_data.shape)
#
# # data output
# '''
# [[ 73.  80.  75.]
#  [ 93.  88.  93.]
#  ...
#  [ 76.  83.  71.]
#  [ 96.  93.  95.]]
# x_data shape: (25, 3)
# [[152.]
#  [185.]
#  ...
#  [149.]
#  [192.]]
# y_data shape: (25, 1)
# '''
#
# # placeholders for a tensor that will be always fed.
# X = tf.placeholder(tf.float32, shape=[None, 3])
# Y = tf.placeholder(tf.float32, shape=[None, 1])
#
# W = tf.Variable(tf.random_normal([3, 1]), name='weight')
# b = tf.Variable(tf.random_normal([1]), name='bias')
#
# # Hypothesis
# hypothesis = tf.matmul(X, W) + b
#
# # Simplified cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Minimize
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
# train = optimizer.minimize(cost)
#
# # Launch the graph in a session.
# sess = tf.Session()
# # Initializes global variables in the graph.
# sess.run(tf.global_variables_initializer())
#
# for step in range(2001):
#     cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
#                                    feed_dict={X: x_data, Y: y_data})
#     if step % 10 == 0:
#         print(step, "Cost:", cost_val, "\nPrediction:\n", hy_val)
#
# # train output
# '''
# 0 Cost: 21027.0
# Prediction:
#  [[22.048063 ]
#  [21.619772 ]
#  ...
#  [31.36112  ]
#  [24.986364 ]]
# 10 Cost: 95.976326
# Prediction:
#  [[157.11063 ]
#  [183.99283 ]
#  ...
#  [167.48862 ]
#  [193.25117 ]]
#  1990 Cost: 24.863274
# Prediction:
#  [[154.4393  ]
#  [185.5584  ]
#  ...
#  [158.27443 ]
#  [192.79778 ]]
# 2000 Cost: 24.722485
# Prediction:
#  [[154.42894 ]
#  [185.5586  ]
#  ...
#  [158.24257 ]
#  [192.79166 ]]
# '''
#
# # Ask my score
# print("Your score will be ", sess.run(hypothesis,
#                                       feed_dict={X: [[100, 70, 101]]}))
#
# print("Other scores will be ", sess.run(hypothesis,
#                                         feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))
#
# '''
# Your score will be  [[ 181.73277283]]
# Other scores will be  [[ 145.86265564]
#  [ 187.23129272]]
# '''
#
#
# # https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-04-4-tf_reader_linear_regression.py
#
# # Lab 4 Multi-variable linear regression
# # https://www.tensorflow.org/programmers_guide/reading_data
#
# import tensorflow as tf
# tf.set_random_seed(777)  # for reproducibility
#
# filename_queue = tf.train.string_input_producer(
#     ['data-01-test-score.csv'], shuffle=False, name='filename_queue')
#
# reader = tf.TextLineReader()
# key, value = reader.read(filename_queue)
#
# # Default values, in case of empty columns. Also specifies the type of the
# # decoded result.
# record_defaults = [[0.], [0.], [0.], [0.]]
# xy = tf.decode_csv(value, record_defaults=record_defaults)
#
# # collect batches of csv in
# train_x_batch, train_y_batch = \
#     tf.train.batch([xy[0:-1], xy[-1:]], batch_size=10)
#
# # placeholders for a tensor that will be always fed.
# X = tf.placeholder(tf.float32, shape=[None, 3])
# Y = tf.placeholder(tf.float32, shape=[None, 1])
#
# W = tf.Variable(tf.random_normal([3, 1]), name='weight')
# b = tf.Variable(tf.random_normal([1]), name='bias')
#
# # Hypothesis
# hypothesis = tf.matmul(X, W) + b
#
# # Simplified cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))
#
# # Minimize
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
# train = optimizer.minimize(cost)
#
# # Launch the graph in a session.
# sess = tf.Session()
# # Initializes global variables in the graph.
# sess.run(tf.global_variables_initializer())
#
# # Start populating the filename queue.
# coord = tf.train.Coordinator()
# threads = tf.train.start_queue_runners(sess=sess, coord=coord)
#
# for step in range(2001):
#     x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
#     cost_val, hy_val, _ = sess.run(
#         [cost, hypothesis, train], feed_dict={X: x_batch, Y: y_batch})
#     if step % 10 == 0:
#         print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
#
# coord.request_stop()
# coord.join(threads)
#
# # Ask my score
# print("Your score will be ",
#       sess.run(hypothesis, feed_dict={X: [[100, 70, 101]]}))
#
# print("Other scores will be ",
#       sess.run(hypothesis, feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))
#
# '''
# Your score will be  [[185.33531]]
# Other scores will be  [[178.36246]
#  [177.03687]]
# '''
