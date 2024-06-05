from fastapi import FastAPI
from app.routers import projects, tracks

app = FastAPI()

app.include_router(projects.router)
app.include_router(tracks.router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
