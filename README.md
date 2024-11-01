# Rossmann Pharmaceuticals Sales Forecasting

## Live Demo

- [Streamlit Application](https://rossman-sales-biniyam.herokuapp.com/)

---

## Table of Contents

- [Overview](#overview)
- [Objective](#objective)
- [Requirements](#requirements)
- [Installation](#installation)
- [Data](#data)
  - [Data Fields](#data-fields)
- [Features](#features)
  - [Folder Structure](#folder-structure)
  - [Data Processing and Analysis](#data-processing-and-analysis)
- [Scripts](#scripts)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

Rossmann Pharmaceuticals operates multiple stores across several cities. The finance team needs a reliable, data-driven approach to forecast sales for the next six weeks. Until now, managers have relied on their experience and intuition to make sales predictions, but this model provides a more systematic and scalable solution.

This project builds an end-to-end forecasting product, from data processing and feature engineering to model building, deployment, and visualization. The final model can be served directly to analysts in the finance team for improved accuracy and efficiency.

## Objective

To develop and deploy a predictive analytics solution that delivers sales forecasts to the finance team.

---

## Requirements

- Python 3.7 or higher
- Libraries: `mlflow`, `dvc`, `scikit-learn`, `matplotlib`, `seaborn`, `pandas`, `numpy`, `xgboost`, and `streamlit` for deployment.

---

## Installation

To get started, clone the repository and install the required packages:

  ```bash
    git clone https://github.com/benbel376/rossman_predictive_analysis.git
    cd rossman_predictive_analysis
    pip install -r requirements.txt
  ```


## Data:
  **description:** "The dataset can be downloaded from Kaggle: Rossmann Store Sales. This data includes historical sales information, promotions, holidays, and store attributes that impact sales performance."
  fields:
    - Store: "Unique ID for each store"
    - Sales: "Sales revenue for each day (target variable)"
    - Customers: "Number of customers for each day"
    - Open: "Indicator if the store was open (1) or closed (0)"
    - StateHoliday: "State holiday indicator (a: public, b: Easter, c: Christmas, 0: None)"
    - SchoolHoliday: "Indicator if the store was affected by school holidays"
    - StoreType: "Type of store (a, b, c, d)"
    - Assortment: "Level of product assortment (a: basic, b: extra, c: extended)"
    - CompetitionDistance: "Distance to nearest competitor store"
    - CompetitionOpenSince: "Month and year the nearest competitor opened"
    - Promo: "Whether a store was running a promotion"
    - Promo2: "Continuous and periodic promotion (0: not participating, 1: participating)"
    - Promo2Since: "Year and calendar week when Promo2 started"
    - PromoInterval: "Months when Promo2 promotions start (e.g., 'Feb,May,Aug,Nov')"

## Features:
  **Folder_Structure:**
    description: "The project is organized as follows:"
    structure:
      - .dvc/: "Data version control configuration"
      - .github/: "GitHub workflows and CI/CD configurations"
      - notebooks/: "Jupyter notebooks for exploratory data analysis"
      - src/: "Main source code for the project"
      - src/apps:
          - __init__.py: "Package initialization"
          - data_loader.py: "Loads and preprocesses sales data"
          - eda.py: "Exploratory data analysis scripts"
          - feature_engineering.py: "Feature engineering for model improvement"
          - modeling.py: "Model training and hyperparameter tuning"
          - predict.py: "Script for making predictions on new data"
          - evaluation.py: "Evaluation metrics and model assessment"
          - preprocessing.py: "Data cleaning and encoding"
          - main.py: "Main pipeline to execute end-to-end workflow"
      - src/infra:
          - Dockerfile: "Dockerfile for containerizing the application"
          - docker-compose.yml: "Multi-container setup for deployment"
          - nginx/nginx.conf: "NGINX configuration for reverse proxy"
          - setup_infrastructure.sh: "Script to install Docker and Docker Compose"
          - deploy.sh: "Deployment script"
      - README.md: "Project documentation"

## Data_Processing_and_Analysis:
  description: "Data processing and analysis include steps like data cleaning, handling missing values, encoding categorical variables, and scaling numeric values."
  steps:
    - Exploratory_Data_Analysis: "Analyze sales trends, seasonal patterns, and key drivers of sales using eda.py."
    - Feature_Engineering: "Enhance the dataset with engineered features (e.g., year, month, competition distance) using feature_engineering.py."
    - Model_Selection: "Train models like Linear Regression, Decision Trees, Random Forest, and XGBoost using modeling.py."

## Scripts:
  description: "All the scripts for data loading, preprocessing, model training, and evaluation are located within the src/apps directory. Each script is modular and can be run independently or as part of the main pipeline in main.py."

## Testing:
  description: "Tests for the scripts are located in the tests folder and ensure the reliability of each component."
  tests_include: 
    - "Data integrity checks"
    - "Model accuracy validation"
    - "Feature engineering correctness"

## Future_Improvements:
  - Model_Optimization: "Experiment with deep learning models for improved accuracy."
  - Additional_Data_Sources: "Integrate external data like weather or economic indicators."
  - Parameter_Tuning: "Use advanced methods like Bayesian optimization for hyperparameter tuning."

## License:
  description: "This project is licensed under the MIT License - see the LICENSE file for details."

## Summary:
  description: "With this README, users can get a comprehensive view of the project, from installation and data structure to features and deployment."
