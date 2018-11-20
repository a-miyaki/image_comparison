import cv2 as cv
import tkinter as tk
import tkinter.filedialog as fd
import numpy as np
from PIL import Image

from error_map import make_error_map
from BGR_error import BGR_error
from calculation_ROI import Calculation_ROI

def main():
    # ディレクトリの指定
    path = './image_error_map/'
    iter = 5700
    iter_padded = '{0:08d}'.format(iter)
    path_A = path + 'image_gt_' + iter_padded + '.png'
    path_B = path + 'image_gen_' + iter_padded + '.png'

    image_A = cv.imread(path_A, 1)
    image_B = cv.imread(path_B, 1)

    error_map = make_error_map(image_A, image_B)
    list = BGR_error(error_map)
    ROI_list = Calculation_ROI()

    Red_error_ROI = list[0] / ROI_list[0] / 256 * 100
    print('RのROIエラー(%)')
    print(Red_error_ROI)
    Blue_error_ROI = list[2] / ROI_list[2] / 256 * 100
    print('BのROIエラー(%)')
    print(Blue_error_ROI)
    Green_error_ROI = list[1] / ROI_list[1] / 256 * 100
    print('GのROIエラー(%)')
    print(Green_error_ROI)

if __name__ == "__main__":
    main()
