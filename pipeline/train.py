from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_model(X_train, y_train, save_path="models/model.pkl"):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, save_path)
    return model
