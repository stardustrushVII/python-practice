import numpy as np

v = np.array([2, 3])

scaling_matrix = np.array([
[2, 0], 
[0, 2],
])

result = scaling_matrix @ v
print("Scaled Vector:", result)

rotation_matrix = np.array([
[0, 1],
[1, 0]
])

v = np.array([2, 0])
rotated = rotation_matrix @ v
print("Rotated vector:", rotated)