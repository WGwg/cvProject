from ..vision.u_net_model import *
from ..vision.u_net_data import *
from keras import backend

def predict_u_net(url,filename):
    img_list = []
    filename = filename[0:-4]
    # 清除上次加载完模型中 遗留的数据
    backend.clear_session()

    model = unet(pretrained_weights = './model/unet_membrane.hdf5')
    testGene = aaa(url)
    print(testGene)
    results = model.predict_generator(testGene,1,verbose=1)
    img_new = saveResult("./images/Segmentation",results,filename)
    print(img_new)
    img_list.append(img_new)
    return img_list
