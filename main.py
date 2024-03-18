import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the trained model and data
rf_regressor = joblib.load('random_forest_model_new_python_pp2.joblib')
data = pd.read_csv('datasetlast.csv')

# Create a Flask web app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input values from the form
        user_month = int(request.form['month'])
        user_day_type = request.form['day_type']
        user_cost = int(request.form['promotion_cost'])

        # Create a DataFrame with the user input
        user_input = pd.DataFrame({
            "Month": [user_month],
            "Day_Type_poyaday": 0,
            "Day_Type_public": 0,
            "Day_Type_weekday": 0,
            "Day_Type_weekend": 0,
            "Total_Promotional_Cost": [user_cost]  # Include the promotion cost in the DataFrame
        })

        # Set the selected day type to 1
        user_input["Day_Type_" + user_day_type] = 1

        # Make a prediction using the trained model
        predicted_attendees = rf_regressor.predict(user_input)

        # Return the prediction as JSON
        return jsonify({"prediction": predicted_attendees[0]})

if __name__ == '__main__':
    app.run(debug=True)
