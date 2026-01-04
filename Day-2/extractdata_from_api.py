import requests
import sqlite3
import pandas as pd
from datetime import datetime

# EXTRACT: Fetch data from an API
def extract_data():
    """Extract data from a public API"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    return data

# TRANSFORM: Clean and process data
def transform_data(data):
    """Clean and transform the data"""
    df = pd.DataFrame(data)
    # Remove unnecessary columns
    df = df[['userId', 'id', 'title', 'body']]
    # Remove duplicates
    df = df.drop_duplicates()
    # Rename columns
    df.columns = ['user_id', 'post_id', 'title', 'content']
    return df

# LOAD: Store data into database
def load_data(df, db_name='etl_database.db'):
    """Load data into SQLite database"""
    conn = sqlite3.connect(db_name)
    df.to_sql('posts', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data loaded successfully into {db_name}")

# Main ETL Pipeline
if __name__ == "__main__":
    print("Starting ETL Process...")
    print(f"Timestamp: {datetime.now()}")
    
    # Extract
    raw_data = extract_data()
    print(f"Extracted {len(raw_data)} records")
    
    # Transform
    clean_data = transform_data(raw_data)
    print(f"Transformed data shape: {clean_data.shape}")
    
    # Load
    load_data(clean_data)
    
    print("ETL Process Completed!")