import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("health_data.csv")

X = data[['HeartRate', 'Oxygen', 'Movement']]
y = data['Status']

model = DecisionTreeClassifier()

model.fit(X, y)


def predict_risk(heart_rate, oxygen, movement):
    prediction = model.predict([[heart_rate, oxygen, movement]])
    return prediction[0]