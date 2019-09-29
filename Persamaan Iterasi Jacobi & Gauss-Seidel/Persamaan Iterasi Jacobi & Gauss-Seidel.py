# Iterasi Jacobi & Gauss-Seidel
# Tentukan X, Y, Z yang memenuhi sistem persamaan berikut
# X + 2Y - 2Z = 7 .. (1)
# X + 3Y + Z = 4 .. (2)
# 2X + 3Y + 7Z = 6 .. (3)


import numpy as np

# Jacobi
print(" ======================= Persamaan Jacobi ======================= ")
print()
x = np.zeros(30)
y = np.zeros(30)
z = np.zeros(30)
x[0] = 0
y[0] = 0
z[0] = 0

for i in range(29):
    x[i + 1] = 7 - 2 * y[i] + 2 * z[i]
    y[i + 1] = (4 - x[i] - z[i]) / 3
    z[i + 1] = (6 - 2 * x[i] - 3 * y[i]) / 7
    print(i + 1, x[i + 1], y[i + 1], z[i + 1])

print()
print()

# Gauss-Seidel
print(" ======================= Persamaan Gauss-Seidel ======================= ")
print()
for j in range(29):
    x[j + 1] = 7 - 2 * y[j] + 2 * z[j]
    y[j + 1] = (4 - x[j + 1]) - z[j] / 3
    z[j + 1] = (6 - 2) * x[j + 1] - 3 * y[j + 1] / 7
    print(j + 1, x[j + 1], y[j + 1], z[j + 1])
