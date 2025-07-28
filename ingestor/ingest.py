from io import StringIO
import pandas as pd
from db_writer_postgres import save_df_to_postgres
from config import S3_CONFIG

def extract_data(s3):
    response = s3.get_object(Bucket=S3_CONFIG['bucket'], Key=S3_CONFIG['key'])
    content = response['Body'].read().decode('latin1')
    df = pd.read_csv(StringIO(content), on_bad_lines='skip', engine='python')
    return df

def filter_relevant_columns(df):
    df_cleaned = df[
        [
            'Plant state abbreviation',
            'DOE/EIA ORIS plant or facility code',
            'Plant name',
            'Generator ID',
            'Generator annual net generation (MWh)']]
    return df_cleaned

def transform_data(df):
    df = filter_relevant_columns(df);

    # Rename columns for easier access
    df.columns = ["state", "plant_id", "plant_name", "genid", "net_generation_mwh"]

    # Convert net_generation_mwh to numeric, coercing errors to NaN
    df.loc[:, 'net_generation_mwh'] = pd.to_numeric(df['net_generation_mwh'], errors='coerce')

    # Drop rows where net_generation_mwh is NaN (invalid or missing data)
    df = df.dropna(subset=['net_generation_mwh'])

    # Optional: strip whitespace from string columns
    df['state'] = df['state'].str.strip()
    df['plant_name'] = df['plant_name'].str.strip()
    df['genid'] = df['genid'].str.strip()
    return df


def ingest_data(s3_client):
    df = extract_data(s3_client)
    df = transform_data(df)
    save_df_to_postgres(df);

