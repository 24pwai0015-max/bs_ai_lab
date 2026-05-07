import numpy as np

# Task 1

a = np.array([1,2,3,4,5,6,7,8,9,10])

b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

c = np.zeros((4,4))

d = np.ones((2,5))

print(a)
print(b)
print(c)
print(d)


# Task 2

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.ndim)


# Task 3

arr = np.array([10,20,30,40,50,60])

print(arr[0])
print(arr[-1])
print(arr[2])
print(arr[arr > 30])


# Task 4

arr = np.array([10,20,30,40,50,60])

print(arr[1:5])
print(arr[::-1])
print(arr[::2])

m = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(m[0])
print(m[:,1])
print(m[1:])


# Task 5

arr = np.array([1,2,3,4,5])

print(arr * 5)
print(arr + 10)
print(arr ** 2)


# Task 6

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr + 10)
print(arr * 2)


# Task 7

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A + B)
print(A - B)


# Task 8

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(np.dot(A,B))
print(A.T)


# Task 9

arr = np.random.randint(1,101,(4,4))

print(arr)

d = np.random.rand(4,4)

print(d)

print(arr.max())
print(arr.min())
print(arr.mean())


# Task 10

marks = np.array([78,85,92,45,67,88,34,90,76,59])

print(marks.mean())
print(marks.max())
print(marks.min())
print(np.sum(marks > 80))
print(marks[marks < 50])


# Task 11

img = np.random.randint(0,256,(5,5))

print(img)
print(img.max())
print(img.min())
print(img.shape)


# Task 12

data = np.array([10,20,30,40,50])

norm = (data - data.min()) / (data.max() - data.min())

print(norm)


# Task 13

data = np.array([
    [25,30000,0],
    [30,50000,1],
    [35,60000,1],
    [28,45000,0],
    [40,80000,1]
])

X = data[:,:2]

y = data[:,2]

print(data)
print(X)
print(y)
print(np.mean(data[:,1]))
print(np.max(data[:,0]))
print(data.shape)