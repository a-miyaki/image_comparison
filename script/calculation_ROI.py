from PIL import Image
import cv2 as cv

path = "./image_error_map/"
iter = 5700
iter_padded = '{0:08d}'.format(iter)
path_A = path + 'image_gt_' + iter_padded + '.png'
path_B = path + 'image_gen_' + iter_padded + '.png'

def Calculation_ROI():
    img_A = cv.imread(path_A, 1)
    img_B = cv.imread(path_B, 1)
    merge = cv.add(img_A, img_B)

    cv.imwrite(path + "merge.png", merge)
    cv.imshow('merge', merge)
    cv.waitKey()
    cv.destroyAllWindows()

    img = Image.open(path + "merge.png")
    pixelSizeTuple = img.size

    rlist = []
    glist = []
    blist = []

    # 各ピクセルのRGBをリスト化する
    for i in range(pixelSizeTuple[0]):
        for j in range(pixelSizeTuple[1]):
            r, g, b = img.getpixel((i, j))
            rlist.append(r)
            glist.append(g)
            blist.append(b)

    # リストをエクセルで出力
    f = open(path + 'output.csv', 'w')
    f.write("r,g,b\n")
    n = len(rlist)
    for i in range(0, n-1):
        f.write(str(rlist[i]) + "," + str(glist[i]) + "," + str(blist[i]) + "\n")
    
    f.close()

    # 画像の面積(pixel)
    # area = pixelSizeTuple[0] * pixelSizeTuple[1]
    area = pixelSizeTuple[0] * pixelSizeTuple[1]
    # 各リストの0をカウントし、全ピクセル数から引く
    Red_ROI = int(area) - int(rlist.count(0))
    Blue_ROI = int(area) - int(blist.count(0))
    Green_ROI = int(area) - int(glist.count(0))
    ROI_list = [Red_ROI, Blue_ROI, Green_ROI]

    # ROIの出力
    print('赤の関心領域')
    print(Red_ROI)
    print('青の関心領域')
    print(Blue_ROI)
    print('緑の関心領域')
    print(Green_ROI)

    return ROI_list

if __name__ == "__main__":
    Calculation_ROI()
