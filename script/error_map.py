import cv2 as cv

# パスの指定
path = "./image_error_map/"
iter = 5700
iter_padded = '{0:08d}'.format(iter)
path_A = path + 'image_gt_' + iter_padded + '.png'
path_B = path + 'image_gen_' + iter_padded + '.png'
# 画像を読み込む
image_A = cv.imread(path_A, 1)
image_B = cv.imread(path_B, 1)

def make_error_map(image_A, image_B):

    # 画像のサイズを確認する 画像サイズが違うと動かない
    """print(image_A.shape)
    print(image_B.shape)"""

    # エラーマップ作製
    error_map = cv.absdiff(image_A, image_B, dst=None)

    # 画像の表示
    cv.imshow('error_map', error_map)

    # 画像の保存
    cv.imwrite(path + 'error_map_diff.png', error_map)

    # キー入力待ち 入力すると開いているウインドウをすべて閉じる
    cv.waitKey(0)
    cv.destroyAllWindows()

    return error_map

if __name__ == "__make_error_map__":
    make_error_map()