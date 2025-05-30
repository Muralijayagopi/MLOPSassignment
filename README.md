# IT Employee Salary Predictor (Linear Regression)

## Overview
This app predicts IT employee salary based on years of experience using a linear regression model.

## Features
- Trained using synthetic data
- Flask-based web interface
- Dockerized for deployment
- GitHub Actions for CI/CD and retraining

## Endpoints
- `/` - form to submit experience
- `/predict` - returns predicted salary

## Running Locally
```bash
pip install -r requirements.txt
python model/train.py
python app/app.py
