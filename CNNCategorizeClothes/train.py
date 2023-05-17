import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

EPOCHS_NUM = 23

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'), 
    tf.keras.layers.Dense(10),
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=EPOCHS_NUM)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(EPOCHS_NUM,'epochs loss:',test_loss,' accuracy:', test_acc)

model.save("model_epoch23.h5")

# 10 epochs loss: 0.3272 accuracy: 0.8855000138282776 

# 15 epochs loss: 0.3964 - accuracy: 0.8626

# 20 epochs loss: 0.3568 - accuracy: 0.8881

# 21 epochs loss: 0.3542228639125824  accuracy: 0.8844000101089478

# 22 epochs loss: 0.38110747933387756  accuracy: 0.8863000273704529

# 23 epochs loss: 0.3592 - accuracy: 0.8891

# 25 epochs loss: 0.3859 - accuracy: 0.8878

# 30 epochs loss: 0.4059 - accuracy: 0.8846

# 40 epochs loss: 0.4811 - accuracy: 0.8875

# 50 epochs loss: 0.4941 - accuracy: 0.8916

# 100 epochs loss: 0.7976 - accuracy: 0.8858

# 150 epochs loss: 1.0965 - accuracy: 0.8800

# 200 epochs loss: 1.3522 - accuracy: 0.8833

# 250 epochs loss: 1.4642285108566284  accuracy: 0.8788999915122986

# 300 epochs loss: 1.547567367553711  accuracy: 0.8802000284194946






