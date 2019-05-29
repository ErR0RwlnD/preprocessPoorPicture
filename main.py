from PIL import Image
import numpy as np


def filling(matrix):
    x, y = matrix.shape
    r = matrix.copy()
    for i in range(1, x):
        for j in range(1, y):
            if matrix[i, j] == 0:
                kernel = r[i-1:i+2, j-1:j+2]
                count = sum(sum(kernel != 0))
                if count != 0:
                    matrix[i, j] = sum(sum(kernel))/count
    return matrix


if __name__ == "__main__":
    img = Image.open('data/A.png')
    img = np.array(img)
    img = filling(img)
    Image.fromarray(img, 'L').save('data/A1.png')
    img = filling(img)
    img = Image.fromarray(img, 'L')
    img.save('data/A2.png')
