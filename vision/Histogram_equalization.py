# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         aaaa
# Author:       WG
# Date:         2020/5/24
# Description: 
#-------------------------------------------------------------------------------

import cv2
from .image_to_resize import scale_byRatio

def Histogram_equalization_img(url,filename):
    img_list = []
    filename = filename[0:-4]
    img = cv2.imread(url)
    img = cv2.resize(img, (400, 430))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_gray.jpg', img_gray)
    # img_resize_img_gray = scale_byRatio('./images/Histogram_equalization/' + filename + '_img_gray.jpg')
    # cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_gray.jpg', img_resize_img_gray)
    # img_list.append(filename + '_img_gray.jpg')
    #
    # histeq = cv2.equalizeHist(img_gray)
    # # cv2.imshow('histeq', histeq)
    # cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_gray_histeq.jpg', histeq)
    # img_resize_img_gray_histeq = scale_byRatio('./images/Histogram_equalization/' + filename + '_img_gray_histeq.jpg')
    # cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_gray_histeq.jpg', img_resize_img_gray_histeq)
    # img_list.append(filename + '_img_gray_histeq.jpg')


    yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])

    img_histeq = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)

    # cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_oral.jpg', img)
    # img_resize_img_oral = scale_byRatio('./images/Histogram_equalization/' + filename + '_img_oral.jpg')
    # cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_oral.jpg', img_resize_img_oral)
    # img_list.append(filename + '_img_oral.jpg')

    cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_oral_histeq.jpg', img_histeq)
    img_resize_img_oral_histeq = scale_byRatio('./images/Histogram_equalization/' + filename + '_img_oral_histeq.jpg')
    cv2.imwrite('./images/Histogram_equalization/' + filename + '_img_oral_histeq.jpg', img_resize_img_oral_histeq)
    img_list.append( filename + '_img_oral_histeq.jpg')

    return img_list

