# routers/albums.py
from fastapi import APIRouter, Query
from typing import Optional, List
from schemas.album import Album
from services.album_service import get_albums

router = APIRouter(prefix="/albums", tags=["albums"])

@router.get("", response_model=List[Album])
async def list_albums(artist_id: Optional[int] = Query(None, alias="artist_id")):
    """
    List all albums, or filter by ?artist_id=<id>.
    """
    return await get_albums(artist_id)
