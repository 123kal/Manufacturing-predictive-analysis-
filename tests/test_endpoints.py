import requests

# Base URL for your API (replace with actual URL)
API_URL = "http://localhost:8000"

def test_upload_endpoint():
  """
  Tests the /upload endpoint for successful data upload.
  """

  # Replace 'data.csv' with the actual file path of your test CSV data
  with open("data.csv", "rb") as file:
    data = file.read()
  files = {"file": (open("data.csv", "rb"), "data.csv")}
  response = requests.post(f"{API_URL}/upload", files=files)
  assert response.status_code == 200
  assert response.json() == {"message": "Data uploaded and model trained successfully!"}

def test_predict_endpoint():
  """
  Tests the /predict endpoint for successful prediction on valid data.
  """

  # Replace with a sample input dictionary containing your features
  data = {"Temperature": 100, "Run_Time": 60}
  response = requests.post(f"{API_URL}/predict", json=data)
  assert response.status_code == 200
  assert "prediction" in response.json()
  assert "confidence" in response.json()

def test_predict_endpoint_error():
  """
  Tests the /predict endpoint for error handling with invalid data.
  """

  # Replace with invalid data that might cause an error (e.g., missing feature)
  data = {"Run_Time": 60}  # Missing 'Temperature' feature
  response = requests.post(f"{API_URL}/predict", json=data)
  assert response.status_code == 400
  assert "error" in response.json()