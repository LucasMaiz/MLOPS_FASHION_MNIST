from tensorflow import keras
from model import *
import numpy as np


def predict_result(data):
    predicts_proba = fashion_mnist_model.predict(data)
    accuracy = np.max(predicts_proba)*100
    prediction_index = np.argmax(predicts_proba)
    return {"accuracy": round(accuracy,2), "cloth" : class_names[prediction_index]}
    

def parse_query(pixels):
    return (np.array([np.fromstring(pixels.replace("[", "").replace("]", "").replace(" ", ""), sep=";").reshape(28,28)]))/255