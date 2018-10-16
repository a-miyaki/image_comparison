import numpy as np
import cv2 as cv
from PIL import Image, ImageDraw, ImageFilter

# 画像を読み込む
image_A = cv.imread('./result/image_gt_00010000.png', 1)
image_B = cv.imread('./result/image_gen_00010000.png', 1)

# 画像のサイズを確認する
print(image_A.shape)
print(image_B.shape)

# 画像を合成する
# alpha = 1, beta = 1, gamma = 0でaddとほぼ同じ？
merge = cv.addWeighted(image_A, 1, image_B, 1, 0)

# 画像を表示する
cv.imshow('frame', merge)

# 画像を保存する
cv.imwrite('./result/merge.png', merge)
cv.waitKey(0)
cv.destroyAllWindows()
