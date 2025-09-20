import os
import time

def check_trigger():
    file_path = "data/training_data_new.csv" if os.path.exists("data/training_data_new.csv") else "data/training_data.csv"
    last_modified = os.path.getmtime(file_path)
    if (time.time() - last_modified) < 60:
        print("Trigger detected: new data available")
        return True
    return False
