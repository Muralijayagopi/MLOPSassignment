import pickle
import numpy as np

# Load the model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(experience: float) -> float:
    experience_array = np.array([[experience]])
    prediction = model.predict(experience_array)
    return prediction[0]

