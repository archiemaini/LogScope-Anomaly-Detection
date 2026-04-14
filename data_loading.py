import pandas as pd

def load_data(file_path):
    """
    Load log data from a CSV file.
    Expects a column named 'log' containing the text messages.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} logs from {file_path}")
        if 'log' not in df.columns:
            if 'Content' in df.columns:
                df.rename(columns={'Content': 'log'}, inplace=True)
            else:
                raise ValueError("The dataset must contain a 'log' or 'Content' column.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
