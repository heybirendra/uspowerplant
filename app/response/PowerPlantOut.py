from pydantic import BaseModel

class PowerPlantOut(BaseModel):
    plant_id: int
    plant_name: str
    state: str
    net_generation_mwh: float

    class Config:
        orm_mode = True