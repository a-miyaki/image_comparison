import numpy as np
import cv2 as cv
from PIL import Image, ImageDraw, ImageFilter

# 画像を読み込む
image_A = cv.imread('./result/image_gt_00010000.png', 1)
image_B = cv.imread('./result/image_gen_00010000.png', 1)

# 画像のサイズを確認する
print(image_A.shape)
print(image_B.shape)

# エラーマップ作製
error_map = cv.absdiff(image_A, image_B, dst=None)

# 画像の表示
cv.imshow('error_map', error_map)

# 画像の保存
cv.imwrite('./result/error_map_diff.png', error_map)

cv.waitKey(0)
cv.destroyAllWindows()