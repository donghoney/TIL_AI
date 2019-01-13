import numpy as np
import random
hundred = np.arange(20)
print(hundred)
print(hundred[-1])
print(hundred[-2])
random.shuffle(hundred)
for i, name in enumerate(hundred):
    print(i,name)
