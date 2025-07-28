CREATE TABLE IF NOT EXISTS powerplant (
    id serial primary key,
    state TEXT not null
    plant_id TEXT not null,
    plant_name TEXT not null
    genid TEXT not null,
    net_generation_mwh FLOAT not null,
    unique (state, plant_id, genid)
);

CREATE TABLE IF NOT EXISTS uploaded_files (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) UNIQUE NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
