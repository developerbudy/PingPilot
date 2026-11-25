from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import Response


app = FastAPI(
    title="PingPilot",
    description="A backend built with FastAPI",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


@app.head("/", include_in_schema=False)
def home_head():
    return Response(status_code=200)


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