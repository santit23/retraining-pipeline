import pandas as pd
from sklearn.datasets import make_classification
import os

def generate_dataset(file_path="data/training_data.csv", n_samples=500):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=5,        # 5 input features
        n_informative=3,
        n_redundant=0,
        random_state=42
    )
    
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(1, 6)])
    df["target"] = y
    
    os.makedirs("data", exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"Dummy dataset generated at {file_path}")

if __name__ == "__main__":
    generate_dataset()
