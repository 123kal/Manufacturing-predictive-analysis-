from fastapi import FastAPI
from app.routes import upload  # Import the app object from upload.py

app = upload.app  # Use the app object from upload.py

# Create FastAPI app instance (optional, but recommended for clarity)
# app = FastAPI(
#     title="Predictive Analysis API",
#     description="An API for predicting manufacturing defects using machine learning.",
#     version="1.0.0",
# )

# Include the prediction router (if you have one)
# app.include_router(routes.router) 

# Root endpoint (optional)
@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to the Predictive Manufacturing API!"}