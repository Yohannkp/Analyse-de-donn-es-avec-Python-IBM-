import pandas as pd

def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)

def handle_missing_values(df):
    """Handle missing values in the DataFrame."""
    # Example: Fill missing values with the mean of the column
    return df.fillna(df.mean())

def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()

def format_data_types(df):
    """Format data types of the DataFrame."""
    # Example: Convert 'date' column to datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df

def clean_data(file_path):
    """Main function to clean the data."""
    df = load_data(file_path)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = format_data_types(df)
    return df

if __name__ == "__main__":
    # Example usage
    cleaned_data = clean_data('data/raw/example_data.csv')
    cleaned_data.to_csv('data/processed/cleaned_data.csv', index=False)