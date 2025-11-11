from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..database import engine
from ..models.models import RideRequest, User
from ..services.scheduler import assign_driver_to_ride


router = APIRouter(prefix="/ride-requests", tags=["Ride Requests"])


def get_session():
    with Session(engine) as session:
        yield session


@router.get("/", response_model=list[RideRequest])
def list_rides(session: Session = Depends(get_session)):
    statement = select(RideRequest)
    return session.exec(statement).all()


@router.post("/", response_model=RideRequest)
def create_ride(req: RideRequest, session: Session = Depends(get_session)):
    # 1) Validate user
    user = session.get(User, req.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 2) Initialize lifecycle fields
    req.status = "requested"
    req.requested_at = datetime.utcnow()

    session.add(req)
    session.commit()
    session.refresh(req)

    # 3) Try to auto-assign a driver
    assigned = assign_driver_to_ride(session, req)
    if not assigned:
        # leave as "requested" if no driver or missing coords
        raise HTTPException(status_code=400, detail="No available drivers or missing pickup coordinates")

    return assigned
