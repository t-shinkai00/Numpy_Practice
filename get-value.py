import numpy as np

# a=np.array([1,3,5,7,9,11])
a=np.arange(1,13,2)
b=np.array([
  [2,4,6],
  [-1,5,-3],
  [0,-2,3],
])

# 指定した範囲の値を取得
print(a[2:-1])
print(b[0])
print(b[2,0])
print(b[1:, 1:])

# 全ての値を逆順に取得
print(a[::-1])
print(b[::-1])