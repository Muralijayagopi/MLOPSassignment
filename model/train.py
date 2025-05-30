import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

from model.preprocessing import preprocess_data  # if used

# Load and preprocess data
df = pd.read_csv('data/sample_data.csv')
X = df[['YearsExperience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

# Ensure the model directory exists
os.makedirs('model', exist_ok=True)

# Save the trained model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

