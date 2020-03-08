import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCmsBtI_-G5-LBGyQCLHSJx4VNofyNPE90",
    "authDomain": "mytest-19777.firebaseapp.com",
    "databaseURL": "https://mytest-19777.firebaseio.com",
    "projectId": "mytest-19777",
    "storageBucket": "mytest-19777.appspot.com",
    "messagingSenderId": "956995070498",
    "appId": "1:956995070498:web:659ab90e8c55cf6513387b",
    "measurementId": "G-HYS8L9CWBD"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


from flask import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def basic():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug = True)