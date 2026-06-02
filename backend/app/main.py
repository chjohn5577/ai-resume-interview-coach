from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Base, User
from app.schemas import UserCreate
from app.dependencies import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Resume Interview Coach",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Interview Coach API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "user_id": new_user.id
    }