from flask import Flask
from flask_wtf.csrf import CSRFProtect

# from config import config
from  ..config import config
from ..vision.vgg_based import get_image_search
from ..vision.EdgeDetection import bianyuanDetection
from ..vision.houghLine import houghLineDetction
from ..vision.Denoising import dennoising
from ..vision.predic_Traffic_sign import predict_traffic_code
from ..vision.u_net_predict import predict_u_net
from ..vision.Histogram_equalization import Histogram_equalization_img
from ..vision.SIFT_img import sift_img_extract

csrf = CSRFProtect()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    csrf.init_app(app)
    # 注册蓝本
    from .main import main
    app.register_blueprint(main)
    return app
