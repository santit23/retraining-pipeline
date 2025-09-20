from pipeline.preprocess import load_and_split
from pipeline.train import train_model
from pipeline.evaluate import evaluate_model
from pipeline.utils import check_trigger
import joblib

if __name__ == "__main__":
    if check_trigger():
        X_train, X_test, y_train, y_test = load_and_split()
        model = train_model(X_train, y_train)
        acc = evaluate_model(model, X_test, y_test)

        if acc > 0.8:  # simple threshold condition
            joblib.dump(model, "models/model_prod.pkl")
            print("New model promoted to production")
        else:
            print("Model not promoted, accuracy below threshold")
    else:
        print("No trigger, skipping retrain")
