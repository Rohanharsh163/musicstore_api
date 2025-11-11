# dao/album_dao.py
from typing import List, Optional
from db import get_pool
from schemas.album import Album

async def list_albums(artist_id: Optional[int] = None) -> List[Album]:
    pool = get_pool()
    if pool is None:
        raise RuntimeError("DB pool not initialized")
    if artist_id is not None:
        sql = "SELECT album_id, title, artist_id FROM album WHERE artist_id = $1 ORDER BY title;"
        async with pool.acquire() as conn:
            rows = await conn.fetch(sql, artist_id)
    else:
        sql = "SELECT album_id, title, artist_id FROM album ORDER BY title;"
        async with pool.acquire() as conn:
            rows = await conn.fetch(sql)
    return [Album(album_id=r["album_id"], title=r["title"], artist_id=r["artist_id"]) for r in rows]
