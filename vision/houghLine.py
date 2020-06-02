# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         houghLine
# Author:       WG
# Date:         2020/3/12
# Description:

# cv2.HoughLines()，它返回(ρ, θ)值的序列，ρ单位像素，θ单位弧度
# （lines: lines[i][0]为第i条直线的rho，lines[i][1]表示第i条直线的theta）。
# 第一个参数，输入的图片是一个二进制图片，在使用hough变换之前，应用阈值或使用canny边缘检测。
# 第二和第三个参数分别是ρ（rho:像素精度，一般设置为1；）和θ的精度（theta：角度精度，一般设置为CV_PI/180），
# 第4个参数是阈值，指可以被认为是一个线条的最小计数值。由于计数值的多少取决于线上的点数（threshold:表示累计的像素达到多少才能形成直线），
# 所以这代表了可以被识别为线的最小长度。


#-------------------------------------------------------------------------------
import cv2
import numpy as np
#hough变换的程序实现

def houghLineDetction(url,filename):
    list_img =[]
    img = cv2.imread(url)#读取图片
    img2 = img.copy()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#将图片转换为灰度图
    edges = cv2.Canny(gray,50,150,apertureSize = 3)#canny算法提取轮廓

    #标准的hough变换......................................................
    lines_standards = cv2.HoughLines(edges,1,np.pi/180,200) #标准hough变换查找直线    返回值就是极坐标表示的直线（ρ, θ）。ρ 的单位是像素，θ 的单位是弧度。

    #绘制hough变换后找到的所有直线，返回数据是一个二位数组
    try:
        for lines_standard in lines_standards:
            for rho, theta in lines_standard:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(img2, (x1, y1), (x2, y2), (0, 0, 255), 2)
            print(lines_standards)  # 打印出找到的直线的极坐标系坐标、
        filename  = filename[0:-4]
        cv2.imwrite('./images/houghLine/houghLine_'+filename+'.jpg', img2)
        list_img.append('houghLine_'+filename+'.jpg')
    except Exception:
        print("无坐标")
        list_img=[]

    return  list_img
