# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from sklearn.tree import DecisionTreeClassifier
# import pandas as pd

# app = Flask(__name__)
# CORS(app)

# data = pd.read_csv("health_data.csv")

# X = data[['HeartRate', 'Oxygen', 'Movement']]
# y = data['Status']

# model = DecisionTreeClassifier()
# model.fit(X, y)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json

#     heart_rate = data['heartRate']
#     oxygen = data['oxygen']
#     movement = data['movement']

#     prediction = model.predict([[heart_rate, oxygen, movement]])

#     return jsonify({
#         "status": prediction[0]
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
import os

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/dashboard')
def dashboard():
    return app.send_static_file('dashboard.html')

@app.route('/map')
def map_page():
    return app.send_static_file('map.html')

if __name__ == '__main__':
    app.run(debug=True)