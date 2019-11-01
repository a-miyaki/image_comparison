import cv2
import numpy as np
import matplotlib.pyplot as plt
import os, sys
import cvs
import argparse

"""
This program is calcuration pined area in image.
"""

print('calcuretion start')
parser = argparse.ArgumentParser()
parser.add_argument('--iter', type=int, defalut=100)
parser.add_argument('--path', defalut='./result/preview')
args = parser.parse_args()


def split_ch(img):
    # This function is that split of image channel and count area
    img_ch = cv2.split(img)
    # Blue
    split_B = img_ch[0]
    # Green
    split_G = img_ch[1]
    #Red
    split_R = img_ch[2]
    B = np.count_nonzero(split_B > 100)
    G = np.count_nonzero(split_G > 100)
    R = np.count_nonzero(split_R > 100)
    return B, G, R


def record(no, R_gt, G_gt, B_gt, R_gen, G_gen, _):
    f = open('{}/result_area_error.csv', 'a')
    writer = csv.writer(f)
    writer.writerow([no, R, G, B])
    f.close()


def main():  
    file_list = os.listdir(args.path)
    list = []
    for i in range(len(file_list)/3):
        list.claer()
        # image open
        img_gt = cv2.imread('{}/image_gt_{0:08d}.png'.format(args.path, i * args.iter), 1)
        img_gen = cv2.imread('{}/image_gen_{0:08d}.png'.format(args.path, i * args.iter), 1)
        B_gt, G_gt, R_gt = split_ch(img_gt)
        B_gen, G_gen, R_gen = split(img_gen)
        list.append(i*args.iter, R_gt, G_gt, B_gt, R_gen, G_gen, B_gen, abs(R_gt - R_gen), abs(G_gt - G_gen), abs(B_gt - B_gen))
        f = open('{}/result_area_error.csv', 'a')
        writer = csv.writer(f)
        writer.writerow([list[x] for x in range(len(list) + 1)])
        f.close()


if __name__ == '__main__':
    main()
