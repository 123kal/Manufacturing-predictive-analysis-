# Manufacturing-predictive-analysis-
This API provides an endpoint for uploading a manufacturing dataset, training a machine learning model (Random Forest Classifier) on the data, and returning model metrics.

1. Prerequisites

Python: Ensure you have Python installed on your system.
Virtual Environment (Recommended): Create and activate a virtual environment to isolate project dependencies:

python -m venv venv  # Create a virtual environment named 'venv'
source venv/bin/activate  # Activate the virtual environment (on macOS/Linux)
.\venv\Scripts\activate  # Activate the virtual environment (on Windows)

Install Dependencies: Install required packages within the activated environment:
pip install fastapi uvicorn pandas scikit-learn

To check Model Accuracy and F-1 Score:
python app\model\model_traning.py

2. . Project Setup:

Clone or download this repository.
Navigate to the project directory in your terminal.

3. Run the API:

Start the FastAPI server:
uvicorn main:app --host 0.0.0.0 --port 8000

4. API Endpoint:

/upload/ (POST):
Request:
Content-Type: multipart/form-data
file: CSV file containing manufacturing data (see data schema below)

Response:
On success:
{
    "message": "File uploaded and model trained successfully!",
    "model_metrics": {
        "accuracy": 0.95, 
        "f1_score": 0.94 
    }
}

On failure:
{
    "error": "Error message describing the issue" 
}

README.md
Predictive Manufacturing API

This API provides an endpoint for uploading a manufacturing dataset, training a machine learning model (Random Forest Classifier) on the data, and returning model metrics.

1. Prerequisites

Python: Ensure you have Python installed on your system.
Virtual Environment (Recommended): Create and activate a virtual environment to isolate project dependencies:
Bash

python -m venv venv  # Create a virtual environment named 'venv'
source venv/bin/activate  # Activate the virtual environment (on macOS/Linux)
.\venv\Scripts\activate  # Activate the virtual environment (on Windows)
Install Dependencies: Install required packages within the activated environment:
Bash

pip install fastapi uvicorn pandas scikit-learn
2. Project Setup:

Clone or download this repository.
Navigate to the project directory in your terminal.
3. Run the API:

Start the FastAPI server:
Bash

uvicorn main:app --host 0.0.0.0 --port 8000
4. API Endpoint:

/upload/ (POST):
Request:
Content-Type: multipart/form-data
file: CSV file containing manufacturing data

Response:
On success:
{
    "message": "File uploaded and model trained successfully!",
    "model_metrics": {
        "accuracy": 0.95, 
        "f1_score": 0.94 
    }
}

On failure:

{
    "error": "Error message describing the issue" 
}




