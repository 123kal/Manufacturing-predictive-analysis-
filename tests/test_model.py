import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Load the testing dataset (replace with your actual data path)
data = pd.read_csv("data/testing_data.csv")

# Preprocess the data (assuming same preprocessing steps as in model_training.py)
X = data[["Temperature", "Run_Time"]]
y = data["Downtime_Flag"]

# Split the data into training and testing sets (not required for testing, but shown for clarity)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model (replace with your model loading logic)
# Assuming the model is saved as 'model.pkl' in 'app/model' directory
import pickle
with open("app/model/model.pkl", "rb") as file:
    model = pickle.load(file)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Model Accuracy on Testing Set: {accuracy:.2f}")
print(f"F1 Score on Testing Set: {f1:.2f}")