from io import StringIO
import pandas as pd
from config import S3_BUCKET
from db_writer_postgres import save_df_to_postgres


def list_csv_files_from_s3(bucket_name, s3_client):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = []
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith('.csv'):
            files.append(key)
    return files

def get_already_uploaded_files(raw_connection):
    with raw_connection.cursor() as cur:
        cur.execute("SELECT filename FROM uploaded_files")
        rows = cur.fetchall()
    return set(row[0] for row in rows)

def mark_file_uploaded(raw_connection, filename):
    with raw_connection.cursor() as cur:
        cur.execute("INSERT INTO uploaded_files (filename) VALUES (%s) ON CONFLICT DO NOTHING",
                    (filename,))
    raw_connection.commit()

def ingest_data(bucket_name, filename, s3_client, raw_connection):
    response = s3_client.get_object(Bucket=bucket_name, Key=filename)
    content = response['Body'].read().decode('latin1')
    df = pd.read_csv(StringIO(content), on_bad_lines='skip', engine='python')
    mark_file_uploaded(raw_connection, filename)
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

def ingest(s3_client, engine):

    raw_connection = engine.raw_connection();
    uploaded_files = get_already_uploaded_files(raw_connection)
    csv_files = list_csv_files_from_s3(S3_BUCKET, s3_client)
    print(csv_files)

    for file in csv_files:
        if file not in uploaded_files:
            print(f"Ingesting new file: {file}")
            df = ingest_data(S3_BUCKET, file, s3_client, raw_connection)
            df = transform_data(df)
            save_df_to_postgres(engine, df);
        else:
            print(f"File already ingested: {file}")
