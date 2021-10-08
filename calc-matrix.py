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

# 転置
print(a.T)
print(b.T)

# 行列式
print(np.linalg.det(a))
print(np.linalg.det(b))

# 逆行列
print(np.linalg.inv(a))
print(np.linalg.inv(b))

# 行列×スカラー
print(a*3)
print(b*2)