# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         image_to_resize
# Author:       WG
# Date:         2020/5/22
# Description:  将输入图像成比例resize  几乎不损失原图
#  直接调用 scale_byRatio(url)
#-------------------------------------------------------------------------------
import cv2

def center_crop(x, center_crop_size):
    centerw, centerh = x.shape[0] // 2, x.shape[1] // 2
    halfw, halfh = center_crop_size[0] // 2, center_crop_size[1] // 2
    cropped = x[centerw - halfw : centerw + halfw,
                 centerh - halfh : centerh + halfh, :]

    return cropped

def scale_byRatio(img_path, return_width=150, crop_method=center_crop):
    # Given an image path, return a scaled array
    img = cv2.imread(img_path)
    h = img.shape[0]
    w = img.shape[1]
    shorter = min(w, h)
    longer = max(w, h)
    img_cropped = crop_method(img, (shorter, shorter))
    img_resized = cv2.resize(img_cropped, (return_width, return_width), interpolation=cv2.INTER_CUBIC)

    return img_resized