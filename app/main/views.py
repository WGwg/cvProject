import os

from flask import (current_app, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename

from ...utils import download
from .. import get_image_search,bianyuanDetection,houghLineDetction,dennoising,predict_traffic_code,predict_u_net,Histogram_equalization_img,sift_img_extract    #需要在app/__init__.py中 先导入
from . import main
from .forms import ImgForm, URLForm

# 不同数据集有不同的路径
dataset_path_dict = {
    'holiday': 'video1/',
    'bianyuanTough': 'bianyuanTough/',
    'houghLine': 'houghLine/',
    'dennoising': 'dennoising/',
    'trafficSignCode':'trafficSignCode/',
    'Segmentation':'Segmentation/',
    'Histogram_equalization':'Histogram_equalization/',
    'sift_extract':'sift_extract/'
}


@main.route('/', methods=['GET', 'POST'])
def index():
    imgform = ImgForm()
    urlform = URLForm()

    if imgform.validate_on_submit():
        if imgform.imageRetrieval.data:
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.result', filename=filename))

        if imgform.edgeDetction.data:
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.bianyuanDetectioRresult', filename=filename))

        if imgform.hough.data:
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.houghLineRresult', filename=filename))

        if imgform.denoising.data:
            print(imgform.denoising.data)
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.denoisingRresult', filename=filename))

        if imgform.trafficSignCode.data:
            print(imgform.denoising.data)
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.trafficSignCode', filename=filename))
        if imgform.Segmentation.data:
            print(imgform.denoising.data)
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.Segmentation', filename=filename))
        if imgform.Histogram_equalization.data:
            print(imgform.denoising.data)
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.Histogram_equalization', filename=filename))

        if imgform.sift_extract.data:
            print(imgform.denoising.data)
            file = imgform.fileimg.data
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            return redirect(url_for('.sift_extract_img', filename=filename))

    elif urlform.validate_on_submit():
        url = urlform.txturl.data
        filename = secure_filename(url.split('/')[-1])
        filepath = os.path.join(current_app.config['UPLOAD_DIR'], filename)
        download(url, current_app.config['UPLOAD_DIR'], filename)
        if not os.path.exists(filepath):
            flash('无法取回指定URL的图片')
            return redirect(url_for('.index'))
        else:
            return redirect(url_for('.result', filename=filename))
    return render_template('index.html')


@main.route('/result', methods=['GET'])
def result():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    print(uri)
    img_d, images, scores = get_image_search(uri,return_num=5)
    print(images)
    dataset = 'holiday'
    images = [os.path.join(dataset_path_dict[dataset], i) for i in images]
    print(images)
    return render_template('result.html', filename=filename, images=images)

@main.route('/bianyuanDetectioRresult', methods=['GET'])
def bianyuanDetectioRresult():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    print(uri)
    img_list = bianyuanDetection(uri,filename)
    print(img_list)
    dataset = 'bianyuanTough'
    img_list = [os.path.join(dataset_path_dict[dataset], i) for i in img_list]
    print(img_list)

    return render_template('result.html', filename=filename, images=img_list)

@main.route('/houghLineRresult', methods=['GET'])
def houghLineRresult():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    print(uri)
    hough_img_list = houghLineDetction(uri,filename)
    print(hough_img_list)
    dataset = 'houghLine'
    hough_img_list = [os.path.join(dataset_path_dict[dataset], i) for i in hough_img_list]
    print(hough_img_list)

    return render_template('result.html', filename=filename, images=hough_img_list)

@main.route('/denoisingRresult', methods=['GET'])
def denoisingRresult():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    print(uri)
    dennoising_img_list = dennoising(uri,filename)
    print(dennoising_img_list)
    dataset = 'dennoising'
    dennoising_img_list = [os.path.join(dataset_path_dict[dataset], i) for i in dennoising_img_list]
    print(dennoising_img_list)

    return render_template('result.html', filename=filename, images=dennoising_img_list)


@main.route('/trafficSignCode', methods=['GET'])
def trafficSignCode():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    print(uri)
    trafficSignCode_img_list = predict_traffic_code(uri,filename)
    print(trafficSignCode_img_list)
    dataset = 'trafficSignCode'
    trafficSignCode_img_list = [os.path.join(dataset_path_dict[dataset], i) for i in trafficSignCode_img_list]
    print(trafficSignCode_img_list)

    return render_template('result.html', filename=filename, images=trafficSignCode_img_list)

@main.route('/Segmentation', methods=['GET'])
def Segmentation():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    # print(uri)
    predict_u_net_img_list = predict_u_net(uri,filename)
    # print(predict_u_net_img_list)
    dataset = 'Segmentation'
    predict_u_net_img_list = [os.path.join(dataset_path_dict[dataset], i) for i in predict_u_net_img_list]
    # print(predict_u_net_img_list)

    return render_template('result.html', filename=filename, images=predict_u_net_img_list)


@main.route('/Histogram_equalization', methods=['GET'])
def Histogram_equalization():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    # print(uri)
    Histogram_equalization_img_list = Histogram_equalization_img(uri,filename)
    # print(predict_u_net_img_list)
    dataset = 'Histogram_equalization'
    Histogram_equalization_img_list = [os.path.join(dataset_path_dict[dataset], i) for i in Histogram_equalization_img_list]
    # print(predict_u_net_img_list)

    return render_template('result.html', filename=filename, images=Histogram_equalization_img_list)


@main.route('/sift_extract_img', methods=['GET'])
def sift_extract_img():
    filename = request.args.get('filename')
    uri = os.path.join(current_app.config['UPLOAD_DIR'], filename)
    # print(uri)
    sift_img_extract_img_list = sift_img_extract(uri,filename)
    # print(predict_u_net_img_list)
    dataset = 'sift_extract'
    sift_img_extract_img_list_img_list = [os.path.join(dataset_path_dict[dataset], i) for i in sift_img_extract_img_list]
    # print(predict_u_net_img_list)

    return render_template('result.html', filename=filename, images=sift_img_extract_img_list_img_list)

@main.route('/images/<path:uri>')
def download_file(uri):
    return send_from_directory(current_app.config['DATABASE_DIR'],
                               uri, as_attachment=True)
