from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Interview Coach",
    description="Backend API for resume analysis and interview preparation",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Resume Interview Coach API",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }