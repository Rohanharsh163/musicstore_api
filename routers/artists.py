# routers/artists.py
from fastapi import APIRouter
from typing import List
from schemas.artist import Artist
from services.artist_service import get_artists

router = APIRouter(prefix="/artists", tags=["artists"])

@router.get("", response_model=List[Artist])
async def list_artists():
    """Return list of artists."""
    return await get_artists()
