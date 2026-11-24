from fastapi import FastAPI


app = FastAPI(
    title="PingPilot",
    description="A backend built with FastAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to PingPilot!",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "message": "PingPilot is healthy!",
        "status": "success"
    }