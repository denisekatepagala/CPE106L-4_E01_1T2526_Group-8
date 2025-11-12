from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import engine
from ..services.analytics import rides_per_day, avg_wait_minutes

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/rides-per-day")
def get_rides_per_day(days: int = 7, session: Session = Depends(get_session)):
    return rides_per_day(session, days)

@router.get("/avg-wait-time")
def get_avg_wait_time(days: int = 30, session: Session = Depends(get_session)):
    return avg_wait_minutes(session, days)
