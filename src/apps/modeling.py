# src/modeling.py
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def get_model(model_name):
    if model_name == 'linear_regression':
        return LinearRegression()
    elif model_name == 'decision_tree':
        return DecisionTreeRegressor(random_state=42)
    elif model_name == 'random_forest':
        return RandomForestRegressor(random_state=42, n_jobs=-1)
    elif model_name == 'xgboost':
        return XGBRegressor(random_state=42)
    else:
        raise ValueError("Unknown model name")

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model
