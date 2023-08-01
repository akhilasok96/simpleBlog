from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user, post, blog

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

app.include_router(user.router)
app.include_router(post.router)
app.include_router(blog.router)

app.get("/")
def root():
    return {"message": "Blog API"}