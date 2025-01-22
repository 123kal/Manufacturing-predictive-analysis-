from fastapi import APIRouter, Body, UploadFile, File, JSONResponse
from app import model

router = APIRouter()

@router.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    """
    Uploads a CSV file containing manufacturing data and trains the model.

    Parameters:
        file (UploadFile): The uploaded CSV file.

    Returns:
        JSONResponse: A JSON response indicating successful data upload and model training.
    """

    # Read the uploaded CSV file and preprocess the data
    data = await file.read()
    df = pd.read_csv(data)  # Assuming CSV data
    X = model.preprocess_data(df)

    # Train the model on the preprocessed data
    model.train_model(X)

    return JSONResponse({"message": "Data uploaded and model trained successfully!"})

@router.post("/predict")
async def predict(data: dict = Body(...)):
    """
    Makes a prediction on the provided data using the trained model.

    Parameters:
        data (dict): A dictionary containing the input features for prediction.

    Returns:
        JSONResponse: A JSON response with the predicted outcome and confidence score.
    """

    try:
        # Prepare the input data for the model
        X = model.preprocess_data(data)

        # Make a prediction using the trained model
        prediction = model.predict(X)
        confidence = model.predict_proba(X)[0][prediction]  # Assuming predict_proba for confidence

        # Return the prediction and confidence score in JSON format
        return JSONResponse({"prediction": prediction, "confidence": confidence})

    except Exception as e:
        # Handle errors gracefully
        return JSONResponse({"error": str(e)}, status_code=400)