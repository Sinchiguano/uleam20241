import tensorflow as tf
import numpy as np
from tensorflow import keras 




print(tf.__version__)


# model=tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# model.compile(optimizer='sgd',loss='mean_squared_error')

# xs=np.array([-1.0,0.0,1.0,2.0,3.0,4.0],dtype=float)
# ys=np.array([-3.0,-1.0,1.0,3.0,5.0,7.0],dtype=float)

# model.fit(xs,ys,epochs=500)

# tmp=np.array([10.0])
# print(model.predict(tmp))
print('ok!!!!!!')




fashion_mnist=tf.keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()





import numpy as np
import matplotlib.pyplot as plt


index=42


#set number of characters per row when printing
np.set_printoptions(linewidth=320)


print(f"LABEL: {train_labels[index]}")
print(f"\n IMAGE PIXEL ARRAY: \n{train_images[index]}")

#VISULIZE THE IMAGE
# plt.imshow(train_images[index], cmap="Greys")
plt.imshow(train_images[index])
plt.show()

#NORMALIZE THE PIXEL VALUES OF THE TRAIN AND TEST IMAGES

train_images=train_images/255
test_images=test_images/255



# BUILD THE CLASSIFICATION MODEL
model=tf.keras.models.Sequential([tf.keras.llayers.Flatten()])













print('ok!!!!!!')
