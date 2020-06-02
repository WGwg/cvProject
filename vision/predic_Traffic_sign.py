# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras import backend
import numpy as np
import imutils
import cv2

norm_size = 32

def predict_traffic_code(url,filename):
    img_list = []

    #清除上次加载完模型中 遗留的数据
    backend.clear_session()

    # load the trained convolutional neural network
    print("[INFO] loading network...")
    model = load_model('./model/traffic_sign.model')
    #load the image
    image = cv2.imread(url)
    orig = image.copy()
     
    # pre-process the image for classification
    image = cv2.resize(image, (norm_size, norm_size))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
     
    # classify the input image
    result = model.predict(image)[0]
    #print (result.shape)
    proba = np.max(result)
    label = str(np.where(result==proba)[0])
    label = "{}: {:.2f}%".format(label, proba * 100)
    print(label)
    if label.find("21"):
        label = label.replace('21','stop:stop to run')
        print(label)
    if label.find("49"):
        label = label.replace('49','P:park of bus')
        print(label)

    output = imutils.resize(orig, width=400)
    orig = cv2.putText(output, label, (10, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    filename = filename[0:-4]
    cv2.imwrite('./images/trafficSignCode/trafficSignCode_' + filename + '.jpg', orig)
    img_list.append('trafficSignCode_' + filename + '.jpg')
    return img_list
