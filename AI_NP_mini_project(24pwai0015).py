import numpy as np



data = np.array([
    [78, 85, 80, 90, 1],
    [45, 50, 40, 55, 0],
    [88, 92, 85, 91, 1],
    [60, 65, 70, 58, 1],
    [30, 40, 35, 45, 0],
    [95, 98, 92, 96, 1],
    [55, 58, 60, 62, 0],
    [70, 72, 68, 75, 1],
    [48, 52, 46, 50, 0],
    [82, 88, 84, 86, 1]
])


X = data[:, :4]   # marks
y = data[:, 4]    # result

avg_marks = np.mean(X, axis=1)
max_marks = np.max(X, axis=1)
min_marks = np.min(X, axis=1)

print("Average Marks:", avg_marks)
print("Max Marks:", max_marks)
print("Min Marks:", min_marks)


passed = np.sum(y == 1)
failed = np.sum(y == 0)

print("\nPassed Students:", passed)
print("Failed Students:", failed)


above_80 = np.where(avg_marks > 80)[0]
below_50 = np.where(avg_marks < 50)[0]

print("\nAbove 80 Avg Index:", above_80)
print("Below 50 Avg Index:", below_50)


X_norm = (X - np.min(X)) / (np.max(X) - np.min(X))

print("\nNormalized Data:\n", X_norm)


predictions = (avg_marks >= 60).astype(int)

print("\nPredictions:", predictions)


accuracy = np.mean(predictions == y) * 100

print("\nModel Accuracy:", accuracy, "%")