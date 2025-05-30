import pickle
from model.preprocessing import preprocess_input

# Load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_salary(experience):
    X = preprocess_input(experience)
    return model.predict(X)[0]
