# src/data_loader.py
import pandas as pd

def load_data():
    # Load datasets
    store_df = pd.read_csv("data/store.csv")
    train_df = pd.read_csv("data/train.csv")
    test_df = pd.read_csv("data/test.csv")
    
    # Merge train and test with store data
    train_merged_df = train_df.merge(store_df, how='left', on='Store')
    test_merged_df = test_df.merge(store_df, how='left', on='Store')
    
    # Drop unnecessary column
    train_merged_df = train_merged_df.drop(['PromoInterval'], axis=1)
    
    return train_merged_df, test_merged_df
