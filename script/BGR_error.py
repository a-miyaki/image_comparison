import numpy as np
import cv2 as cv
from PIL import Image

# パスの指定
path = './image_error_map/'

def BGR_error(error_map):
    # 画像読み込み
    img = Image.open(path + 'error_map_diff.png')
    pixelSizeTuple = img.size

    redlist = []
    greenlist = []
    bluelist = []

    # 各ピクセルのRGBをリスト化する
    for i in range(pixelSizeTuple[0]):
        for j in range(pixelSizeTuple[1]):
            r, g, b = img.getpixel((i, j))
            redlist.append(r)
            greenlist.append(g)
            bluelist.append(b)

    r = sum(redlist)
    g = sum(greenlist)
    b = sum(bluelist)
    print('R, G, B')
    print(r)
    print(g)
    print(b)

    return r, g, b

if __name__ == "__BGR_error__":
    BGR_error()
