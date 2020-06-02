from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Regexp


class ImgForm(FlaskForm):
    fileimg = FileField(validators=[
        FileRequired(),
        FileAllowed(['png', 'jpg', 'jpeg', 'gif','tif'])
    ])
    imageRetrieval = SubmitField('imageRetrieval')  # 图像检索
    edgeDetction = SubmitField('edgeDetction')  # 边缘检测
    hough = SubmitField('hough')  # hough变换
    denoising = SubmitField('denoising')  # 图像去燥
    trafficSignCode = SubmitField('trafficSignCode')  # 交通标志检测
    Segmentation = SubmitField('Segmentation')  # 细胞边缘分割
    Histogram_equalization = SubmitField('Histogram_equalization')  # 直方图均衡化
    sift_extract = SubmitField('sift_extract')  # 直方图均衡化


class URLForm(FlaskForm):
    txturl = StringField(validators=[
        DataRequired(),
        Regexp(r'(?:http\:|https\:)?\/\/.*\.(?:png|jpg|jpeg|gif)$',
               message="Invalid image url.")
    ])
