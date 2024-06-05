from fastapi import APIRouter

router = APIRouter(
    prefix="/tracks",
    tags=["tracks"],
)


@router.get("/")
async def get_tracks():
    return {"message": "tracks"}
