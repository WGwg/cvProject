# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         biaoyuanTough
# Author:       WG
# Date:         2020/3/8
# Description: 边缘检测
#-------------------------------------------------------------------------------
import cv2
from .image_to_resize import scale_byRatio

def bianyuanDetection(url,filename):
    lenna = cv2.imread(url, 0)
    sobel = cv2.Sobel(lenna, -1, 1, 1, ksize=5)  #一阶微分算子Sobel   使用Prewitt或Sobel算子对图像进行卷积，将梯度幅值大于阈值的点标记为边缘;将边缘细化为一个像素宽度
    laplacian = cv2.Laplacian(lenna, -1)   #二阶微分算子Laplacian   拉普拉斯滤波器 进行卷积操作  结果相较原图会锐化  凸显细节出来
    canny = cv2.Canny(lenna, 100, 200)   #高斯模糊Canny

    filename = filename[0:-4]

    cv2.imwrite('./images/bianyuanTough/' + filename + '_sobel.jpg', sobel)
    img_resize_sobel = scale_byRatio('./images/bianyuanTough/'+filename+'_sobel.jpg')
    cv2.imwrite('./images/bianyuanTough/' + filename + '_sobel_resize.jpg', img_resize_sobel)

    cv2.imwrite('./images/bianyuanTough/'+filename+'_laplacian.jpg', laplacian)
    img_resize_laplacian = scale_byRatio('./images/bianyuanTough/'+filename+'_laplacian.jpg')
    cv2.imwrite('./images/bianyuanTough/' + filename + '_laplacian_resize.jpg', img_resize_laplacian)

    cv2.imwrite('./images/bianyuanTough/'+filename+'_canny.jpg', canny)
    img_resize_canny = scale_byRatio('./images/bianyuanTough/'+filename+'_canny.jpg')
    cv2.imwrite('./images/bianyuanTough/' + filename + '_canny_resize.jpg', img_resize_canny)

    img_list = [filename+'_sobel_resize.jpg',filename+'_laplacian_resize.jpg',filename+'_canny_resize.jpg']


    return  img_list
