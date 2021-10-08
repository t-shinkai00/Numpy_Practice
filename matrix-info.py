import numpy as np

a=np.array([[2,3,4]])
b=np.array([
  [1.2, 3.5, 5.1],
  [-0.3, 1.1, -4.5]
])

# 形状
print(a.shape)
print(b.shape)

# 次元
print(a.ndim)
print(b.ndim)

# データ型
print(a.dtype)
print(b.dtype)

# 要素数
print(a.size)
print(b.size)