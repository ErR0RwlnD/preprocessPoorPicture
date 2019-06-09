from PIL import Image
import numpy as np


def filling(matrix):
    x, y = matrix.shape
    r = matrix.copy()
    for i in range(1, x-1):
        for j in range(1, y-1):
            if matrix[i, j] == 0:
                kernel = r[i-1:i+2, j-1:j+2]
                count = sum(sum(kernel != 0))
                if count != 0:
                    matrix[i, j] = sum(sum(kernel))/count

    for i in range(1, x-1):
        if matrix[i, 0] == 0:
            kernel = r[i-1:i+2, 0:2]
            count = sum(sum(kernel != 0))
            if count != 0:
                matrix[i, 0] = sum(sum(kernel))/count

        if matrix[i, y-1] == 0:
            kernel = r[i-1:i+2, y-2:y]
            count = sum(sum(kernel != 0))
            if count != 0:
                matrix[i, y-1] = sum(sum(kernel))/count

    for j in range(1, y-1):
        if matrix[0, j] == 0:
            kernel = r[0:2, j-1:j+2]
            count = sum(sum(kernel != 0))
            if count != 0:
                matrix[0, j] = sum(sum(kernel))/count

        if matrix[x-1, j] == 0:
            kernel = r[x-2:x, j-1:j+2]
            count = sum(sum(kernel != 0))
            if count != 0:
                matrix[x-1, j] = sum(sum(kernel))/count

    if matrix[0, 0] == 0:
        kernel = matrix[0:2, 0:2]
        count = sum(sum(kernel != 0))
        if count != 0:
            matrix[0, 0] = sum(sum(kernel))/count

    if matrix[0, y-1] == 0:
        kernel = matrix[0:2, y-2:y]
        count = sum(sum(kernel != 0))
        if count != 0:
            matrix[0, y-1] = sum(sum(kernel))/count

    if matrix[x-1, 0] == 0:
        kernel = matrix[x-2:x, 0:2]
        count = sum(sum(kernel != 0))
        if count != 0:
            matrix[x-1, 0] = sum(sum(kernel))/count

    if matrix[x-1, j-1] == 0:
        kernel = matrix[x-2:x, j-2:j]
        count = sum(sum(kernel != 0))
        if count != 0:
            matrix[x-1, j-1] = sum(sum(kernel))/count
    return matrix


if __name__ == "__main__":
    img = Image.open('data/A.png')
    img = np.array(img)
    img = filling(img)
    Image.fromarray(img, 'L').save('data/A1.png')
    img = filling(img)
    Image.fromarray(img, 'L').save('data/A2.png')
    img = filling(img)
    Image.fromarray(img, 'L').save('data/A3.png')
    img = filling(img)
    Image.fromarray(img, 'L').save('data/A4.png')
