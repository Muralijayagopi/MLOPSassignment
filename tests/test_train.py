import os
from model import train

def test_model_file_exists():
    train  # trigger training if not already done
    assert os.path.exists('model/model.pkl')
