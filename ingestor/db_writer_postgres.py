from sqlalchemy import create_engine
import os
from orm.PowerPlant import Base

def save_df_to_postgres(engine, df, table_name="powerplant"):
    Base.metadata.create_all(engine)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

