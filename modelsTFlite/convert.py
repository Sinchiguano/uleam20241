

import tensorflow as tf
print(tf.__version__)

import keras
print(keras.__version__)

from keras.models import load_model

from tensorflow.keras.models import load_model

model=load_model("ResNet50.h5")


# converter=tf.lite.TFliteConverter.from_keras_model(model)


# converter.optimizations=[tf.lite.optimizations]

# lite_model=converter.convert()
# with open("lite_model.tflite","wb") as f:
#     f.write(lite_model)
