#from train import test_labels
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import PIL.ImageOps 

def testing():
    path1 = '/Users/mulunur/Documents/univer/diploma/narniaAppBackDjango/CNNCategorizeClothes/photo_top-PhotoRoom_rmbg_invert.png'
    path ='/Users/mulunur/Documents/univer/diploma/narniaAppBackDjango/CNNCategorizeClothes/png-transparent-t-shirt-sleeve-crop-top-hoodie-crop-tops-tshirt-fashion-aesthetics.png'
    img = Image.open(path).convert('L').resize((28, 28), Image.ANTIALIAS)
    inverted_img = PIL.ImageOps.invert(img)
    img = inverted_img
    img.save("result_reducing.jpg")
    #img = Image.open(path)
    img = np.array(img)
    print(img.shape)

    img = (np.expand_dims(img,0))

    print(img.shape)

    model = tf.keras.models.load_model(os.getcwd()+'/model.h5')
    #probability_model = tf.keras.models.load_model(os.getcwd()+'/probability_model.h5')

    probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
    predictions_single = probability_model.predict(img)

    print(predictions_single)
    # def plot_value_array(i, predictions_array, true_label):
    #   true_label = true_label[i]
    #   plt.grid(False)
    #   plt.xticks(range(10))
    #   plt.yticks([])
    #   thisplot = plt.bar(range(10), predictions_array, color="#777777")
    #   plt.ylim([0, 1])
    #   predicted_label = np.argmax(predictions_array)

    #   thisplot[predicted_label].set_color('red')
    #   thisplot[true_label].set_color('blue')

    # plot_value_array(1, predictions_single[0], test_labels)
    # _ = plt.xticks(range(10), class_names, rotation=45)
    # plt.show()

    print(np.argmax(predictions_single[0]))
    print(class_names[np.argmax(predictions_single[0])])
    



class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']



fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


def predictImage(image):
    #img = Image.open(path).convert('L').resize((28, 28), Image.ANTIALIAS)

    img = image.convert('L').resize((28, 28), Image.ANTIALIAS)
    inverted_img = PIL.ImageOps.invert(img)
    img = inverted_img
    
    #img = Image.open(path)
    #img = np.array(np.squeeze(np.array(img[:,:,None])))
    img = np.array(img)
    img = img / 255.0
    print(img.shape)

    img = (np.expand_dims(img,0))

    print(img.shape)
    
    # plt.figure()
    # plt.imshow(img)
    # plt.colorbar()
    # plt.grid(False)
    # plt.show()
    
    model = tf.keras.models.load_model(os.getcwd()+'/model_epoch23.h5')

    probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
    
    predictions_single = probability_model.predict(img)

    result=class_names[np.argmax(predictions_single[0])]
    
    print(result)
    return result






