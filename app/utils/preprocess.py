import pandas as pd
from sklearn.impute import SimpleImputer

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
  """
  Preprocesses the input data for model training or prediction.

  Args:
      data (pd.DataFrame): The input data as a pandas DataFrame.

  Returns:
      pd.DataFrame: The preprocessed data as a pandas DataFrame.
  """

  # Handle missing values (replace with most frequent value by default)
  imputer = SimpleImputer(strategy="most_frequent")
  df = imputer.fit_transform(data)

  # Handle categorical features (convert to numerical using one-hot encoding)
  categorical_features = [col for col in df.columns if df[col].dtype == object]
  df = pd.get_dummies(df, columns=categorical_features, drop_first=True)

  # Handle other preprocessing steps as needed (scaling, normalization, etc.)
  # ...

  return df