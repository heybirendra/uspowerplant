from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy import text, func
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.orm.PowerPlant import PowerPlant

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pp/states")
def get_states(db: Session = Depends(get_db)):
    states = db.query(PowerPlant.state).distinct().order_by(PowerPlant.state).all()
    return [state[0] for state in states]

@router.get("/pp/powerplants")
def get_powerplants(
    limit: int = Query(10, gt=0, le=1000),
    state: Optional[str] = Query(None, min_length=2, max_length=2),
    db: Session = Depends(get_db),
):
    query = db.query(
        PowerPlant.plant_id,
        PowerPlant.plant_name,
        PowerPlant.state,
        func.sum(PowerPlant.net_generation_mwh).label("net_generation_mwh")
    )

    if state:
        query = query.filter(PowerPlant.state == state.upper())

    query = query.group_by(
        PowerPlant.plant_id,
        PowerPlant.plant_name,
        PowerPlant.state
    ).order_by(func.sum(PowerPlant.net_generation_mwh).desc()).limit(limit)
    results = query.all()

    # Convert result to list of dicts for JSON response
    return [
        {
            "plant_id": r.plant_id,
            "plant_name": r.plant_name,
            "state": r.state,
            "net_generation_mwh": r.net_generation_mwh
        }
        for r in results
    ]

