import pickle
from sklearn.neural_network import MLPClassifier

user_data = 
model = pickle.load(open("diabetes.p", "rb"))
model.predict(user_data)
