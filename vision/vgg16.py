import numpy as np
from numpy import linalg as LA
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Flatten, Dense, AveragePooling2D

class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.pooling = 'max'
        self.model = VGG16(weights = 'imagenet',
                           input_shape = (self.input_shape[0], 
                           self.input_shape[1], self.input_shape[2]), pooling = self.pooling, include_top = False)
        self.model.predict(np.zeros((1, 224, 224 , 3)))

    # def train(self):
    #     print('Adding Average Pooling Layer and Softmax Output Layer ...')
    #     output = self.model.get_layer(index=-1).output  # Shape: (8, 8, 2048)
    #     output = AveragePooling2D((8, 8), strides=(8, 8), name='avg_pool')(output)
    #     output = Flatten(name='flatten')(output)
    #     output = Dense(8, activation='relu', name='predictions')(output)
    #
    #
    #     InceptionV3_model = Model(self.model.input, output)
    #     # InceptionV3_model.summary()
    #
    #     optimizer = SGD(lr=learning_rate, momentum=0.9, decay=0.0, nesterov=True)
    #     InceptionV3_model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    #
    #     # autosave best Model
    #     best_model_file = "./NCFM/weights.h5"
    #     best_model = ModelCheckpoint(best_model_file, monitor='val_acc', verbose=1,
    #                                  save_best_only=True)  # verbose=1  会输出日志流
    #     # ModelCheckpoint详解  https://blog.csdn.net/zengNLP/article/details/94589469
    #
    #
    #     # this is the augmentation configuration we will use for training
    #     # 一些 data augmentation
    #     train_datagen = ImageDataGenerator(
    #         rescale=1. / 255,
    #         shear_range=0.1,
    #         zoom_range=0.1,
    #         rotation_range=10.,
    #         width_shift_range=0.1,
    #         height_shift_range=0.1,
    #         horizontal_flip=True)
    #
    #     # this is the augmentation configuration we will use for validation:
    #     # only rescaling
    #     val_datagen = ImageDataGenerator(rescale=1. / 255)
    #
    #     train_generator = train_datagen.flow_from_directory(
    #         train_data_dir,
    #         target_size=(img_width, img_height),
    #         batch_size=batch_size,
    #         shuffle=True,
    #         # save_to_dir = '/Users/Desktop/python/DeepLearning/Kaggle/NCFM/data/visualization',
    #         # save_prefix = 'aug',
    #         classes=FishNames,
    #         class_mode='categorical')
    #
    #     validation_generator = val_datagen.flow_from_directory(
    #         val_data_dir,
    #         target_size=(img_width, img_height),
    #         batch_size=batch_size,
    #         shuffle=True,
    #         # save_to_dir = '/Users/Desktop/python/DeepLearning/Kaggle/NCFM/data/visulization',
    #         # save_prefix = 'aug',
    #         classes=FishNames,
    #         class_mode='categorical')
    #
    #     InceptionV3_model.fit_generator(
    #         train_generator,
    #         samples_per_epoch=nbr_train_samples,
    #         nb_epoch=nbr_epochs,
    #         validation_data=validation_generator,
    #         nb_val_samples=nbr_validation_samples,
    #         callbacks=[best_model])

    # 获取最后一层卷积输出的特征
    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0]/LA.norm(feat[0])
        return norm_feat
