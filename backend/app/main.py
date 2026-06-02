from fastapi import FastAPI

from app.database import engine
from app.models import Base

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