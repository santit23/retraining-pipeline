from sklearn.metrics import accuracy_score
import joblib

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Model Accuracy: {acc:.4f}")
    return acc
