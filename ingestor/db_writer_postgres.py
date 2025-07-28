from sqlalchemy import create_engine
import os
from orm.PowerPlant import Base

# user = os.getenv("POSTGRES_USER")
# password = os.getenv("POSTGRES_PASSWORD")
# host = os.getenv("POSTGRES_HOST")
# port = os.getenv("POSTGRES_PORT", 5432)
# db = os.getenv("POSTGRES_DB")
#
# db_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"

def save_df_to_postgres(df, table_name="powerplant"):
    engine = create_engine("postgresql://aiq:aiq@postgres:5432/powergen")
    Base.metadata.create_all(engine)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

