import os
import numpy as np
from PIL import Image


def singleChannel(ip, ref, verbose=False):
    reffer = Image.open(ref)
    reffer = np.array(reffer)
    img = Image.open(ip)
    img = np.array(img)[1:-1, 1:-1]
    ns = 0
    x, y = reffer.shape
    assert((x, y) == reffer.shape)
    for i in range(x):
        for j in range(y):
            if img[i, j] != reffer[i, j] and reffer[i, j] != 0:
                ns += abs(img[i, j]-reffer[i, j])

    return ns


def multiChannel(ip, ref, verbose=False):
    reffer = Image.open(ref)
    reffer = np.array(reffer)
    img = Image.open(ip)
    img = np.array(img)[1:-1, 1:-1, :]
    ns = 0
    x, y, ch = reffer.shape
    for c in range(ch):
        for i in range(x):
            for j in range(y):
                if img[i, j, c] != reffer[i, j, c] and reffer[i, j, c] != 0:
                    ns += 1

    if verbose:
        print(str(ref)+' : '+str(ns))
    return ns


# x = singleChannel('data/A_out01.png', 'data/A.png')
# print(x)
# y1 = multiChannel('data/C_out005.png', 'data/C.png')
# print(y1)
# y2 = multiChannel('data/C_out001.png', 'data/C.png')
# print(y2)

def singleChannelHW(ip, ref):
    reffer = Image.open(ref)
    reffer = np.array(reffer)
    img = Image.open(ip)
    img = np.array(img)[1:-1, 1:-1]
    x, y = reffer.shape
    assert((x, y) == reffer.shape)
    for i in range(x):
        for j in range(y):
            if img[i, j] != reffer[i, j] and reffer[i, j] != 0:
                img[i, j] = reffer[i, j]
    Image.fromarray(img, 'L').save('data/ahw.png')


def multiChannelHWB(ip, ref):
    reffer = Image.open(ref)
    reffer = np.array(reffer)
    img = Image.open(ip)
    img = np.array(img)[1:-1, 1:-1, :]
    ns = 0
    x, y, ch = reffer.shape
    for c in range(ch):
        for i in range(x):
            for j in range(y):
                if img[i, j, c] != reffer[i, j, c] and reffer[i, j, c] != 0:
                    img[i, j, c] = reffer[i, j, c]
    Image.fromarray(img, 'RGB').save('data/bhw.png')


def multiChannelHWC(ip, ref):
    reffer = Image.open(ref)
    reffer = np.array(reffer)
    img = Image.open(ip)
    img = np.array(img)[1:-1, 1:-1, :]
    ns = 0
    x, y, ch = reffer.shape
    for c in range(ch):
        for i in range(x):
            for j in range(y):
                if img[i, j, c] != reffer[i, j, c] and reffer[i, j, c] != 0:
                    img[i, j, c] = reffer[i, j, c]
    Image.fromarray(img, 'RGB').save('data/chw.png')


multiChannelHWB('data/B_out005.png', 'data/B.png')
multiChannelHWC('data/C_out005.png', 'data/C.png')
