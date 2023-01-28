from functions import *

fashion_mnist_model = keras.models.load_model("models/my_h5_model.h5")

class_names = ["T-shirt/top",
              "Trouser",
              "Pullover",
              "Dress",
              "Coat",
              "Sandal",
              "Shirt",
              "Sneaker",
              "Bag",
              "Ankle boot"]