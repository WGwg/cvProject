# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         SIFT_demo
# Author:       WG
# Date:         2020/5/24
# Description: 
#-------------------------------------------------------------------------------
import cv2
from .image_to_resize import scale_byRatio

def sift_img_extract(url,filename):
    filename = filename[0:-4]
    img_list = []
    img = cv2.imread(url)  # 读取要处理的图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    fd_alg = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptor = fd_alg.detectAndCompute(gray, None)
    img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints,
                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                            color=(51, 163, 236))

    cv2.imwrite('./images/sift_extract/' + filename + '_sift_extract.jpg', img)
    img_resize_sift_extract = scale_byRatio('./images/sift_extract/' + filename + '_sift_extract.jpg')
    cv2.imwrite('./images/sift_extract/' + filename + '_sift_extract.jpg', img_resize_sift_extract)
    img_list.append(filename + '_sift_extract.jpg')

    return  img_list