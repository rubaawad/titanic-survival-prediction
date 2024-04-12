## End to End Machine Learning Ptorject
## Prediction model for Titanic dataset
Getting Started
Installation
To run this project locally, follow these steps:

# Clone the repository:
git clone https://github.com/your_username/titanic-survival-prediction.git

# Navigate to the project directory:
cd titanic-survival-prediction

# Install the required dependencies:
pip install -r requirements.txt

Usage
    1. Run the Flask application:
    python app.py

    2. Open your web browser and go to http://localhost:5000 to access the application.

    3. Enter the passenger details (age, sex, class, embarked) and click "Predict" to see the predicted survival status.

# Model Deployment
The trained logistic regression model is deployed as a web service using Flask. The model is loaded along with the scaler, and predictions are made based on user input.

# Credits
Dataset: Kaggle Titanic Dataset
Inspiration: This project was inspired by the Titanic survival prediction challenge on Kaggle.