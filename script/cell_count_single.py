import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./preview/image_gt_00011400.png', 1)
img_chs = cv2.split(img)

binimg = (img_chs[2] > 40)
plt.imshow(binimg)
plt.show()
binimg = binimg.astype(np.uint8)
distmap = cv2.distanceTransform(binimg, 1, 3)

out = distmap * 0
ksize = 10
for x in range(ksize, distmap.shape[0] - ksize * 2):
    for y in range(ksize, distmap.shape[1] - ksize * 2):
        if distmap[x, y] > 0 and distmap[x, y] == np.max(distmap[x - ksize:x + ksize, y - ksize:y + ksize]):
            out[x, y] = 1

out = cv2.dilate(out, (3, 3))

img, contours, _ = cv2.findContours(out.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

arr = []
for i in contours:
    x_ = 0
    y_ = 0
    for j in i:
        x_ += j[0][0]
        y_ += j[0][1]
    arr.append([x_ / len(i), y_ / len(i)])
arr = np.array(arr)

print(len(arr))
