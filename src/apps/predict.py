# src/predict.py
import pandas as pd

def make_predictions(model, test_inputs):
    predictions = model.predict(test_inputs)
    submission_df = pd.read_csv('data/sample_submission.csv')
    submission_df['Sales'] = predictions
    submission_df.to_csv('submission.csv', index=False)
    print("Predictions saved to submission.csv")
