from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PowerPlant(Base):
    __tablename__ = 'powerplant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state = Column(String(2))
    plant_id = Column(String)
    plant_name = Column(String)
    genid = Column(String)
    net_generation_mwh = Column(Float, nullable=True)
