# main.py
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import plot_sales_distribution, plot_sales_vs_customers
from src.feature_engineering import add_features
from src.modeling import get_model, train_model
from src.evaluation import evaluate_model
from src.predict import make_predictions

def main():
    # Load data
    train_df, test_df = load_data()
    
    # Preprocess data
    train_df, test_df = preprocess_data(train_df, test_df)
    
    # EDA
    plot_sales_distribution(train_df)
    plot_sales_vs_customers(train_df)
    
    # Feature Engineering
    train_df = add_features(train_df)
    test_df = add_features(test_df)
    
    # Split data
    input_cols = ['Store', 'DayOfWeek', 'Promo', 'StateHoliday', 'StoreType', 'Assortment', 'Promo2', 'Day', 'Month', 'Year']
    X_train = train_df[input_cols]
    y_train = train_df['Sales']
    X_val = test_df[input_cols]
    
    # Train and evaluate model
    model = get_model('random_forest')
    model = train_model(model, X_train, y_train)
    train_rmse, val_rmse, train_rmspe, val_rmspe = evaluate_model(model, X_train, y_train, X_val, y_val)
    
    print(f"Train RMSE: {train_rmse}, Val RMSE: {val_rmse}")
    print(f"Train RMSPE: {train_rmspe}, Val RMSPE: {val_rmspe}")
    
    # Prediction
    make_predictions(model, X_val)

if __name__ == "__main__":
    main()
