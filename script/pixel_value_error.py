import numpy as np
import cv2
import os
import argparse
import csv
from PIL import Image

parser = argparse.AugumentParser(description='image coparsion')
parser.add_argument('--path', default='./resultdir/preview2')
parser.add_argument('--iter', type=int, default=100, help='iteration of out image by GAN')
args = parser.parse_args()


def make_error_map(image_A, image_B, no):
    """
    This function make absolut error map, image to image.
    If you don't want to save error map, you need to add # front cv.imwrite().
    """
    # If image size is difficult, cv2.absdiff() will report error.
    """print(image_A.shape)
    print(image_B.shape)"""

    # make error map
    error_map = cv.absdiff(image_A, image_B, dst=None)

    # show image
    cv.imshow('error_map', error_map)

    # save image
    cv.imwrite('{}/error_map_{}.png'.format(args.path, no), error_map)

    # wait for input key, and close all windows
    cv.waitKey(0)
    cv.destroyAllWindows()

    return error_map


def split_RGB(no):
    img = Image.open('{}/error_map_{}.png'.format(args.path, no))
    img = np.array(img)
    
    img_R = img.copy()
    img_R[:, :, (1, 2)] = 0
    img_G = img.copy()
    img_G[:, :, (0, 2)] = 0
    img_B = img.copy()
    img_B[:, :, (0, 1)] = 0
    retun img_R, img_G, img_B


def record(filename, iter, R, G, B, Rstd, Gstd, Bstd):
    f = open(filename, 'a')
    writer = csv.writer(f)
    writer.writerow([iter, R, G, B, Rstd, Gstd, Bstd])
    f.close()


def main():
    print(' Strat calcuration of pixel value error')
    for i in range(1, len(os.listdir(args.path)) / 3):
        img_a = cv2.imread('{}/image_gen_{0:08d}.png'.format(args.path, i * args.iter), 1)
        img_b = cv2.imread('{}/image_gt_{0:08d}.png'.format(args.path, i * args.iter), 1)
        
        error_map = make_error_map(img_a, img_b, i * args.iter)
        R, G, B = split_RGB(i * args.iter)
        R_error = np.sum(R / 256) * 100
        G_error = np.sum(G / 256) * 100
        B_error = np.sum(B / 256) * 100
        R_std = np.std(R)
        G_std = np.std(G)
        B_std = np.std(B)
        record('{}/result.csv'.format(args.path), i * args.iter, R_error, G_error, B_error, R_std, G_std, B_std)
    print('Finish calcuration')


if __name__ == '__main__':
    main()
