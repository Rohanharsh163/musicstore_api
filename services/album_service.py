# services/album_service.py
from typing import Optional, List
from dao.album_dao import list_albums
from schemas.album import Album

async def get_albums(artist_id: Optional[int] = None) -> List[Album]:
    return await list_albums(artist_id)
