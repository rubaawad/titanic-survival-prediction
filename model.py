import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
# Load the trained model
model = joblib.load('lr_model.pkl')
# Load the scaler
scaler = joblib.load('scaler.pkl')
def preprocess_input(data):
    # Preprocess the input data (similar to the preprocessing steps before training)
    sex = 0 if data['Sex'] == 'male' else 1
    embarked = {'C': 0, 'Q': 1, 'S': 2}.get(data['Embarked'], 2)
    
    # Define the order of features
    features = [
        data['Pclass'],
        sex,
        data['Age'],
        data['SibSp'],
        data['Parch'],
        data['Fare'],
        embarked
    ]
    
    # Convert features to DataFrame
    features_df = pd.DataFrame([features], columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'])
    
    # Scale the features using the same scaler used during training
    scaled_features = scaler.transform(features_df)
    return scaled_features
def predict_survival(data):
    scaled_features = preprocess_input(data)
    prediction = model.predict(scaled_features)
    return prediction[0]