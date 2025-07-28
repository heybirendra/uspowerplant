CREATE TABLE IF NOT EXISTS powerplant (
    id serial primary key,
    state TEXT not null
    plant_id TEXT not null,
    plant_name TEXT not null
    genid TEXT not null,
    net_generation_mwh FLOAT not null,
    unique (state, plant_id, genid)
);
