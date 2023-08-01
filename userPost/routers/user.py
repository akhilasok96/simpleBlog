from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemas import CreateUser, UserResponse
from models import User
from typing import List

router = APIRouter(
    prefix="/users"
)

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/create", response_model=UserResponse)
def create_user(details: CreateUser, db: Session = Depends(get_db)):
    to_create = User(**details.dict())     

    db.add(to_create)
    db.commit()
    db.refresh(to_create)
    return to_create

@router.get("/{id}", response_model=UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.uid == id).first()

@router.put("/{id}")
def update_user(id: int, details: CreateUser, db: Session = Depends(get_db)):
    db.query(User).filter(User.uid == id).update({**details.dict()})
    db.commit()
    return {"success": True}

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.uid == id).delete()
    db.commit()
    return {"success": True}