import numpy as np

v1 = np.array([3, 4])
v2 = np.array([1, 2])

result = v1 + v2
print("addition:", result)

scaled = 5 * v1
print("Scaled by 5:", scaled)

dot = np.dot(v1, v2)
print("dot product:", dot)

magnitude = np.linalg.norm(v1)
print("magnitude of v1:", magnitude)
