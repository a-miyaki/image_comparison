import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os, sys

def main():
    # ディレクトリ指定
    files = u"./cell_image/"
    file_list = os.listdir(r'./cell_image/')

    # ファイルを読み込む
    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == u'.png':
            abs_name = files + '/' + file_name
            image = cv.imread(abs_name, 1)
            # ファイルのチャネルを分割
            img_ch = cv.split(image)
            # 0,1,2でB,G,Rを表示する # 閾値30で2値化する
            binimg = (img_ch[0] > 30)
            binimg = binimg.astype(np.uint8)
            distmap = cv.distanceTransform(binimg, 1, 3)

            out = distmap * 0
            ksize = 10
            for x in range(ksize, distmap.shape[0] - ksize * 2):
                for y in range(ksize, distmap.shape[1] - ksize * 2):
                    if distmap[x, y] > 0 and distmap[x, y] == np.max(distmap[x - ksize:x + ksize, y - ksize:y + ksize]):
                        out[x, y] = 1

            out = cv.dilate(out, (3, 3))

            image, contours, _ = cv.findContours(out.astype(np.uint8), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

            arr = []
            for i in contours:
                x_ = 0
                y_ = 0
                for j in i:
                    x_ += j[0][0]
                    y_ += j[0][1]
                arr.append([x_ / len(i), y_ / len(i)])
            arr = np.array(arr)

            plt.imshow(out[0:100, 0:100])
            plt.colorbar()
            plt.show()

            print(len(arr))

if __name__ == '__main__':
    main()
