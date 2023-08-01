
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
from models import User, Post

router = APIRouter(
    prefix="/getBlog"
)

@router.get("/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    result = db.query(Post, User).join(User).where(User.uid == id).all()
    bloglist = []
    for posts, users in result:
         bloglist.append({"user_id":users.uid, "ptitle":posts.title,"pcontent":posts.content,"ptime":posts.created_time,"umail": users.email})
    return bloglist