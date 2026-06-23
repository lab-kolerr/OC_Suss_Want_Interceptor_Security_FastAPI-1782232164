from fastapi import APIRouter, Depends
from app.schemas import UserCreate
from app.models import User
from app.database import SessionLocal

router = APIRouter()

@router.post('/users/')
async def create_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user