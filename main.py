from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

data = pd.read_csv('AmesHousing.csv')

# Select relevant features for the model
features = [
    'Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Year Built', 'Total Bsmt SF'
]
X = data[features]
y = data['SalePrice']

# Handle missing values by imputing them with the median
imputer = SimpleImputer(strategy='median')
X = imputer.fit_transform(X)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

app = Flask('app')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    form_data = [int(request.form.get(feature)) for feature in features]

    # Convert data to a numpy array and reshape for the model
    input_data = np.array(form_data).reshape(1, -1)

    # Predict using the model
    prediction = model.predict(input_data)[0]

    # Return the result
    return render_template('result.html', prediction=round(prediction, 2))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
