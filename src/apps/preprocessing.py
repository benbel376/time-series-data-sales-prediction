# src/preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(train_df, test_df):
    # Replace '0' with 0 in StateHoliday
    train_df['StateHoliday'].replace({'0': 0}, inplace=True)
    test_df['StateHoliday'].replace({'0': 0}, inplace=True)
    
    # Filter rows where store is open and sales is greater than zero
    train_df = train_df[train_df['Open'] == 1]
    
    # Convert date column to datetime
    train_df['Date'] = pd.to_datetime(train_df['Date'])
    test_df['Date'] = pd.to_datetime(test_df['Date'])
    
    # Extract year, month, and day
    for df in [train_df, test_df]:
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
    
    # Drop columns with mismatch in encoding
    train_df = pd.get_dummies(train_df, drop_first=False)
    test_df = pd.get_dummies(test_df)
    
    # Scale numerical columns
    num_cols = ['Store', 'DayOfWeek', 'Day', 'Month', 'Year']
    scaler = MinMaxScaler().fit(train_df[num_cols])
    train_df[num_cols] = scaler.transform(train_df[num_cols])
    test_df[num_cols] = scaler.transform(test_df[num_cols])
    
    return train_df, test_df
