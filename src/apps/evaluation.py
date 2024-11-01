# src/evaluation.py
import numpy as np
from sklearn.metrics import mean_squared_error

def rmspe(y_true, y_pred):
    percentage_error = (y_true - y_pred) / y_true
    percentage_error[y_true == 0] = 0
    return np.sqrt(np.mean(percentage_error ** 2))

def evaluate_model(model, X_train, y_train, X_val, y_val):
    train_preds = model.predict(X_train)
    val_preds = model.predict(X_val)
    
    train_rmse = mean_squared_error(y_train, train_preds, squared=False)
    val_rmse = mean_squared_error(y_val, val_preds, squared=False)
    
    train_rmspe = rmspe(y_train, train_preds)
    val_rmspe = rmspe(y_val, val_preds)
    
    return train_rmse, val_rmse, train_rmspe, val_rmspe
