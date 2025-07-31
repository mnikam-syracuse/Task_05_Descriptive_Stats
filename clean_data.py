import pandas as pd

# clean_data.py
# This script demonstrates how to clean and preprocess a dataset before analysis.
# IMPORTANT: Do not upload the dataset to GitHub as per professor's instructions.

def clean_dataset(input_path, output_path):
    """
    Load the dataset, clean it, and save the cleaned version.
    input_path: str - Path to raw dataset (CSV)
    output_path: str - Path to save cleaned dataset
    """
    # Load dataset
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print("Error: Input file not found. Please provide the correct path.")
        return

    # Example cleaning steps:
    # 1. Standardize column names
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

    # 2. Handle missing values (example: fill with 0 or drop rows)
    df = df.fillna(0)

    # 3. Ensure numeric columns are correctly typed
    numeric_cols = ['goals', 'assists', 'games']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 4. Remove duplicate rows if any
    df = df.drop_duplicates()

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    # Replace 'raw_data.csv' with your input dataset path
    # Replace 'cleaned_data.csv' with desired output path
    clean_dataset('raw_data.csv', 'cleaned_data.csv')
