import numpy as np
import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt

# 画像読み込み
img = cv.imread('./result/error_map_diff.png', 1)

# 画像を表示
cv.imshow('frame', img)
cv.waitKey(0)
cv.destroyAllWindows()

# RGB値の平均値を求める
average_color_per_row = np.average(img, axis=0)

average_color = np.average(average_color_per_row, axis=0)

average_color = np.uint8(average_color)
print("BGRの平均値")
print(average_color)

# numpyの配列をリスト化する
list = average_color.tolist()

error_of_image = (list[0] + list[1] + list[2]) / 256 * 100
print("エラー率(%)")
print(error_of_image)
