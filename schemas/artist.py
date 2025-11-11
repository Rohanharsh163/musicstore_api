# schemas/artist.py
from pydantic import BaseModel
from typing import Optional

class Artist(BaseModel):
    artist_id: int
    name: Optional[str]
