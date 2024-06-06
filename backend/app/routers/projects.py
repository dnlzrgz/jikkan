from fastapi import APIRouter

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)


@router.get("/")
async def get_projects():
    return {"message": "projects"}
