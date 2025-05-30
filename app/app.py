from flask import Flask, request, render_template
from model.predict import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    experience = float(request.form['experience'])
    predicted_salary = predict(experience)
    return render_template('result.html', salary=round(predicted_salary, 2))

if __name__ == '__main__':
    app.run(debug=True)
