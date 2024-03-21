from flask import Flask, request, jsonify,render_template
import numpy as np
import pickle

#creating flask app
flask_app = Flask(__name__)


# Load the pickle model
model = pickle.load(open("model.pkl","rb"))


@flask_app.route('/')
def home():
    return render_template("index.html")

@flask_app.route('/predict', methods=['POST'])

def predict():

    int_feature= [int(year) for year in request.form.values()]
    features = [np.array(int_feature)] #converting the feature to numpy array
    prediction = model.predict(features)

    return render_template("index.html", prediction_text = "The fee for this year is USD {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)