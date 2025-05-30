import app.app as app_module
from flask.testing import FlaskClient

def test_flask_prediction():
    app = app_module.app
    client: FlaskClient = app.test_client()
    response = client.post('/predict', data={'experience': '5'})
    assert response.status_code == 200
    assert b'Predicted Salary' in response.data
