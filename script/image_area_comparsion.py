import cv2
import numpy as np
import matplotlib.pyplot as plt
import os, sys
import csv
import argparse

"""
This program is calcuration pined area in image.
"""

print('calcuretion start')
parser = argparse.ArgumentParser()
parser.add_argument('--iter', type=int, default=10000)
parser.add_argument('--path', default='./image')
args = parser.parse_args()


def Binarization(img):
    img = img.astype(np.uint8)
    img = cv2.distanceTransform(img, 1, 3)
    cv2.imshow("Frame", img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def split_ch(img):
    # This function is that split of image channel and count area
    img_ch = cv2.split(img)
    # Blue
    split_B = img_ch[0]
    # Green
    split_G = img_ch[1]
    #Red
    split_R = img_ch[2]
    B = np.count_nonzero(split_B > 30)
    G = np.count_nonzero(split_G > 50)
    R = np.count_nonzero(split_R > 50)
    split_B = (img_ch[0] > 30)
    split_G = (img_ch[1] > 50)
    split_R = (img_ch[2] > 50)
    Binarization(split_B)
    Binarization(split_G)
    Binarization(split_R)
    return B, G, R


def main(args):
    file_list = len([name for name in os.listdir(args.path)])
    for i in range(1, int(file_list/2) + 1):
        print(i * args.iter)
        # image open
        img_gt = cv2.imread(args.path + '/image_gt_{0:08d}.png'.format(i * args.iter), 1)
        img_gen = cv2.imread(args.path + '/image_gen_{0:08d}.png'.format(i * args.iter), 1)
        h, w, _ = img_gt.shape
        # cv2.imshow("frame", img_gen)
        B_gt, G_gt, R_gt = split_ch(img_gt)
        B_gen, G_gen, R_gen = split_ch(img_gen)
        with open('{}/result_area_error.csv'.format(args.path), 'a') as f:
            fieldname = ['iter', 'R_gt', 'G_gt', 'B_gt', 'R_gen', 'G_gen', 'B_gen', 'abs(R)', 'abs(G)', 'abs(B)']
            writer = csv.DictWriter(f, fieldnames=fieldname)
            writer.writeheader()
            writer.writerow({'iter': i * args.iter, 'R_gt': R_gt, 'G_gt': G_gt, 'B_gt': B_gt,
                             'R_gen': R_gen, 'G_gen': G_gen, 'B_gen': B_gen,
                             'abs(R)': abs(R_gt - R_gen) / h / w,
                             'abs(G)': abs(G_gt - G_gen) / h / w,
                             'abs(B)': abs(B_gt - B_gen) / h / w})
            f.close()


if __name__ == '__main__':
    main(args)
    print('finish')
