from fastapi import FastAPI, UploadFile, File
import pandas as pd
from model_training import train_model  # Assuming model_training.py is in a subfolder

app = FastAPI()

@app.post("/upload/")
async def upload_data(file: UploadFile = File(...)):
    """
    API endpoint to upload a CSV file for training the model.
    """
    try:
        # Read data from uploaded CSV file
        data = pd.read_csv(file.file)

        # Call the train_model function to train the model
        model_metrics = train_model(data)

        # Prepare successful response with basic metrics
        response = {
            "message": "File uploaded and model trained successfully!",
            "model_metrics": model_metrics,
        }
        return response

    except Exception as e:
        # Handle any errors during upload or training
        return {"error": str(e)}