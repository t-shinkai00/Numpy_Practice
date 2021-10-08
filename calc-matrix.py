import numpy as np

a=np.array([
  [1,3],
  [-2,4],
])
b=np.array([
  [2,-1],
  [3,0]
])

# 和
print(a+b)

# 差
print(a-b)

# 積
print(a@b)

# アダマール積
print(a*b)