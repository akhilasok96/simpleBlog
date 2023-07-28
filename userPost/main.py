from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import CreateUser, CreatePost,UserResponse, PostResponse
from models import User, Post
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/user", response_model=UserResponse)
def create_user(details: CreateUser, db: Session = Depends(get_db)):
    to_create = User(**details.dict())     

    db.add(to_create)
    db.commit()
    db.refresh(to_create)
    return to_create

@app.get("/user/{id}", response_model=UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.uid == id).first()

@app.put("/user/{id}")
def update_user(id: int, details: CreateUser, db: Session = Depends(get_db)):
    db.query(User).filter(User.uid == id).update({**details.dict()})
    db.commit()
    return {"success": True}

@app.delete("/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.uid == id).delete()
    db.commit()
    return {"success": True}

@app.get("/posts", response_model=List[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.post("/post", response_model=PostResponse)
def create_post(details: CreatePost, db: Session = Depends(get_db)):
    to_create = Post(**details.dict())     

    db.add(to_create)
    db.commit()
    db.refresh(to_create)
    return to_create

@app.get("/post/{id}", response_model=PostResponse)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.pid == id).first()

@app.put("/post/{id}")
def update_post(id: int, details: CreatePost, db: Session = Depends(get_db)):
    db.query(Post).filter(Post.pid == id).update({**details.dict()})
    db.commit()
    return {"success": True}

@app.delete("/post/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    db.query(Post).filter(Post.pid == id).delete()
    db.commit()
    return {"success": True}

@app.get("/getBlog/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    result = db.query(Post, User).join(User).where(User.uid == id).all()
    bloglist = []
    for posts, users in result:
         bloglist.append({"user_id":users.uid, "ptitle":posts.title,"pcontent":posts.content,"ptime":posts.created_time,"umail": users.email})
    return bloglist


