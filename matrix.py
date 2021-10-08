import numpy as np

# 1×4行列
A=np.array([1,2,3,4])
print(A)

# 3×1行列
B=np.array([[4],[-1],[6]])
print(B)

# 3×4行列
C=np.array([
  [3,-2,0,1],
  [7,1,-1,2],
  [4,-5,1,3]])
print(C)

# 1×2零行列
D=np.zeros((1,2))
print(D)

# 4×1の要素が全て1の行列
E=np.ones((4,1))
print(E)

# 単位行列
F=np.eye(3)
print(F)

# 対角行列(?)
G=np.eye(3,4)
print(G)