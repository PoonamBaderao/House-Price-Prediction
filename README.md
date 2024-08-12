# House Price Prediction Using Flask and Machine Learning

This project is a Flask-based web application that predicts house prices based on input features using a machine learning model. The model is trained using the Ames Housing dataset, and the application allows users to input house features to get a predicted sale price.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model](#model)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The goal of this project is to create a simple and intuitive web application that can predict the price of a house based on various features such as the number of bedrooms, bathrooms, square footage, and more. The project is implemented using Flask for the web application and a Linear Regression model for the price prediction.

## Features

- **Input Form:** A user-friendly form where users can input various house features.
- **Prediction:** The application uses a pre-trained machine learning model to predict house prices.
- **Real-Time Feedback:** The predicted house price is displayed in real-time after the user submits the form.

## Dataset

The model is trained on the Ames Housing dataset, which contains information on 2,930 houses in Ames, Iowa. The dataset includes 79 explanatory variables describing various aspects of residential homes.

## Model

A simple Linear Regression model is used for predicting the house prices. The model is trained using features such as `Overall Qual`, `Gr Liv Area`, `Garage Cars`, `Year Built`, and `Total Bsmt SF`.

## Setup Instructions

Follow these steps to set up and run the project on Replit:

1. **Clone the Repository:**
   - Clone the project repository from GitHub to your local machine or directly to Replit.

2. **Install Dependencies:**
   - Ensure that all necessary Python packages are installed. The main packages used are:
     - Flask
     - scikit-learn
     - pandas
     - numpy

   You can install these packages manually using:
   ```bash
   pip install Flask scikit-learn pandas numpy

3. **Run the Flask Application:**
   - Start the Flask application by running:
     ```bash
     python main.py
     ```
   - The application will be accessible in the Replit preview window.

## Usage

1. **Open the Application:**
   - Once the Flask server is running, open the web application in the Replit preview.

2. **Enter House Features:**
   - Use the form to input house features like the number of bedrooms, bathrooms, square footage, etc.

3. **Get Prediction:**
   - Submit the form to receive the predicted house price in U.S. dollars.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Please ensure that your contributions are well-documented and tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
