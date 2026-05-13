# task 1:

import numpy as np
data = np.array([
    [85, 90, 78, 88, 1],
    [70, 65, 72, 60, 1],
    [40, 45, 50, 35, 0],
    [95, 92, 96, 94, 1],
    [55, 60, 58, 62, 1],
    [30, 25, 40, 20, 0],
    [80, 82, 78, 85, 1],
    [60, 50, 55, 58, 1]
])
# \n is used fir next line,donot think it is a copy paste
print("Dataset:\n", data)

# task 2

X = data[:, :4]   
y = data[:, 4]    
print("Features (X):\n", X)
print("Labels (y):\n", y)

avg_marks = np.mean(X, axis=0)
max_marks = np.max(X, axis=0)
min_marks = np.min(X, axis=0)

print("Average Marks:", avg_marks)
print("Highest Marks:", max_marks)
print("Lowest Marks:", min_marks)

above_80 = data[np.any(X > 80, axis=1)]
print("Students scoring above 80:\n", above_80)

below_50 = data[np.any(X < 50, axis=1)]
print("Students scoring below 50:\n", below_50)

# task 3

X_min = X.min(axis=0)
X_max = X.max(axis=0)

X_norm = (X - X_min) / (X_max - X_min)

print("Normalized Data:\n", X_norm)

