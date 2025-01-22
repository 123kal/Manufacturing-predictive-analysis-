import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import pickle

# Load the dataset
data = pd.read_csv("data/manufacturing_defect_dataset.csv")

# Print the column names to verify
print(data.columns)

# Preprocess the data
X = data[["ProductionVolume", "ProductionCost", "SupplierQuality", "DeliveryDelay", "DefectRate",
          "QualityScore", "MaintenanceHours", "DowntimePercentage", "InventoryTurnover",
          "StockoutRate", "WorkerProductivity", "SafetyIncidents",
          "EnergyConsumption", "EnergyEfficiency", "AdditiveProcessTime",
          "AdditiveMaterialCost"]]
y = data["DefectStatus"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1:.2f}")

# Save the model
with open("app/model/model.pkl", "wb") as file:
  pickle.dump(model, file)