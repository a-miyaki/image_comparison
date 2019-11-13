#!/usr/bin/env python
# coding:utf-8

import argparse
import numpy as np
import chainer
#import chainer.functions as F
#import chainer.links as L
from PIL import Image
import PIL

parser = argparse.ArgumentParser(description='chainer implementation of pix2pix')

parser.add_argument('--dataset', '-i',
                    default='./20191101/',
                        help='Directory of image files.')
parser.add_argument('--file_name', '-f',default='f',
                        help='File Name :(default) ')
parser.add_argument('--outset', '-o',default='./adjust/',
                        help='Directory of output image files.')
parser.add_argument('--start_no', '-s',type=int,default=1,
                        help='Start file No.')
parser.add_argument('--end_no', '-e',type=int,default=456,
                        help='End file No.')

args = parser.parse_args()
dir = args.dataset

start_no = args.start_no
end_no = args.end_no

print('Data Dir : {}'.format(args.dataset))
print('file name : {}'.format(args.file_name))
#print('threshold : {}'.format(args.threshold))
print('Start > {} , End > {}'.format(args.start_no,args.end_no))

for k in range(start_no,end_no+1):
    #file_name = args.file_name + "%04d.jpg" %k
    file_name = args.file_name + "%04d.png" %k
    
    im = np.array(Image.open(dir + file_name))

    im_R = im.copy()
    im_R[:,:, (1, 2)] = 0    #　色分解
    im_G = im.copy()
    im_G[:,:, (0, 2)] = 0
    im_B = im.copy()
    im_B[:,:, (0, 1)] = 0

    R_min = np.min(im_R[0:300,0:300,0]) # 最小値検出　0:400はファイルサイズ指定、最後の0は色指定でRを指す
    G_min = np.min(im_G[0:300,0:300,1])
    B_min = np.min(im_B[0:300,0:300,2])

    print(':min > {},{},{}'.format(R_min,G_min,B_min))

    im_R = np.where(im_R >= R_min, im_R - R_min, 0) # 最小値を引く
    im_G = np.where(im_G >= G_min, im_G - G_min, 0)
    im_B = np.where(im_B >= B_min, im_B - B_min, 0)

# end 

    pil_img = Image.fromarray(im_R + im_G + im_B)  # 色合成
    pil_img.save(args.outset + file_name)
    print(' {} end'.format(file_name))

exit(0)
