from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from schemas import CreatePost, PostResponse
from models import Post
from typing import List

router = APIRouter(
    prefix="/posts"
)

@router.get("/", response_model=List[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@router.post("/create", response_model=PostResponse)
def create_post(details: CreatePost, db: Session = Depends(get_db)):
    to_create = Post(**details.dict())     

    db.add(to_create)
    db.commit()
    db.refresh(to_create)
    return to_create

@router.get("/{id}", response_model=PostResponse)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.pid == id).first()

@router.put("/{id}")
def update_post(id: int, details: CreatePost, db: Session = Depends(get_db)):
    db.query(Post).filter(Post.pid == id).update({**details.dict()})
    db.commit()
    return {"success": True}

@router.delete("/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    db.query(Post).filter(Post.pid == id).delete()
    db.commit()
    return {"success": True}
