from flask import Flask, render_template, request
from model import predict_survival
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    prediction = predict_survival(data)
    return render_template('result.html', prediction=prediction)
if __name__ == '__main__':
    app.run(debug=True)