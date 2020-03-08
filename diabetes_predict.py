import pickle
from sklearn.neural_network import MLPClassifier

user_data = [[5, 147, 75, 34, 0, 0.6, 52]]
model = pickle.load(open("diabetes.p", "rb"))
model.predict(user_data)
