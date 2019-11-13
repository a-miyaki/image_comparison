import numpy as np
import cv2 as cv
import os
import argparse
import csv
from PIL import Image

parser = argparse.ArgumentParser(description='image coparsion')
parser.add_argument('--path', default='./image')
parser.add_argument('--iter', type=int, default=10000, help='iteration of out image by GAN')
args = parser.parse_args()


def split_RGB(img):
    img = np.array(img)

    img_R = img.copy()
    img_R[:, :, (1, 2)] = 0
    img_G = img.copy()
    img_G[:, :, (0, 2)] = 0
    img_B = img.copy()
    img_B[:, :, (0, 1)] = 0
    return img_R, img_G, img_B


def main():
    filename = args.path + '/pixel_value_error.csv'

    print(' Strat calcuration of pixel value error')

    n = len([name for name in os.listdir(args.path)])

    with open(filename, 'a') as f:
        fieldname = ['iter', 'R', 'G', 'B', 'Rstd', 'Gstd', 'Bstd']
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        f.close()

    for i in range(1, int(n / 2) + 1):
        img_a = Image.open('./image/image_gen_{0:08d}.png'.format(i * args.iter))
        img_b = Image.open('./image/image_gt_{0:08d}.png'.format(i * args.iter))
        img_a.show()

        img_a_R, img_a_G, img_a_B = split_RGB(img_a)
        img_b_R, img_b_G, img_b_B = split_RGB(img_b)

        R = np.sum(abs(((img_a_R + 1) - (img_b_R + 1)) / (img_b_R + 1))) / 256 / 256
        G = np.sum(abs(((img_a_G + 1) - (img_b_G + 1)) / (img_b_G + 1))) / 256 / 256
        B = np.sum(abs(((img_a_B + 1) - (img_b_B + 1)) / (img_b_B + 1))) / 256 / 256
        Rstd = np.std(abs(img_a_R - img_b_R))
        Gstd = np.std(abs(img_a_G - img_b_G))
        Bstd = np.std(abs(img_a_B - img_b_B))

        with open(filename, 'a') as f:
            fieldname = ['iter', 'R', 'G', 'B', 'Rstd', 'Gstd', 'Bstd']
            writer = csv.DictWriter(f, fieldnames=fieldname)
            writer.writerow({'iter': i * args.iter, 'R': R, 'G': G, 'B': B, 'Rstd': Rstd, 'Gstd': Gstd, 'Bstd': Bstd})
            f.close()

    print('finish')


if __name__ == '__main__':
    main()

