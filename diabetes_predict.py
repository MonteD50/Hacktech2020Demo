import pickle
from sklearn.neural_network import MLPClassifier
import numpy as np

def predict_diabeties(data=[5, 147, 75, 34, 0,34, 0.6, 52]): 
    """
    input a one dimensional 8 elemnt array. These are the class in this specific order: 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'
    """
    data = np.array(data).reshape(1, -1)
    model = pickle.load(open("diabetes.p", "rb"))
    accuracy = 0.797
    prediction = model.predict(data)
    return prediction, accuracy