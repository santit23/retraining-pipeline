# Automated Model Retraining Pipeline

This repository demonstrates a **self-contained automated retraining pipeline** for a machine learning model. The pipeline detects triggers (new data), retrains the model, evaluates it, and promotes it to production if performance thresholds are met. A dummy dataset is included to simulate real-world usage.

---

## **Project Structure**

retraining_pipeline/
├── data/                          # Dummy datasets
│   ├── training_data.csv          # Initial training dataset
│   └── training_data_new.csv      # Simulates new data arrival
│
├── models/                        # Trained models storage
│   ├── model.pkl                  # Current model version
│   └── model_prod.pkl             # Production model
│
├── logs/                          # Retraining logs and metrics
│   ├── training_logs/             # Training execution logs
│   └── performance_metrics/       # Model performance history
│
├── pipeline/                      # Modular pipeline components
│   ├── preprocess.py              # Data loading, cleaning, and splitting
│   ├── train.py                   # Model training and hyperparameter tuning
│   ├── evaluate.py                # Model evaluation and metrics calculation
│   └── utils.py                   # Trigger detection and helper functions
│
├── generate_data.py               # Script to generate dummy dataset
├── main.py                        # Orchestrates the retraining pipeline
├── requirements.txt               # Python dependencies
│
└── .github/workflows/             # GitHub Actions CI/CD workflows
    └── retrain.yaml               # Automated retraining workflow

---

## **Workflow Overview**

1. **Trigger Detection**  
   - Checks if new data is available (simulated via `training_data_new.csv` or modification time of `training_data.csv`).

2. **Data Loading & Preprocessing**  
   - Loads CSV data.
   - Splits it into training and test sets.

3. **Model Training**  
   - Trains a **Logistic Regression** model on the dataset.
   - Saves the trained model to `models/model.pkl`.

4. **Evaluation & Promotion**  
   - Evaluates accuracy on the test set.
   - If accuracy ≥ threshold (default 0.8), promotes the model to production (`models/model_prod.pkl`).

5. **Logging & Notifications**  
   - Prints clear steps to the console.
   - Appends retraining logs to `logs/retrain_log.txt`.

6. **Optional CI/CD Automation**  
   - GitHub Actions workflow triggers retraining on:
     - Schedule (e.g., every hour)
     - Data file changes (`data/training_data.csv`)

---

## **How to Run the Pipeline**

### **Step 1: Install Dependencies**

```bash
pip install -r requirements.txt 
```

### **Step 2: Generate Dummy Data ***
```bash
python generate_data.py
```

### **Step 3: Run Retraining Pipeline

```bash
python main.py
```





