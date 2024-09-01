import numpy as np
import matplotlib.pyplot as plt
def bi_interpolation(arr, x, y):
    height, width = arr.shape
    x1 = int(x)
    y1 = int(y)
    x2 = x1 + 1
    y2 = y1 + 1
    if x2 >= width:
        x2 = x1
    if y2 >= height:
        y2 = y1
 
    p11 = arr[y1, x1]
    p12 = arr[y2, x1]
    p21 = arr[y1, x2]
    p22 = arr[y2, x2]
 
    x_diff = x - x1
    y_diff = y - y1
 
    interpolated = (p11 * (1 - x_diff) * (1 - y_diff) +
                          p21 * x_diff * (1 - y_diff) +
                          p12 * (1 - x_diff) * y_diff +
                          p22 * x_diff * y_diff)
 
    return interpolated
 
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
x = 1.5
y = 1.5
interpolated = bi_interpolation(arr, x, y)
print("Interpolated value at ({x}, {y}): {interpolated_value}")
xx, yy = np.meshgrid(range(arr.shape[1]), range(arr.shape[0]))
plt.plot(xx, yy, 'ko')
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        plt.text(j, i, f'{arr[i, j]}', ha='center', va='center')
plt.plot(x, y, 'ro')
plt.text(x, y, f'interpolado: {interpolated:.2f}', ha='left', va='bottom')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bilinear Interpolation')
plt.show()