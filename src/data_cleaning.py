# src/data_cleaning.py
import pandas as pd

def clean_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Perform basic data cleaning
    data = data.dropna()  # Drop rows with missing values
    data = data.drop(columns=['Column1', 'Column2'])  # Drop unnecessary columns (replace with actual columns)

    return data

def save_cleaned_data(data, output_path):
    # Save the cleaned data to a new CSV file
    data.to_csv(output_path, index=False)


