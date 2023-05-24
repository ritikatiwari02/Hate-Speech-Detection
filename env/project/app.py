from flask import Flask, escape, request, render_template
import pickle
from sklearn.model_selection import train_test_split


model = pickle.load(open("./finalized_model.pkl",'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")




if __name__ == '__main__':
    app.run()