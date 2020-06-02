# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         imgClear
# Author:       WG
# Date:         2020/3/8
# Description: 图像处理-python实现图像处理（消噪，直方图均衡化，二值化，形态学）  https://blog.csdn.net/wsh596823919/article/details/79982485
#-------------------------------------------------------------------------------
import cv2
import numpy as np
from .image_to_resize import scale_byRatio




def dennoising(url,filename):
    img_List =[]
    filename = filename[0:-4]

    img = cv2.imread(url)
    # 1、消除椒盐噪声：
    # 中值滤波器
    median = cv2.medianBlur(img, 5)
    # 消除噪声图

    # cv2.imshow("median-image", median)
    cv2.imwrite('./images/dennoising/'+filename+'_'+'medianBlur'+'.jpg',median)
    img_resize_median = scale_byRatio('./images/dennoising/'+filename+'_'+'medianBlur'+'.jpg')
    cv2.imwrite('./images/dennoising/'+filename+'_'+'medianBlur2'+'.jpg', img_resize_median)
    img_List.append(filename+'_'+'medianBlur2'+'.jpg')

    # 转化为灰度图
    Grayimg = cv2.cvtColor(median, cv2.COLOR_RGB2GRAY)
    # 2、直方图均衡化：
    hist = cv2.equalizeHist(Grayimg)

    # cv2.imshow('hist', hist)
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'equalizeHist' + '.jpg', hist)
    img_resize_hist = scale_byRatio('./images/dennoising/' + filename + '_' + 'equalizeHist' + '.jpg')
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'equalizeHist2' + '.jpg', img_resize_hist)
    img_List.append(filename + '_' + 'equalizeHist2' + '.jpg')


    # 3、二值化处理：
    # 阈值为140
    ret, binary = cv2.threshold(hist, 140, 255, cv2.THRESH_BINARY)

    # cv2.imshow("binary-image", binary)
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'binary-image' + '.jpg', binary)
    img_resize_binary = scale_byRatio('./images/dennoising/' + filename + '_' + 'binary-image' + '.jpg')
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'binary-image2' + '.jpg', img_resize_binary)
    img_List.append(filename + '_' + 'binary-image2' + '.jpg')

    # 二值形态处理
    dennosing_img_list = morphology(binary,img_List,filename)

    return  dennosing_img_list

    # cv2.waitKey(0)


# 二值形态学运算
def morphology(img,img_List,filename):
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 14))  # 腐蚀矩阵
    iFushi = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel1)  # 对文字腐蚀运算


    # cv2.imshow('fushi', iFushi)
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'fushi' + '.jpg', iFushi)
    img_resize_iFushi = scale_byRatio('./images/dennoising/' + filename + '_' + 'fushi' + '.jpg')
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'fushi2' + '.jpg', img_resize_iFushi)
    img_List.append(filename + '_' + 'fushi2' + '.jpg')


    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))  # 膨胀矩阵
    iPengzhang = cv2.morphologyEx(iFushi, cv2.MORPH_ERODE, kernel2)  # 对背景进行膨胀运算


    # cv2.imshow('pengzhang', iPengzhang)
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'pengzhang' + '.jpg', iPengzhang)
    img_resize_iPengzhang = scale_byRatio('./images/dennoising/' + filename + '_' + 'pengzhang' + '.jpg')
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'pengzhang2' + '.jpg', img_resize_iPengzhang)
    img_List.append(filename + '_' + 'pengzhang2' + '.jpg')


    # 背景图和二分图相减-->得到文字
    jian = np.abs(iPengzhang - img)


    # cv2.imshow("jian", jian)
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'jian' + '.jpg', jian)
    img_resize_jian = scale_byRatio('./images/dennoising/' + filename + '_' + 'jian' + '.jpg')
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'jian2' + '.jpg', img_resize_jian)
    img_List.append(filename + '_' + 'jian2' + '.jpg')


    kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 6))  # 膨胀
    iWenzi = cv2.morphologyEx(jian, cv2.MORPH_DILATE, kernel3)  # 对文字进行膨胀运算


    # cv2.imshow('wenzi', iWenzi)
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'wenzi' + '.jpg', iWenzi)
    img_resize_iWenzi = scale_byRatio('./images/dennoising/' + filename + '_' + 'wenzi' + '.jpg')
    cv2.imwrite('./images/dennoising/' + filename + '_' + 'wenzi2' + '.jpg', img_resize_iWenzi)
    img_List.append(filename + '_' + 'wenzi2' + '.jpg')

    return img_List