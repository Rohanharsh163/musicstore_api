# services/artist_service.py
from typing import List
from dao.artist_dao import list_artists
from schemas.artist import Artist

async def get_artists() -> List[Artist]:
    return await list_artists()
