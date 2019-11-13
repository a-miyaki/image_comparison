from PIL import Image
import os
import numpy as np

path = u'../dataset/20191101'
list = os.listdir(path)


def function(array):
    min = array.min()
    equal = array - min
    Image.fromarray(equal).convert('L')
    return equal


def main():
    i = 1
    for file_name in list:
        root, ext = os.path.splitext(file_name)
        if 'f' in root:
            abs_name = path + '/' + file_name
            img = Image.open(abs_name)
            img = np.asarray(img)

            img_R = img.copy()
            img_R[:, :, (1, 2)] = 0
            img_G = img.copy()
            img_G[:, :, (0, 2)] = 0
            img_B = img.copy()
            img_B[:, :, (0, 1)] = 0
            R = function(img_R)
            G = function(img_G)
            B = function(img_B)
            merge = Image.merge('RGB', (R, G, B))
            merge.save(abs_name)
        else:
            pass
        print('---{} / {} ---'.format(i, len(list)))
        i += 1
    print('finish')


if __name__ == '__main__':
    main()
