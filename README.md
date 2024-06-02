# Titanic Survival Prediction

## Project Overview

This project aims to build a machine learning model to predict whether a passenger on the Titanic survived or not, using the Titanic dataset. The dataset provides a variety of features such as age, gender, ticket class, fare, and cabin information.

## Dataset

The dataset contains the following key information about individual passengers:

- PassengerId: Unique identifier for each passenger.
- Survived: Survival status (0 = No, 1 = Yes).
- Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
- Name: Name of the passenger.
- Sex: Gender of the passenger.
- Age: Age of the passenger.
- SibSp: Number of siblings or spouses aboard the Titanic.
- Parch: Number of parents or children aboard the Titanic.
- Ticket: Ticket number.
- Fare: Passenger fare.
- Cabin: Cabin number.
- Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

## Project Structure

- `titanic_survival_prediction.py`: The main Python file containing the code for loading the dataset, preprocessing, model building, training, and evaluation.

## Methodology

### Data Preprocessing:

- Handling missing values.
- Encoding categorical variables.
- Feature scaling.

### Exploratory Data Analysis (EDA):

- Visualizing the distribution of features.
- Understanding the relationship between features and the target variable (Survived).

### Model Building:

- Splitting the data into training and testing sets.
- Training various machine learning models (e.g., Logistic Regression, Decision Trees, Random Forests).
- Evaluating model performance using metrics like accuracy, precision, recall, and F1 score.

## Results

The model's performance will be evaluated based on the accuracy and other relevant metrics obtained from the test dataset.

## Conclusion

This project demonstrates the process of building a machine learning model to predict survival on the Titanic using a variety of features. It covers data preprocessing, exploratory data analysis, model training, and evaluation.

## Usage

- Install the required dependencies listed in `requirements.txt`.
- Run the Flask application using `web: gunicorn --bind :$PORT app:app`.

## Web Application

The project includes a web application for predicting survival chances on the Titanic. Users can input their details and get a prediction. Check out the HTML files and Flask app for implementation details.

## Acknowledgments

Special thanks to the Titanic dataset creators and the open-source community for their contributions.

