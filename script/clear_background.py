from PIL import Image
import os
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='chainer implementation of pix2pix')
parser.add_argument('--dataset', '-i', default=u'./20191101')
parser.add_argument('--out', default='./adjust')
args = parser.parse_args()

list = os.listdir(args.dataset)
if not os.path.exists(args.out):
    os.mkdir(args.out)


def main():
    i = 1
    for file_name in list:
        root, ext = os.path.splitext(file_name)
        if 'f' in root:
            abs_name = args.dataset + '/' + file_name
            img = Image.open(abs_name)
            img = np.asarray(img)

            img_R = img.copy()
            img_R[:, :, (1, 2)] = 0
            img_G = img.copy()
            img_G[:, :, (0, 2)] = 0
            img_B = img.copy()
            img_B[:, :, (0, 1)] = 0
            R_min = np.min(img_R[:, :, 0])
            G_min = np.min(img_G[:, :, 1])
            B_min = np.min(img_B[:, :, 2])

            R = np.where(img_R >= R_min, img_R - R_min, 0)
            G = np.where(img_G >= G_min, img_G - G_min, 0)
            B = np.where(img_B >= B_min, img_B - B_min, 0)
            merge = Image.fromarray(R + G + B)
            merge.save(args.out + '/' + file_name)
        else:
            pass
        print('---{} / {} ---'.format(i, len(list)))
        i += 1
    print('finish')


if __name__ == '__main__':
    main()
