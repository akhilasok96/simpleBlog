from pydantic import BaseModel

class CreateUser(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    uid: int
    email: str
    password: str

    class Config:
        orm_mode = True
    
class CreatePost(BaseModel):
    title: str
    content: str
    published: bool
    uid: int

class PostResponse(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True

# class BlogResponse(BaseModel):
#     email: str
#     title: str
#     content: str
#     date_time: str

#     class Config:
#         orm_mode = True

