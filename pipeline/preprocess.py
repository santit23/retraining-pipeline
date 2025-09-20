import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split(data_path="data/training_data.csv"):
    df = pd.read_csv(data_path)
    X = df.drop("target", axis=1)
    y = df["target"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
