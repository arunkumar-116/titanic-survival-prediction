from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Parse user input from the form
    Pclass = int(request.form['Pclass'])
    Sex = request.form['Sex']
    Age = float(request.form['Age'])
    SibSp = int(request.form['SibSp'])
    Parch = int(request.form['Parch'])
    Embarked = request.form['Embarked']

    # Convert categorical variables to numeric values
    Sex = 0 if Sex == 'male' else 1
    Embarked = {'S': 0, 'C': 1, 'Q': 2}[Embarked]

    # Create a DataFrame from the user input
    user_data = pd.DataFrame([[Pclass, Sex, Age, SibSp, Parch, Embarked]],
                             columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked'])

    # Make a prediction
    prediction = model.predict(user_data)
    prediction_proba = model.predict_proba(user_data)

    # Determine the predicted survival status and probability
    result = 'Survived' if prediction[0] == 1 else 'Did not survive'
    probability = prediction_proba[0][1] * 100  # Assuming the positive class index is 1

    # Format the probability nicely
    probability = "{:.2f}%".format(probability)

    # Render the result template with the prediction
    return render_template('result.html', result=result, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
