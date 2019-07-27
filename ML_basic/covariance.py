import numpy as np

# 평균
def mean(x):
    return sum(x) / len(x)

# 평균과 각 요소의 차이
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

# 내적, 각 요소를 곱한다
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

# 공분산
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / n



p = np.array(([2,1],[1,3],[2,5],[3,3]))
u = np.array(([2,3]))

c = np.array(([2,6]))
b = np.array(([4,3]))

cov1 = covariance(p,p)

print(cov1)

