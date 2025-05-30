import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from preprocessing import preprocess_data

# Load and preprocess data
df = pd.read_csv('data/sample_data.csv')
df = preprocess_data(df)

X = df[['YearsExperience']]
y = df['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
