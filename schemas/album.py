# schemas/album.py
from pydantic import BaseModel

class Album(BaseModel):
    album_id: int
    title: str
    artist_id: int
