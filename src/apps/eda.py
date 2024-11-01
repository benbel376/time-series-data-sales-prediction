# src/eda.py
import seaborn as sns
import matplotlib.pyplot as plt

def plot_sales_distribution(df):
    sns.histplot(data=df, x='Sales')
    plt.title('Sales Distribution')
    plt.show()

def plot_sales_vs_customers(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['Sales'], y=df['Customers'])
    plt.title('Sales vs Customers')
    plt.show()
    
# Additional EDA functions can be added as needed
