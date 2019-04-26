# -*- coding: utf-8 -*-

import os
import cv2
import time

# パス1の指定　元画像のパスを入れる
path1 = "E:\\pytorch\\train\MCF_7"
# パス2の指定　保存先のパスを入れる
path2 = "E:\\pytorch\\train\MCF-7"


def main():
    # 保存先を作成
    if not os.path.exists(path2):
        os.mkdir(path2)

    i = 1
    for x in os.listdir(path1):
        img_name1 = path1 + "\\" + x
        print(x)
        img = cv2.imread(img_name1, 1)
        # 名前の変更
        cv2.imwrite(path2 + "/MCF" + '{0:04d}'.format(i) + ".png", img)
        img_name2 = path2 + "/MCF" + '{0:04d}'.format(i) + ".png"
        print(img_name2)
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    main()

