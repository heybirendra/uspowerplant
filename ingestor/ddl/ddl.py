from sqlalchemy import text

def create_powerplan_table(engine):
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS powerplant (
        id serial primary key,
        state TEXT not null,
        plant_id TEXT not null,
        plant_name TEXT not null,
        genid TEXT not null,
        net_generation_mwh FLOAT not null,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        unique (state, plant_id, genid)
        );
        """
    with engine.connect() as conn:
        conn.execute(text(create_table_sql))
        conn.commit()

def create_uploaded_files_table(engine):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS uploaded_files (
        id SERIAL PRIMARY KEY,
        filename VARCHAR(255) UNIQUE NOT NULL,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with engine.connect() as conn:
        conn.execute(text(create_table_sql))
        conn.commit()

def ensure_tables_exist(engine):
    create_powerplan_table(engine)
    create_uploaded_files_table(engine)